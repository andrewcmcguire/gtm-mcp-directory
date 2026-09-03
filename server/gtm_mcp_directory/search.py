"""Matching, ordering and result projection.

Two ordering modes, both disclosed in the response:

- No free-text query: the published display rule, precomputed at build time
  into `display_rank`. Official MCP first, then community, then unknown, then
  n/a, then none-found; within each band free, paid, enterprise-leaning,
  enterprise-only, unknown; then alphabetical.
- Free-text query: relevance first (how many distinct query terms matched,
  then a weighted field score), ties broken by that same display rule.

Nothing here is tunable per vendor and nothing here is purchasable.
"""

from __future__ import annotations

import difflib
import re
from typing import Any

STOPWORDS = {
    "a", "an", "the", "and", "or", "of", "for", "to", "from", "with",
    "i", "we", "my", "our", "me", "you", "your", "it", "its", "this", "that",
    "these", "those", "is", "are", "be", "can", "how", "do", "does", "did",
    "want", "need", "needs", "please", "get", "got", "use", "using", "used",
    "in", "on", "by", "at", "as", "into", "out", "up", "about", "which",
    "what", "who", "when", "where", "any", "some", "all", "best", "good",
    "tool", "tools", "vendor", "vendors", "server", "servers", "mcp", "gtm",
    "s", "there",
}

SEARCH_FIELDS: tuple[tuple[str, float], ...] = (
    ("name", 5.0),
    ("what_it_does", 3.0),
    ("revops_role", 3.0),
    ("ai_features", 2.0),
    ("category_label", 2.0),
    ("category", 2.0),
    ("notes", 1.0),
)

MCP_STATUS_VALUES = ("official", "community", "unknown", "n-a", "none-found")
GATE_VALUES = (
    "free",
    "paid",
    "enterprise-leaning",
    "enterprise-only",
    "unknown",
    "n-a",
)

GATE_ALIASES = {
    "enterprise": "enterprise-only",
    "enterprise only": "enterprise-only",
    "enterprise_only": "enterprise-only",
    "enterpriseonly": "enterprise-only",
    "enterprise-leaning": "enterprise-leaning",
    "enterprise leaning": "enterprise-leaning",
    "enterprise_leaning": "enterprise-leaning",
    "n/a": "n-a",
    "na": "n-a",
    "n_a": "n-a",
    "not applicable": "n-a",
    "self-serve": "free",
    "selfserve": "free",
}

STATUS_ALIASES = {
    "none": "none-found",
    "none found": "none-found",
    "none_found": "none-found",
    "no": "none-found",
    "nonefound": "none-found",
    "n/a": "n-a",
    "na": "n-a",
    "n_a": "n-a",
}


def normalize_gate(value: str) -> str | None:
    v = (value or "").strip().lower().replace("_", "-")
    if v in GATE_VALUES:
        return v
    return GATE_ALIASES.get((value or "").strip().lower())


def normalize_status(value: str) -> str | None:
    v = (value or "").strip().lower().replace("_", "-")
    if v in MCP_STATUS_VALUES:
        return v
    return STATUS_ALIASES.get((value or "").strip().lower())


def tokenize(query: str) -> list[str]:
    out: list[str] = []
    for raw in re.findall(r"[a-z0-9][a-z0-9\.\-_]*", (query or "").lower()):
        token = raw.strip(".-_")
        if len(token) < 2 or token in STOPWORDS:
            continue
        if token not in out:
            out.append(token)
    return out


def stem(token: str) -> str:
    """Crude prefix stem so 'enrich' reaches 'enrichment' without a thesaurus.

    Deliberately NOT a synonym map. A hand-written synonym list is an editorial
    opinion about what a vendor meant, and this directory does not put words in
    a vendor's mouth.
    """
    if len(token) <= 4:
        return token
    return token[: max(4, len(token) - 3)]


def score_entry(entry: dict[str, Any], tokens: list[str]) -> tuple[int, float, list[str]]:
    """Returns (distinct tokens matched, weighted score, matched tokens)."""
    total = 0.0
    matched: list[str] = []
    stems = [(t, re.compile(r"\b" + re.escape(stem(t)))) for t in tokens]
    for field, weight in SEARCH_FIELDS:
        value = entry.get(field)
        if not isinstance(value, str) or not value:
            continue
        low = value.lower()
        for token, pattern in stems:
            hits = len(pattern.findall(low))
            if hits:
                total += weight * min(hits, 3)
                if token not in matched:
                    matched.append(token)
    return len(matched), round(total, 2), matched


def relevance_floor(tokens: list[str]) -> int:
    if len(tokens) <= 1:
        return 1
    return 2


