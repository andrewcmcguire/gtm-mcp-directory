"""Smoke test: spawn the server over stdio and exercise every tool with real queries.

Run it from this directory:

    python qa_stdio.py

It spawns `python -m gtm_mcp_directory` as a real subprocess, speaks MCP over
stdio to it, calls all eleven tools, prints trimmed output, and asserts the
things that are load-bearing:

- every tool is registered and callable
- every response carries honesty.tier and honesty.last_checked
- every response carries the job-tag meaning line
- "enrich a linkedin profile url" returns tools that actually do that
- the counts match the build report
- the CLI and GitHub organisation layers count what the data counts, and say
  "not measured" rather than 0 when they have not run
- nothing needs the network

Exit code 0 means the server is honest and working. Anything else is a fail.
"""

from __future__ import annotations

import asyncio
import json
import os
import sys
from pathlib import Path
from typing import Any

from fastmcp import Client
from fastmcp.client.transports import StdioTransport

HERE = Path(__file__).resolve().parent
FAILURES: list[str] = []
CHECKS = 0


def expected_counts() -> dict[str, int]:
    """The load-bearing totals, read from the live data rather than typed here.

    A constant in this file drifted from the data once (solo_reachable 117 vs
    123) and the test failed on a true build. The build report and the baked
    directory are the counting authority; this test only checks that the server
    agrees with them.
    """
    data_dir = HERE.parent / "data"
    directory = json.loads((data_dir / "directory.json").read_text(encoding="utf-8"))
    entries = directory["entries"]
    official = sum(1 for e in entries if e.get("mcp_status_bucket") == "official")
    solo = sum(
        1
        for e in entries
        if e.get("mcp_status_bucket") in ("official", "community")
        and e.get("api_gate_bucket") in ("free", "paid")
    )
    bench = sum(1 for e in entries if e.get("tier") == "BENCH-TESTED")
    official_live = sum(
        1 for e in entries
        if e.get("mcp_status_bucket") == "official"
        and e.get("endpoint_status") in ("live", "live-auth-gated")
    )
    gates: dict[str, int] = {}
    for e in entries:
        g = e.get("api_gate_bucket") or "unknown"
        gates[g] = gates.get(g, 0) + 1

    # The command-line layer. The top-level "cli" summary and the per-entry
    # cli_status must agree with each other before the server is asked to agree
    # with either. A build without the layer reads as not measured.
    cli_layer = directory.get("cli") or {}
    by_cli: dict[str, int] = {}
    for e in entries:
        k = e.get("cli_status") or "not-checked"
        by_cli[k] = by_cli.get(k, 0) + 1
    cli_reachable = by_cli.get("official", 0) + by_cli.get("community", 0)
    summary_status = cli_layer.get("by_status") or {}
    cli_summary_reachable = int(summary_status.get("official") or 0) + int(summary_status.get("community") or 0)
    cli_measured = bool(cli_layer.get("generated_on")) and any(k != "not-checked" for k in by_cli)

    orgs_layer = directory.get("github_orgs") or {}
    by_org: dict[str, int] = {}
    for e in entries:
        k = e.get("github_org_status") or "not-checked"
        by_org[k] = by_org.get(k, 0) + 1
    orgs_measured = bool(orgs_layer.get("generated_on")) and any(k != "not-checked" for k in by_org)
    orgs_resolved_canonical = sum(
        1 for e in entries if e.get("canonical", True) and e.get("github_org_status") == "resolved"
    )
    ai_sdr = next(
        (c.get("total") for c in directory.get("categories", []) if c.get("slug") == "ai-sdr-agents"),
        None,
    )
    return {
        "entries": len(entries),
        "ai_sdr_agents": ai_sdr,
        "official": official,
        "solo_reachable": solo,
        "bench_tested": bench,
        "gates": gates,
        "official_live": official_live,
        "cli_reachable": cli_reachable,
        "cli_summary_reachable": cli_summary_reachable,
        "cli_measured": cli_measured,
        "cli_checked_on": cli_layer.get("generated_on"),
        "orgs_measured": orgs_measured,
        "orgs_checked_on": orgs_layer.get("generated_on"),
        "orgs_resolved_canonical": orgs_resolved_canonical,
        "orgs_by_status": by_org,
    }


EXPECTED = expected_counts()

REQUIRED_TOOLS = [
    "find_tools",
    "get_tool",
    "list_categories",
    "whats_mcpd",
    "find_by_gate",
    "get_docs_digest",
    "list_jobs",
    "get_server_tools",
    "plan_stack",
    "get_install",
    "whats_building",
]

PLAN_GOAL = "find a person's linkedin from a name and company, get their work email, verify it"


def candidate_sets(plan: dict[str, Any]) -> list[list[str]]:
    """Per step, the sorted candidate names, so two plans can be compared as sets."""
    out = []
    for step in plan.get("steps") or []:
        rows = ([step["recommended"]] if step.get("recommended") else []) + (step.get("alternatives") or [])
        out.append(sorted(r["name"] for r in rows))
    return out


def check(label: str, condition: bool, detail: str = "") -> None:
    global CHECKS
    CHECKS += 1
    if condition:
        print("   PASS  %s" % label)
    else:
        print("   FAIL  %s %s" % (label, detail))
        FAILURES.append(label + (" " + str(detail) if detail not in ("", None) else ""))


def rule(title: str) -> None:
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


def trim(text: Any, width: int = 150) -> str:
    s = str(text or "").replace("\n", " ")
    return s if len(s) <= width else s[: width - 3] + "..."


def payload(result: Any) -> dict[str, Any]:
    data = getattr(result, "data", None)
    if isinstance(data, dict):
        return data
    structured = getattr(result, "structured_content", None)
    if isinstance(structured, dict):
        if set(structured.keys()) == {"result"}:
            return structured["result"]
        return structured
    content = getattr(result, "content", None) or []
    for block in content:
        text = getattr(block, "text", None)
        if text:
            try:
                return json.loads(text)
            except ValueError:
                continue
    raise AssertionError("could not decode a JSON payload from %r" % result)


