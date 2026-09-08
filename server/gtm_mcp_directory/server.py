"""The GTM MCP Directory MCP server.

Eleven read-only tools over a directory of GTM tools, answering the question
nobody else answers honestly: which of these can an agent actually call, and
what does it cost to get in.

  find_tools        which tools claim a job, and by which interface (MCP, CLI)
  get_tool          one entry, every field, every source URL
  list_categories   the 15 categories with counts and gates
  whats_mcpd        the market statistics
  find_by_gate      the access axis on its own
  get_docs_digest   structured facts from vendor API docs, when crawled
  get_server_tools  what one MCP server actually exposes
  get_install       both routes into one tool: the MCP endpoint and the CLI
  whats_building    what vendors ship in public on GitHub, dated
  plan_stack        a step-by-step shortlist for a multi-step GTM job
  list_jobs         the closed capability vocabulary

No write tools. No telemetry. No outbound requests. No featured field.
"""

from __future__ import annotations

import datetime as dt
import os
import re
import sys
from typing import Any, Optional

from fastmcp import FastMCP

from . import PRODUCT_NAME, REPO, SERVER_NAME, SERVER_VERSION, UMBRELLA
from .honesty import (
    CLI_LAYER_UNMEASURED,
    ORG_LAYER_UNMEASURED,
    HonestyBuilder,
    cli_caveats,
    entry_honesty,
    github_org_caveats,
)
from .loading import Directory, DirectoryDataError, load_directory
from .search import (
    ORDERING_DISCLOSURE_DISPLAY,
    ORDERING_DISCLOSURE_RELEVANCE,
    CLI_STATUS_VALUES,
    GATE_VALUES,
    INTERFACE_VALUES,
    MCP_STATUS_VALUES,
    cli_install_view,
    has_cli,
    has_mcp,
    match_name,
    normalize_cli_status,
    normalize_gate,
    normalize_interface,
    normalize_status,
    order,
    relevance_floor,
    result_row,
    score_entry,
    tokenize,
)
from .vocabulary import Vocabulary, load_vocabulary

INSTRUCTIONS = """
{product}, part of {umbrella}.

A local, offline directory of GTM tools scored on one axis nobody else
publishes: can an agent actually call this, and what does it cost to get in.

Use find_tools for "which tool can do X" (interface="cli" or "mcp" narrows it
to one kind of interface). Use get_install for everything needed to start
using one tool: its MCP endpoint and its CLI install commands, each quoted
from a source on a date. Use whats_building for what a vendor ships in public
on GitHub. Use whats_mcpd for the state of the market. Use list_categories to
browse and list_jobs to learn the capability vocabulary before asking
precisely.

Read the honesty block on every response. Two tiers exist. RESEARCHED means
the facts came from public sources with URLs and nobody has run the tool.
BENCH-TESTED means a human ran it on a stated date. A job tag means the vendor
says the tool does this; it is never a test result.

This server makes zero outbound requests. Everything is served from a
directory baked on {generated}.
""".strip()


# ---------------------------------------------------------------------------
# Startup: load once, verify loudly, then never touch the disk again.
# ---------------------------------------------------------------------------
try:
    DIRECTORY: Directory = load_directory()
except DirectoryDataError as exc:
    print("FATAL: %s" % exc, file=sys.stderr)
    raise SystemExit(2) from exc

VOCAB: Vocabulary = load_vocabulary(DIRECTORY.data_path, DIRECTORY.payload)
HONESTY = HonestyBuilder(DIRECTORY, VOCAB)
ENTRIES: list[dict[str, Any]] = DIRECTORY.entries

mcp = FastMCP(
    name=SERVER_NAME,
    version=SERVER_VERSION,
    instructions=INSTRUCTIONS.format(
        product=PRODUCT_NAME, umbrella=UMBRELLA, generated=DIRECTORY.generated_on
    ),
)


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def _meta(extra: dict[str, Any] | None = None) -> dict[str, Any]:
    meta = HONESTY.server_meta()
    if extra:
        meta.update(extra)
    return meta


def _bucket_counts(entries: list[dict[str, Any]], field: str, values: tuple[str, ...]) -> dict[str, int]:
    out = {v: 0 for v in values}
    for e in entries:
        key = e.get(field)
        if key in out:
            out[key] += 1
        else:
            out.setdefault("other", 0)
            out["other"] += 1
    return out


def _solo_reachable(entries: list[dict[str, Any]]) -> int:
    """Official or community MCP AND a gate an individual can pass alone."""
    return sum(
        1
        for e in entries
        if e.get("mcp_status_bucket") in ("official", "community")
        and e.get("api_gate_bucket") in ("free", "paid")
    )


def _summary_sentence(entries: list[dict[str, Any]], subject: str) -> str:
    if not entries:
        tail = "" if HONESTY.cli_measured else " The CLI layer has not been measured on this build."
        return "Nothing in the directory matched %s.%s" % (subject, tail)
    n = len(entries)
    status = _bucket_counts(entries, "mcp_status_bucket", MCP_STATUS_VALUES)
    gates = _bucket_counts(entries, "api_gate_bucket", GATE_VALUES)
    bench = sum(1 for e in entries if e.get("tier") == "BENCH-TESTED")
    parts = [
        "%d %s matched %s." % (n, "tool" if n == 1 else "tools", subject),
        "%d have an official MCP server, %d community, %d none found, %d unknown."
        % (
            status.get("official", 0),
            status.get("community", 0),
            status.get("none-found", 0),
            status.get("unknown", 0),
        ),
        "On access: %d free, %d paid, %d enterprise-only, %d unknown."
        % (
            gates.get("free", 0),
            gates.get("paid", 0),
            gates.get("enterprise-only", 0),
            gates.get("unknown", 0),
        ),
        "%d are solo-reachable (an MCP server plus a gate you can pass without "
        "a sales call)." % _solo_reachable(entries),
    ]
    parts.append(
        "None have been bench-tested."
        if bench == 0
        else "%d have been bench-tested." % bench
    )
    if HONESTY.cli_measured:
        cli = _bucket_counts(entries, "cli_status", CLI_STATUS_VALUES)
        parts.append(
            "On the command line: %d have a first-party CLI, %d a community one, "
            "%d none found, %d not yet checked (measured %s)."
            % (
                cli.get("official", 0),
                cli.get("community", 0),
                cli.get("none-found", 0),
                cli.get("not-checked", 0) + cli.get("other", 0),
                HONESTY.cli_checked_on,
            )
        )
    else:
        parts.append("The CLI layer has not been measured on this build.")
    return " ".join(parts)


def _apply_filters(
    entries: list[dict[str, Any]],
    category: Optional[str],
    mcp_status: Optional[str],
    gate: Optional[str],
    tier: Optional[str],
    has_github: Optional[bool],
    has_github_candidate: Optional[bool],
    canonical_only: Optional[bool],
    interface: Optional[str] = None,
    cli_status: Optional[str] = None,
) -> tuple[list[dict[str, Any]], dict[str, Any], list[str]]:
    applied: dict[str, Any] = {}
    notes: list[str] = []
    out = entries

    if cli_status:
        norm = normalize_cli_status(cli_status)
        if norm is None:
            notes.append(
                "cli_status '%s' is not in the vocabulary %s, so the filter was "
                "ignored." % (cli_status, list(CLI_STATUS_VALUES))
            )
        else:
            out = [e for e in out if (e.get("cli_status") or "not-checked") == norm]
            applied["cli_status"] = norm
            if not HONESTY.cli_measured:
                notes.append(
                    CLI_LAYER_UNMEASURED
                    + " cli_status='%s' therefore keeps %s."
                    % (norm, "every entry" if norm == "not-checked" else "nothing")
                )
            elif norm == "none-found":
                notes.append(
                    "none-found is what the CLI harvest found on %s across vendor "
                    "docs, npm, PyPI, Homebrew and GitHub. It is not proof that "
                    "these vendors ship no CLI." % HONESTY.cli_checked_on
                )
            elif norm == "not-checked":
                notes.append(
                    "not-checked means the CLI harvest of %s did not reach these "
                    "entries. Unmeasured, not a finding." % HONESTY.cli_checked_on
                )

    if interface:
        norm = normalize_interface(interface)
        if norm is None:
            notes.append(
                "interface '%s' is not one of %s, so the filter was ignored."
                % (interface, list(INTERFACE_VALUES))
            )
        else:
            before = len(out)
            if norm == "mcp":
                out = [e for e in out if has_mcp(e)]
            elif norm == "cli":
                out = [e for e in out if has_cli(e)]
            else:
                out = [e for e in out if has_mcp(e) or has_cli(e)]
            applied["interface"] = norm
            if norm in ("cli", "either") and not HONESTY.cli_measured:
                notes.append(
                    CLI_LAYER_UNMEASURED
                    + (
                        " interface='cli' keeps nothing on this build."
                        if norm == "cli"
                        else " interface='either' reduces to the MCP layer on this build."
                    )
                )
            elif norm in ("cli", "either"):
                notes.append(
                    "interface='%s' kept %d of %d entries. The CLI layer was measured "
                    "on %s: an entry dropped here has cli_status none-found (the "
                    "harvest found nothing that day) or not-checked (the harvest did "
                    "not reach it), and neither is proof that the vendor ships no CLI."
                    % (norm, len(out), before, HONESTY.cli_checked_on)
                )
            else:
                notes.append(
                    "interface='mcp' kept %d of %d entries whose mcp_status is official "
                    "or community. That is the research finding, not liveness; add "
                    "live_endpoint_only=true for a URL that answered as a server."
                    % (len(out), before)
                )

    if category:
        cat = DIRECTORY.category(category)
        if cat is None:
            notes.append(
                "category '%s' is not one of the 15 category slugs, so the "
                "filter was ignored. Valid slugs: %s."
                % (category, ", ".join(DIRECTORY.category_slugs))
            )
        else:
            out = [e for e in out if e.get("category_slug") == cat["slug"]]
            applied["category"] = cat["slug"]

    if mcp_status:
        norm = normalize_status(mcp_status)
        if norm is None:
            notes.append(
                "mcp_status '%s' is not in the vocabulary %s, so the filter was "
                "ignored." % (mcp_status, list(MCP_STATUS_VALUES))
            )
        else:
            out = [e for e in out if e.get("mcp_status_bucket") == norm]
            applied["mcp_status"] = norm

    if gate:
        norm = normalize_gate(gate)
        if norm is None:
            notes.append(
                "gate '%s' is not in the vocabulary %s, so the filter was "
                "ignored." % (gate, list(GATE_VALUES))
            )
        else:
            out = [e for e in out if e.get("api_gate_bucket") == norm]
            applied["gate"] = norm

    if tier:
        norm = tier.strip().upper().replace("_", "-")
        out = [e for e in out if (e.get("tier") or "").upper() == norm]
        applied["tier"] = norm
        if norm == "BENCH-TESTED":
            notes.append(
                "0 of %d entries are BENCH-TESTED. Nobody has run these tools "
                "yet, so this filter is expected to return nothing."
                % HONESTY.total
            )

    if has_github is not None:
        out = [e for e in out if bool(e.get("github_url")) is bool(has_github)]
        applied["has_github"] = bool(has_github)
        if has_github and HONESTY.with_github == 0:
            notes.append(
                "github_url has never been measured (0 of %d entries). This "
                "filter returns nothing today. %d entries do carry "
                "github_candidates[] parsed out of mcp_url and sources; use "
                "has_github_candidate=true for that lead list, and treat it as "
                "a lead list, not a measurement."
                % (
                    HONESTY.total,
                    sum(1 for e in ENTRIES if e.get("github_candidates")),
                )
            )

    if has_github_candidate is not None:
        out = [
            e
            for e in out
            if bool(e.get("github_candidates")) is bool(has_github_candidate)
        ]
        applied["has_github_candidate"] = bool(has_github_candidate)
        notes.append(
            "github_candidates[] are github.com URLs parsed out of mcp_url and "
            "sources at build time. They have never been fetched or verified."
        )

    if canonical_only:
        out = [e for e in out if e.get("canonical")]
        applied["canonical_only"] = True

    return out, applied, notes


