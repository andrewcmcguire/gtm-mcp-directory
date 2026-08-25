"""Smoke test: spawn the server over stdio and exercise every tool with real queries.

Run it from this directory:

    python qa_stdio.py

It spawns `python -m gtm_mcp_directory` as a real subprocess, speaks MCP over
stdio to it, calls all seven tools, prints trimmed output, and asserts the
things that are load-bearing:

- every tool is registered and callable
- every response carries honesty.tier and honesty.last_checked
- every response carries the job-tag meaning line
- "enrich a linkedin profile url" returns tools that actually do that
- the counts match the build report
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

REQUIRED_TOOLS = [
    "find_tools",
    "get_tool",
    "list_categories",
    "whats_mcpd",
    "find_by_gate",
    "get_docs_digest",
    "list_jobs",
]


def check(label: str, condition: bool, detail: str = "") -> None:
    global CHECKS
    CHECKS += 1
    if condition:
        print("   PASS  %s" % label)
    else:
        print("   FAIL  %s %s" % (label, detail))
        FAILURES.append(label + (" " + detail if detail else ""))


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
        check("entry total is 293", body["entries"] == 293, body["entries"])
        check("official is 144", body["official"] == 144, body["official"])
        check("solo_reachable is 117", body["solo_reachable"] == 117, body["solo_reachable"])
        check("bench_tested is 0 and is not hidden", body["bench_tested"] == 0)

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
        check("category scope narrows the set", body["entries"] == 23, body["entries"])

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
        check("free gate count is 57", body["match_count"] == 57, body["match_count"])

        body = payload(
            await client.call_tool("find_by_gate", {"gate": "enterprise only", "limit": 3})
        )
        print("   alias 'enterprise only' -> %s, %d matches" % (body["gate"], body["match_count"]))
        check("gate aliases normalize", body["gate"] == "enterprise-only")
        check("enterprise-only count is 45", body["match_count"] == 45, body["match_count"])

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
            any("0 of 293" in c for c in body["honesty"]["caveats"]),
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
    print("   fixture: 55-job vocabulary kept, every jobs[] tag removed, restamped")
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