def assert_envelope(label: str, body: dict[str, Any]) -> None:
    h = body.get("honesty") or {}
    check("%s: honesty.tier present" % label, bool(h.get("tier")), repr(h.get("tier")))
    check(
        "%s: honesty.last_checked present" % label,
        bool(h.get("last_checked")),
        repr(h.get("last_checked")),
    )
    check(
        "%s: job-tag meaning present" % label,
        "the vendor says the tool does this" in (h.get("job_tag_meaning") or "").lower()
        and "the vendor says the tool does this" in (h.get("jobs_meaning") or "").lower(),
    )
    check(
        "%s: server metadata rides along" % label,
        bool((body.get("server") or {}).get("server_version"))
        and (body.get("server") or {}).get("network_calls_this_response") == 0,
    )


async def run() -> None:
    transport = StdioTransport(
        command=sys.executable,
        args=["-m", "gtm_mcp_directory"],
        cwd=str(HERE),
    )
    async with Client(transport) as client:
        rule("0. HANDSHAKE AND TOOL REGISTRY")
        tools = await client.list_tools()
        names = sorted(t.name for t in tools)
        print("   tools registered: %s" % ", ".join(names))
        for name in REQUIRED_TOOLS:
            check("tool registered: %s" % name, name in names)

        # ------------------------------------------------------------------
        rule("1. find_tools('enrich a linkedin profile url')")
        body = payload(
            await client.call_tool(
                "find_tools", {"job_or_query": "enrich a linkedin profile url", "limit": 8}
            )
        )
        qr = body["query_resolved"]
        print("   mode:            %s" % qr["mode"])
        print("   vocabulary:      %s" % trim(qr["vocabulary"]["note"]))
        print("   resolved_jobs:   %s" % qr["resolved_jobs"])
        print("   fallback:        %s" % trim(qr.get("fallback")))
        print("   search terms:    %s" % qr["search_terms_used"])
        print("   match_count:     %s (returned %s)" % (body["match_count"], body["returned"]))
        print("   sort:            %s" % trim(body["sort"]))
        for r in body["results"]:
            print(
                "     - %-28s %-11s %-16s %s"
                % (
                    trim(r["name"], 28),
                    r["mcp_status"],
                    r["api_gate"],
                    "terms=%s" % ",".join(r.get("matched_terms") or [])
                    if qr["mode"] == "text-search"
                    else "jobs=%d" % len(r["jobs"]),
                )
            )
        print("   summary:         %s" % trim(body["summary"], 300))
        print("   tagging:         %s" % body["honesty"]["tagging"])
        print("   caveat[0]:       %s" % trim(body["honesty"]["caveats"][0], 200))
        assert_envelope("find_tools/query", body)
        top = [r["name"].lower() for r in body["results"]]
        check(
            "linkedin enrichment query returns enrichment vendors",
            any(
                v in " ".join(top)
                for v in ("dropcontact", "cufinder", "findymail", "people data labs", "lusha")
            ),
            top[:4],
        )
        if qr["mode"] == "job-tags":
            check(
                "tagged mode resolved a real slug",
                bool(qr["resolved_jobs"]) and qr["confidence"] != "none",
                qr["confidence"],
            )
            check(
                "every tagged result carries the resolved job",
                all(
                    any(j["job"] in r["jobs"] for j in qr["resolved_jobs"])
                    for r in body["results"]
                ),
            )
            check(
                "tagging provenance is disclosed",
                any(
                    "machine pass" in c.lower() or "not been read by a human" in c.lower()
                    for c in body["honesty"]["caveats"]
                )
                or body["honesty"]["tagging"]["tagged_by"] != {},
            )
        else:
            check(
                "capability answer states it is a text match, not a tag",
                any("text matches" in c.lower() for c in body["honesty"]["caveats"]),
            )

        # ------------------------------------------------------------------
        rule("2. find_tools with filters only (official MCP, free gate, enrichment)")
        body = payload(
            await client.call_tool(
                "find_tools",
                {
                    "category": "data-enrichment",
                    "mcp_status": "official",
                    "gate": "free",
                    "limit": 5,
                },
            )
        )
        print("   filters:     %s" % body["filters_applied"])
        print("   match_count: %s" % body["match_count"])
        for r in body["results"]:
            print("     - %-24s %s" % (trim(r["name"], 24), trim(r["mcp_auth"], 60)))
        print("   sort:        %s" % trim(body["sort"]))
        assert_envelope("find_tools/filters", body)
        check(
            "every filtered result really is official and free",
            all(
                r["mcp_status"] == "official" and r["api_gate"] == "free"
                for r in body["results"]
            ),
        )

        # ------------------------------------------------------------------
        rule("3. find_tools with a nonsense query")
        body = payload(
            await client.call_tool("find_tools", {"job_or_query": "quantum yak shaving"})
        )
        print("   match_count: %s" % body["match_count"])
        print("   fallback:    %s" % trim(body["query_resolved"].get("fallback"), 220))
        print("   summary:     %s" % trim(body["summary"]))
        assert_envelope("find_tools/nonsense", body)
        check("a no-match query still explains itself", body["match_count"] == 0)

        # ------------------------------------------------------------------
        rule("4. get_tool('Lusha') and an ambiguous lookup")
        body = payload(await client.call_tool("get_tool", {"name": "Lusha"}))
        e = body["entry"]
        print("   status:      %s (match=%s)" % (body["status"], body["match_method"]))
        print("   name:        %s  [%s]" % (e["name"], e["id"]))
        print("   mcp_status:  %s   gate: %s   tier: %s" % (e["mcp_status"], e["api_gate"], e["tier"]))
        print("   mcp_urls:    %s" % e["mcp_urls"])
        print("   sources:     %d URLs" % len(e["source_urls"]))
        print("   caveats:")
        for c in e["honesty"]["caveats"][:3]:
            print("     * %s" % trim(c, 170))
        assert_envelope("get_tool", body)
        check("get_tool returns the full 50-key entry", len(e) >= 50, len(e))
        check("entry carries its own tier", e["tier"] == "RESEARCHED")

        body = payload(await client.call_tool("get_tool", {"name": "clay"}))
        print("   ambiguity probe 'clay' -> status=%s" % body["status"])
        if body["status"] == "ambiguous":
            for c in body["candidates"][:4]:
                print("     ? %s (%s)" % (c["name"], c["category"]))
        check("ambiguous or exact, never silently wrong", body["status"] in ("ok", "ambiguous"))

        body = payload(await client.call_tool("get_tool", {"name": "HubSpot"}))
        print(
            "   cross-listing probe 'HubSpot' -> %s"
            % trim((body.get("cross_listing") or {}).get("canonical_id"))
        )

        # ------------------------------------------------------------------
        rule("5. list_categories()")
        body = payload(await client.call_tool("list_categories", {}))
        print(
            "   %d categories, %d entries, %d unique products"
            % (body["category_count"], body["total_entries"], body["unique_products"])
        )
        print("   %-26s %5s %5s %5s %8s" % ("category", "total", "off", "comm", "reach"))
        for c in body["categories"]:
            print(
                "     %-24s %5d %5d %5d %8s"
                % (c["slug"], c["total"], c["official"], c["community"], c["mcp_reachable_ratio"])
            )
        first = body["categories"][0]
        print(
            "   top_jobs for %s: %s"
            % (first["slug"], first["top_jobs"] or trim(first["top_jobs_note"], 150))
        )
        assert_envelope("list_categories", body)
        check("15 categories", body["category_count"] == 15)
        check(
            "category totals sum to the entry count",
            sum(c["total"] for c in body["categories"]) == body["total_entries"],
        )

        # ------------------------------------------------------------------
        rule("6. whats_mcpd() and whats_mcpd(category='ai-sdr-agents')")
        body = payload(await client.call_tool("whats_mcpd", {}))
        print("   scope:           %s (%s)" % (body["scope"], body["scope_basis"]))
        print(
            "   entries=%d official=%d community=%d none_found=%d unknown=%d n_a=%d"
            % (
                body["entries"],
                body["official"],
                body["community"],
                body["none_found"],
                body["unknown"],
                body["n_a"],
            )
        )
        print("   official_pct:    %s   mcp_reachable: %s" % (body["official_pct"], body["mcp_reachable"]))
        print("   gates:           %s" % body["gates"])
        print("   solo_reachable:  %s" % body["solo_reachable"])
        print("   bench_tested:    %s" % body["bench_tested"])
        print("   most_mcpd:       %s" % body["extremes"]["most_mcpd"])
        print("   least_mcpd:      %s" % body["extremes"]["least_mcpd"])
        print("   headline:        %s" % trim(body["headline"], 320))
        print("   mcp_url note:    %s" % trim(body["mcp_url_parse_note"], 260))
        assert_envelope("whats_mcpd", body)
        check("entry total matches the data (%d)" % EXPECTED["entries"], body["entries"] == EXPECTED["entries"], body["entries"])
        check("official matches the data (%d)" % EXPECTED["official"], body["official"] == EXPECTED["official"], body["official"])
        check("solo_reachable matches the data (%d)" % EXPECTED["solo_reachable"], body["solo_reachable"] == EXPECTED["solo_reachable"], body["solo_reachable"])
        check("bench_tested matches the data (%d) and is not hidden" % EXPECTED["bench_tested"], body["bench_tested"] == EXPECTED["bench_tested"], body["bench_tested"])
        check("whats_mcpd carries the endpoint split", "official_with_live_endpoint" in body and "official_docs_only" in body)
        check("endpoint split matches the data (%d live)" % EXPECTED["official_live"], body["official_with_live_endpoint"] == EXPECTED["official_live"], body["official_with_live_endpoint"])

        body = payload(await client.call_tool("whats_mcpd", {"category": "ai-sdr-agents"}))
        print(
            "   scoped: %s entries=%d official=%d reachable=%s pct=%s"
            % (
                body["scope"],
                body["entries"],
                body["official"],
                body["mcp_reachable"],
                body["mcp_reachable_pct"],
            )
        )
        check("category scope narrows the set (%d)" % EXPECTED["ai_sdr_agents"], body["entries"] == EXPECTED["ai_sdr_agents"] and body["entries"] < EXPECTED["entries"], body["entries"])

        # ------------------------------------------------------------------
        rule("7. find_by_gate('free') and find_by_gate('enterprise-only')")
        body = payload(await client.call_tool("find_by_gate", {"gate": "free", "limit": 6}))
        print("   gate:        %s" % body["gate"])
        print("   meaning:     %s" % trim(body["gate_meaning"], 180))
        print("   match_count: %s" % body["match_count"])
        print("   breakdown:   %s" % body["breakdown"])
        for r in body["results"]:
            print("     - %-26s %-10s %s" % (trim(r["name"], 26), r["mcp_status"], trim(r["mcp_auth"], 50)))
        print("   summary:     %s" % trim(body["summary"], 300))
        assert_envelope("find_by_gate/free", body)
        check("free gate count matches the data (%d)" % EXPECTED["gates"].get("free", 0), body["match_count"] == EXPECTED["gates"].get("free", 0), body["match_count"])

        body = payload(
            await client.call_tool("find_by_gate", {"gate": "enterprise only", "limit": 3})
        )
        print("   alias 'enterprise only' -> %s, %d matches" % (body["gate"], body["match_count"]))
        check("gate aliases normalize", body["gate"] == "enterprise-only")
        check("enterprise-only count matches the data (%d)" % EXPECTED["gates"].get("enterprise-only", 0), body["match_count"] == EXPECTED["gates"].get("enterprise-only", 0), body["match_count"])

        body = payload(await client.call_tool("find_by_gate", {"gate": "cheap"}))
        print("   bad gate 'cheap' -> %s" % body["status"])
        check("an unknown gate returns the vocabulary, not an empty list", body["status"] == "unknown gate")

        # ------------------------------------------------------------------
        rule("8. get_docs_digest on a known docs_url, and on one without")
        body = payload(await client.call_tool("get_docs_digest", {"name": "Anymail Finder"}))
        print("   name:     %s" % body["name"])
        print("   status:   %s" % body["status"])
        print("   docs_url: %s" % body["docs_url"])
        print("   digest:   %s" % body["digest"])
        print("   message:  %s" % trim(body["message"], 260))
        assert_envelope("get_docs_digest/known", body)
        check("known docs_url is returned", bool(body["docs_url"]))
        check("uncrawled entry says not yet digested", body["status"] == "not yet digested")
        check("no digest is invented", body["digest"] is None)

        body = payload(await client.call_tool("get_docs_digest", {"name": "Lusha"}))
        print("   Lusha -> status=%s docs_url=%s" % (body["status"], body["docs_url"]))
        print("   message: %s" % trim(body["message"], 260))
        check("a missing docs_url is explained, not nulled", body["status"] == "no docs_url on file")

        # ------------------------------------------------------------------
        rule("9. list_jobs()")
        body = payload(await client.call_tool("list_jobs", {}))
        print("   status:     %s" % body["status"])
        print("   vocabulary: %s" % trim(body["vocabulary"]["note"], 220))
        if body["status"] == "ok":
            print("   jobs:       %d in %d families" % (body["job_count"], len(body["families"])))
            print("   tagging:    %s" % trim(body["tagging_progress"]["note"], 200))
            for j in body["jobs"][:8]:
                print("     - %-38s %s" % (j["slug"], j["supply_note"]))
            zero = [j["slug"] for j in body["jobs"] if j["tool_count"] == 0]
            thin = [
                "%s (%d claim, %d callable)" % (j["slug"], j["tool_count"], j["official_mcp"])
                for j in body["jobs"]
                if j["tool_count"] >= 5 and j["official_mcp"] <= 1
            ]
            print("   jobs with no supply at all: %s" % (zero or "none"))
            print("   claimed but barely callable: %s" % (thin[:4] or "none"))
        else:
            print("   message:    %s" % trim(body["message"], 300))
        assert_envelope("list_jobs", body)
        check(
            "list_jobs answers either way",
            body["status"] in ("ok", "vocabulary not installed", "vocabulary unreadable"),
            body["status"],
        )

        # ------------------------------------------------------------------
        rule("9b. find_tools(interface='cli'): the command-line layer as a filter")
        body = payload(await client.call_tool("find_tools", {"interface": "cli", "limit": 100}))
        print("   cli layer measured (data): %s on %s" % (EXPECTED["cli_measured"], EXPECTED["cli_checked_on"]))
        print("   filters:     %s" % body["filters_applied"])
        print("   match_count: %s (data says %s reachable, summary says %s)" % (body["match_count"], EXPECTED["cli_reachable"], EXPECTED["cli_summary_reachable"]))
        for n in body["filter_notes"][:2]:
            print("   note:        %s" % trim(n, 220))
        for r in body["results"][:6]:
            inst = (r["cli_install"] or [{}])[0]
            print("     - %-24s %-10s %-10s %s" % (trim(r["name"], 24), r["cli_status"], trim(r["cli_binary"], 10), trim(inst.get("cmd"), 50)))
        print("   summary:     %s" % trim(body["summary"], 320))
        assert_envelope("find_tools/interface=cli", body)
        check(
            "the data agrees with itself on cli official+community (%d)" % EXPECTED["cli_reachable"],
            EXPECTED["cli_reachable"] == EXPECTED["cli_summary_reachable"],
            EXPECTED["cli_summary_reachable"],
        )
        check(
            "interface=cli count matches the data (%d)" % EXPECTED["cli_reachable"],
            body["match_count"] == EXPECTED["cli_reachable"],
            body["match_count"],
        )
        check(
            "every interface=cli result has cli_status official or community",
            all(r["cli_status"] in ("official", "community") for r in body["results"]),
        )
        check(
            "every cli result carries cli_checked_on",
            all(r["cli_checked_on"] for r in body["results"]),
        )
        check(
            "the result view carries the CLI and organisation fields",
            all(k in (body["results"][0] if body["results"] else {"cli_status": 1, "cli_binary": 1, "cli_install": 1, "cli_party": 1, "cli_checked_on": 1, "github_org": 1, "github_org_repos": 1, "github_org_latest_activity": 1})
                for k in ("cli_status", "cli_binary", "cli_install", "cli_party", "cli_checked_on", "github_org", "github_org_repos", "github_org_latest_activity")),
        )
        if not EXPECTED["cli_measured"]:
            check(
                "an unmeasured CLI layer says so in the filter notes",
                any("has not been measured" in n for n in body["filter_notes"]),
                body["filter_notes"][:1],
            )
            check(
                "an unmeasured CLI layer says so in the summary",
                "has not been measured" in body["summary"],
            )
        else:
            check(
                "a measured CLI layer states its date in the notes",
                any(EXPECTED["cli_checked_on"] in n for n in body["filter_notes"]),
            )
        check(
            "the envelope carries the CLI layer sentence",
            any("CLI layer" in c for c in body["honesty"]["caveats"]),
        )

        body = payload(await client.call_tool("find_tools", {"interface": "either", "limit": 1}))
        either = body["match_count"]
        body = payload(await client.call_tool("find_tools", {"interface": "mcp", "limit": 1}))
        print("   interface=mcp %d, interface=either %d" % (body["match_count"], either))
        check("interface=either is at least interface=mcp", either >= body["match_count"])
        check("interface=mcp matches official+community MCP", body["match_count"] == EXPECTED["official"] + sum(
            1 for e in json.loads((HERE.parent / "data" / "directory.json").read_text(encoding="utf-8"))["entries"]
            if e.get("mcp_status_bucket") == "community"), body["match_count"])

        # ------------------------------------------------------------------
        rule("9c. get_install('ZoomInfo'): both routes in one answer")
        body = payload(await client.call_tool("get_install", {"name": "ZoomInfo"}))
        print("   status:          %s (match=%s) -> %s" % (body["status"], body["match_method"], body["name"]))
        print("   mcp route:       %s" % trim(body["mcp"]["route"], 200))
        print("   hosted_or_local: %s" % body["mcp"]["hosted_or_local"])
        print("   cli route:       %s" % trim(body["cli"]["route"], 200))
        for i in body["cli"]["cli_install"]:
            print("     $ %-50s <- %s (%s)" % (trim(i["cmd"], 50), trim(i["source_url"], 60), i["fetched_on"]))
        print("   recommendation:  %s" % trim(body["recommendation"], 300))
        for c in body["caveats"][:3]:
            print("     * %s" % trim(c, 170))
        assert_envelope("get_install", body)
        check("get_install resolved ZoomInfo", body["status"] == "ok" and body["name"] == "ZoomInfo", body.get("name"))
        check("get_install carries both routes", "mcp" in body and "cli" in body)
        check("the MCP route states endpoint_status", body["mcp"]["endpoint_status"] is not None)
        check("the MCP route states hosted or local", body["mcp"]["hosted_or_local"] in ("hosted", "local", "unknown", "none"))
        check("recommendation names both routes", body["recommendation"].startswith("MCP:") and "CLI:" in body["recommendation"])
        check("recommendation does not rank vendors", "best" not in body["recommendation"].lower() and "recommend" not in body["recommendation"].lower())
        if body["cli"]["cli_status"] == "official":
            check("official CLI: at least one install command", len(body["cli"]["cli_install"]) >= 1)
            check(
                "official CLI: every install command has a non-empty source_url",
                all(i.get("source_url") for i in body["cli"]["cli_install"]),
            )
            check(
                "official CLI: every install command has a fetched_on date",
                all(i.get("fetched_on") for i in body["cli"]["cli_install"]),
            )
            check("official CLI: the caveats say the command was quoted, not run", any("not run" in c for c in body["caveats"]))
        elif body["cli"]["cli_status"] == "not-checked":
            check("unmeasured CLI: the route says not measured", "not been measured" in body["cli"]["route"] or "not measured" in body["cli"]["route"], body["cli"]["route"])
        elif body["cli"]["cli_status"] == "none-found":
            check("none-found CLI: the route carries the date", (body["cli"]["cli_checked_on"] or "") in body["cli"]["route"])
        else:
            check("community CLI: the route says third party", "third party" in body["cli"]["route"])

        body = payload(await client.call_tool("get_install", {"name": "quantum yak shaving inc"}))
        print("   unknown name -> %s" % body["status"])
        check("get_install explains a miss", body["status"] == "not found" and "not been researched" in body["message"])

        # ------------------------------------------------------------------
        rule("9d. whats_building(): what vendors ship in public, dated")
        body = payload(await client.call_tool("whats_building", {}))
        print("   orgs layer measured (data): %s on %s" % (EXPECTED["orgs_measured"], EXPECTED["orgs_checked_on"]))
        print("   status:    %s   scope=%s" % (body["status"], body["scope"]))
        print("   window:    %s" % body["window"])
        print("   counts:    %s" % body["counts"])
        if body["status"] == "ok":
            print("   silence:   %s" % trim(body["silence_note"], 260))
            for v in body["active_vendors"][:5]:
                top = (v["recent_repos"] or [{}])[0]
                print("     - %-20s %-18s repos=%-4s mcp=%-3s last=%s  top=%s" % (trim(v["name"], 20), trim(v["github_org"], 18), v["repos_public_non_fork"], v["repos_mcp"], trim(v["latest_activity"], 10), trim(top.get("name"), 30)))
        else:
            print("   message:   %s" % trim(body["message"], 260))
        assert_envelope("whats_building", body)
        if EXPECTED["orgs_measured"]:
            check("whats_building serves when the layer is measured", body["status"] == "ok", body["status"])
            check("resolved count matches the data (%d canonical)" % EXPECTED["orgs_resolved_canonical"], body["counts"]["resolved"] == EXPECTED["orgs_resolved_canonical"], body["counts"]["resolved"])
            check("every count carries checked_on", body["counts"]["checked_on"] == EXPECTED["orgs_checked_on"], body["counts"]["checked_on"])
            check("active vendors all carry a last push and a date", all(v["latest_activity"] and v["checked_on"] for v in body["active_vendors"]))
            check("active vendors are sorted most recent first", [v["latest_activity"] for v in body["active_vendors"]] == sorted((v["latest_activity"] for v in body["active_vendors"]), reverse=True))
            check("silence is counted, not hidden", body["counts"]["silent_total"] == body["counts"]["entries_in_scope"] - body["counts"]["resolved"])
        else:
            check("whats_building says not measured", body["status"] == "not measured", body["status"])
            check("unmeasured counts are null, not zero", body["counts"]["resolved"] is None and body["counts"]["not_checked"] is None)
            check("the message says the layer has not been measured", "has not been measured" in body["message"])

        body = payload(await client.call_tool("whats_building", {"name": "Apify"}))
        print("   Apify -> org=%s status=%s repos=%s last=%s" % (body.get("github_org"), body.get("github_org_status"), body.get("repos"), trim(body.get("latest_activity"), 10)))
        print("   message: %s" % trim(body.get("message"), 240))
        check("whats_building(name) resolves a vendor", body["status"] == "ok" and body["name"] == "Apify", body.get("name"))
        if body["github_org_status"] == "resolved":
            check("a resolved org carries integer repo counts and a date", isinstance(body["repos"]["public_non_fork"], int) and bool(body["repos"]["checked_on"]))
            check("a resolved org carries recent repos with pushed dates", bool(body["recent_repos"]) and all(r.get("pushed_at") for r in body["recent_repos"]))
        else:
            check("an unresolved or unchecked org carries null counts", body["repos"]["public_non_fork"] is None)

        # ------------------------------------------------------------------
        rule("9e. plan_stack(prefer_interface='cli') reorders, never removes")
        base = payload(await client.call_tool("plan_stack", {"goal": PLAN_GOAL}))
        pref = payload(await client.call_tool("plan_stack", {"goal": PLAN_GOAL, "prefer_interface": "cli"}))
        print("   steps: %d; preference note: %s" % (len(pref["steps"]), trim(pref["interface_preference"]["note"], 200)))
        for st in pref["steps"]:
            rec = st["recommended"] or {}
            print("     %d. %-34s -> %-22s cli=%s" % (st["step"], st["job"], trim(rec.get("name"), 22), (rec.get("cli") or {}).get("status")))
        check("plan_stack still plans the goal", base["status"] == "ok" and len(base["steps"]) >= 2, base["status"])
        check("every candidate carries a cli block", all(
            "cli" in c and "status" in c["cli"] and "install" in c["cli"]
            for st in base["steps"] for c in ([st["recommended"]] if st["recommended"] else []) + st["alternatives"]
        ))
        check("prefer_interface=cli returns the same candidate set per step", candidate_sets(base) == candidate_sets(pref), (candidate_sets(base), candidate_sets(pref)))
        check("prefer_interface is disclosed", pref["interface_preference"]["asked"] == "cli" and bool(pref["interface_preference"]["note"]))
        if EXPECTED["cli_measured"]:
            check("with a measured CLI layer, CLI-bearing candidates lead each step", all(
                [c["cli"]["status"] in ("official", "community") for c in ([st["recommended"]] if st["recommended"] else []) + st["alternatives"]]
                == sorted([c["cli"]["status"] in ("official", "community") for c in ([st["recommended"]] if st["recommended"] else []) + st["alternatives"]], reverse=True)
                for st in pref["steps"]
            ))
        else:
            check("with an unmeasured CLI layer the note says so", "has not been measured" in (pref["interface_preference"]["note"] or ""))

        # ------------------------------------------------------------------
        rule("10. INTEGRITY RESOURCE")
        res = await client.read_resource("gtm-directory://integrity")
        raw = getattr(res[0], "text", None)
        info = json.loads(raw) if raw else {}
        for c in info["integrity"]["checks"]:
            print("   %-18s %s  %s" % (c["check"], "PASS" if c["passed"] else "FAIL", trim(c["detail"], 90)))
        print("   expected_entries: %s (%s)" % (info["integrity"]["expected_entries"], info["integrity"]["expected_entries_source"]))
        check("all startup checks passed", info["integrity"]["all_passed"])
        check(
            "expected count came from the build report",
            "build_report.json" in info["integrity"]["expected_entries_source"],
        )