# ---------------------------------------------------------------------------
# 1. find_tools
# ---------------------------------------------------------------------------
@mcp.tool
def find_tools(
    job_or_query: Optional[str] = None,
    category: Optional[str] = None,
    mcp_status: Optional[str] = None,
    gate: Optional[str] = None,
    tier: Optional[str] = None,
    has_github: Optional[bool] = None,
    has_github_candidate: Optional[bool] = None,
    canonical_only: Optional[bool] = None,
    live_endpoint_only: Optional[bool] = None,
    tool_query: Optional[str] = None,
    interface: Optional[str] = None,
    cli_status: Optional[str] = None,
    limit: int = 20,
) -> dict[str, Any]:
    """Find GTM tools by capability, and say whether an agent can actually reach them.

    `job_or_query` takes either a job slug from the controlled vocabulary
    (see list_jobs) or plain natural language such as "enrich a linkedin
    profile url". The response always states what it resolved to and how. If
    it resolves to nothing it says so and hands back the vocabulary rather
    than returning a silent empty list.

    Filters: category (one of the 15 slugs), mcp_status
    (official/community/none-found/unknown/n-a), gate
    (free/paid/enterprise-leaning/enterprise-only/unknown/n-a), tier
    (RESEARCHED/BENCH-TESTED), has_github, has_github_candidate,
    canonical_only (drop the 16 cross-listed second entries),
    live_endpoint_only (keep only entries whose recorded MCP URL answered as
    a server on the last probe: endpoint_status live or live-auth-gated. This
    is liveness, not a test of the tools; a docs-only entry may still have a
    perfectly good server at a URL the directory does not record),
    tool_query (match against the ACTUAL tool names and descriptions each
    server exposes, rather than the vendor's description of the product. This
    is the capability layer: "linkedin url", "verify email", "create deal".
    Only servers whose tool list has been harvested can match, so a miss means
    unmeasured as often as it means absent; the response says which),
    interface ("mcp", "cli" or "either": keep entries an agent can reach by
    that kind of interface. "mcp" keeps official or community MCP servers,
    "cli" keeps entries whose cli_status is official or community, "either"
    keeps entries with at least one. An entry dropped by "cli" has cli_status
    none-found or not-checked: none-found is what the harvest found on
    cli_checked_on, not-checked means the harvest did not reach it, and
    neither is proof that the vendor ships no CLI),
    cli_status (official/community/none-found/not-checked, the direct filter
    on the command-line layer. official is a first-party source, community is
    a third party's wrapper, and the same reading of none-found applies).

    Each result carries its CLI fields (cli_status, cli_binary, the first two
    cli_install commands with the source_url and date each was quoted from)
    and its vendor organisation fields (github_org, github_org_repos,
    github_org_latest_activity, dated). get_install returns every install
    command for one tool.
    """
    limit = max(1, min(int(limit or 20), 100))
    query = (job_or_query or "").strip()

    resolved: list[dict[str, Any]] = VOCAB.resolve(query) if query else []
    tagged_slugs = {j for e in ENTRIES for j in (e.get("jobs") or [])}

    # Only the best resolution, plus anything scoring within 5 percent of it,
    # actually filters. Weaker candidates are reported so the caller can see
    # them and re-ask, but they do not quietly widen the answer.
    if resolved:
        cutoff = resolved[0]["score"] * 0.95
        accepted = [r for r in resolved if r["score"] >= cutoff]
    else:
        accepted = []
    also_considered = [r for r in resolved if r not in accepted]
    usable = [r for r in accepted if r["job"] in tagged_slugs]

    pool, applied, filter_notes = _apply_filters(
        ENTRIES,
        category,
        mcp_status,
        gate,
        tier,
        has_github,
        has_github_candidate,
        canonical_only,
        interface=interface,
        cli_status=cli_status,
    )
    if tool_query:
        q = tool_query.strip().lower()
        terms = [t for t in re.split(r"[^a-z0-9]+", q) if len(t) > 2]
        before = len(pool)
        harvested = [e for e in pool if e.get("mcp_tool_count")]
        hits = []
        for e in harvested:
            matched = []
            for t in e.get("mcp_tools") or []:
                blob = ((t.get("name") or "") + " " + (t.get("description") or "")).lower()
                if q in blob or (terms and all(term in blob for term in terms)):
                    matched.append(t.get("name"))
            if matched:
                hits.append((e, matched))
        pool = [e for e, _ in hits]
        applied["tool_query"] = tool_query
        tool_matches = {e["id"]: m for e, m in hits}
        filter_notes.append(
            "tool_query matched the tool lists of %d servers out of %d in scope, of which %d "
            "have a harvested tool list at all. A server with no harvested list cannot match: "
            "that is unmeasured, not a statement that it lacks the capability."
            % (len(pool), before, len(harvested))
        )
    else:
        tool_matches = {}

    if live_endpoint_only:
        before = len(pool)
        pool = [e for e in pool if e.get("endpoint_status") in ("live", "live-auth-gated")]
        applied["live_endpoint_only"] = True
        filter_notes.append(
            "live_endpoint_only kept %d of %d entries whose recorded MCP URL "
            "answered an initialize as a server on the last probe. Entries "
            "marked docs-only or not-probed were dropped; that is a statement "
            "about the URL the directory records, not about the vendor."
            % (len(pool), before)
        )

    by_relevance = False
    text_fallback = False
    matched: list[dict[str, Any]] = []
    scored: list[dict[str, Any]] = []
    tokens: list[str] = []
    fallback_reason: Optional[str] = None

    if not query:
        mode = "filters-only"
        matched = list(pool)
        scored = [{"entry": e, "_hits": 0, "_score": 0.0, "_terms": []} for e in matched]
    elif usable:
        mode = "job-tags"
        wanted = {r["job"] for r in usable}
        matched = [e for e in pool if wanted & set(e.get("jobs") or [])]
        scored = [{"entry": e, "_hits": 0, "_score": 0.0, "_terms": []} for e in matched]
    else:
        mode = "text-search"
        text_fallback = True
        by_relevance = True
        if accepted:
            fallback_reason = (
                "Your query resolved to the job slug(s) %s, but 0 of %d entries "
                "carry a jobs[] tag yet (SPEC 2.4 phase 2 has not run on this "
                "install). The search fell back to a literal text match over "
                "each vendor's own description."
                % (", ".join(r["job"] for r in accepted), HONESTY.total)
            )
        elif VOCAB:
            fallback_reason = (
                "Your query did not resolve to any slug in the %d-job "
                "vocabulary, so the search fell back to a literal text match "
                "over each vendor's own description. Call list_jobs to see the "
                "vocabulary." % len(VOCAB.jobs)
            )
        elif VOCAB.path is not None:
            fallback_reason = (
                "A jobs.yaml exists on this install but no usable vocabulary "
                "could be read from it (%s), so the search is a literal text "
                "match over each vendor's own description of itself."
                % VOCAB.note
            )
        else:
            fallback_reason = (
                "No jobs vocabulary is installed (jobs.yaml, SPEC 2.4, is phase "
                "2 and has not landed here), so the search is a literal text "
                "match over each vendor's own description of itself."
            )

        # The words the caller actually typed decide WHETHER an entry matches.
        # A resolved job's aliases and one-liner only help RANK the matches, so
        # a wide vocabulary entry cannot quietly widen the result set.
        core_tokens = tokenize(query)
        search_text = query
        for r in accepted:
            search_text += " " + VOCAB.search_text_for(r["job"])
        tokens = tokenize(search_text)
        floor = relevance_floor(core_tokens)
        weak = 0
        for e in pool:
            core_hits, _, core_terms = score_entry(e, core_tokens)
            if core_hits >= floor:
                _, sc, terms = score_entry(e, tokens)
                scored.append(
                    {
                        "entry": e,
                        "_hits": core_hits,
                        "_score": sc,
                        "_terms": core_terms,
                    }
                )
            elif core_hits:
                weak += 1
        matched = [r["entry"] for r in scored]
        if weak:
            filter_notes.append(
                "%d further entries matched only one of your query terms and "
                "were held back as too weak to call a match." % weak
            )

    ordered = order(scored, by_relevance)
    shown = ordered[:limit]

    results = [
        result_row(
            r["entry"],
            entry_honesty(r["entry"]),
            matched_terms=r["_terms"] if by_relevance else None,
            relevance=r["_score"] if by_relevance else None,
        )
        for r in shown
    ]

    subject = "'%s'" % query if query else "your filters"
    query_resolved: dict[str, Any] = {
        "input": job_or_query,
        "mode": mode,
        "vocabulary": VOCAB.status(),
        "resolved_jobs": accepted,
        "also_considered": also_considered,
        "resolution_rule": (
            "The best-scoring job, plus any within 5 percent of it, filters the "
            "results. Weaker candidates are listed in also_considered so you "
            "can re-ask precisely rather than being handed a widened answer."
        ),
        "matched_from": job_or_query,
        "confidence": accepted[0]["confidence"] if accepted else "none",
        "search_terms_used": tokens,
    }
    if fallback_reason:
        query_resolved["fallback"] = fallback_reason
    if query and not resolved and VOCAB:
        query_resolved["vocabulary_hint"] = (
            "Call list_jobs to read the closed vocabulary. An agent cannot "
            "guess a closed vocabulary, so ask once and then ask precisely."
        )

    return {
        "query_resolved": query_resolved,
        "filters_applied": applied,
        "filter_notes": filter_notes,
        "match_count": len(matched),
        "returned": len(results),
        "not_returned": "%d result(s) were trimmed by limit=%d."
        % (max(0, len(matched) - len(results)), limit),
        "sort": ORDERING_DISCLOSURE_RELEVANCE if by_relevance else ORDERING_DISCLOSURE_DISPLAY,
        "results": results,
        "summary": _summary_sentence(matched, subject),
        "server": _meta(),
        "honesty": HONESTY.envelope(
            matched,
            capability=True,
            text_fallback=text_fallback,
            scope_note="Capability answer for %s." % subject,
        ),
    }