def match_name(entries: list[dict[str, Any]], name: str) -> tuple[list[dict[str, Any]], str]:
    """Resolve a tool name. On ambiguity, return the candidates instead of picking."""
    q = (name or "").strip().lower()
    if not q:
        return [], "empty"
    q_norm = re.sub(r"[^a-z0-9]+", "", q)

    exact = [
        e
        for e in entries
        if q
        in {
            (e.get("name") or "").lower(),
            (e.get("display_name") or "").lower(),
            (e.get("slug") or "").lower(),
            (e.get("normalized_name") or "").lower(),
            (e.get("id") or "").lower(),
        }
    ]
    if exact:
        return exact, "exact"

    squashed = [
        e
        for e in entries
        if q_norm
        and q_norm
        in {
            re.sub(r"[^a-z0-9]+", "", (e.get("name") or "").lower()),
            re.sub(r"[^a-z0-9]+", "", (e.get("slug") or "").lower()),
            re.sub(r"[^a-z0-9]+", "", (e.get("normalized_name") or "").lower()),
        }
    ]
    if squashed:
        return squashed, "normalized-exact"

    prefix = [
        e
        for e in entries
        if (e.get("name") or "").lower().startswith(q)
        or (e.get("slug") or "").lower().startswith(q)
    ]
    if prefix:
        return prefix, "prefix"

    contains = [
        e
        for e in entries
        if q in (e.get("name") or "").lower() or q in (e.get("slug") or "").lower()
    ]
    if contains:
        return contains, "substring"

    scored = []
    for e in entries:
        ratio = max(
            difflib.SequenceMatcher(None, q, (e.get("name") or "").lower()).ratio(),
            difflib.SequenceMatcher(None, q, (e.get("slug") or "").lower()).ratio(),
        )
        if ratio >= 0.66:
            scored.append((ratio, e))
    scored.sort(key=lambda p: (-p[0], p[1].get("display_rank", 0)))
    return [e for _, e in scored[:6]], "fuzzy" if scored else "none"


def order(rows: list[dict[str, Any]], by_relevance: bool) -> list[dict[str, Any]]:
    if by_relevance:
        return sorted(
            rows,
            key=lambda r: (
                -r["_hits"],
                -r["_score"],
                r["entry"].get("display_rank", 10**6),
            ),
        )
    return sorted(rows, key=lambda r: r["entry"].get("display_rank", 10**6))


ORDERING_DISCLOSURE_DISPLAY = (
    "The published display rule, precomputed at build time: official MCP "
    "first, then community, then unknown, then n/a, then none-found; within "
    "each band the gate order is free, paid, enterprise-leaning, "
    "enterprise-only, unknown; then alphabetical by name."
)

ORDERING_DISCLOSURE_RELEVANCE = (
    "Relevance to your query first (how many distinct query terms matched, "
    "then a weighted field score across name, what_it_does, revops_role, "
    "ai_features, category and notes), with ties broken by the published "
    "display rule: official MCP first, then community, then unknown, then "
    "n/a, then none-found; within each band free, paid, enterprise-leaning, "
    "enterprise-only, unknown; then alphabetical."
)


def result_row(
    entry: dict[str, Any],
    honesty: dict[str, Any],
    *,
    matched_terms: list[str] | None = None,
    relevance: float | None = None,
) -> dict[str, Any]:
    """The compact projection used by list-shaped tools."""
    row: dict[str, Any] = {
        "id": entry.get("id"),
        "name": entry.get("name"),
        "vendor_url": entry.get("vendor_url"),
        "category": entry.get("category_slug") or entry.get("category"),
        "category_label": entry.get("category_label"),
        "what_it_does": entry.get("what_it_does"),
        "revops_role": entry.get("revops_role"),
        "mcp_status": entry.get("mcp_status_bucket"),
        "mcp_urls": entry.get("mcp_urls") or [],
        "mcp_url_raw": entry.get("mcp_url"),
        "mcp_endpoint": entry.get("mcp_endpoint"),
        "mcp_docs_url": entry.get("mcp_docs_url"),
        "endpoint_status": entry.get("endpoint_status"),
        "endpoint_last_probed": entry.get("endpoint_last_probed"),
        "mcp_auth": entry.get("mcp_auth"),
        "api_gate": entry.get("api_gate_bucket"),
        "api_gate_raw": entry.get("api_gate"),
        "jobs": entry.get("jobs") or [],
        "jobs_tagged_by": entry.get("jobs_tagged_by"),
        "jobs_tagged_on": entry.get("jobs_tagged_on"),
        "github_url": entry.get("github_url"),
        "github_stars": entry.get("github_stars"),
        "github_last_commit": entry.get("github_last_commit"),
        "github_fetched_on": entry.get("github_fetched_on"),
        "github_candidates": entry.get("github_candidates") or [],
        "docs_url": entry.get("docs_url"),
        "docs_last_crawled": entry.get("docs_last_crawled"),
        "tier": entry.get("tier"),
        "last_checked": entry.get("last_checked"),
        "canonical": entry.get("canonical"),
        "canonical_id": entry.get("canonical_id"),
        "also_listed_in": entry.get("also_listed_in") or [],
        "honesty": honesty,
    }
    if matched_terms is not None:
        row["matched_terms"] = matched_terms
    if relevance is not None:
        row["relevance_score"] = relevance
    return row