def strip_layer(payload: dict, *, drop_vocabulary: bool, drop_tags: bool) -> dict:
    """Return a copy of the directory with a phase-2 layer removed, restamped."""
    from gtm_mcp_directory.loading import content_sha256

    out = json.loads(json.dumps(payload))
    if drop_vocabulary:
        out.pop("jobs_vocabulary", None)
        out.pop("job_families", None)
    if drop_tags:
        for entry in out["entries"]:
            entry["jobs"] = []
            entry["jobs_tagged_by"] = None
            entry["jobs_tagged_on"] = None
        if isinstance(out.get("counts"), dict):
            out["counts"]["entries_tagged"] = 0
            out["counts"]["entries_untagged"] = len(out["entries"])
    out["content_sha256"] = content_sha256(out)
    return out


CLI_DEFAULTS = {
    "cli_status": "not-checked", "cli_party": None, "cli_binary": None, "cli_install": [],
    "cli_login": None, "cli_commands_seen": [], "cli_docs_url": None, "cli_repo": None,
    "cli_packages": [], "cli_evidence": None, "cli_checked_on": None,
}
ORG_DEFAULTS = {
    "github_org": None, "github_org_status": "not-checked", "github_org_url": None,
    "github_org_evidence": None, "github_org_repos": 0, "github_org_repos_mcp": 0,
    "github_org_repos_cli": 0, "github_org_latest_activity": None,
    "github_org_recent_repos": [], "github_org_checked_on": None,
}