# ---------------------------------------------------------------------------
# 2. get_tool
# ---------------------------------------------------------------------------
@mcp.tool
def get_tool(name: str) -> dict[str, Any]:
    """Return one tool's full entry, every field and every source URL.

    Fuzzy-matches the name. On ambiguity it returns the candidates instead of
    picking one for you. If the product is listed in more than one category it
    names the canonical entry so you never count one product twice.
    """
    candidates, how = match_name(ENTRIES, name)

    if not candidates:
        return {
            "query": name,
            "status": "not found",
            "match_method": how,
            "message": (
                "No tool in the directory matched '%s'. The directory holds %d "
                "entries covering %d unique products; a tool being absent means "
                "it has not been researched yet, not that it does not exist."
                % (name, HONESTY.total, HONESTY.server_meta()["unique_products"])
            ),
            "did_you_mean": [],
            "server": _meta(),
            "honesty": HONESTY.envelope([], scope_note="Lookup for '%s'." % name),
        }

    if len(candidates) > 1:
        # Cross-listed duplicates of the SAME product are not real ambiguity.
        canon = {c.get("canonical_id") for c in candidates}
        if len(canon) == 1:
            candidates = [c for c in candidates if c.get("canonical")] or candidates[:1]

    if len(candidates) > 1:
        return {
            "query": name,
            "status": "ambiguous",
            "match_method": how,
            "message": (
                "'%s' matched %d entries. Naming one for you would be a guess, "
                "so here are the candidates." % (name, len(candidates))
            ),
            "candidates": [
                {
                    "id": c.get("id"),
                    "name": c.get("name"),
                    "category": c.get("category_slug"),
                    "mcp_status": c.get("mcp_status_bucket"),
                    "api_gate": c.get("api_gate_bucket"),
                    "what_it_does": c.get("what_it_does"),
                }
                for c in sorted(
                    candidates, key=lambda c: c.get("display_rank", 10**6)
                )
            ],
            "server": _meta(),
            "honesty": HONESTY.envelope(
                candidates, scope_note="Ambiguous lookup for '%s'." % name
            ),
        }

    entry = candidates[0]
    full = {k: v for k, v in entry.items()}
    full["honesty"] = entry_honesty(entry)

    cross = None
    if entry.get("also_listed_in"):
        canonical = DIRECTORY.by_id(entry.get("canonical_id") or "")
        cross = {
            "canonical_id": entry.get("canonical_id"),
            "canonical_name": canonical.get("name") if canonical else None,
            "this_entry_is_canonical": bool(entry.get("canonical")),
            "also_listed_in": entry.get("also_listed_in"),
            "note": (
                "This product appears in more than one category file on "
                "purpose; the entries say different things about different "
                "sides of the product. They are one product. Count the "
                "canonical id."
            ),
        }

    return {
        "query": name,
        "status": "ok",
        "match_method": how,
        "entry": full,
        "cross_listing": cross,
        "docs": {
            "docs_url": entry.get("docs_url"),
            "digest_available": bool(entry.get("docs_digest")),
            "how_to_get_it": "Call get_docs_digest with this tool's name.",
        },
        "server": _meta(),
        "honesty": HONESTY.envelope(
            [entry], capability=True, scope_note="Full entry for %s." % entry.get("name")
        ),
    }


# ---------------------------------------------------------------------------
# 3. list_categories
# ---------------------------------------------------------------------------
@mcp.tool
def list_categories() -> dict[str, Any]:
    """The 15 categories with entry counts, MCP breakdowns and access gates.

    Counts come from directory.json, which is reconciled against
    tools_recount.py at build time. If the two ever disagree the build fails
    rather than publishing a drifted number.
    """
    cats = []
    for cat in DIRECTORY.categories:
        members = [e for e in ENTRIES if e.get("category_slug") == cat["slug"]]
        job_counts: dict[str, int] = {}
        for e in members:
            for j in e.get("jobs") or []:
                job_counts[j] = job_counts.get(j, 0) + 1
        top_jobs = [
            j for j, _ in sorted(job_counts.items(), key=lambda kv: (-kv[1], kv[0]))[:5]
        ]
        status = cat["mcp_status"]
        reachable = status.get("official", 0) + status.get("community", 0)
        cats.append(
            {
                "num": cat["num"],
                "slug": cat["slug"],
                "label": cat["label"],
                "file": cat["file"],
                "one_line": cat["one_line"],
                "total": cat["total"],
                "official": status.get("official", 0),
                "community": status.get("community", 0),
                "none_found": status.get("none-found", 0),
                "unknown": status.get("unknown", 0),
                "n_a": status.get("n-a", 0),
                "mcp_reachable": reachable,
                "mcp_reachable_ratio": "%d/%d" % (reachable, cat["total"]),
                "gates": {
                    "free": cat["api_gate"].get("free", 0),
                    "paid": cat["api_gate"].get("paid", 0),
                    "enterprise_leaning": cat["api_gate"].get("enterprise-leaning", 0),
                    "enterprise_only": cat["api_gate"].get("enterprise-only", 0),
                    "unknown": cat["api_gate"].get("unknown", 0),
                    "n_a": cat["api_gate"].get("n-a", 0),
                },
                "solo_reachable": _solo_reachable(members),
                "top_jobs": top_jobs,
                "top_jobs_note": (
                    None
                    if top_jobs
                    else "No job tags exist in this category yet, so there is "
                    "nothing to rank. This is an unbuilt layer, not an empty "
                    "category."
                ),
            }
        )

    return {
        "generated": DIRECTORY.generated_on,
        "total_entries": HONESTY.total,
        "unique_products": HONESTY.server_meta()["unique_products"],
        "cross_listed_entries": DIRECTORY.counts.get("cross_listed_entries"),
        "category_count": len(cats),
        "counted_by": "tools_recount.py, reconciled at build time",
        "categories": cats,
        "server": _meta(),
        "honesty": HONESTY.envelope(
            ENTRIES,
            scope_note="All 15 categories.",
            include_source_urls=False,
        ),
    }


