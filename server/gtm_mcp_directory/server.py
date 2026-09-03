"""The GTM MCP Directory MCP server.

Seven read-only tools over a directory of GTM tools, answering the question
nobody else answers honestly: which of these can an agent actually call, and
what does it cost to get in.

No write tools. No telemetry. No outbound requests. No featured field.
"""

from __future__ import annotations

import os
import sys
from typing import Any, Optional

from fastmcp import FastMCP

from . import PRODUCT_NAME, REPO, SERVER_NAME, SERVER_VERSION, UMBRELLA
from .honesty import HonestyBuilder, entry_honesty
from .loading import Directory, DirectoryDataError, load_directory
from .search import (
    ORDERING_DISCLOSURE_DISPLAY,
    ORDERING_DISCLOSURE_RELEVANCE,
    GATE_VALUES,
    MCP_STATUS_VALUES,
    match_name,
    normalize_gate,
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

Use find_tools for "which tool can do X". Use whats_mcpd for the state of the
market. Use list_categories to browse and list_jobs to learn the capability
vocabulary before asking precisely.

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
        return "Nothing in the directory matched %s." % subject
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
) -> tuple[list[dict[str, Any]], dict[str, Any], list[str]]:
    applied: dict[str, Any] = {}
    notes: list[str] = []
    out = entries

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
    perfectly good server at a URL the directory does not record).
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
    )
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
# 7. list_jobs
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
    gtm-mcp-directory` gets. `--transport http` exposes the same seven read-only
    tools at /mcp for a host that wants a shared endpoint. Nothing about the
    data, the tools or the network policy changes between the two: the server
    still makes zero outbound requests either way.
    """
    import argparse

    parser = argparse.ArgumentParser(prog="gtm-mcp-directory", add_help=True)
    parser.add_argument("--transport", choices=("stdio", "http"), default=os.environ.get("GTM_DIRECTORY_TRANSPORT", "stdio"))
    parser.add_argument("--host", default=os.environ.get("HOST", "127.0.0.1"))
    parser.add_argument("--port", type=int, default=int(os.environ.get("PORT", "8000")))
    args = parser.parse_args(argv)
    if args.transport == "http":
        mcp.run(transport="http", host=args.host, port=args.port, show_banner=False)
    else:
        mcp.run(transport="stdio", show_banner=False)


if __name__ == "__main__":
    main()