def strip_interface_layers(payload: dict) -> dict:
    """Return a copy of the directory as a build on which neither harvest has run."""
    from gtm_mcp_directory.loading import content_sha256

    out = json.loads(json.dumps(payload))
    for entry in out["entries"]:
        entry.update(json.loads(json.dumps(CLI_DEFAULTS)))
        entry.update(json.loads(json.dumps(ORG_DEFAULTS)))
    out["cli"] = {
        "source": "data/cli_inventory.json", "generated_on": None,
        "by_status": {"official": 0, "community": 0, "none-found": 0, "not-checked": 0},
        "meaning": "The CLI harvest has not run on this build.",
    }
    out["github_orgs"] = {"source": "data/github_orgs.json", "generated_on": None, "resolved": 0,
                          "meaning": "The organisation harvest has not run on this build."}
    out["content_sha256"] = content_sha256(out)
    return out


def write_fixture(tmp: Path, name: str, payload: dict) -> Path:
    from gtm_mcp_directory.loading import resolve_data_path

    live = resolve_data_path()
    d = tmp / name
    d.mkdir(parents=True, exist_ok=True)
    (d / "directory.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (d / "build_report.json").write_text(
        (live.parent / "build_report.json").read_text(encoding="utf-8"), encoding="utf-8"
    )
    return d / "directory.json"