# ---------------------------------------------------------------------------
# 4. whats_mcpd
# ---------------------------------------------------------------------------
@mcp.tool
def whats_mcpd(
    category: Optional[str] = None, job: Optional[str] = None
) -> dict[str, Any]:
    """The stats tool: how much of GTM is actually reachable by an agent.

    Official, community, none-found and unknown MCP counts, access gates, the
    solo-reachable count, the bench-tested count, and the most and least
    MCP-covered categories. Optionally scoped to one category or one job.
    """
    scope = "all"
    basis = "all-entries"
    notes: list[str] = []
    text_fallback = False
    pool = ENTRIES

    if category:
        cat = DIRECTORY.category(category)
        if cat is None:
            notes.append(
                "category '%s' is not one of the 15 slugs, so the scope stayed "
                "at all entries. Valid slugs: %s."
                % (category, ", ".join(DIRECTORY.category_slugs))
            )
        else:
            pool = [e for e in pool if e.get("category_slug") == cat["slug"]]
            scope = "category:%s-%s" % (cat["num"], cat["slug"])
            basis = "category"

    if job:
        resolved = VOCAB.resolve(job)
        slugs = {r["job"] for r in resolved} or {job.strip()}
        tagged = [e for e in pool if slugs & set(e.get("jobs") or [])]
        if tagged:
            pool = tagged
            scope = "job:%s" % ",".join(sorted(slugs))
            basis = "job-tags"
        else:
            core_tokens = tokenize(job)
            floor = relevance_floor(core_tokens)
            hits = []
            for e in pool:
                h, _, _ = score_entry(e, core_tokens)
                if h >= floor:
                    hits.append(e)
            pool = hits
            scope = "job:%s" % ",".join(sorted(slugs))
            basis = "text-match"
            text_fallback = True
            notes.append(
                "No entry carries a jobs[] tag yet, so this scope was built by "
                "text-matching '%s' against each vendor's own description. "
                "These percentages describe a text-match set, not a tagged set."
                % job
            )

    status = _bucket_counts(pool, "mcp_status_bucket", MCP_STATUS_VALUES)
    gates = _bucket_counts(pool, "api_gate_bucket", GATE_VALUES)
    total = len(pool)
    official_pct = round(100.0 * status.get("official", 0) / total, 1) if total else 0.0
    reachable = status.get("official", 0) + status.get("community", 0)
    reachable_pct = round(100.0 * reachable / total, 1) if total else 0.0

    ratios = []
    for cat in DIRECTORY.categories:
        s = cat["mcp_status"]
        r = s.get("official", 0) + s.get("community", 0)
        if cat["total"]:
            ratios.append((r / cat["total"], r, cat["total"], cat["slug"], cat["label"]))
    ratios.sort()
    most = ratios[-1] if ratios else None
    least = ratios[0] if ratios else None
    sdr = next((r for r in ratios if r[3] == "ai-sdr-agents"), None)

    headline_bits = []
    if most and least:
        headline_bits.append(
            "%s is %d of %d MCP-reachable. %s is %d of %d."
            % (most[4], most[1], most[2], least[4], least[1], least[2])
        )
    if sdr:
        headline_bits.append(
            "The tools sold AS agents, the AI SDRs, are %d of %d."
            % (sdr[1], sdr[2])
        )
    headline_bits.append(
        "Across all %d entries, %d have an official MCP server (%.1f percent) "
        "and %d are solo-reachable."
        % (
            HONESTY.total,
            DIRECTORY.counts["mcp_status"].get("official", 0),
            round(
                100.0
                * DIRECTORY.counts["mcp_status"].get("official", 0)
                / HONESTY.total,
                1,
            ),
            _solo_reachable(ENTRIES),
        )
    )

    return {
        "scope": scope,
        "scope_basis": basis,
        "scope_notes": notes,
        "entries": total,
        "official": status.get("official", 0),
        "community": status.get("community", 0),
        "none_found": status.get("none-found", 0),
        "unknown": status.get("unknown", 0),
        "n_a": status.get("n-a", 0),
        "official_pct": official_pct,
        "mcp_reachable": reachable,
        "mcp_reachable_pct": reachable_pct,
        "gates": {
            "free": gates.get("free", 0),
            "paid": gates.get("paid", 0),
            "enterprise_leaning": gates.get("enterprise-leaning", 0),
            "enterprise_only": gates.get("enterprise-only", 0),
            "unknown": gates.get("unknown", 0),
            "n_a": gates.get("n-a", 0),
        },
        "solo_reachable": _solo_reachable(pool),
        "official_with_live_endpoint": sum(
            1 for e in pool
            if e.get("mcp_status_bucket") == "official"
            and e.get("endpoint_status") in ("live", "live-auth-gated")
        ),
        "official_docs_only": sum(
            1 for e in pool
            if e.get("mcp_status_bucket") == "official" and e.get("endpoint_status") == "docs-only"
        ),
        "endpoint_probe_date": next(
            (e.get("endpoint_last_probed") for e in pool if e.get("endpoint_last_probed")), None
        ),
        "endpoint_meaning": (
            "official_with_live_endpoint counts official entries whose recorded "
            "mcp_url answered an MCP initialize as a server (401/402/407, 406, or "
            "200 with jsonrpc) on endpoint_probe_date. official_docs_only counts "
            "those whose recorded URL is a documentation page. The second is not "
            "a downgrade; it is the gap between where to read and where to "
            "connect. bench_tested is untouched by either."
        ),
        "solo_reachable_meaning": (
            "An official or community MCP server AND an access gate of free or "
            "paid, meaning one person can get in without a sales call."
        ),
        "bench_tested": sum(1 for e in pool if e.get("tier") == "BENCH-TESTED"),
        "bench_tested_note": (
            "0 is not a bug and does not get hidden. It stays 0 until somebody "
            "actually runs these tools and says so with a date."
        ),
        "gate_unknown_note": (
            "%d of %d entries have api_gate 'unknown'. That is the directory's "
            "biggest open quality problem and it is published rather than "
            "rounded away."
            % (
                DIRECTORY.counts["api_gate"].get("unknown", 0),
                HONESTY.total,
            )
        ),
        "mcp_url_parse_note": (
            "%d entries carry an mcp_url field, %d of which parse to at least "
            "one URL. The other %d are prose (a sentence about where the "
            "server lives) and are returned verbatim as mcp_url_raw rather "
            "than being dropped or invented."
            % (
                sum(1 for e in ENTRIES if e.get("mcp_url")),
                sum(1 for e in ENTRIES if e.get("mcp_urls")),
                sum(1 for e in ENTRIES if e.get("mcp_url") and not e.get("mcp_urls")),
            )
        ),
        "extremes": {
            "most_mcpd": (
                {
                    "category": most[3],
                    "label": most[4],
                    "ratio": "%d/%d" % (most[1], most[2]),
                    "pct": round(100.0 * most[0], 1),
                }
                if most
                else None
            ),
            "least_mcpd": (
                {
                    "category": least[3],
                    "label": least[4],
                    "ratio": "%d/%d" % (least[1], least[2]),
                    "pct": round(100.0 * least[0], 1),
                }
                if least
                else None
            ),
            "computed_over": "all 15 categories, regardless of scope",
        },
        "headline": " ".join(headline_bits),
        "counted_by": "tools_recount.py",
        "generated": DIRECTORY.generated_on,
        "server": _meta(),
        "honesty": HONESTY.envelope(
            pool,
            capability=bool(job),
            text_fallback=text_fallback,
            scope_note="Statistics for scope %s." % scope,
            include_source_urls=False,
        ),
    }


# ---------------------------------------------------------------------------
# 5. find_by_gate
# ---------------------------------------------------------------------------
@mcp.tool
def find_by_gate(
    gate: str,
    category: Optional[str] = None,
    mcp_status: Optional[str] = None,
    limit: int = 25,
) -> dict[str, Any]:
    """List tools by access gate: can you get an API key alone, or is it a sales call.

    gate is one of free, paid, enterprise-leaning, enterprise-only, unknown,
    n-a. This is the second axis the directory exists for: an MCP server you
    cannot get a key for is not reachable, whatever the vendor's marketing
    says.
    """
    limit = max(1, min(int(limit or 25), 100))
    norm = normalize_gate(gate)
    if norm is None:
        return {
            "query": gate,
            "status": "unknown gate",
            "message": (
                "'%s' is not an access gate in this directory's vocabulary. The "
                "vocabulary is closed on purpose: %s."
                % (gate, ", ".join(GATE_VALUES))
            ),
            "valid_gates": list(GATE_VALUES),
            "gate_meanings": GATE_MEANINGS,
            "counts_by_gate": DIRECTORY.counts["api_gate"],
            "server": _meta(),
            "honesty": HONESTY.envelope([], scope_note="Gate lookup for '%s'." % gate),
        }

    pool, applied, notes = _apply_filters(
        ENTRIES, category, mcp_status, norm, None, None, None, None
    )
    ordered = sorted(pool, key=lambda e: e.get("display_rank", 10**6))
    shown = ordered[:limit]
    status = _bucket_counts(pool, "mcp_status_bucket", MCP_STATUS_VALUES)

    return {
        "gate": norm,
        "gate_meaning": GATE_MEANINGS.get(norm, "No definition on file."),
        "gate_raw_note": (
            "api_gate_raw on each result is the verbatim sentence from the "
            "research pass. Where a vendor changed its gate the sentence says "
            "so, and the sentence is the truth while the bucket is only the "
            "index."
        ),
        "filters_applied": applied,
        "filter_notes": notes,
        "match_count": len(pool),
        "returned": len(shown),
        "not_returned": "%d result(s) were trimmed by limit=%d."
        % (max(0, len(pool) - len(shown)), limit),
        "sort": ORDERING_DISCLOSURE_DISPLAY,
        "breakdown": {
            "official": status.get("official", 0),
            "community": status.get("community", 0),
            "none_found": status.get("none-found", 0),
            "unknown": status.get("unknown", 0),
            "n_a": status.get("n-a", 0),
            "solo_reachable": _solo_reachable(pool),
        },
        "all_gate_counts": DIRECTORY.counts["api_gate"],
        "results": [result_row(e, entry_honesty(e)) for e in shown],
        "summary": _summary_sentence(pool, "the '%s' access gate" % norm),
        "server": _meta(),
        "honesty": HONESTY.envelope(
            pool, scope_note="Access gate '%s'." % norm
        ),
    }


GATE_MEANINGS: dict[str, str] = {
    "free": (
        "An API or MCP key is available on a free or self-serve plan. One "
        "person can get in with a credit card at most and no conversation."
    ),
    "paid": (
        "API or MCP access exists on a paid self-serve plan. No sales call, "
        "but it costs money."
    ),
    "enterprise-leaning": (
        "Access is nominally self-serve but the vendor pushes towards a quote. "
        "One entry in the directory sits here."
    ),
    "enterprise-only": (
        "API or MCP access requires a sales conversation, a contract, or an "
        "enterprise tier. An individual cannot get in alone."
    ),
    "unknown": (
        "The vendor's public pricing did not state clearly whether API or MCP "
        "access is self-serve. This is published as unknown rather than "
        "guessed."
    ),
    "n-a": "The product has no API or MCP surface for this axis to apply to.",
}


# ---------------------------------------------------------------------------
# 6. get_docs_digest
# ---------------------------------------------------------------------------
@mcp.tool
def get_docs_digest(name: str) -> dict[str, Any]:
    """Structured facts from a vendor's public API documentation, when they exist.

    Returns docs_url plus a structured digest (auth model, endpoint count,
    capabilities, rate limits, pricing model, webhooks, SDKs, OpenAPI spec).
    It never reproduces documentation prose and it never invents a digest: an
    uncrawled entry says "not crawled yet" and hands you the URL to read.
    """
    candidates, how = match_name(ENTRIES, name)
    if not candidates:
        return {
            "query": name,
            "status": "tool not found",
            "message": "No tool matched '%s' in the directory." % name,
            "server": _meta(),
            "honesty": HONESTY.envelope([], scope_note="Docs lookup for '%s'." % name),
        }
    if len(candidates) > 1:
        canon = {c.get("canonical_id") for c in candidates}
        if len(canon) == 1:
            candidates = [c for c in candidates if c.get("canonical")] or candidates[:1]
    if len(candidates) > 1:
        return {
            "query": name,
            "status": "ambiguous",
            "candidates": [
                {"id": c.get("id"), "name": c.get("name"), "docs_url": c.get("docs_url")}
                for c in sorted(candidates, key=lambda c: c.get("display_rank", 10**6))
            ],
            "server": _meta(),
            "honesty": HONESTY.envelope(
                candidates, scope_note="Ambiguous docs lookup for '%s'." % name
            ),
        }

    entry = candidates[0]
    digest = entry.get("docs_digest")
    docs_url = entry.get("docs_url")

    if digest:
        status = "digested"
        message = (
            "Structured facts extracted from the vendor's public documentation "
            "on %s. No documentation text is reproduced here. Read the source "
            "page for detail." % (entry.get("docs_last_crawled") or "an unstamped date")
        )
    elif docs_url:
        status = "not yet digested"
        message = (
            "A documentation URL is on file for %s but it has never been "
            "crawled, so there is no digest. The docs intel layer (SPEC 3) has "
            "not run: 0 of %d entries carry a digest today. Read the URL "
            "yourself; do not treat this as an absence of documentation."
            % (entry.get("name"), HONESTY.total)
        )
    else:
        status = "no docs_url on file"
        message = (
            "No API documentation URL has been found for %s yet. %d of %d "
            "entries carry a docs_url; this is not one of them. The %d source "
            "URL(s) below are the research trail and may include a docs page."
            % (
                entry.get("name"),
                sum(1 for e in ENTRIES if e.get("docs_url")),
                HONESTY.total,
                len(entry.get("source_urls") or []),
            )
        )

    return {
        "name": entry.get("name"),
        "id": entry.get("id"),
        "match_method": how,
        "status": status,
        "message": message,
        "docs_url": docs_url,
        "digest": digest,
        "crawled_on": entry.get("docs_last_crawled"),
        "changed_since_last_crawl": [],
        "source_note": (
            "The digest, when it exists, is structured facts only: auth model, "
            "endpoint count, capabilities, rate limits, pricing model, "
            "webhooks, SDKs, OpenAPI spec URL. Never mirrored prose, never a "
            "paraphrase of the docs body."
        ),
        "mcp_urls": entry.get("mcp_urls") or [],
        "mcp_url_raw": entry.get("mcp_url"),
        "source_urls": entry.get("source_urls") or [],
        "server": _meta(),
        "honesty": HONESTY.envelope(
            [entry], scope_note="Documentation digest for %s." % entry.get("name")
        ),
    }


