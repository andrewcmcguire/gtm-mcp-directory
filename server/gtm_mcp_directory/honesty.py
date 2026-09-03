"""The honesty envelope (SPEC 4.2). It rides on every response, without exception.

Two rules do the heavy lifting:

- `tier` is never absent and never inferred. It is the value in the file.
- Unmeasured is not the same as missing. A field that has never been measured
  says so in a sentence, because an agent reading `github_stars: null` learns
  nothing while an agent reading "no public repo was found for this vendor"
  learns the right thing.
"""

from __future__ import annotations

from typing import Any, Iterable

from . import PRODUCT_NAME, REPO, SERVER_NAME, SERVER_VERSION, UMBRELLA

JOB_TAG_MEANING = (
    "A job tag means THE VENDOR SAYS THE TOOL DOES THIS, taken from public "
    "vendor material with a source URL. It is not a test result, not a "
    "benchmark, and not an endorsement. Nobody has run these tools."
)

TEXT_MATCH_MEANING = (
    "These are TEXT MATCHES against each vendor's own description of itself, "
    "not capability tags and not test results. The vendor wrote the sentence "
    "that matched your query."
)

ORDERING_NOTE = (
    "Ordering is computed, disclosed, and not purchasable. No entry can pay "
    "for position and there is no featured or recommended field in the schema."
)

NO_NETWORK_NOTE = (
    "This server made zero outbound requests to answer this. Every fact comes "
    "from a directory baked on the build date below."
)


def _dates(values: Iterable[str | None]) -> list[str]:
    return sorted({v for v in values if isinstance(v, str) and v})


def entry_caveats(entry: dict[str, Any]) -> list[str]:
    """Everything this specific entry does NOT know, said in sentences."""
    out: list[str] = []
    status = entry.get("mcp_status_bucket") or entry.get("mcp_status")
    checked = entry.get("last_checked") or "the build date"

    if status in ("official", "community"):
        es = entry.get("endpoint_status")
        probed = entry.get("endpoint_last_probed")
        if es in ("live", "live-auth-gated") and probed:
            out.append(
                "The recorded MCP URL answered as a server on %s (%s, HTTP %s): "
                "something is listening at mcp_endpoint. That is liveness, not a "
                "test of what the tools do; bench_tested is unaffected."
                % (probed, es, entry.get("endpoint_http_status"))
            )
        elif es == "repo-local" and probed:
            out.append(
                "The recorded MCP URL is a repository or package (mcp_docs_url): "
                "a server you install and run locally over stdio, checked "
                "reachable on %s. Callable after an install; not a remote "
                "endpoint. Nobody has run its tools." % probed
            )
        elif es == "docs-only" and probed:
            out.append(
                "On %s the recorded MCP URL served a documentation page, not an "
                "MCP endpoint (mcp_docs_url). The server may well exist; the "
                "entry records where to read about it, not where to connect. "
                "An agent needs an endpoint URL before it can call this tool."
                % probed
            )
        elif es == "unreachable" and probed:
            out.append(
                "On %s no recorded MCP URL for this entry answered at all "
                "(dead, blocked, or error). Re-verify before relying on it."
                % probed
            )
        elif entry.get("mcp_urls"):
            out.append(
                "The MCP endpoint has not been probed live yet (endpoint_status: "
                "not-probed). The status was established by hand on %s." % checked
            )
        else:
            out.append(
                "mcp_status says '%s' but no parseable URL was found in the "
                "mcp_url field; it is prose, returned verbatim as mcp_url_raw. "
                "Read it before assuming an endpoint exists." % status
            )
    elif status == "none-found":
        out.append(
            "No MCP server was found for this tool as of %s. That is a "
            "not-found, not a proof of absence." % checked
        )
    elif status == "unknown":
        out.append("MCP status could not be determined from public sources.")

    if not entry.get("jobs"):
        out.append(
            "No job tags yet (jobs_tagged_by is null). Capability matching for "
            "this entry is a text match over the vendor's own description, not "
            "a tag."
        )
    elif entry.get("jobs_tagged_by") == "machine-pass":
        out.append(
            "Job tags on this entry came from a machine pass over its own "
            "what_it_does, ai_features and revops_role text on %s, and have "
            "not been read by a human (jobs_tagged_by: machine-pass). Treat "
            "them as a first pass, not an editorial judgement."
            % (entry.get("jobs_tagged_on") or "an unstamped date")
        )

    if not entry.get("github_url"):
        n = len(entry.get("github_candidates") or [])
        if n:
            out.append(
                "github_url has not been measured. %d github.com URL(s) were "
                "parsed out of mcp_url and sources as candidates; they have "
                "never been fetched, so stars, last commit and archived state "
                "are unknown." % n
            )
        else:
            out.append(
                "No github_url found for this vendor. Many GTM SaaS vendors "
                "have no public repo at all, so this is a common and correct "
                "answer rather than a gap."
            )

    if entry.get("docs_url") and not entry.get("docs_digest"):
        out.append("docs_url is known but the documentation has never been crawled.")
    elif not entry.get("docs_url"):
        out.append("No API documentation URL is on file for this vendor yet.")

    if (entry.get("api_gate_bucket") or entry.get("api_gate")) == "unknown":
        out.append(
            "api_gate is 'unknown': the vendor's public pricing did not state "
            "clearly whether API or MCP access is self-serve."
        )

    if len(entry.get("source_urls") or []) < 2:
        out.append(
            "Thin sourcing: fewer than two independent source URLs back this "
            "entry."
        )

    if entry.get("also_listed_in"):
        others = ", ".join(
            "%s in %s" % (a.get("name"), a.get("category_slug"))
            for a in entry["also_listed_in"]
        )
        out.append(
            "This product is listed in more than one category (%s). The "
            "canonical entry is %s. Do not count it twice."
            % (others, entry.get("canonical_id"))
        )
    return out