def spawn(data_path: Path | None = None) -> StdioTransport:
    env = dict(os.environ)
    env.pop("GTM_DIRECTORY_ALLOW_CHECKSUM_DRIFT", None)
    if data_path is not None:
        env["GTM_DIRECTORY_DATA"] = str(data_path)
    return StdioTransport(
        command=sys.executable, args=["-m", "gtm_mcp_directory"], cwd=str(HERE), env=env
    )


async def run_degradation(tmp: Path) -> None:
    """The brief's hard requirement: work with jobs, and degrade honestly without them.

    The live build is tagged today. These two fixtures put the server back in
    the worlds it still has to serve: a user on an older build with no tags,
    and a build where the vocabulary exists but the tagging pass has not run.
    Neither is allowed to produce a silent empty list.
    """
    from gtm_mcp_directory.loading import resolve_data_path

    live = json.loads(resolve_data_path().read_text(encoding="utf-8"))

    # ---------------------------------------------------------------- 11 ---
    rule("11. DEGRADATION: an UNTAGGED build (no vocabulary, no tags)")
    bare = write_fixture(
        tmp, "bare", strip_layer(live, drop_vocabulary=True, drop_tags=True)
    )
    print("   fixture: jobs_vocabulary and every jobs[] tag removed, restamped")
    async with Client(spawn(bare)) as client:
        body = payload(
            await client.call_tool(
                "find_tools",
                {"job_or_query": "enrich a linkedin profile url", "limit": 6},
            )
        )
        qr = body["query_resolved"]
        print("   mode:          %s" % qr["mode"])
        print("   vocabulary:    %s" % trim(qr["vocabulary"]["note"], 180))
        print("   fallback:      %s" % trim(qr.get("fallback"), 260))
        print("   match_count:   %s" % body["match_count"])
        for r in body["results"]:
            print(
                "     - %-24s %-11s %-16s terms=%s"
                % (
                    trim(r["name"], 24),
                    r["mcp_status"],
                    r["api_gate"],
                    ",".join(r.get("matched_terms") or []),
                )
            )
        print("   summary:       %s" % trim(body["summary"], 280))
        assert_envelope("untagged/find_tools", body)
        check("untagged build falls back to text search", qr["mode"] == "text-search", qr["mode"])
        check("it still returns the right vendors", body["match_count"] > 10, body["match_count"])
        check(
            "it says out loud that these are text matches",
            any("text matches" in c.lower() for c in body["honesty"]["caveats"]),
        )
        check(
            "it says out loud that nothing is tagged",
            any(("0 of %d" % EXPECTED["entries"]) in c for c in body["honesty"]["caveats"]),
            [c for c in body["honesty"]["caveats"] if "tag" in c.lower()][:1],
        )

        body = payload(await client.call_tool("list_jobs", {}))
        print("   list_jobs:     status=%s" % body["status"])
        print("   message:       %s" % trim(body["message"], 260))
        check(
            "list_jobs explains itself rather than returning an empty menu",
            body["status"] in ("vocabulary not installed", "vocabulary unreadable"),
            body["status"],
        )
        check("it points at the categories instead", bool(body["categories_to_browse_instead"]))

        body = payload(await client.call_tool("list_categories", {}))
        first = body["categories"][0]
        print("   top_jobs note: %s" % trim(first["top_jobs_note"], 180))
        check("empty top_jobs is explained, not blank", bool(first["top_jobs_note"]))

    # ---------------------------------------------------------------- 12 ---
    rule("12. DEGRADATION: vocabulary present, corpus NOT yet tagged")
    half = write_fixture(
        tmp, "half", strip_layer(live, drop_vocabulary=False, drop_tags=True)
    )
    print(
        "   fixture: %d-job vocabulary kept, every jobs[] tag removed, restamped"
        % len(live["jobs_vocabulary"]["jobs"])
    )
    async with Client(spawn(half)) as client:
        body = payload(
            await client.call_tool(
                "find_tools",
                {"job_or_query": "enrich a linkedin profile url", "limit": 4},
            )
        )
        qr = body["query_resolved"]
        print("   mode:          %s" % qr["mode"])
        print("   resolved_jobs: %s" % qr["resolved_jobs"])
        print("   fallback:      %s" % trim(qr.get("fallback"), 300))
        print("   match_count:   %s" % body["match_count"])
        for r in body["results"]:
            print("     - %-24s %-11s %s" % (trim(r["name"], 24), r["mcp_status"], r["api_gate"]))
        assert_envelope("half/find_tools", body)
        check("falls back to text search", qr["mode"] == "text-search", qr["mode"])
        check(
            "the fallback names the slug it resolved to",
            "enrich-person-from-linkedin-url" in (qr.get("fallback") or ""),
        )
        check("it still answers usefully", body["match_count"] > 0, body["match_count"])

        body = payload(await client.call_tool("list_jobs", {}))
        zero = sum(1 for j in body["jobs"] if j["tool_count"] == 0)
        print("   list_jobs:     status=%s, %d of %d jobs show zero supply" % (body["status"], zero, body["job_count"]))
        print("   supply_note:   %s" % trim(body["jobs"][0]["supply_note"], 200))
        check("the menu still serves", body["status"] == "ok")
        check(
            "an untagged corpus does not read as a real supply gap",
            "untagged corpus" in body["jobs"][0]["supply_note"],
        )

        body = payload(
            await client.call_tool("whats_mcpd", {"job": "enrich-person-from-linkedin-url"})
        )
        print(
            "   whats_mcpd(job): basis=%s entries=%d note=%s"
            % (body["scope_basis"], body["entries"], trim(body["scope_notes"][0] if body["scope_notes"] else "", 160))
        )
        check("job stats disclose the text-match basis", body["scope_basis"] == "text-match")

    # ---------------------------------------------------------------- 12b --
    rule("12b. DEGRADATION: neither the CLI nor the organisation harvest has run")
    bare_iface = write_fixture(tmp, "no-interfaces", strip_interface_layers(live))
    print("   fixture: every cli_* and github_org_* field reset to not-checked, summaries unstamped, restamped")
    async with Client(spawn(bare_iface)) as client:
        body = payload(await client.call_tool("whats_building", {}))
        print("   whats_building: status=%s counts=%s" % (body["status"], body["counts"]))
        print("   message:        %s" % trim(body["message"], 240))
        check("unmeasured org layer: status says not measured", body["status"] == "not measured", body["status"])
        check("unmeasured org layer: counts are null, not zero", all(
            body["counts"][k] is None for k in ("resolved", "unresolved", "no_github_signal", "not_checked", "silent_total", "checked_on")
        ), body["counts"])
        check("unmeasured org layer: the sentence says so", "has not been measured" in body["message"])

        body = payload(await client.call_tool("whats_building", {"name": "Apify"}))
        print("   whats_building(Apify): status=%s repos=%s" % (body["github_org_status"], body["repos"]))
        check("unmeasured org layer: a vendor lookup carries null counts", body["repos"]["public_non_fork"] is None)
        check("unmeasured org layer: a vendor lookup says so", "not been measured" in body["message"])

        body = payload(await client.call_tool("get_install", {"name": "ZoomInfo"}))
        print("   get_install(ZoomInfo) cli route: %s" % trim(body["cli"]["route"], 200))
        check("unmeasured CLI layer: get_install says the layer has not been measured", "has not been measured" in body["cli"]["route"])
        check("unmeasured CLI layer: the MCP route still answers", body["mcp"]["endpoint_status"] is not None)
        check("unmeasured CLI layer: the recommendation still names both routes", body["recommendation"].startswith("MCP:") and "CLI:" in body["recommendation"])

        body = payload(await client.call_tool("find_tools", {"interface": "cli", "limit": 5}))
        print("   find_tools(interface=cli): match_count=%s note=%s" % (body["match_count"], trim(body["filter_notes"][0] if body["filter_notes"] else "", 200)))
        check("unmeasured CLI layer: interface=cli keeps nothing and says why", body["match_count"] == 0 and any("has not been measured" in n for n in body["filter_notes"]))
        check("unmeasured CLI layer: the summary says not measured", "has not been measured" in body["summary"])

        body = payload(await client.call_tool("find_tools", {"interface": "either", "limit": 1}))
        print("   find_tools(interface=either): match_count=%s" % body["match_count"])
        check("unmeasured CLI layer: interface=either reduces to MCP", body["match_count"] == EXPECTED["official"] + sum(
            1 for e in live["entries"] if e.get("mcp_status_bucket") == "community"), body["match_count"])

        body = payload(await client.call_tool("plan_stack", {"goal": PLAN_GOAL, "prefer_interface": "cli"}))
        print("   plan_stack(prefer cli): %s" % trim(body["interface_preference"]["note"], 200))
        check("unmeasured CLI layer: plan_stack says the preference changes nothing", "has not been measured" in (body["interface_preference"]["note"] or ""))
        check("unmeasured CLI layer: plan summary carries null, not zero", body["summary"]["steps_with_a_cli_route"] is None and body["summary"]["cli_measured_on"] is None)