# ---------------------------------------------------------------------------
# shared: resolve one name to one entry, or explain why not
# ---------------------------------------------------------------------------
def _resolve_entry(
    name: str, scope: str
) -> tuple[dict[str, Any] | None, str, dict[str, Any] | None]:
    """Resolve a name to exactly one entry, or build the not-found or ambiguous answer.

    Cross-listed duplicates of one product collapse to the canonical entry, so a
    product that appears in two categories is never reported as ambiguous.
    """
    candidates, how = match_name(ENTRIES, name)
    if not candidates:
        return None, how, {
            "query": name,
            "status": "not found",
            "match_method": how,
            "message": (
                "No tool in the directory matched '%s'. The directory holds %d "
                "entries covering %d unique products; a tool being absent means "
                "it has not been researched yet, not that it does not exist."
                % (name, HONESTY.total, HONESTY.server_meta()["unique_products"])
            ),
            "server": _meta(),
            "honesty": HONESTY.envelope([], scope_note="%s for '%s'." % (scope, name)),
        }
    if len(candidates) > 1:
        canon = {c.get("canonical_id") for c in candidates}
        if len(canon) == 1:
            candidates = [c for c in candidates if c.get("canonical")] or candidates[:1]
    if len(candidates) > 1:
        return None, how, {
            "query": name,
            "status": "ambiguous",
            "match_method": how,
            "message": (
                "'%s' matched %d entries. Naming one for you would be a guess, "
                "so here are the candidates." % (name, len(candidates))
            ),
            "candidates": [
                {
                    "id": c.get("id"),
                    "name": c.get("name"),
                    "category": c.get("category_slug"),
                    "mcp_status": c.get("mcp_status_bucket"),
                    "cli_status": c.get("cli_status") or "not-checked",
                    "github_org": c.get("github_org"),
                }
                for c in sorted(candidates, key=lambda c: c.get("display_rank", 10**6))
            ],
            "server": _meta(),
            "honesty": HONESTY.envelope(
                candidates, scope_note="Ambiguous %s for '%s'." % (scope.lower(), name)
            ),
        }
    return candidates[0], how, None


def _mcp_route(e: dict[str, Any]) -> dict[str, Any]:
    """The MCP way in, as the directory recorded it, with the hosted-versus-local call."""
    status = e.get("mcp_status_bucket")
    es = e.get("endpoint_status") or "not-probed"
    probed = e.get("endpoint_last_probed") or "an unstamped date"
    checked = e.get("last_checked") or "the build date"
    repo = e.get("mcp_tools_repo")
    docs = e.get("mcp_docs_url")

    if es in ("live", "live-auth-gated"):
        shape = "hosted"
        shape_note = (
            "A remote endpoint answered an MCP initialize on %s. Point a client at "
            "mcp_endpoint; nothing to install." % probed
        )
        if es == "live":
            sentence = "MCP: a live endpoint at %s that answered without asking for a key on %s." % (
                e.get("mcp_endpoint"), probed)
        else:
            sentence = "MCP: a live endpoint at %s that asks for a key (probed %s)." % (
                e.get("mcp_endpoint"), probed)
    elif es == "repo-local":
        shape = "local"
        shape_note = (
            "The recorded URL is a repository or package (mcp_docs_url), checked "
            "reachable on %s. Install it and run it locally over stdio." % probed
        )
        sentence = "MCP: a server to install from %s and run locally over stdio (checked %s)." % (
            docs or repo, probed)
    elif es == "docs-only":
        shape = "unknown"
        shape_note = (
            "On %s the recorded URL served a documentation page, not an endpoint. "
            "The entry says where to read, not where to connect." % probed
        )
        sentence = (
            "MCP: %s per research, but the recorded URL is a documentation page (probed %s), "
            "so there is no endpoint on record to connect to." % (status, probed)
        )
    elif es == "auth-wall":
        shape = "unknown"
        shape_note = e.get("endpoint_wall_note") or (
            "The recorded URL answers an auth challenge at every path: a wall, not a proven server."
        )
        sentence = "MCP: the recorded URL answers an auth challenge at every path (probed %s); a wall, not a proven server." % probed
    elif es == "unreachable":
        shape = "unknown"
        shape_note = "On %s no recorded MCP URL for this entry answered at all." % probed
        sentence = "MCP: %s per research, but no recorded URL answered on %s." % (status, probed)
    elif status == "none-found":
        shape = "none"
        shape_note = "No MCP server was found as of %s. A not-found, not a proof of absence." % checked
        sentence = "MCP: none found as of %s." % checked
    elif status == "n-a":
        shape = "none"
        shape_note = "The product has no MCP surface for this to apply to."
        sentence = "MCP: not applicable to this product."
    elif status == "unknown":
        shape = "unknown"
        shape_note = "MCP status could not be determined from public sources."
        sentence = "MCP: status unknown from public sources."
    elif e.get("mcp_urls"):
        shape = "unknown"
        shape_note = "The recorded URL has not been probed live (endpoint_status not-probed)."
        sentence = "MCP: %s per research (established %s); the recorded URL has not been probed live." % (status, checked)
    else:
        shape = "unknown"
        shape_note = (
            "mcp_status is '%s' but the mcp_url field is prose with no parseable URL; "
            "read mcp_url_raw before assuming an endpoint exists." % status
        )
        sentence = "MCP: %s per research, but no parseable URL is on record; read mcp_url_raw." % status

    return {
        "mcp_status": status,
        "endpoint_status": es,
        "endpoint_last_probed": e.get("endpoint_last_probed"),
        "mcp_endpoint": e.get("mcp_endpoint"),
        "mcp_docs_url": docs,
        "mcp_urls": e.get("mcp_urls") or [],
        "mcp_url_raw": e.get("mcp_url"),
        "install_from": docs if es == "repo-local" else repo,
        "repo_party": e.get("mcp_tools_repo_party"),
        "mcp_auth": e.get("mcp_auth"),
        "api_gate": e.get("api_gate_bucket"),
        "api_gate_raw": e.get("api_gate"),
        "hosted_or_local": shape,
        "hosted_or_local_note": shape_note,
        "tool_count": e.get("mcp_tool_count") or 0,
        "tools_evidence": e.get("mcp_tools_evidence"),
        "tools_harvested_on": e.get("mcp_tools_fetched_on"),
        "route": sentence,
    }


def _cli_route(e: dict[str, Any]) -> dict[str, Any]:
    """The command-line way in: every install command, each quoted from a URL on a date."""
    status = e.get("cli_status") or "not-checked"
    installs = cli_install_view(e, None)
    checked = e.get("cli_checked_on") or "an unstamped date"
    first = installs[0] if installs else None

    def quoted(i: dict[str, Any]) -> str:
        return "%s, quoted from %s on %s" % (i.get("cmd"), i.get("source_url") or "an unrecorded URL", i.get("fetched_on") or "an unstamped date")

    if status == "official":
        if first:
            sentence = "CLI: official, %s." % quoted(first)
        else:
            sentence = "CLI: official, binary %s, documented at %s (checked %s); no install command was quoted." % (
                e.get("cli_binary") or "not recorded", e.get("cli_docs_url") or e.get("cli_repo") or "an unrecorded URL", checked)
    elif status == "community":
        if first:
            sentence = "CLI: community (a third party's work, not the vendor's), %s." % quoted(first)
        else:
            sentence = "CLI: community (a third party's work, not the vendor's), at %s (checked %s); no install command was quoted." % (
                e.get("cli_repo") or e.get("cli_docs_url") or "an unrecorded URL", checked)
    elif status == "none-found":
        sentence = "CLI: none found on %s." % checked
    elif HONESTY.cli_measured:
        sentence = "CLI: not measured for this entry; the harvest of %s did not reach it." % HONESTY.cli_checked_on
    else:
        sentence = "CLI: the CLI layer has not been measured on this build."

    return {
        "cli_status": status,
        "cli_party": e.get("cli_party"),
        "cli_binary": e.get("cli_binary"),
        "cli_install": installs,
        "cli_login": e.get("cli_login"),
        "cli_commands_seen": e.get("cli_commands_seen") or [],
        "cli_docs_url": e.get("cli_docs_url"),
        "cli_repo": e.get("cli_repo"),
        "cli_packages": e.get("cli_packages") or [],
        "cli_evidence": e.get("cli_evidence"),
        "cli_checked_on": e.get("cli_checked_on"),
        "route": sentence,
    }