def entry_honesty(entry: dict[str, Any]) -> dict[str, Any]:
    """The per-entry envelope. Compact, because it rides on every result row."""
    return {
        "tier": entry.get("tier"),
        "tier_meaning": TIER_MEANINGS.get(entry.get("tier"), "Unknown tier."),
        "last_checked": entry.get("last_checked"),
        "measured_on": {
            "github": entry.get("github_fetched_on"),
            "docs": entry.get("docs_last_crawled"),
            "mcp_url_liveness": entry.get("endpoint_last_probed"),
        },
        "source_urls": entry.get("source_urls") or [],
        "caveats": entry_caveats(entry),
    }


TIER_MEANINGS: dict[str, str] = {
    "RESEARCHED": (
        "Facts from public sources with URLs. No usage claims. Nobody has run "
        "this tool."
    ),
    "BENCH-TESTED": (
        "Andrew personally ran it on a stated date. Cannot be bought."
    ),
}


class HonestyBuilder:
    """Builds the response-level envelope from whatever the tool actually served."""

    def __init__(self, directory, vocabulary) -> None:  # noqa: ANN001
        self.directory = directory
        self.vocabulary = vocabulary
        TIER_MEANINGS.update(directory.tier_meanings or {})
        # The build states what a tag means in its own words. Carry that
        # verbatim rather than paraphrasing it, so the server and the data can
        # never say two different things about the same claim.
        self.jobs_meaning: str = (
            (directory.payload.get("honesty") or {}).get("jobs_meaning") or ""
        ).strip()
        counts = directory.counts
        self.total = int(counts.get("entries") or 0)
        self.bench_tested = int(counts.get("bench_tested") or 0)
        self.tagged = sum(1 for e in directory.entries if e.get("jobs"))
        self.tagged_by: dict[str, int] = {}
        for e in directory.entries:
            if e.get("jobs"):
                key = e.get("jobs_tagged_by") or "unstamped"
                self.tagged_by[key] = self.tagged_by.get(key, 0) + 1
        self.with_docs_digest = sum(1 for e in directory.entries if e.get("docs_digest"))
        self.with_github = sum(1 for e in directory.entries if e.get("github_url"))
        self.official_total = sum(1 for e in directory.entries if e.get("mcp_status_bucket") == "official")
        self.official_live = sum(
            1 for e in directory.entries
            if e.get("mcp_status_bucket") == "official"
            and e.get("endpoint_status") in ("live", "live-auth-gated")
        )
        self.official_docs_only = sum(
            1 for e in directory.entries
            if e.get("mcp_status_bucket") == "official" and e.get("endpoint_status") == "docs-only"
        )
        self.endpoint_probe_date = next(
            (e.get("endpoint_last_probed") for e in directory.entries if e.get("endpoint_last_probed")), None
        )

    # -- pieces -----------------------------------------------------------
    def server_meta(self) -> dict[str, Any]:
        """Rides on every response so a stale local install is self-evident."""
        return {
            "server": SERVER_NAME,
            "server_version": SERVER_VERSION,
            "product": PRODUCT_NAME,
            "umbrella": UMBRELLA,
            "repo": REPO,
            "data_generated_on": self.directory.generated_on,
            "entry_count": self.total,
            "unique_products": int(
                self.directory.counts.get("canonical_entries") or self.total
            ),
            "data_content_sha256": self.directory.payload.get("content_sha256"),
            "data_verified_at_startup": all(
                c["passed"] for c in self.directory.checks
            ),
            "network_calls_this_response": 0,
        }

    def envelope(
        self,
        entries: list[dict[str, Any]] | None = None,
        *,
        capability: bool = False,
        text_fallback: bool = False,
        scope_note: str | None = None,
        extra_caveats: Iterable[str] | None = None,
        include_source_urls: bool = True,
    ) -> dict[str, Any]:
        entries = entries or []
        tiers = sorted({e.get("tier") for e in entries if e.get("tier")})
        if len(tiers) == 1:
            tier: Any = tiers[0]
        elif len(tiers) > 1:
            tier = "MIXED"
        else:
            # No rows in this response. The corpus-level tier still applies and
            # is never omitted.
            tier = sorted({e.get("tier") for e in self.directory.entries})[0]

        checked = _dates(e.get("last_checked") for e in entries)
        if not checked:
            checked = _dates(e.get("last_checked") for e in self.directory.entries)

        caveats: list[str] = list(self.directory.startup_caveats)
        if capability:
            caveats.append(JOB_TAG_MEANING)
            if self.jobs_meaning:
                caveats.append(self.jobs_meaning)
        if text_fallback:
            caveats.append(TEXT_MATCH_MEANING)
        if self.bench_tested == 0:
            caveats.append(
                "BENCH-TESTED count is 0 across all %d entries. Nothing in this "
                "directory has been run by a human yet. That number is not "
                "hidden and it will stay 0 until it is earned." % self.total
            )
        if self.tagged == 0:
            caveats.append(
                "Job tagging has not run: 0 of %d entries carry a jobs[] tag "
                "(SPEC 2.4 phase 2). Capability answers today are text matches "
                "over vendor descriptions." % self.total
            )
        else:
            if self.tagged < self.total:
                caveats.append(
                    "Job tagging is partial: %d of %d entries carry a jobs[] "
                    "tag. An untagged tool can still do the job; it has just "
                    "not been read yet, so an empty jobs[] is a gap in the "
                    "directory rather than a fact about the tool."
                    % (self.tagged, self.total)
                )
            machine = self.tagged_by.get("machine-pass", 0)
            if machine:
                caveats.append(
                    "%d of the %d tagged entries were tagged by a MACHINE PASS "
                    "over their own description text and have not been read by "
                    "a human (jobs_tagged_by: machine-pass). SPEC 2.4 treats "
                    "the machine pass as a first pass, not a finished one. "
                    "Provenance per entry is in jobs_tagged_by."
                    % (machine, self.tagged)
                )
        if self.endpoint_probe_date:
            caveats.append(
                "Endpoint liveness was measured on %s: %d of %d official entries "
                "record a URL that answered as an MCP server (live or asking for "
                "a key), and %d record a documentation page rather than an "
                "endpoint. docs-only is not a downgrade of mcp_status; it means "
                "the entry says where to read, not where to connect."
                % (self.endpoint_probe_date, self.official_live, self.official_total, self.official_docs_only)
            )
        else:
            caveats.append(
                "Endpoint liveness has not been measured on this build: "
                "endpoint_status is not-probed everywhere."
            )
        if self.with_github == 0:
            caveats.append(
                "GitHub health has never been measured: github_url, stars, last "
                "commit and archived state are null on all %d entries." % self.total
            )
        if self.with_docs_digest == 0:
            caveats.append(
                "The docs intel layer has not run: 0 of %d entries carry a "
                "docs_digest." % self.total
            )
        if extra_caveats:
            caveats.extend([c for c in extra_caveats if c])

        env = {
            "tier": tier,
            "tier_meaning": TIER_MEANINGS.get(
                tier,
                "Mixed tiers in this response; read the per-entry tier on each "
                "result.",
            ),
            "tier_counts": _tier_counts(entries or self.directory.entries),
            "last_checked": checked[0] if checked else None,
            "last_checked_range": {
                "oldest": checked[0] if checked else None,
                "newest": checked[-1] if checked else None,
            },
            "last_checked_meaning": (
                "The date the facts in the entry were pulled by hand from "
                "public sources. Not the date this file was baked."
            ),
            "measured_on": {
                "github": None,
                "docs": None,
                "mcp_url_liveness": None,
            },
            "measured_on_note": (
                "null means never measured, not measured-as-zero. Any of these "
                "that becomes non-null carries the date it was measured, "
                "because an unstamped number is a lie."
            ),
            "job_tag_meaning": JOB_TAG_MEANING,
            "jobs_meaning": self.jobs_meaning or JOB_TAG_MEANING,
            "jobs_meaning_source": (
                "directory.json honesty.jobs_meaning, verbatim"
                if self.jobs_meaning
                else "this server (the build carries no jobs_meaning)"
            ),
            "tagging": {
                "entries_tagged": self.tagged,
                "entries_total": self.total,
                "tagged_by": dict(sorted(self.tagged_by.items())),
            },
            "ordering": ORDERING_NOTE,
            "no_network": NO_NETWORK_NOTE,
            "counting_authority": "tools_recount.py, reconciled at build time",
            "caveats": _dedupe(caveats),
        }
        if scope_note:
            env["scope_note"] = scope_note
        if include_source_urls:
            urls: list[str] = []
            for e in entries:
                urls.extend(e.get("source_urls") or [])
            env["source_urls"] = _dedupe(urls)[:60]
            env["source_urls_note"] = (
                "Every claim in this response traces to these public URLs. "
                "Per-entry sources are on each result."
            )
        return env


def _tier_counts(entries: list[dict[str, Any]]) -> dict[str, int]:
    out: dict[str, int] = {}
    for e in entries:
        t = e.get("tier") or "UNKNOWN"
        out[t] = out.get(t, 0) + 1
    return dict(sorted(out.items()))


def _dedupe(items: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        if item and item not in seen:
            seen.add(item)
            out.append(item)
    return out