def run_startup_gate(tmp: Path) -> None:
    """The server must refuse to start on drifted data. Prove it, do not claim it."""
    import subprocess

    from gtm_mcp_directory.loading import resolve_data_path

    rule("13. STARTUP GATE: the server refuses to serve drifted data")
    live = resolve_data_path()
    payload_json = json.loads(live.read_text(encoding="utf-8"))
    gate = tmp / "gate"
    gate.mkdir(parents=True, exist_ok=True)
    (gate / "build_report.json").write_text(
        (live.parent / "build_report.json").read_text(encoding="utf-8"), encoding="utf-8"
    )

    edited = json.loads(json.dumps(payload_json))
    edited["entries"][0]["what_it_does"] = "EDITED BY HAND AFTER THE BUILD"
    (gate / "directory.json").write_text(
        json.dumps(edited, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    short = json.loads(json.dumps(payload_json))
    short["entries"] = short["entries"][:290]
    short["counts"]["entries"] = 290
    (gate / "short.json").write_text(
        json.dumps(short, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (gate / "bad.json").write_text("not json at all", encoding="utf-8")

    cases = [
        ("missing file", gate / "does-not-exist.json", "Refusing to silently fall back"),
        ("hand-edited entry", gate / "directory.json", "Content checksum mismatch"),
        ("wrong entry count", gate / "short.json", "Entry count mismatch"),
        ("unparseable JSON", gate / "bad.json", "is not valid JSON"),
    ]
    for label, path, needle in cases:
        env = dict(os.environ)
        env["GTM_DIRECTORY_DATA"] = str(path)
        env.pop("GTM_DIRECTORY_ALLOW_CHECKSUM_DRIFT", None)
        proc = subprocess.run(
            [sys.executable, "-m", "gtm_mcp_directory"],
            cwd=str(HERE),
            env=env,
            stdin=subprocess.DEVNULL,
            capture_output=True,
            text=True,
            timeout=60,
        )
        print("   %-20s exit=%s  %s" % (label, proc.returncode, trim(proc.stderr.strip().splitlines()[0] if proc.stderr.strip() else "", 100)))
        check("%s fails loudly" % label, proc.returncode != 0, "exit=%s" % proc.returncode)
        check("%s explains itself" % label, needle in proc.stderr)


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001 - older interpreters, cosmetic only
        pass
    sys.path.insert(0, str(HERE))
    print("The GTM MCP Directory: stdio smoke test")
    print("spawning: %s -m gtm_mcp_directory (cwd=%s)" % (sys.executable, HERE))
    asyncio.run(run())

    import tempfile

    with tempfile.TemporaryDirectory(prefix="gtm-mcp-qa-") as tmp:
        asyncio.run(run_degradation(Path(tmp)))
        run_startup_gate(Path(tmp))
    rule("RESULT")
    print("   %d checks, %d failures" % (CHECKS, len(FAILURES)))
    if FAILURES:
        for f in FAILURES:
            print("   FAILED: %s" % f)
        return 1
    print("   ALL GREEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