# ---------------------------------------------------------------------------
# 8. get_install
# ---------------------------------------------------------------------------
@mcp.tool
def get_install(name: str) -> dict[str, Any]:
    """Everything an agent needs to start using one tool, both routes in one answer.

    The MCP route: the endpoint that answered as a server, or the repository to
    install, with endpoint_status, the auth model, the access gate and the
    hosted-versus-local call (a live endpoint is hosted and needs no install; a
    repo-local server is installed and run over stdio; a docs-only URL is a page
    to read, not a place to connect).

    The CLI route: cli_status, the binary, every install command with the
    source_url and date it was quoted from, the login command seen, the
    subcommands seen, the docs page, the repository and the registry packages.

    `recommendation` says which routes exist and are reachable. It describes
    routes; it does not rank vendors. Three caveats always apply: a community
    CLI is a third party's work, an install command is quoted from a page on a
    date and was not run here, and none-found means not found on that date.
    """
    e, how, err = _resolve_entry(name, "Install lookup")
    if err:
        return err
    mcp_route = _mcp_route(e)
    cli_route = _cli_route(e)
    caveats = [
        "Routes are described, not ranked. Whichever exists and is reachable is "
        "the one to try first; nothing here has been run.",
    ]
    caveats.extend(cli_caveats(e))
    if e.get("cli_status") == "community":
        caveats.append(
            "A community CLI is a third party's work: it wraps the vendor's API, "
            "the vendor did not publish it, and it can lag or break without notice."
        )
    if cli_route["cli_install"]:
        caveats.append(
            "Each install command is quoted from its source_url on its fetched_on "
            "date. It was not run here; read the page before pasting it."
        )
    if (e.get("cli_status") or "not-checked") == "none-found":
        caveats.append("none-found means not found on %s, not absent." % (e.get("cli_checked_on") or "that date"))
    return {
        "query": name,
        "status": "ok",
        "match_method": how,
        "name": e.get("name"),
        "id": e.get("id"),
        "category": e.get("category_slug"),
        "vendor_url": e.get("vendor_url"),
        "mcp": mcp_route,
        "cli": cli_route,
        "recommendation": "%s %s" % (mcp_route["route"], cli_route["route"]),
        "caveats": caveats,
        "measured_on": {
            "mcp_url_liveness": e.get("endpoint_last_probed"),
            "cli": e.get("cli_checked_on"),
            "research": e.get("last_checked"),
        },
        "server": _meta(),
        "honesty": HONESTY.envelope(
            [e], scope_note="Install routes for %s." % e.get("name")
        ),
    }


# ---------------------------------------------------------------------------
# 9. whats_building
# ---------------------------------------------------------------------------
def _day(value: Any) -> dt.date | None:
    """Parse the first ten characters of an ISO date or datetime, or None."""
    if not isinstance(value, str) or len(value) < 10:
        return None
    try:
        return dt.date.fromisoformat(value[:10])
    except ValueError:
        return None


def _org_counts(pool: list[dict[str, Any]]) -> dict[str, Any]:
    """Status counts for a pool of entries, every one stamped with the measurement date."""
    by = _bucket_counts(pool, "github_org_status", ("resolved", "unresolved", "no-github-signal", "not-checked"))
    resolved = [e for e in pool if e.get("github_org_status") == "resolved"]
    return {
        "entries_in_scope": len(pool),
        "resolved": by.get("resolved", 0),
        "unresolved": by.get("unresolved", 0),
        "no_github_signal": by.get("no-github-signal", 0),
        "not_checked": by.get("not-checked", 0) + by.get("other", 0),
        "silent_total": len(pool) - by.get("resolved", 0),
        "repos_public_non_fork": sum(e.get("github_org_repos") or 0 for e in resolved),
        "repos_mcp": sum(e.get("github_org_repos_mcp") or 0 for e in resolved),
        "repos_cli": sum(e.get("github_org_repos_cli") or 0 for e in resolved),
        "checked_on": HONESTY.orgs_checked_on,
    }


def _vendor_building(e: dict[str, Any], how: str) -> dict[str, Any]:
    status = e.get("github_org_status") or "not-checked"
    resolved = status == "resolved"
    checked = e.get("github_org_checked_on")
    return {
        "query": e.get("name"),
        "status": "ok",
        "match_method": how,
        "name": e.get("name"),
        "id": e.get("id"),
        "category": e.get("category_slug"),
        "github_org": e.get("github_org"),
        "github_org_status": status,
        "github_org_url": e.get("github_org_url"),
        "github_org_evidence": e.get("github_org_evidence"),
        "repos": {
            "public_non_fork": e.get("github_org_repos") if resolved else None,
            "mcp": e.get("github_org_repos_mcp") if resolved else None,
            "cli": e.get("github_org_repos_cli") if resolved else None,
            "checked_on": checked,
        },
        "latest_activity": e.get("github_org_latest_activity") if resolved else None,
        "recent_repos": e.get("github_org_recent_repos") if resolved else [],
        "recent_repos_note": (
            "The five most recently pushed public non-fork repositories on %s. kind is a "
            "heuristic from the repository's name, topics and description, not a "
            "statement by the vendor. latest_release is the newest release tag seen, or null."
            % (checked or "an unstamped date")
        ),
        "message": github_org_caveats(e)[0],
        "other_github_fields": {
            "github_url": e.get("github_url"),
            "mcp_tools_repo": e.get("mcp_tools_repo"),
            "mcp_tools_repo_party": e.get("mcp_tools_repo_party"),
            "github_candidates": e.get("github_candidates") or [],
        },
        "server": _meta(),
        "honesty": HONESTY.envelope(
            [e], scope_note="GitHub activity for %s." % e.get("name"), include_source_urls=False
        ),
    }


@mcp.tool
def whats_building(
    name: Optional[str] = None,
    category: Optional[str] = None,
    days: int = 90,
    limit: int = 20,
) -> dict[str, Any]:
    """What vendors are shipping in public on GitHub, from their resolved organisations.

    With a name: that vendor's GitHub organisation, how it was tied to the
    vendor (domain evidence, never a name match alone), its public repository
    counts, and the five most recently pushed repositories with description,
    kind, stars, pushed date and latest release.

    Without a name: across the directory, or one category, the vendors whose
    organisation pushed something within `days` of the measurement date, most
    recent first, each with its most recently pushed repositories. The counts
    of unresolved, no-signal and not-yet-checked vendors ride alongside so that
    silence is never mistaken for inactivity: a vendor absent from this list
    may be building furiously under an organisation the instrument could not
    tie to it.

    Every count carries github_org_checked_on. If the organisation layer has
    not been measured on this build the counts are null, not zero, and the
    response says so in a sentence. Repository kinds are heuristics from name,
    topics and description, not vendor statements.
    """
    days = max(1, min(int(days or 90), 3650))
    limit = max(1, min(int(limit or 20), 100))

    if name:
        e, how, err = _resolve_entry(name, "GitHub activity lookup")
        if err:
            return err
        body = _vendor_building(e, how)
        if not HONESTY.orgs_measured:
            body["message"] = ORG_LAYER_UNMEASURED
        return body

    notes: list[str] = []
    scope = "all"
    pool = [e for e in ENTRIES if e.get("canonical", True)]
    if category:
        cat = DIRECTORY.category(category)
        if cat is None:
            notes.append(
                "category '%s' is not one of the 15 category slugs, so the scope "
                "stayed at all entries. Valid slugs: %s."
                % (category, ", ".join(DIRECTORY.category_slugs))
            )
        else:
            pool = [e for e in pool if e.get("category_slug") == cat["slug"]]
            scope = "category:%s" % cat["slug"]

    if not HONESTY.orgs_measured:
        return {
            "status": "not measured",
            "scope": scope,
            "scope_notes": notes,
            "window": {"days": days, "reference_date": None, "cutoff": None},
            "message": (
                ORG_LAYER_UNMEASURED
                + " Nothing here can say what any vendor is shipping; the counts "
                "below are null because unmeasured is not zero."
            ),
            "counts": {
                "entries_in_scope": len(pool),
                "resolved": None,
                "unresolved": None,
                "no_github_signal": None,
                "not_checked": None,
                "silent_total": None,
                "repos_public_non_fork": None,
                "repos_mcp": None,
                "repos_cli": None,
                "checked_on": None,
            },
            "active_vendors": [],
            "server": _meta(),
            "honesty": HONESTY.envelope(
                [], scope_note="GitHub activity, scope %s." % scope, include_source_urls=False
            ),
        }

    ref = _day(HONESTY.orgs_checked_on) or _day(DIRECTORY.generated_on)
    cutoff = ref - dt.timedelta(days=days) if ref else None
    resolved = [e for e in pool if e.get("github_org_status") == "resolved"]
    active = []
    for e in resolved:
        last = _day(e.get("github_org_latest_activity"))
        if last is None:
            continue
        if cutoff is None or last >= cutoff:
            active.append(e)
    active.sort(key=lambda e: e.get("github_org_latest_activity") or "", reverse=True)
    shown = active[:limit]
    counts = _org_counts(pool)

    rows = [
        {
            "name": e.get("name"),
            "id": e.get("id"),
            "category": e.get("category_slug"),
            "github_org": e.get("github_org"),
            "github_org_url": e.get("github_org_url"),
            "repos_public_non_fork": e.get("github_org_repos"),
            "repos_mcp": e.get("github_org_repos_mcp"),
            "repos_cli": e.get("github_org_repos_cli"),
            "latest_activity": e.get("github_org_latest_activity"),
            "recent_repos": e.get("github_org_recent_repos") or [],
            "checked_on": e.get("github_org_checked_on"),
        }
        for e in shown
    ]

    return {
        "status": "ok",
        "scope": scope,
        "scope_notes": notes,
        "window": {
            "days": days,
            "reference_date": ref.isoformat() if ref else None,
            "cutoff": cutoff.isoformat() if cutoff else None,
            "rule": (
                "A vendor is active if its organisation's most recent push falls on "
                "or after the cutoff. The window is measured back from the date the "
                "layer was read, not from today, because this server has no clock "
                "it trusts over its data."
            ),
        },
        "active_count": len(active),
        "returned": len(rows),
        "not_returned": "%d active vendor(s) were trimmed by limit=%d." % (max(0, len(active) - len(rows)), limit),
        "sort": "Most recent organisation push first, from github_org_latest_activity. Not a ranking of vendors.",
        "active_vendors": rows,
        "counts": counts,
        "silence_note": (
            "%d of %d vendors in scope are silent here: %d unresolved (GitHub accounts "
            "seen, none passed the domain-evidence rules), %d with no GitHub signal, %d "
            "not yet reached by the harvest of %s. Silence is not inactivity."
            % (
                counts["silent_total"],
                counts["entries_in_scope"],
                counts["unresolved"],
                counts["no_github_signal"],
                counts["not_checked"],
                counts["checked_on"],
            )
        ),
        "kind_note": (
            "Repository kind (mcp-server, cli, sdk, app, plugin-or-integration, "
            "docs-or-examples, infra, api-client, other) is a heuristic from the "
            "repository's name, topics and description, not a statement by the vendor."
        ),
        "server": _meta(),
        "honesty": HONESTY.envelope(
            shown, scope_note="GitHub activity, scope %s." % scope, include_source_urls=False
        ),
    }


# ---------------------------------------------------------------------------
# 10. get_server_tools
# ---------------------------------------------------------------------------

@mcp.tool()
def get_server_tools(name: str) -> dict[str, Any]:
    """What an MCP server actually exposes: every tool it names, with the evidence.

    This is the capability layer, and it answers a different question from
    find_tools. find_tools asks which PRODUCTS claim a job. This asks what one
    SERVER will let an agent call, by tool name, with the required parameters
    where they are recorded.

    Every tool carries the evidence that produced it, strongest first:
      live-list  the server answered tools/list on the date recorded
      source     the tool is registered in the server's own source code
      docs       the vendor's documentation names it
      readme     a README table names it, which can drift from the code

    A tool listed here has NOT been called. bench_tested is a separate and much
    stronger claim, and it is still 1 across the whole directory.
    """
    matches, how = match_name(ENTRIES, name)
    if not matches:
        return {
            **HONESTY.server_meta(),
            "status": "no-match",
            "asked_for": name,
            "message": "No entry matched that name. Call find_tools or list_categories to see what exists.",
        }
    if len(matches) > 1:
        return {
            **HONESTY.server_meta(),
            "status": "ambiguous",
            "asked_for": name,
            "candidates": [e["display_name"] for e in matches[:12]],
            "message": "Several entries matched. Ask again with one of these exact names.",
        }
    e = matches[0]
    tools = e.get("mcp_tools") or []
    body = {
        **HONESTY.server_meta(),
        "status": "ok",
        "name": e["display_name"],
        "matched_by": how,
        "mcp_status": e.get("mcp_status_bucket"),
        "api_gate": e.get("api_gate_bucket"),
        "mcp_endpoint": e.get("mcp_endpoint"),
        "mcp_docs_url": e.get("mcp_docs_url"),
        "endpoint_status": e.get("endpoint_status"),
        "tool_count": len(tools),
        "evidence": e.get("mcp_tools_evidence"),
        "harvested_on": e.get("mcp_tools_fetched_on"),
        "tools": tools,
        "honesty": entry_honesty(e),
    }
    if not tools:
        body["message"] = (
            "No tool list has been harvested for this server yet. That is unmeasured, "
            "not a claim that the server exposes nothing. mcp_status is %s and the "
            "recorded URL is %s."
            % (e.get("mcp_status_bucket"), (e.get("mcp_endpoint") or e.get("mcp_docs_url") or e.get("mcp_url") or "not recorded"))
        )
    return body



# ---------------------------------------------------------------------------
# 11. plan_stack
# ---------------------------------------------------------------------------

# What "reachable" costs an agent, cheapest first. An endpoint that answered a
# handshake is the only kind you can call without installing anything; a repo is
# an install; a docs page is a URL to go read; unmeasured is a research task.
_REACH_RANK = {"live": 0, "live-auth-gated": 1, "repo-local": 2, "docs-only": 3, "not-probed": 4, "unreachable": 5, "not-applicable": 6}
_GATE_RANK = {"free": 0, "paid": 1, "enterprise-leaning": 2, "enterprise-only": 3, "unknown": 4, "n-a": 5}
_STATUS_RANK = {"official": 0, "community": 1, "unknown": 2, "n-a": 3, "none-found": 4}


_STOPWORDS = {"from", "with", "into", "your", "this", "that", "them", "and", "the", "for", "get", "a"}


def _job_terms(job_slug: str, job: dict[str, Any]) -> list[str]:
    """The words that make this job distinctive, for matching real tool names.

    Built from the slug and the job's own label rather than its one-liner: the
    one-liner is prose and drags in words like "database" and "list" that match
    almost any tool, which is how a plan ends up recommending a call that has
    nothing to do with the step.
    """
    blob = job_slug.replace("-", " ") + " " + (job.get("label") or "")
    terms = {w for w in re.split(r"[^a-z0-9]+", blob.lower()) if len(w) > 3 and w not in _STOPWORDS}
    return sorted(terms)


def _match_tools(entry: dict[str, Any], terms: list[str]) -> list[str]:
    """Tool names on this server that plausibly do this step, name matches first.

    A hit in the tool's NAME is worth more than one in its description, because
    a description mentioning "email" is common and a tool called find_email is
    the thing you would actually call. Requires two distinct term hits when the
    match is only in the description, which is what stops "company" alone from
    dragging in every enrich tool.
    """
    named, described = [], []
    for t in entry.get("mcp_tools") or []:
        name = (t.get("name") or "").lower()
        desc = (t.get("description") or "").lower()
        in_name = [w for w in terms if w in name]
        in_desc = [w for w in terms if w in desc]
        if in_name:
            named.append((len(in_name), t.get("name")))
        elif len(in_desc) >= 2:
            described.append((len(in_desc), t.get("name")))
    named.sort(reverse=True)
    described.sort(reverse=True)
    return [n for _, n in named][:5] + [n for _, n in described][:3]


def _step_candidates(job_slug: str, max_per_step: int, job: dict[str, Any]) -> list[dict[str, Any]]:
    """Every entry that claims this job, ranked by what it costs an agent to use it."""
    terms = _job_terms(job_slug, job or {})
    rows = []
    for e in ENTRIES:
        if job_slug not in (e.get("jobs") or []):
            continue
        if e.get("mcp_status_bucket") in ("none-found", "n-a"):
            continue
        reach = e.get("endpoint_status") or "not-probed"
        tools = e.get("mcp_tools") or []
        # Tool names whose own text looks like this step, so the plan can name a
        # call rather than only a vendor.
        matched = _match_tools(e, terms)
        rows.append({
            "name": e["display_name"],
            "mcp_status": e.get("mcp_status_bucket"),
            "api_gate": e.get("api_gate_bucket"),
            "api_gate_verbatim": e.get("api_gate"),
            "endpoint_status": reach,
            "connect_at": e.get("mcp_endpoint") or e.get("mcp_docs_url") or e.get("mcp_url"),
            "auth": e.get("mcp_auth"),
            "tool_count": e.get("mcp_tool_count") or 0,
            "tools_matching_step": len(matched),
            "candidate_tool_names": matched,
            "tools_evidence": e.get("mcp_tools_evidence"),
            "repo_party": e.get("mcp_tools_repo_party"),
            "catalog_shape": e.get("mcp_catalog_shape"),
            # The command-line route beside the MCP one, so a planner can pick
            # whichever is cheaper to wire. status not-checked means unmeasured.
            "cli": {
                "status": e.get("cli_status") or "not-checked",
                "binary": e.get("cli_binary"),
                "install": (cli_install_view(e, 1) or [None])[0],
                "checked_on": e.get("cli_checked_on"),
            },
            "_sort": (
                _REACH_RANK.get(reach, 9),
                _GATE_RANK.get(e.get("api_gate_bucket"), 9),
                _STATUS_RANK.get(e.get("mcp_status_bucket"), 9),
                0 if matched else 1,
                -(e.get("mcp_tool_count") or 0),
                e["display_name"].lower(),
            ),
        })
    rows.sort(key=lambda r: r["_sort"])
    for r in rows:
        r.pop("_sort", None)
    return rows[:max_per_step]


@mcp.tool()
def plan_stack(
    goal: str,
    prefer_free: Optional[bool] = None,
    connectable_only: Optional[bool] = None,
    max_per_step: int = 4,
    prefer_interface: Optional[str] = None,
) -> dict[str, Any]:
    """Plan how to actually DO a go-to-market job with these tools, step by step.

    find_tools answers "who claims this". get_server_tools answers "what does
    this one expose". This answers the question an operator actually has: given
    what I am trying to do, what should my agent call, in what order, what will
    it cost me to get in, and where does the chain break.

    `goal` is plain language and may describe several steps at once, for example
    "find a person's linkedin from a name and company, get their work email,
    verify it, then write the contact to my CRM". Each step resolves against the
    56-job vocabulary; the response says what resolved and what did not.

    For every step it returns candidate tools ranked by what they cost an agent:
    an endpoint that answered a live handshake first, then a repo you install,
    then a documentation page you have to go read. Within that, free before
    paid, official before community, and a server whose own tool names match the
    step before one that only claims the job.

    prefer_free drops anything an operator cannot start on without a sales call.
    connectable_only drops anything whose URL has never answered as a server.

    Every candidate also carries `cli` (status, binary, the first install
    command with the URL and date it was quoted from) beside its MCP route, so
    a planner can pick whichever is cheaper to wire. prefer_interface ("mcp" or
    "cli") reorders the candidates within each step so that the ones with that
    kind of interface come first; it never removes a candidate and never changes
    the set. Candidates are still drawn from entries that claim an MCP server;
    a vendor with only a CLI is found with find_tools(interface="cli").

    Two honesty rules ride on every plan. A job tag means the vendor says the
    product does this, so a ranking is a reading order, not a benchmark. And
    nothing here has been run: bench_tested is 1 across the whole directory, so
    treat the plan as the shortlist to go test, never as a verified pipeline.
    """
    max_per_step = max(1, min(int(max_per_step or 4), 10))
    raw = (goal or "").strip()
    if not raw:
        return {**HONESTY.server_meta(), "status": "no-goal",
                "message": "Describe what you are trying to do. Call list_jobs to see the 56 jobs this directory can plan against."}

    # Split the goal into steps on the connectives people actually use.
    parts = [p.strip() for p in re.split(r"\s*(?:,|;|\bthen\b|\band then\b|\bafter that\b|\bnext\b|->|→)\s*", raw) if p.strip()]
    if not parts:
        parts = [raw]

    pref = normalize_interface(prefer_interface) if prefer_interface else None
    pref_note = None
    if prefer_interface and pref not in ("mcp", "cli"):
        pref_note = (
            "prefer_interface '%s' is not 'mcp' or 'cli', so the ranking was left as is."
            % prefer_interface
        )
        pref = None
    elif pref == "cli" and not HONESTY.cli_measured:
        pref_note = CLI_LAYER_UNMEASURED + " prefer_interface='cli' therefore changes nothing on this build."
    elif pref == "cli":
        pref_note = (
            "Within each step, candidates with an official or community CLI (measured %s) "
            "come first; the rest keep the reachability order. Nothing was removed."
            % HONESTY.cli_checked_on
        )
    elif pref == "mcp":
        pref_note = (
            "Within each step, candidates whose MCP URL answered as a server or is an "
            "installable repository come first. That is already the default order, so "
            "this rarely changes anything. Nothing was removed."
        )

    steps, unresolved, seen = [], [], set()
    for part in parts[:8]:
        resolved = VOCAB.resolve(part) if VOCAB else []
        if not resolved:
            unresolved.append(part)
            continue
        best = resolved[0]
        slug = best["job"]
        if slug in seen:
            continue
        seen.add(slug)
        job = VOCAB._by_slug.get(slug) or next((j for j in (VOCAB.jobs or []) if j.get("id") == slug), {})
        cands = _step_candidates(slug, max_per_step, job)
        if prefer_free:
            kept = [c for c in cands if c["api_gate"] in ("free", "paid")]
            cands = kept or cands
        if connectable_only:
            kept = [c for c in cands if c["endpoint_status"] in ("live", "live-auth-gated")]
            cands = kept or []
        if pref == "cli":
            cands = sorted(cands, key=lambda c: 0 if c["cli"]["status"] in ("official", "community") else 1)
        elif pref == "mcp":
            cands = sorted(cands, key=lambda c: 0 if c["endpoint_status"] in ("live", "live-auth-gated", "repo-local") else 1)
        steps.append({
            "step": len(steps) + 1,
            "asked": part,
            "job": slug,
            "job_label": job.get("label") or slug,
            "job_meaning": job.get("one_liner"),
            "resolved_how": best.get("confidence"),
            "supply": len(cands),
            "recommended": cands[0] if cands else None,
            "alternatives": cands[1:],
            "gap": None if cands else (
                "No tool in the directory both claims this job and has a reachable server under "
                "the filters you set. That is a finding about this directory's coverage as much "
                "as about the market."
            ),
        })

    reachable = [s for s in steps if s["recommended"]]
    gates = [s["recommended"]["api_gate"] for s in reachable]
    return {
        **HONESTY.server_meta(),
        "status": "ok" if steps else "nothing-resolved",
        "goal": raw,
        "steps": steps,
        "unresolved_phrases": unresolved,
        "interface_preference": {
            "asked": prefer_interface,
            "applied": pref,
            "note": pref_note,
        },
        "summary": {
            "steps_planned": len(steps),
            "steps_with_a_tool": len(reachable),
            "steps_with_no_tool": len(steps) - len(reachable),
            "free_steps": sum(1 for g in gates if g == "free"),
            "paid_steps": sum(1 for g in gates if g == "paid"),
            "enterprise_steps": sum(1 for g in gates if g in ("enterprise-only", "enterprise-leaning")),
            "all_free": bool(gates) and all(g == "free" for g in gates),
            "steps_with_a_cli_route": (
                sum(
                    1 for s in steps
                    if any(c["cli"]["status"] in ("official", "community")
                           for c in ([s["recommended"]] if s["recommended"] else []) + s["alternatives"])
                )
                if HONESTY.cli_measured else None
            ),
            "cli_measured_on": HONESTY.cli_checked_on if HONESTY.cli_measured else None,
        },
        "how_to_read_this": (
            "Ranking is by what a tool costs an agent to use, not by quality: a server that "
            "answered a live handshake outranks one you must install, which outranks a "
            "documentation page. Nobody has run any of these. Take the recommended row per step "
            "as the first thing to go and test, and read the api_gate_verbatim line before "
            "assuming you can get a key today."
        ),
        "honesty": HONESTY.envelope(),
    }


# ---------------------------------------------------------------------------
# 12. list_jobs
# ---------------------------------------------------------------------------
@mcp.tool
def list_jobs(family: Optional[str] = None) -> dict[str, Any]:
    """The closed capability vocabulary an agent should ask with, and its supply.

    An agent cannot guess a closed vocabulary. Read this menu once, then ask
    find_tools precisely. Each job carries its tool count and how many of
    those tools have an official MCP server, because a job that 17 tools claim
    and 1 agent can call is the most useful fact in the directory.
    """
    tagged = HONESTY.tagged
    if not VOCAB:
        if VOCAB.path is not None:
            why = (
                "jobs.yaml exists on this install but no usable vocabulary "
                "could be read from it. %s" % VOCAB.note
            )
            status = "vocabulary unreadable"
        else:
            why = (
                "jobs.yaml (SPEC 2.4, the capability vocabulary) is not present "
                "on this install, so there is no menu to hand you."
            )
            status = "vocabulary not installed"
        return {
            "status": status,
            "vocabulary": VOCAB.status(),
            "message": (
                "%s find_tools still works: pass natural language and it runs a "
                "literal text search over each vendor's own description, and "
                "says so in the response." % why
            ),
            "jobs": [],
            "categories_to_browse_instead": DIRECTORY.category_slugs,
            "server": _meta(),
            "honesty": HONESTY.envelope(
                [], capability=True, scope_note="Job vocabulary listing."
            ),
        }

    want_family = (family or "").strip().lower()
    jobs = []
    for job in VOCAB.jobs:
        if want_family and want_family not in {
            (job.get("family") or "").lower(),
            (job.get("family_label") or "").lower(),
        }:
            continue
        members = [e for e in ENTRIES if job["slug"] in (e.get("jobs") or [])]
        status = _bucket_counts(members, "mcp_status_bucket", MCP_STATUS_VALUES)
        jobs.append(
            {
                "slug": job["slug"],
                "label": job["label"],
                "family": job.get("family"),
                "family_label": job.get("family_label"),
                "one_liner": job.get("one_liner"),
                "aliases": job.get("aliases") or [],
                "primary_categories": job.get("primary_categories") or [],
                "tool_count": len(members),
                "official_mcp": status.get("official", 0),
                "community_mcp": status.get("community", 0),
                "solo_reachable": _solo_reachable(members),
                "supply_note": (
                    "%d tool(s) carry this job, %d with an official MCP server."
                    % (len(members), status.get("official", 0))
                )
                if members
                else "No tool carries this job yet. That may be a real supply "
                "gap or an untagged corpus; jobs_tagged_on tells you which.",
            }
        )

    return {
        "status": "ok",
        "vocabulary": VOCAB.status(),
        "job_count": len(jobs),
        "family_filter": family,
        "families": [
            {"id": fid, "label": meta.get("label"), "one_liner": meta.get("one_liner")}
            for fid, meta in sorted(VOCAB.families.items())
        ]
        or sorted({j.get("family") for j in VOCAB.jobs if j.get("family")}),
        "tagging_progress": {
            "entries_tagged": tagged,
            "entries_total": HONESTY.total,
            "tagged_by": dict(sorted(HONESTY.tagged_by.items())),
            "note": (
                "Tool counts below are only as good as the tagging pass behind "
                "them. %d of %d entries have been tagged, by: %s."
                % (
                    tagged,
                    HONESTY.total,
                    ", ".join(
                        "%s %d" % (k, v) for k, v in sorted(HONESTY.tagged_by.items())
                    )
                    or "nobody",
                )
            ),
        },
        "jobs": jobs,
        "server": _meta(),
        "honesty": HONESTY.envelope(
            ENTRIES,
            capability=True,
            scope_note="Job vocabulary listing.",
            include_source_urls=False,
        ),
    }


# ---------------------------------------------------------------------------
# resource: the integrity record, so a user can audit the install
# ---------------------------------------------------------------------------
@mcp.resource("gtm-directory://integrity")
def integrity() -> dict[str, Any]:
    """What the server verified about its data before it agreed to serve anything."""
    return {
        "product": PRODUCT_NAME,
        "umbrella": UMBRELLA,
        "repo": REPO,
        "server_version": SERVER_VERSION,
        "integrity": DIRECTORY.integrity_summary(),
        "vocabulary": VOCAB.status(),
        "startup_caveats": DIRECTORY.startup_caveats,
        "network_policy": (
            "This server makes no outbound requests, at startup or at query "
            "time. Everything network-shaped happens in the weekly build."
        ),
    }


def main(argv: list[str] | None = None) -> None:
    """Run the server. stdio by default; HTTP behind an explicit flag.

    stdio is spawned per session by the client and is what `uvx
    gtm-mcp-directory` gets. `--transport http` exposes the same eleven read-only
    tools at /mcp for a host that wants a shared endpoint. Nothing about the
    data, the tools or the network policy changes between the two: the server
    still makes zero outbound requests either way.
    """
    import argparse

    parser = argparse.ArgumentParser(prog="gtm-mcp-directory", add_help=True)
    parser.add_argument("--transport", choices=("stdio", "http"), default=os.environ.get("GTM_DIRECTORY_TRANSPORT", "stdio"))
    parser.add_argument("--host", default=os.environ.get("HOST", "127.0.0.1"))
    parser.add_argument("--port", type=int, default=int(os.environ.get("PORT", "8000")))
    parser.add_argument("--path", default=os.environ.get("GTM_DIRECTORY_HTTP_PATH", "/mcp"),
                        help="URL path the HTTP transport answers on. The hosted endpoint sits behind a CDN that forwards the full path, so it runs as /gtm-directory/api/mcp.")
    args = parser.parse_args(argv)
    if args.transport == "http":
        from . import gate
        from . import keys as keystore
        if keystore.db_path():
            # The hosted copy: a key store is configured, so the gate wraps the app and uvicorn
            # serves the wrapped ASGI app directly. Local installs never take this branch.
            import uvicorn
            app = gate.wrap(mcp.http_app(path=args.path), args.path, generated_on=str(DIRECTORY.generated_on))
            uvicorn.run(app, host=args.host, port=args.port, log_level=os.environ.get("GTM_LOG_LEVEL", "warning"), access_log=False)
        else:
            mcp.run(transport="http", host=args.host, port=args.port, path=args.path, show_banner=False)
    else:
        mcp.run(transport="stdio", show_banner=False)


if __name__ == "__main__":
    main()
