#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_directory.py - bake the 15 hand-written category files into directory.json.

Phase 1 of The GTM MCP Directory.

All paths below are relative to this file's parent (the product directory).

Source of truth : ../NN-*.md            (auto-discovered, human-edited)
Counting authority: ../tools_recount.py
Job vocabulary  : data/jobs.yaml        (phase 2, closed)
Job tags        : data/tags.yaml        (phase 2, source)
Output          : data/directory.json
                  data/build_report.json
                  data/BUILD_REPORT.md

Laws this file inherits and enforces:

  * ZERO network I/O. Enforced, not claimed: the socket module is disarmed at
    import time and any attempt to open a connection raises.
  * Nothing is silently dropped. Every key found in a source yaml block lands
    somewhere in the output. Unrecognised keys land in `extra_fields`.
  * Missing is explicit. A field that does not exist on an entry ships as null
    (or [] for list-shaped fields), never as an absent key.
  * Raw survives normalisation. Every bucketed field keeps its verbatim source
    string alongside the bucket, because the source string often carries the
    honesty ("free (CHANGED 2026-08-25, see notes)").
  * The count reconciles or the build fails. tools_recount.py is the authority.
    Per-file entry counts, per-file mcp_status buckets, per-file api_gate
    buckets, the grand totals and the cross-file duplicate set are all compared.
    Any disagreement raises BuildFailure and exits non-zero.
  * Deterministic output. Entries are ordered by (category number, slug), key
    order is fixed by construction, and the only field that changes on a
    no-op rebuild is `generated_on`.
  * Job tags live in tags.yaml, never here and never in directory.json.
    directory.json is generated output; a tag written into it would be gone on
    the next rebuild. The merge is one-way: tags.yaml + jobs.yaml -> entry.jobs.
    An unknown job id, an unknown entry name, two keys resolving to the same
    product, or a job listed twice on one product is a BUILD FAILURE, not a
    warning. A closed vocabulary that silently accepts a typo is not closed.
  * A job tag is RESEARCHED tier and says only "the vendor says the tool does
    this". It is not a usage claim. bench_tested stays 0.

Usage:
    python src/build_directory.py                 # build, write, print the report
    python src/build_directory.py --check         # validate only, write nothing
    python src/build_directory.py --quiet         # build, write, print totals only
"""

from __future__ import annotations

import argparse
import glob
import hashlib
import importlib.util
import json
import os
import re
import sys
from collections import Counter, OrderedDict, defaultdict
from datetime import date

# --------------------------------------------------------------------------
# 0. Network guard. This build reads local files and nothing else, ever.
# --------------------------------------------------------------------------


def disarm_network() -> None:
    """Make outbound network I/O impossible for the life of this process."""
    import socket

    message = (
        "build_directory.py performs zero network I/O by design "
        "(SPEC 2.1). Something tried to open a connection."
    )

    def _deny(*_args, **_kwargs):
        raise RuntimeError(message)

    class _DeniedSocket(socket.socket):
        def __init__(self, *_args, **_kwargs):
            raise RuntimeError(message)

    socket.socket = _DeniedSocket
    socket.create_connection = _deny
    socket.getaddrinfo = _deny
    socket.gethostbyname = _deny


# --------------------------------------------------------------------------
# 1. Paths and vocabularies
# --------------------------------------------------------------------------

HERE = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
PRODUCT_DIR = os.path.dirname(HERE).replace("\\", "/")
DIRECTORY_DIR = os.path.dirname(PRODUCT_DIR).replace("\\", "/")
DATA_DIR = PRODUCT_DIR + "/data"
RECOUNT_PATH = DIRECTORY_DIR + "/tools_recount.py"
# Paths as RECORDED in the published artifacts. The absolute forms above are
# used to read from this machine; the baked JSON records the portable form so
# the artifact never carries a local filesystem layout.
DIRECTORY_DIR_REL = ".."
RECOUNT_PATH_REL = "../tools_recount.py"
INDEX_PATH = DIRECTORY_DIR + "/INDEX.md"
SCHEMA_PATH = DIRECTORY_DIR + "/SCHEMA.md"

JOBS_YAML = DATA_DIR + "/jobs.yaml"
TAGS_YAML = DATA_DIR + "/tags.yaml"

OUT_JSON = DATA_DIR + "/directory.json"
OUT_REPORT_JSON = DATA_DIR + "/build_report.json"
OUT_REPORT_MD = DATA_DIR + "/BUILD_REPORT.md"

SCHEMA_VERSION = "1.1"
PRODUCT_NAME = "The GTM MCP Directory"
UMBRELLA_BRAND = "Agent Operator"

# The 14 SCHEMA.md fields, in SCHEMA.md's own order. This list is the contract:
# every one of them appears on every entry, null when the source omits it.
SCHEMA_FIELDS = [
    "name",
    "vendor_url",
    "category",
    "what_it_does",
    "ai_features",
    "mcp_status",
    "mcp_url",
    "mcp_auth",
    "api_gate",
    "revops_role",
    "tier",
    "last_checked",
    "sources",
    "notes",
]

# Fields SPEC 2.3 adds that are already appearing in the source files.
KNOWN_EXTRA_FIELDS = ["docs_url"]

# Short box titles, carried over from map/parse.py so the map, the directory
# and the future site agree on category labels. Unlisted numbers fall back to
# a title-cased slug.
CATEGORY_LABELS = {
    "01": "Data & Enrichment",
    "02": "Engagement & Outbound",
    "03": "Conversation Intel",
    "04": "AI SDRs",
    "05": "Signals & Intent",
    "06": "RevOps Infra",
    "07": "MCP Layer",
    "08": "Video Prospecting",
    "09": "Email Deliverability",
    "10": "Scheduling & Routing",
    "11": "Enablement & Coaching",
    "12": "Forecasting & Revenue",
    "13": "Proposals & Deals",
    "14": "Inbound & PLG Chat",
    "15": "Community & Dark Social",
}

MCP_STATUS_BUCKETS = ["official", "community", "none-found", "unknown", "n-a"]
API_GATE_BUCKETS = [
    "free",
    "paid",
    "enterprise-only",
    "enterprise-leaning",
    "unknown",
    "n-a",
]

# SPEC 4.3: ordering is fixed, disclosed, computed, never purchasable.
MCP_STATUS_RANK = {
    "official": 0,
    "community": 1,
    "unknown": 2,
    "n-a": 3,
    "none-found": 4,
    "other": 5,
}
API_GATE_RANK = {
    "free": 0,
    "paid": 1,
    "enterprise-leaning": 2,
    "enterprise-only": 3,
    "unknown": 4,
    "n-a": 5,
    "other": 6,
}
SORT_RULE = (
    "official MCP first, then community, then unknown, then n/a, then "
    "none-found; within each band gate order is free, paid, "
    "enterprise-leaning, enterprise-only, unknown; then alphabetical by name. "
    "Computed, never curated, never purchasable."
)


class BuildFailure(Exception):
    """Raised when the build cannot be trusted. Never downgraded to a warning."""


# --------------------------------------------------------------------------
# 2. Regexes. Tolerant on purpose, because 15 files were hand-written over weeks.
# --------------------------------------------------------------------------

# Fenced yaml block. \r\n tolerated, trailing spaces on the fence tolerated.
YAML_BLOCK_RE = re.compile(r"^```yaml[ \t]*\r?\n(.*?)\r?\n?^```[ \t]*$", re.S | re.M)
HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*$", re.M)
# A field line: a lowercase key at column 0. Indented lines are continuations,
# which is what the source files actually do (verified: 186 of 186).
FIELD_RE = re.compile(r"^([a-z][a-z0-9_]*):[ \t]*(.*)$")
LIST_ITEM_RE = re.compile(r"^[ \t]*[-*][ \t]+(.*)$")
URL_RE = re.compile(r"https?://[^\s,;)\]<>\"']+", re.I)
CATEGORY_FILE_RE = re.compile(r"^(\d{2})-([a-z0-9\-]+)\.md$")


# --------------------------------------------------------------------------
# 3. Small helpers
# --------------------------------------------------------------------------


def read_text(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def normalize_name(name: str) -> str:
    """Identical to tools_recount.normalize_name. Duplicated here only so the
    reconciliation can compare like with like even if the import fails."""
    n = name.lower()
    n = re.sub(r"\(.*?\)", "", n)
    n = re.sub(r"[^a-z0-9]+", " ", n)
    n = re.sub(r"\s+", " ", n).strip()
    return n


def slugify(name: str) -> str:
    """URL-safe slug for a tool. Parentheticals are dropped, the way the
    duplicate detector drops them, so 'Warmly (Warmly.ai)' and 'Warmly' agree."""
    n = name.lower()
    n = re.sub(r"\(.*?\)", " ", n)
    n = n.replace("&", " and ")
    n = re.sub(r"[^a-z0-9]+", "-", n)
    return n.strip("-") or "unnamed"


def display_name(name: str) -> str:
    """House-rule display form: every dash variant normalised to ' - ',
    whitespace collapsed. The canonical `name` is never altered."""
    d = name.replace("\u2014", " - ").replace("\u2013", " - ")
    return re.sub(r"\s+", " ", d).strip()


def domain_of(value: str | None) -> str | None:
    """Reduce a vendor_url field to a bare registrable host."""
    if not value:
        return None
    v = value.strip().split()[0].strip(",;")
    v = re.sub(r"^https?://", "", v, flags=re.I)
    v = v.split("/")[0].split("?")[0].split("#")[0]
    v = re.sub(r"^www\.", "", v, flags=re.I)
    v = v.strip().lower()
    return v or None


def clean_url(url: str) -> str:
    """Trim trailing punctuation a prose sentence leaves stuck to a URL."""
    u = url.strip()
    while u and u[-1] in ".,;:!":
        u = u[:-1]
    # Balance parentheses: 'https://x/y_(z)' is legal, 'https://x/y)' is not.
    while u.endswith(")") and u.count(")") > u.count("("):
        u = u[:-1]
    return u


def extract_urls(value: str | None) -> list[str]:
    """Every URL in a field, de-duplicated, first-seen order preserved."""
    if not value:
        return []
    out: list[str] = []
    for raw in URL_RE.findall(value):
        u = clean_url(raw)
        if u and u not in out:
            out.append(u)
    return out


def bucket_mcp_status(raw: str | None) -> str:
    if not raw:
        return "unknown"
    low = raw.strip().lower()
    if low.startswith("official"):
        return "official"
    if low.startswith("community"):
        return "community"
    if low.startswith("none-found") or low.startswith("none found"):
        return "none-found"
    if low.startswith("n/a") or low.startswith("n-a"):
        return "n-a"
    if low.startswith("unknown"):
        return "unknown"
    return "other"


def bucket_api_gate(raw: str | None) -> str:
    if not raw:
        return "unknown"
    low = raw.strip().lower()
    if low.startswith("enterprise-only") or low.startswith("enterprise only"):
        return "enterprise-only"
    if low.startswith("enterprise-leaning") or low.startswith("enterprise leaning"):
        return "enterprise-leaning"
    if low.startswith("free"):
        return "free"
    if low.startswith("paid"):
        return "paid"
    if low.startswith("unknown"):
        return "unknown"
    if low.startswith("n/a") or low.startswith("n-a"):
        return "n-a"
    return "other"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# --------------------------------------------------------------------------
# 4. The yaml-ish block parser
# --------------------------------------------------------------------------


def parse_block(block: str) -> tuple[OrderedDict, list[str], dict[str, list[str]]]:
    """Parse one fenced block into {key: raw_value} plus per-block warnings.

    Handles the two shapes that actually occur in the source files:

      inline     sources: https://a, https://b
      block list sources:
                   - https://a
                   - https://b

    A duplicate key keeps the FIRST value (tools_recount keeps the last; the
    difference is recorded as a warning so it can never happen silently, and
    no duplicate keys exist in the current corpus).
    """
    fields: OrderedDict[str, str] = OrderedDict()
    list_fields: dict[str, list[str]] = {}
    warnings: list[str] = []
    current: str | None = None

    for raw_line in block.replace("\r\n", "\n").split("\n"):
        line = raw_line.rstrip()
        if not line.strip():
            continue
        m = FIELD_RE.match(line)
        if m:
            key, value = m.group(1), m.group(2).strip()
            if key in fields:
                warnings.append(
                    "DUPLICATE KEY %r in one block; first value kept" % key
                )
                current = key
                continue
            fields[key] = value
            current = key
            continue
        if current is None:
            warnings.append("ORPHAN LINE before any key: %r" % line.strip()[:80])
            continue
        item = LIST_ITEM_RE.match(line)
        if item:
            list_fields.setdefault(current, []).append(item.group(1).strip())
            continue
        # Plain wrapped continuation of the previous scalar.
        fields[current] = (fields[current] + " " + line.strip()).strip()

    # Fold block lists back into the flat value, but keep the items so the
    # list-shaped fields (sources) can be emitted losslessly.
    for key, items in list_fields.items():
        if fields.get(key):
            warnings.append(
                "MIXED SHAPE on %r: inline value AND a block list" % key
            )
            fields[key] = fields[key] + " " + " ".join(items)
        else:
            fields[key] = ", ".join(items)

    return fields, warnings, list_fields


def split_sources(raw: str | None, items: list[str] | None) -> tuple[list[str], list[str]]:
    """Return (urls, residue).

    `residue` is every non-URL fragment of the sources field, kept rather than
    dropped, because a few entries carry a prose annotation in there and
    throwing it away would be a silent lie about what the file says.
    """
    if items:
        urls: list[str] = []
        residue: list[str] = []
        for item in items:
            found = extract_urls(item)
            for u in found:
                if u not in urls:
                    urls.append(u)
            leftover = URL_RE.sub(" ", item).strip(" ,;.-")
            if leftover:
                residue.append(leftover)
        return urls, residue

    if not raw:
        return [], []
    urls = extract_urls(raw)
    residue = []
    for chunk in re.split(r"\s*,\s*", URL_RE.sub("\x00", raw)):
        text = chunk.replace("\x00", " ").strip(" ,;.-()")
        if text:
            residue.append(text)
    return urls, residue


# --------------------------------------------------------------------------
# 5. Category file discovery and parsing
# --------------------------------------------------------------------------


def discover_category_files() -> list[tuple[str, str, str, str]]:
    """[(path, filename, number, slug)] sorted by number."""
    out = []
    for path in sorted(glob.glob(DIRECTORY_DIR + "/[0-9][0-9]-*.md")):
        filename = os.path.basename(path)
        m = CATEGORY_FILE_RE.match(filename)
        if not m:
            continue
        out.append((path.replace("\\", "/"), filename, m.group(1), m.group(2)))
    return out


def category_blurb(text: str) -> str | None:
    """The intro paragraph between the H1 and the first sub-heading."""
    m = re.search(r"^#[ \t]+.+?$", text, re.M)
    if not m:
        return None
    rest = text[m.end():]
    stop = re.search(r"^#{2,6}[ \t]+", rest, re.M)
    if stop:
        rest = rest[: stop.start()]
    para = rest.strip().split("\n\n")[0].strip()
    para = re.sub(r"\s+", " ", para)
    return display_name(para) if para else None


def parse_category_file(path: str, filename: str, num: str, slug: str) -> dict:
    text = read_text(path)
    headings = [(m.start(), m.group(1), m.group(2)) for m in HEADING_RE.finditer(text)]
    blocks = list(YAML_BLOCK_RE.finditer(text))

    warnings: list[str] = []
    h3 = [h for h in headings if h[1] == "###"]
    if len(h3) != len(blocks):
        warnings.append(
            "PAIRING: %d '### ' headings vs %d yaml blocks" % (len(h3), len(blocks))
        )

    entries = []
    for index, match in enumerate(blocks):
        block_text = match.group(1)
        fields, block_warnings, list_fields = parse_block(block_text)

        # Nearest preceding heading, used only as provenance, never as the name.
        prior = [h for h in headings if h[0] < match.start()]
        heading_level = prior[-1][1] if prior else None
        heading_text = prior[-1][2] if prior else None
        if heading_level != "###":
            warnings.append(
                "BLOCK %d sits under a %s heading (%r), not '###'"
                % (index + 1, heading_level, (heading_text or "")[:60])
            )

        line_no = text.count("\n", 0, match.start()) + 1
        for w in block_warnings:
            warnings.append("entry %d (line %d): %s" % (index + 1, line_no, w))

        entries.append(
            build_entry(
                fields=fields,
                list_fields=list_fields,
                filename=filename,
                num=num,
                slug=slug,
                file_index=index,
                line_no=line_no,
                heading_text=heading_text,
                warnings=warnings,
            )
        )

    return {
        "file": filename,
        "path": path,
        "num": num,
        "slug": slug,
        "label": CATEGORY_LABELS.get(num) or slug.replace("-", " ").title(),
        "blurb": category_blurb(text),
        "entries": entries,
        "warnings": warnings,
        "sha256": sha256_text(text),
    }


def build_entry(
    fields: OrderedDict,
    list_fields: dict,
    filename: str,
    num: str,
    slug: str,
    file_index: int,
    line_no: int,
    heading_text: str | None,
    warnings: list,
) -> OrderedDict:
    """One source block -> one fully-shaped entry. Nothing dropped, nothing invented."""

    def raw(key: str) -> str | None:
        value = fields.get(key)
        if value is None:
            return None
        value = value.strip()
        return value or None

    name = raw("name")
    if not name:
        name = (heading_text or "").strip() or "(unnamed entry %d)" % (file_index + 1)
        warnings.append(
            "entry %d (line %d): MISSING name:, fell back to the heading %r"
            % (file_index + 1, line_no, name)
        )

    missing = [f for f in SCHEMA_FIELDS if f not in fields]
    if missing:
        warnings.append(
            "entry %d (line %d) %r: missing SCHEMA field(s) %s"
            % (file_index + 1, line_no, name, ", ".join(missing))
        )

    mcp_status_raw = raw("mcp_status")
    api_gate_raw = raw("api_gate")
    mcp_status = bucket_mcp_status(mcp_status_raw)
    api_gate = bucket_api_gate(api_gate_raw)
    if mcp_status == "other":
        warnings.append(
            "entry %d (line %d) %r: UNRECOGNIZED mcp_status %r"
            % (file_index + 1, line_no, name, mcp_status_raw)
        )
    if api_gate == "other":
        warnings.append(
            "entry %d (line %d) %r: UNRECOGNIZED api_gate %r"
            % (file_index + 1, line_no, name, api_gate_raw)
        )

    sources_raw = raw("sources")
    source_urls, source_residue = split_sources(sources_raw, list_fields.get("sources"))

    mcp_url_raw = raw("mcp_url")
    mcp_urls = extract_urls(mcp_url_raw)

    category_raw = raw("category")
    if category_raw and category_raw != slug:
        warnings.append(
            "entry %d (line %d) %r: category field %r does not match file slug %r"
            % (file_index + 1, line_no, name, category_raw, slug)
        )

    tier = raw("tier")
    if tier and tier not in ("RESEARCHED", "BENCH-TESTED"):
        warnings.append(
            "entry %d (line %d) %r: tier %r is outside the two-tier vocabulary"
            % (file_index + 1, line_no, name, tier)
        )

    last_checked = raw("last_checked")
    if last_checked and not re.match(r"^\d{4}-\d{2}-\d{2}$", last_checked):
        warnings.append(
            "entry %d (line %d) %r: last_checked %r is not an ISO date"
            % (file_index + 1, line_no, name, last_checked)
        )

    # Anything in the block that is neither a SCHEMA field nor a known SPEC 2.3
    # field is preserved verbatim rather than dropped.
    handled = set(SCHEMA_FIELDS) | set(KNOWN_EXTRA_FIELDS)
    extra = OrderedDict((k, v) for k, v in fields.items() if k not in handled)
    if extra:
        warnings.append(
            "entry %d (line %d) %r: unmapped key(s) %s preserved in extra_fields"
            % (file_index + 1, line_no, name, ", ".join(extra))
        )

    tool_slug = slugify(name)
    entry_id = "%s-%s" % (num, tool_slug)

    # Seeds for phase 6, clearly labelled as seeds. `github_url` itself stays
    # null because nothing has been measured yet (SPEC 2.3 rot law).
    github_candidates = [
        u for u in (mcp_urls + source_urls) if "github.com/" in u.lower()
    ]

    entry = OrderedDict()
    entry["id"] = entry_id
    entry["slug"] = tool_slug
    entry["normalized_name"] = normalize_name(name)

    # --- the 14 SCHEMA.md fields, verbatim ---------------------------------
    entry["name"] = name
    entry["vendor_url"] = raw("vendor_url")
    entry["category"] = category_raw
    entry["what_it_does"] = raw("what_it_does")
    entry["ai_features"] = raw("ai_features")
    entry["mcp_status"] = mcp_status_raw
    entry["mcp_url"] = mcp_url_raw
    entry["mcp_auth"] = raw("mcp_auth")
    entry["api_gate"] = api_gate_raw
    entry["revops_role"] = raw("revops_role")
    entry["tier"] = tier
    entry["last_checked"] = last_checked
    entry["sources"] = sources_raw
    entry["notes"] = raw("notes")

    # --- normalised / derived views, raw always kept above -----------------
    entry["mcp_status_bucket"] = mcp_status
    entry["api_gate_bucket"] = api_gate
    entry["mcp_urls"] = mcp_urls
    entry["source_urls"] = source_urls
    entry["source_annotations"] = source_residue
    entry["vendor_domain"] = domain_of(entry["vendor_url"])
    entry["display_name"] = display_name(name)

    # --- SPEC 2.3 fields, present and explicitly unmeasured ----------------
    entry["docs_url"] = raw("docs_url")
    entry["jobs"] = []
    entry["jobs_tagged_by"] = None
    entry["jobs_tagged_on"] = None
    entry["github_url"] = None
    entry["github_stars"] = None
    entry["github_last_commit"] = None
    entry["github_archived"] = None
    entry["github_fetched_on"] = None
    entry["github_candidates"] = github_candidates
    entry["docs_digest"] = None
    entry["docs_last_crawled"] = None
    entry["submission"] = None

    # --- duplicate wiring, filled in by resolve_duplicates() ---------------
    entry["canonical"] = True
    entry["canonical_id"] = entry_id
    entry["also_listed_in"] = []

    # --- provenance --------------------------------------------------------
    entry["source_file"] = filename
    entry["source_line"] = line_no
    entry["file_index"] = file_index
    entry["category_num"] = num
    entry["category_slug"] = slug
    entry["category_label"] = CATEGORY_LABELS.get(num) or slug.replace("-", " ").title()
    entry["heading"] = heading_text
    entry["missing_schema_fields"] = missing
    entry["extra_fields"] = extra

    return entry


# --------------------------------------------------------------------------
# 6. Duplicates: canonical homes come from INDEX.md, not from a hardcoded list
# --------------------------------------------------------------------------

CANONICAL_LINE_RE = re.compile(
    r"^-[ \t]+\*\*(?P<name>.+?)\*\*[ \t]*[\u2014\u2013-]+[ \t]*canonical:[ \t]*"
    r"(?P<home>\d{2}[-a-z0-9]*)",
    re.M,
)


def read_canonical_map() -> tuple[dict[str, str], list[str]]:
    """normalized product name -> canonical category number, read from INDEX.md.

    INDEX.md is the declared authority for which file owns a cross-listed tool
    ('Duplicates are left in every file on purpose ... but a fact fix must land
    in the canonical entry first'). Reading it beats hardcoding it, because the
    list moves when the directory grows.
    """
    notes: list[str] = []
    try:
        text = read_text(INDEX_PATH)
    except FileNotFoundError:
        return {}, ["INDEX.md not found; no canonical homes could be read"]

    start = text.find("## Cross-category duplicates")
    if start == -1:
        return {}, ["INDEX.md has no 'Cross-category duplicates' section"]
    end = text.find("\n## ", start + 1)
    section = text[start : end if end != -1 else len(text)]

    mapping: dict[str, str] = {}
    for m in CANONICAL_LINE_RE.finditer(section):
        norm = normalize_name(m.group("name"))
        home = m.group("home")[:2]
        if norm in mapping and mapping[norm] != home:
            notes.append(
                "INDEX.md declares two canonical homes for %r (%s and %s); "
                "first wins" % (norm, mapping[norm], home)
            )
            continue
        mapping[norm] = home
    return mapping, notes


def resolve_duplicates(entries: list[OrderedDict]) -> tuple[list[dict], list[str], list[str]]:
    """Wire canonical/also_listed_in across cross-file duplicates.

    A duplicate is the same normalized name appearing in two or more DIFFERENT
    category files. That is the same test tools_recount.py applies, so the two
    can be compared exactly.
    """
    canonical_map, notes = read_canonical_map()
    warnings: list[str] = []

    by_norm: dict[str, list[OrderedDict]] = defaultdict(list)
    for e in entries:
        by_norm[e["normalized_name"]].append(e)

    groups = []
    for norm in sorted(by_norm):
        members = by_norm[norm]
        files = {e["source_file"] for e in members}
        if len(files) < 2:
            continue

        declared = canonical_map.get(norm)
        chosen = None
        if declared:
            for e in sorted(members, key=lambda x: x["id"]):
                if e["category_num"] == declared:
                    chosen = e
                    break
            if chosen is None:
                warnings.append(
                    "INDEX.md names category %s as canonical for %r but no entry "
                    "for it exists there; falling back to the lowest category number"
                    % (declared, norm)
                )
        if chosen is None:
            chosen = sorted(members, key=lambda x: (x["category_num"], x["id"]))[0]
            if not declared:
                warnings.append(
                    "cross-file duplicate %r has no canonical home declared in "
                    "INDEX.md; defaulted to %s" % (norm, chosen["id"])
                )

        for e in members:
            e["canonical"] = e["id"] == chosen["id"]
            e["canonical_id"] = chosen["id"]
            e["also_listed_in"] = [
                OrderedDict(
                    [
                        ("id", o["id"]),
                        ("name", o["name"]),
                        ("category_num", o["category_num"]),
                        ("category_slug", o["category_slug"]),
                        ("source_file", o["source_file"]),
                        ("canonical", o["id"] == chosen["id"]),
                    ]
                )
                for o in sorted(members, key=lambda x: x["id"])
                if o["id"] != e["id"]
            ]

        groups.append(
            OrderedDict(
                [
                    ("normalized_name", norm),
                    ("canonical_id", chosen["id"]),
                    ("canonical_file", chosen["source_file"]),
                    ("declared_in_index", bool(declared)),
                    (
                        "members",
                        [
                            OrderedDict(
                                [
                                    ("id", e["id"]),
                                    ("name", e["name"]),
                                    ("source_file", e["source_file"]),
                                    ("canonical", e["canonical"]),
                                ]
                            )
                            for e in sorted(members, key=lambda x: x["id"])
                        ],
                    ),
                ]
            )
        )

    return groups, warnings, notes


# --------------------------------------------------------------------------
# 6b. A tiny YAML reader, deliberately not PyYAML
# --------------------------------------------------------------------------
#
# This build is stdlib-only and stays that way, so jobs.yaml and tags.yaml are
# read by a parser that supports exactly the subset those two files use:
# nested mappings, block sequences, sequences of mappings, plain scalars,
# single-line flow sequences (["01", "05"]), folded and literal block scalars
# (>, >-, |, |-), and whole-line comments.
#
# Anything outside that subset raises. That is the point: a vocabulary file
# that quietly parses into the wrong shape is worse than one that will not
# parse at all, and this file is small enough that a strict reader costs
# nothing. PyYAML is present on this box and is deliberately not imported.

_YAML_KEY_RE = re.compile(r"^([^\s#:\-\[][^:]*?):(?:[ \t]+(.*))?$")
_YAML_BLOCK_MARKERS = (">", ">-", ">+", "|", "|-", "|+")


class YamlSubsetError(Exception):
    """The file used YAML this reader deliberately does not support."""


def _yaml_scalar(raw: str):
    value = raw.strip()
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [_yaml_scalar(part) for part in inner.split(",")]
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    if value in ("true", "True"):
        return True
    if value in ("false", "False"):
        return False
    if value in ("null", "~", ""):
        return None
    return value


def _yaml_block_scalar(items, i, indent, marker):
    parts = []
    while i < len(items) and items[i][0] > indent:
        parts.append(items[i][1])
        i += 1
    if not parts:
        return "", i
    text = ("\n" if marker.startswith("|") else " ").join(parts)
    return text.strip(), i


def _yaml_node(items, i, indent):
    if items[i][1].startswith("- ") or items[i][1] == "-":
        return _yaml_seq(items, i, indent)
    return _yaml_map(items, i, indent)


def _yaml_map(items, i, indent):
    out = OrderedDict()
    while i < len(items) and items[i][0] == indent:
        line = items[i][1]
        if line.startswith("- ") or line == "-":
            break
        m = _YAML_KEY_RE.match(line)
        if not m:
            raise YamlSubsetError("not a key line: %r" % line[:120])
        key = m.group(1).strip()
        rest = (m.group(2) or "").strip()
        if key in out:
            raise YamlSubsetError("duplicate key %r" % key)
        i += 1
        if rest in _YAML_BLOCK_MARKERS:
            out[key], i = _yaml_block_scalar(items, i, indent, rest)
        elif rest == "":
            if i < len(items) and items[i][0] > indent:
                out[key], i = _yaml_node(items, i, items[i][0])
            else:
                out[key] = None
        else:
            out[key] = _yaml_scalar(rest)
    return out, i


def _yaml_seq(items, i, indent):
    out = []
    while i < len(items) and items[i][0] == indent and (
        items[i][1].startswith("- ") or items[i][1] == "-"
    ):
        rest = items[i][1][2:].strip() if items[i][1].startswith("- ") else ""
        if rest and _YAML_KEY_RE.match(rest):
            # A sequence item that is itself a mapping. Re-index the item's own
            # first key to the indent its siblings actually sit at, then parse
            # the whole run as an ordinary mapping.
            child_indent = indent + 2
            block = [(child_indent, rest)]
            j = i + 1
            while j < len(items) and items[j][0] > indent:
                block.append(items[j])
                j += 1
            node, consumed = _yaml_map(block, 0, child_indent)
            if consumed != len(block):
                raise YamlSubsetError(
                    "unparsed lines inside a list item near %r" % rest[:80]
                )
            out.append(node)
            i = j
        elif rest:
            out.append(_yaml_scalar(rest))
            i += 1
        else:
            i += 1
            if i < len(items) and items[i][0] > indent:
                node, i = _yaml_node(items, i, items[i][0])
                out.append(node)
            else:
                out.append(None)
    return out, i


def load_yaml_subset(path: str):
    text = read_text(path)
    items = []
    for raw in text.replace("\r\n", "\n").split("\n"):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        items.append((len(raw) - len(raw.rstrip("\n").lstrip(" ")), raw.strip()))
    if not items:
        raise YamlSubsetError("%s is empty" % path)
    value, i = _yaml_node(items, 0, items[0][0])
    if i != len(items):
        raise YamlSubsetError(
            "%s: could not parse from %r onward" % (path, items[i][1][:120])
        )
    return value


# --------------------------------------------------------------------------
# 6c. The jobs vocabulary and the job tags
# --------------------------------------------------------------------------


def load_jobs() -> tuple[list, list, dict]:
    """Read jobs.yaml. Returns (families, jobs, meta).

    The vocabulary is closed, so every structural rule is enforced here rather
    than discovered later by a surface that renders a broken job page.
    """
    if not os.path.exists(JOBS_YAML):
        raise BuildFailure(
            "jobs.yaml not found at %s. Phase 2 has landed; the job vocabulary "
            "is required. Restore it rather than building without jobs." % JOBS_YAML
        )
    try:
        doc = load_yaml_subset(JOBS_YAML)
    except YamlSubsetError as exc:
        raise BuildFailure("jobs.yaml did not parse: %s" % exc)

    families = doc.get("families") or []
    jobs = doc.get("jobs") or []
    if not families:
        raise BuildFailure("jobs.yaml declares no families")
    if not jobs:
        raise BuildFailure("jobs.yaml declares no jobs")

    family_ids = []
    for fam in families:
        for key in ("id", "label", "one_liner"):
            if not fam.get(key):
                raise BuildFailure("jobs.yaml family missing %r: %r" % (key, fam))
        if fam["id"] in family_ids:
            raise BuildFailure("jobs.yaml duplicate family id %r" % fam["id"])
        family_ids.append(fam["id"])

    seen = set()
    for index, job in enumerate(jobs):
        for key in ("id", "family", "phrasing", "label", "one_liner"):
            if not job.get(key):
                raise BuildFailure(
                    "jobs.yaml job %d missing %r: %r" % (index + 1, key, job)
                )
        if job["id"] in seen:
            raise BuildFailure("jobs.yaml duplicate job id %r" % job["id"])
        seen.add(job["id"])
        if not re.match(r"^[a-z][a-z0-9\-]*$", job["id"]):
            raise BuildFailure(
                "jobs.yaml job id %r is not a lowercase hyphenated slug" % job["id"]
            )
        if job["family"] not in family_ids:
            raise BuildFailure(
                "jobs.yaml job %r names family %r, which is not declared"
                % (job["id"], job["family"])
            )
        aliases = job.get("aliases") or []
        if not isinstance(aliases, list) or not aliases:
            raise BuildFailure(
                "jobs.yaml job %r has no aliases; find_tools needs them" % job["id"]
            )
        job["aliases"] = [str(a) for a in aliases]
        cats = job.get("primary_categories") or []
        job["primary_categories"] = [str(c) for c in cats]
        job["order"] = index

    meta = OrderedDict(
        [
            ("version", doc.get("version")),
            ("vocabulary_status", doc.get("vocabulary_status")),
            ("written_on", doc.get("written_on")),
            ("tier", doc.get("tier")),
            ("tier_meaning", doc.get("tier_meaning")),
            ("source_file", "data/jobs.yaml"),
            ("source_sha256", sha256_text(read_text(JOBS_YAML))),
        ]
    )
    return families, jobs, meta


def load_tags() -> tuple[OrderedDict, list, dict]:
    """Read tags.yaml. Returns (tags, needs_review, meta). No validation of the
    keys against the corpus happens here; that is merge_jobs's job, because it
    needs the parsed entries to do it."""
    if not os.path.exists(TAGS_YAML):
        raise BuildFailure(
            "tags.yaml not found at %s. Job tags live in that file and nowhere "
            "else. Restore it rather than shipping 293 empty jobs lists as if "
            "the tagging pass had never happened." % TAGS_YAML
        )
    try:
        doc = load_yaml_subset(TAGS_YAML)
    except YamlSubsetError as exc:
        raise BuildFailure("tags.yaml did not parse: %s" % exc)

    tags = doc.get("tags") or OrderedDict()
    if not isinstance(tags, OrderedDict):
        raise BuildFailure("tags.yaml `tags:` is not a mapping")
    needs_review = doc.get("needs_review") or []

    meta = OrderedDict(
        [
            ("version", doc.get("version")),
            ("tagged_on", doc.get("tagged_on")),
            ("tagged_by", doc.get("tagged_by")),
            ("tier", doc.get("tier")),
            ("tier_meaning", doc.get("tier_meaning")),
            ("key_resolution", doc.get("key_resolution")),
            ("source_file", "data/tags.yaml"),
            ("source_sha256", sha256_text(read_text(TAGS_YAML))),
        ]
    )
    if not meta["tagged_on"]:
        raise BuildFailure("tags.yaml has no tagged_on date; the rot law needs one")
    if meta["tagged_by"] not in ("machine-pass", "editorial", "editorial-reviewed"):
        raise BuildFailure(
            "tags.yaml tagged_by %r is outside the SPEC 2.3 vocabulary "
            "(machine-pass | editorial | editorial-reviewed)" % meta["tagged_by"]
        )
    return tags, needs_review, meta


def merge_jobs(entries: list, jobs: list, tags: OrderedDict, needs_review: list,
               tags_meta: dict) -> tuple[OrderedDict, list]:
    """Merge tags.yaml into entries[].jobs. Fails loudly, never quietly.

    A tags.yaml key is resolved against normalized_name, so one key covers every
    entry of a cross-listed product. That is deliberate: the 16 cross-file
    duplicates are one product each and one product does one set of jobs.
    """
    failures: list[str] = []
    notes: list[str] = []

    job_order = {j["id"]: j["order"] for j in jobs}
    by_norm: dict[str, list] = defaultdict(list)
    for e in entries:
        by_norm[e["normalized_name"]].append(e)

    resolved: dict[str, str] = {}   # normalized name -> the key that claimed it
    applied = 0

    for key, job_ids in tags.items():
        norm = normalize_name(str(key))
        if job_ids is None:
            job_ids = []
        if not isinstance(job_ids, list):
            failures.append("tags.yaml key %r: value is not a list of job ids" % key)
            continue
        if norm not in by_norm:
            failures.append(
                "tags.yaml key %r matches no entry (normalized to %r). A tag on a "
                "tool that is not in the directory is a typo, not a fact." % (key, norm)
            )
            continue
        if norm in resolved:
            failures.append(
                "tags.yaml keys %r and %r both resolve to the same product (%r). "
                "One product, one tag list." % (resolved[norm], key, norm)
            )
            continue
        resolved[norm] = key

        clean: list[str] = []
        for job_id in job_ids:
            job_id = str(job_id).strip()
            if job_id not in job_order:
                failures.append(
                    "tags.yaml key %r carries job id %r, which is not in jobs.yaml. "
                    "The vocabulary is closed: add the job there with a rationale, "
                    "or fix the typo." % (key, job_id)
                )
                continue
            if job_id in clean:
                failures.append(
                    "tags.yaml key %r lists job %r twice" % (key, job_id)
                )
                continue
            clean.append(job_id)

        clean.sort(key=lambda j: job_order[j])
        for e in by_norm[norm]:
            e["jobs"] = list(clean)
            e["jobs_tagged_by"] = tags_meta["tagged_by"] if clean else None
            e["jobs_tagged_on"] = tags_meta["tagged_on"] if clean else None
            applied += 1
        if not clean:
            notes.append("tags.yaml key %r resolved to an empty job list" % key)

    review_payload = []
    for item in needs_review:
        if not isinstance(item, dict) or not item.get("name"):
            failures.append("tags.yaml needs_review item is missing a name: %r" % item)
            continue
        norm = normalize_name(str(item["name"]))
        if norm not in by_norm:
            failures.append(
                "tags.yaml needs_review names %r, which matches no entry "
                "(normalized to %r)" % (item["name"], norm)
            )
            continue
        members = sorted(by_norm[norm], key=lambda x: x["id"])
        review_payload.append(
            OrderedDict(
                [
                    ("name", item["name"]),
                    ("entry_ids", [m["id"] for m in members]),
                    ("tagged", bool(members[0]["jobs"])),
                    ("job_count", len(members[0]["jobs"])),
                    ("reason", item.get("reason") or "(no reason given)"),
                ]
            )
        )

    if failures:
        for f in failures:
            print("JOB TAG FAILURE: " + f, file=sys.stderr)
        raise BuildFailure(
            "%d job-tagging problem(s) in tags.yaml; nothing was written" % len(failures)
        )

    tagged = [e for e in entries if e["jobs"]]
    untagged = [e for e in entries if not e["jobs"]]
    per_entry = Counter(len(e["jobs"]) for e in entries)

    summary = OrderedDict(
        [
            ("vocabulary_size", len(jobs)),
            ("tags_keys", len(tags)),
            ("entries_total", len(entries)),
            ("entries_tagged", len(tagged)),
            ("entries_untagged", len(untagged)),
            (
                "products_tagged",
                sum(1 for e in tagged if e["canonical"]),
            ),
            (
                "products_untagged",
                sum(1 for e in untagged if e["canonical"]),
            ),
            ("tag_assignments", sum(len(e["jobs"]) for e in entries)),
            (
                "tags_per_entry",
                OrderedDict((str(k), per_entry[k]) for k in sorted(per_entry)),
            ),
            (
                "mean_tags_per_tagged_entry",
                round(sum(len(e["jobs"]) for e in tagged) / len(tagged), 2)
                if tagged
                else 0,
            ),
            (
                "max_tags_on_one_entry",
                max((len(e["jobs"]) for e in entries), default=0),
            ),
            ("untagged_entry_ids", [e["id"] for e in untagged]),
            ("needs_review_count", len(review_payload)),
            ("needs_review", review_payload),
            ("notes", notes),
        ]
    )
    return summary, notes


def job_payload(jobs: list, families: list, entries: list, jobs_meta: dict,
                tags_meta: dict) -> tuple[list, list]:
    """The vocabulary, with the supply behind each job counted from the corpus.

    This is what SPEC 4.3's list_jobs serves and what the /jobs pages render.
    A job with almost no supply is a finding, not a hole to hide: the counts
    ship exactly as computed.
    """
    by_job: dict[str, list] = defaultdict(list)
    for e in entries:
        for job_id in e["jobs"]:
            by_job[job_id].append(e)

    out = []
    for job in jobs:
        carriers = by_job.get(job["id"], [])
        canonical = [e for e in carriers if e["canonical"]]
        status = Counter(e["mcp_status_bucket"] for e in carriers)
        gate = Counter(e["api_gate_bucket"] for e in carriers)
        out.append(
            OrderedDict(
                [
                    ("id", job["id"]),
                    ("family", job["family"]),
                    ("phrasing", job["phrasing"]),
                    ("label", job["label"]),
                    ("one_liner", job["one_liner"]),
                    ("primary_categories", job["primary_categories"]),
                    ("aliases", job["aliases"]),
                    ("order", job["order"]),
                    ("entry_count", len(carriers)),
                    ("product_count", len(canonical)),
                    (
                        "mcp_status",
                        OrderedDict(
                            (b, status.get(b, 0)) for b in MCP_STATUS_BUCKETS + ["other"]
                        ),
                    ),
                    (
                        "api_gate",
                        OrderedDict(
                            (b, gate.get(b, 0)) for b in API_GATE_BUCKETS + ["other"]
                        ),
                    ),
                    (
                        "solo_reachable",
                        sum(
                            1
                            for e in carriers
                            if e["mcp_status_bucket"] in ("official", "community")
                            and e["api_gate_bucket"] in ("free", "paid")
                        ),
                    ),
                    ("bench_tested", sum(1 for e in carriers if e["tier"] == "BENCH-TESTED")),
                    (
                        "categories",
                        OrderedDict(
                            sorted(Counter(e["category_num"] for e in carriers).items())
                        ),
                    ),
                    ("entry_ids", sorted(e["id"] for e in carriers)),
                ]
            )
        )

    fam_out = []
    for fam in families:
        members = [j for j in out if j["family"] == fam["id"]]
        fam_out.append(
            OrderedDict(
                [
                    ("id", fam["id"]),
                    ("label", fam["label"]),
                    ("one_liner", fam["one_liner"]),
                    ("job_count", len(members)),
                    ("job_ids", [j["id"] for j in members]),
                    ("entry_count", sum(j["entry_count"] for j in members)),
                ]
            )
        )
    return out, fam_out


# --------------------------------------------------------------------------
# 7. Reconciliation against tools_recount.py
# --------------------------------------------------------------------------


def load_recount():
    spec = importlib.util.spec_from_file_location("tools_recount", RECOUNT_PATH)
    if spec is None or spec.loader is None:
        raise BuildFailure("cannot load the counting authority at " + RECOUNT_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def reconcile(categories: list[dict], duplicate_groups: list[dict]) -> dict:
    """Compare this build against tools_recount.py line by line.

    Every disagreement is a build failure. There is no 'note it and ship'
    path, because a drifted count published as a fact is exactly the class of
    quiet lie the two-tier honesty law exists to prevent.
    """
    recount = load_recount()
    failures: list[str] = []
    checks: list[dict] = []

    recount_files = {
        os.path.basename(p): recount.parse_file(p)
        for p in recount.find_category_files()
    }

    mine_files = {c["file"]: c for c in categories}

    only_mine = sorted(set(mine_files) - set(recount_files))
    only_theirs = sorted(set(recount_files) - set(mine_files))
    if only_mine:
        failures.append("files this build saw but tools_recount did not: %s" % only_mine)
    if only_theirs:
        failures.append("files tools_recount saw but this build did not: %s" % only_theirs)

    grand_mine = Counter()
    grand_theirs = Counter()
    gate_mine = Counter()
    gate_theirs = Counter()
    total_mine = 0
    total_theirs = 0

    for filename in sorted(set(mine_files) & set(recount_files)):
        mine = mine_files[filename]
        theirs = recount_files[filename]

        mine_count = len(mine["entries"])
        theirs_count = theirs["entry_count"]
        total_mine += mine_count
        total_theirs += theirs_count
        ok = mine_count == theirs_count
        if not ok:
            failures.append(
                "%s entry count: build=%d recount=%d" % (filename, mine_count, theirs_count)
            )

        m_status = Counter(e["mcp_status_bucket"] for e in mine["entries"])
        t_status = Counter(theirs["mcp_counts"])
        m_gate = Counter(e["api_gate_bucket"] for e in mine["entries"])
        t_gate = Counter(theirs["gate_counts"])

        grand_mine.update(m_status)
        grand_theirs.update(t_status)
        gate_mine.update(m_gate)
        gate_theirs.update(t_gate)

        for bucket in sorted(set(m_status) | set(t_status)):
            if m_status[bucket] != t_status[bucket]:
                ok = False
                failures.append(
                    "%s mcp_status[%s]: build=%d recount=%d"
                    % (filename, bucket, m_status[bucket], t_status[bucket])
                )
        for bucket in sorted(set(m_gate) | set(t_gate)):
            if m_gate[bucket] != t_gate[bucket]:
                ok = False
                failures.append(
                    "%s api_gate[%s]: build=%d recount=%d"
                    % (filename, bucket, m_gate[bucket], t_gate[bucket])
                )

        # Name-for-name, in file order. Catches a silent re-pairing that the
        # bare counts would hide.
        mine_names = [e["name"] for e in sorted(mine["entries"], key=lambda x: x["file_index"])]
        theirs_names = [e["name"] for e in theirs["entries"]]
        if mine_names != theirs_names:
            ok = False
            diff = [
                (i, a, b)
                for i, (a, b) in enumerate(zip(mine_names, theirs_names))
                if a != b
            ][:5]
            failures.append("%s name sequence differs at %s" % (filename, diff))

        checks.append(
            OrderedDict(
                [
                    ("file", filename),
                    ("build_entries", mine_count),
                    ("recount_entries", theirs_count),
                    ("ok", ok),
                ]
            )
        )

    if total_mine != total_theirs:
        failures.append(
            "grand entry total: build=%d recount=%d" % (total_mine, total_theirs)
        )

    for bucket in sorted(set(grand_mine) | set(grand_theirs)):
        if grand_mine[bucket] != grand_theirs[bucket]:
            failures.append(
                "grand mcp_status[%s]: build=%d recount=%d"
                % (bucket, grand_mine[bucket], grand_theirs[bucket])
            )
    for bucket in sorted(set(gate_mine) | set(gate_theirs)):
        if gate_mine[bucket] != gate_theirs[bucket]:
            failures.append(
                "grand api_gate[%s]: build=%d recount=%d"
                % (bucket, gate_mine[bucket], gate_theirs[bucket])
            )

    # Duplicate sets must agree too.
    theirs_dupes = set()
    name_to_files = defaultdict(set)
    for theirs in recount_files.values():
        for e in theirs["entries"]:
            name_to_files[e["normalized"]].add(theirs["file"])
    for norm, files in name_to_files.items():
        if len(files) > 1:
            theirs_dupes.add(norm)
    mine_dupes = {g["normalized_name"] for g in duplicate_groups}
    if mine_dupes != theirs_dupes:
        failures.append(
            "duplicate sets differ. build-only=%s recount-only=%s"
            % (sorted(mine_dupes - theirs_dupes), sorted(theirs_dupes - mine_dupes))
        )

    recount_warnings = [
        "[%s] %s" % (r["file"], w) for r in recount_files.values() for w in r["warnings"]
    ]

    return OrderedDict(
        [
            ("authority", "tools_recount.py"),
            ("authority_path", RECOUNT_PATH_REL),
            ("per_file", checks),
            ("build_total", total_mine),
            ("recount_total", total_theirs),
            ("build_mcp_status", OrderedDict(sorted(grand_mine.items()))),
            ("recount_mcp_status", OrderedDict(sorted(grand_theirs.items()))),
            ("build_api_gate", OrderedDict(sorted(gate_mine.items()))),
            ("recount_api_gate", OrderedDict(sorted(gate_theirs.items()))),
            ("duplicate_names_build", sorted(mine_dupes)),
            ("duplicate_names_recount", sorted(theirs_dupes)),
            ("recount_warnings", recount_warnings),
            ("failures", failures),
            ("reconciled", not failures),
        ]
    )


# --------------------------------------------------------------------------
# 8. Coverage stats
# --------------------------------------------------------------------------


def field_coverage(entries: list[OrderedDict]) -> OrderedDict:
    total = len(entries)

    def filled(key: str) -> int:
        return sum(1 for e in entries if e.get(key) not in (None, "", [], {}))

    cov = OrderedDict()
    cov["total_entries"] = total
    cov["schema_fields"] = OrderedDict(
        (f, OrderedDict([("present", filled(f)), ("missing", total - filled(f))]))
        for f in SCHEMA_FIELDS
    )
    cov["docs_url_present"] = filled("docs_url")
    cov["docs_url_missing"] = total - filled("docs_url")
    cov["mcp_url_present"] = filled("mcp_url")
    cov["mcp_url_missing"] = total - filled("mcp_url")
    cov["mcp_url_with_parseable_url"] = sum(1 for e in entries if e["mcp_urls"])
    cov["mcp_url_pointing_at_github"] = sum(
        1 for e in entries if any("github.com/" in u.lower() for u in e["mcp_urls"])
    )
    cov["mcp_auth_present"] = filled("mcp_auth")
    cov["github_candidates_any"] = sum(1 for e in entries if e["github_candidates"])
    cov["sources_zero_urls"] = sum(1 for e in entries if not e["source_urls"])
    cov["sources_one_url"] = sum(1 for e in entries if len(e["source_urls"]) == 1)
    cov["sources_two_or_more_urls"] = sum(1 for e in entries if len(e["source_urls"]) >= 2)
    cov["sources_url_total"] = sum(len(e["source_urls"]) for e in entries)
    cov["sources_with_annotations"] = sum(1 for e in entries if e["source_annotations"])
    cov["entries_with_extra_fields"] = sum(1 for e in entries if e["extra_fields"])

    cov["mcp_status"] = OrderedDict(
        sorted(Counter(e["mcp_status_bucket"] for e in entries).items())
    )
    cov["api_gate"] = OrderedDict(
        sorted(Counter(e["api_gate_bucket"] for e in entries).items())
    )
    cov["api_gate_unknown"] = cov["api_gate"].get("unknown", 0)
    cov["tier"] = OrderedDict(sorted(Counter(e["tier"] or "(missing)" for e in entries).items()))
    cov["last_checked"] = OrderedDict(
        sorted(Counter(e["last_checked"] or "(missing)" for e in entries).items())
    )
    cov["bench_tested"] = sum(1 for e in entries if e["tier"] == "BENCH-TESTED")

    # Jobs are measured as of phase 2. Empty is still legal and still honest.
    cov["jobs_tagged"] = sum(1 for e in entries if e["jobs"])
    cov["jobs_untagged"] = total - cov["jobs_tagged"]
    cov["jobs_assignments"] = sum(len(e["jobs"]) for e in entries)
    cov["jobs_tagged_by"] = OrderedDict(
        sorted(Counter(e["jobs_tagged_by"] or "(untagged)" for e in entries).items())
    )

    # SPEC 2.3 fields that exist in the shape but have never been measured.
    cov["unmeasured_spec_fields"] = OrderedDict(
        (f, total)
        for f in (
            "github_url",
            "github_stars",
            "github_last_commit",
            "github_archived",
            "github_fetched_on",
            "docs_digest",
            "docs_last_crawled",
            "submission",
        )
    )

    # SPEC 4.4 "solo_reachable": an agent-callable MCP a solo operator can pay for.
    cov["solo_reachable"] = sum(
        1
        for e in entries
        if e["mcp_status_bucket"] in ("official", "community")
        and e["api_gate_bucket"] in ("free", "paid")
    )
    return cov


def data_quality(entries: list[OrderedDict]) -> OrderedDict:
    """Editorial findings, not build failures.

    These are things a human should look at in the source markdown. The build
    reports them and ships; it does not fix them, because none of them is a
    parse defect and the markdown is the source of truth, not this script.
    """
    law1 = [
        OrderedDict([("id", e["id"]), ("name", e["name"]), ("mcp_status", e["mcp_status"])])
        for e in entries
        if e["mcp_status_bucket"] in ("official", "community") and not e["mcp_urls"]
    ]
    thin_sources = [
        OrderedDict([("id", e["id"]), ("name", e["name"]), ("source_urls", len(e["source_urls"]))])
        for e in entries
        if len(e["source_urls"]) < 2
    ]
    return OrderedDict(
        [
            (
                "schema_law_1_risk",
                OrderedDict(
                    [
                        (
                            "rule",
                            "SCHEMA law 1: an MCP claim requires a URL. These entries "
                            "claim official or community but their mcp_url field "
                            "contains no parseable URL.",
                        ),
                        ("count", len(law1)),
                        ("entries", law1),
                    ]
                ),
            ),
            (
                "thin_sourcing",
                OrderedDict(
                    [
                        (
                            "rule",
                            "SPEC 6.3 item 8: at least two independent sources. These "
                            "entries carry fewer than two source URLs.",
                        ),
                        ("count", len(thin_sources)),
                        ("entries", thin_sources),
                    ]
                ),
            ),
            (
                "api_gate_unknown",
                OrderedDict(
                    [
                        (
                            "rule",
                            "SCHEMA law 4: api_gate is the single most useful column "
                            "for a solo operator. INDEX.md already calls this the "
                            "directory's biggest remaining quality problem.",
                        ),
                        (
                            "count",
                            sum(1 for e in entries if e["api_gate_bucket"] == "unknown"),
                        ),
                        (
                            "entry_ids",
                            [e["id"] for e in entries if e["api_gate_bucket"] == "unknown"],
                        ),
                    ]
                ),
            ),
            (
                "docs_url_missing",
                OrderedDict(
                    [
                        (
                            "rule",
                            "SPEC 3.4: docs_url is blank-legal, but it is the seed for "
                            "the whole docs intel layer (phase 6b/6c).",
                        ),
                        ("count", sum(1 for e in entries if not e["docs_url"])),
                        ("entry_ids", [e["id"] for e in entries if not e["docs_url"]]),
                    ]
                ),
            ),
        ]
    )


# --------------------------------------------------------------------------
# 9. Assembly
# --------------------------------------------------------------------------


def sort_key(entry: OrderedDict) -> tuple:
    """Storage order: stable, file-position independent, diff-friendly."""
    return (entry["category_num"], entry["slug"], entry["name"].lower())


def display_rank(entry: OrderedDict) -> tuple:
    """SPEC 4.3 ordering, precomputed so every surface agrees without guessing."""
    return (
        MCP_STATUS_RANK.get(entry["mcp_status_bucket"], 9),
        API_GATE_RANK.get(entry["api_gate_bucket"], 9),
        entry["name"].lower(),
    )


def build(today: str) -> tuple[OrderedDict, OrderedDict]:
    files = discover_category_files()
    if not files:
        raise BuildFailure("no NN-*.md category files found under " + DIRECTORY_DIR)

    categories = [parse_category_file(*f) for f in files]
    entries: list[OrderedDict] = [e for c in categories for e in c["entries"]]

    duplicate_groups, dup_warnings, dup_notes = resolve_duplicates(entries)

    # Phase 2: merge the closed job vocabulary and the job tags into the
    # entries. Duplicates are resolved first on purpose, because a tags.yaml
    # key covers a whole cross-listed product and the summary counts products
    # as well as entries.
    families, jobs_vocab, jobs_meta = load_jobs()
    tags, needs_review, tags_meta = load_tags()
    jobs_summary, jobs_notes = merge_jobs(
        entries, jobs_vocab, tags, needs_review, tags_meta
    )
    jobs_payload, families_payload = job_payload(
        jobs_vocab, families, entries, jobs_meta, tags_meta
    )

    # Precompute the disclosed display order once.
    ranked = sorted(entries, key=display_rank)
    for position, e in enumerate(ranked):
        e["display_rank"] = position

    entries_sorted = sorted(entries, key=sort_key)

    ids = Counter(e["id"] for e in entries_sorted)
    collisions = sorted(i for i, n in ids.items() if n > 1)
    if collisions:
        raise BuildFailure("entry id collision(s): %s" % collisions)

    reconciliation = reconcile(categories, duplicate_groups)

    cat_payload = []
    for c in categories:
        c_entries = sorted(c["entries"], key=sort_key)
        status = Counter(e["mcp_status_bucket"] for e in c_entries)
        gate = Counter(e["api_gate_bucket"] for e in c_entries)
        cat_jobs = Counter(j for e in c_entries for j in e["jobs"])
        job_rank = {j["id"]: j["order"] for j in jobs_payload}
        top_jobs = [
            j
            for j, _ in sorted(
                cat_jobs.items(), key=lambda kv: (-kv[1], job_rank.get(kv[0], 999))
            )
        ][:8]
        cat_payload.append(
            OrderedDict(
                [
                    ("num", c["num"]),
                    ("slug", c["slug"]),
                    ("label", c["label"]),
                    ("file", c["file"]),
                    ("one_line", c["blurb"]),
                    ("total", len(c_entries)),
                    (
                        "mcp_status",
                        OrderedDict((b, status.get(b, 0)) for b in MCP_STATUS_BUCKETS + ["other"]),
                    ),
                    (
                        "api_gate",
                        OrderedDict((b, gate.get(b, 0)) for b in API_GATE_BUCKETS + ["other"]),
                    ),
                    ("top_jobs", top_jobs),
                    ("jobs_tagged", sum(1 for e in c_entries if e["jobs"])),
                    ("entry_ids", [e["id"] for e in c_entries]),
                    ("source_sha256", c["sha256"]),
                ]
            )
        )

    totals_status = Counter(e["mcp_status_bucket"] for e in entries_sorted)
    totals_gate = Counter(e["api_gate_bucket"] for e in entries_sorted)

    parser_warnings = [
        "[%s] %s" % (c["file"], w) for c in categories for w in c["warnings"]
    ]
    parser_warnings += ["[duplicates] %s" % w for w in dup_warnings]

    payload = OrderedDict()
    payload["schema_version"] = SCHEMA_VERSION
    payload["product"] = OrderedDict(
        [
            ("name", PRODUCT_NAME),
            ("umbrella", UMBRELLA_BRAND),
            ("spec", "directory/product/SPEC.md"),
        ]
    )
    payload["generated_on"] = today
    payload["generated_by"] = "build_directory.py (phase 1)"
    payload["source"] = OrderedDict(
        [
            ("directory", DIRECTORY_DIR_REL),
            ("pattern", "NN-*.md"),
            ("files", [c["file"] for c in categories]),
            ("counting_authority", "tools_recount.py"),
            ("schema", "SCHEMA.md"),
            ("canonical_home_authority", "INDEX.md"),
            ("job_vocabulary", "data/jobs.yaml"),
            ("job_tags", "data/tags.yaml"),
            ("network_calls", 0),
        ]
    )
    payload["counts"] = OrderedDict(
        [
            ("entries", len(entries_sorted)),
            ("canonical_entries", sum(1 for e in entries_sorted if e["canonical"])),
            ("cross_listed_entries", sum(1 for e in entries_sorted if not e["canonical"])),
            ("categories", len(cat_payload)),
            (
                "mcp_status",
                OrderedDict((b, totals_status.get(b, 0)) for b in MCP_STATUS_BUCKETS + ["other"]),
            ),
            (
                "api_gate",
                OrderedDict((b, totals_gate.get(b, 0)) for b in API_GATE_BUCKETS + ["other"]),
            ),
            ("bench_tested", sum(1 for e in entries_sorted if e["tier"] == "BENCH-TESTED")),
            ("jobs", len(jobs_payload)),
            ("job_families", len(families_payload)),
            ("entries_tagged", jobs_summary["entries_tagged"]),
            ("entries_untagged", jobs_summary["entries_untagged"]),
        ]
    )
    payload["sort_rule"] = SORT_RULE
    payload["honesty"] = OrderedDict(
        [
            (
                "tier_meanings",
                OrderedDict(
                    [
                        (
                            "RESEARCHED",
                            "Facts from public sources with URLs. No usage claims. "
                            "Nobody has run this tool.",
                        ),
                        (
                            "BENCH-TESTED",
                            "Andrew personally ran it on a stated date. Cannot be bought.",
                        ),
                    ]
                ),
            ),
            (
                "unmeasured",
                "github_* and docs_digest are present on every entry and are null "
                "or empty everywhere. Nothing has been measured for them yet. "
                "jobs[] IS measured as of phase 2; read jobs_meaning before "
                "trusting a tag, and note that an empty jobs[] means nobody has "
                "tagged that entry, not that the tool does nothing.",
            ),
            (
                "jobs_meaning",
                "A job tag means THE VENDOR SAYS THE TOOL DOES THIS. Tags were "
                "derived from each entry's own what_it_does / ai_features / "
                "revops_role text, which is itself RESEARCHED tier: public "
                "sources with URLs, no usage claims, nobody has run the tool. A "
                "tag is not a test result, not proof the capability is reachable "
                "through the tool's MCP server, and not proof it is available on "
                "the gate the entry records. bench_tested is still 0.",
            ),
            (
                "last_checked_is_the_stamp",
                "last_checked is the date the facts in that entry were pulled by hand. "
                "generated_on is only the date this file was baked.",
            ),
        ]
    )
    payload["categories"] = cat_payload
    payload["job_families"] = families_payload
    payload["jobs_vocabulary"] = OrderedDict(
        [
            ("meta", jobs_meta),
            ("tags_meta", tags_meta),
            ("jobs", jobs_payload),
        ]
    )
    payload["duplicates"] = duplicate_groups
    payload["parser_warnings"] = parser_warnings
    payload["index_notes"] = dup_notes
    payload["entries"] = entries_sorted

    body = json.dumps(
        OrderedDict(
            [
                ("categories", cat_payload),
                ("job_families", families_payload),
                ("jobs_vocabulary", payload["jobs_vocabulary"]),
                ("duplicates", duplicate_groups),
                ("entries", entries_sorted),
            ]
        ),
        ensure_ascii=False,
        indent=2,
    )
    payload["content_sha256"] = sha256_text(body)
    payload["source_sha256"] = sha256_text(
        "".join(c["sha256"] for c in categories)
        + jobs_meta["source_sha256"]
        + tags_meta["source_sha256"]
    )

    report = OrderedDict()
    report["generated_on"] = today
    report["product"] = PRODUCT_NAME
    report["phase"] = "1+2"
    report["entries_parsed"] = len(entries_sorted)
    report["files_parsed"] = len(categories)
    report["reconciliation"] = reconciliation
    report["coverage"] = field_coverage(entries_sorted)
    report["jobs"] = jobs_summary
    report["jobs_meta"] = jobs_meta
    report["tags_meta"] = tags_meta
    report["jobs_supply"] = [
        OrderedDict(
            [
                ("id", j["id"]),
                ("family", j["family"]),
                ("entry_count", j["entry_count"]),
                ("product_count", j["product_count"]),
                ("official_mcp", j["mcp_status"]["official"]),
                ("solo_reachable", j["solo_reachable"]),
                ("bench_tested", j["bench_tested"]),
            ]
        )
        for j in jobs_payload
    ]
    report["data_quality"] = data_quality(entries_sorted)
    report["duplicates_resolved"] = OrderedDict(
        [
            ("groups", len(duplicate_groups)),
            (
                "declared_in_index",
                sum(1 for g in duplicate_groups if g["declared_in_index"]),
            ),
            (
                "defaulted",
                sum(1 for g in duplicate_groups if not g["declared_in_index"]),
            ),
            (
                "detail",
                [
                    OrderedDict(
                        [
                            ("normalized_name", g["normalized_name"]),
                            ("canonical", g["canonical_id"]),
                            (
                                "cross_references",
                                [m["id"] for m in g["members"] if not m["canonical"]],
                            ),
                        ]
                    )
                    for g in duplicate_groups
                ],
            ),
        ]
    )
    report["parser_warnings"] = parser_warnings
    report["index_notes"] = dup_notes
    report["file_fixes"] = []  # every edit made to a source file, logged here
    report["content_sha256"] = payload["content_sha256"]
    report["source_sha256"] = payload["source_sha256"]

    return payload, report


# --------------------------------------------------------------------------
# 10. Report rendering
# --------------------------------------------------------------------------


def render_report_md(payload: OrderedDict, report: OrderedDict) -> str:
    rec = report["reconciliation"]
    cov = report["coverage"]
    total = cov["total_entries"]
    lines: list[str] = []
    add = lines.append

    add("# The GTM MCP Directory - phase 1+2 build report")
    add("")
    add("Generated %s by `build_directory.py`. Zero network calls." % report["generated_on"])
    add("")
    add("## Reconciliation against tools_recount.py")
    add("")
    add("**%s**" % ("PASS" if rec["reconciled"] else "FAIL"))
    add("")
    add("| File | Build | tools_recount | |")
    add("|---|---|---|---|")
    for c in rec["per_file"]:
        add(
            "| %s | %d | %d | %s |"
            % (c["file"], c["build_entries"], c["recount_entries"], "OK" if c["ok"] else "DIFFERS")
        )
    add(
        "| **Total** | **%d** | **%d** | **%s** |"
        % (
            rec["build_total"],
            rec["recount_total"],
            "OK" if rec["build_total"] == rec["recount_total"] else "DIFFERS",
        )
    )
    add("")
    add("mcp_status, build: `%s`" % json.dumps(rec["build_mcp_status"]))
    add("mcp_status, recount: `%s`" % json.dumps(rec["recount_mcp_status"]))
    add("")
    add("api_gate, build: `%s`" % json.dumps(rec["build_api_gate"]))
    add("api_gate, recount: `%s`" % json.dumps(rec["recount_api_gate"]))
    add("")
    if rec["failures"]:
        add("### Failures")
        for f in rec["failures"]:
            add("- %s" % f)
        add("")

    add("## Field coverage, all %d entries" % total)
    add("")
    add("| Field | Present | Missing |")
    add("|---|---|---|")
    for f in SCHEMA_FIELDS:
        s = cov["schema_fields"][f]
        add("| %s | %d | %d |" % (f, s["present"], s["missing"]))
    add("| docs_url | %d | %d |" % (cov["docs_url_present"], cov["docs_url_missing"]))
    add("")
    add("- mcp_url non-empty: **%d of %d** (%d parse to at least one URL, %d point at github.com)"
        % (cov["mcp_url_present"], total, cov["mcp_url_with_parseable_url"],
           cov["mcp_url_pointing_at_github"]))
    add("- mcp_auth non-empty: **%d of %d**" % (cov["mcp_auth_present"], total))
    add("- docs_url present: **%d of %d**" % (cov["docs_url_present"], total))
    add("- api_gate `unknown`: **%d of %d**" % (cov["api_gate_unknown"], total))
    add("- entries with at least one github.com URL anywhere (phase 6 seed): **%d**"
        % cov["github_candidates_any"])
    add("- sources: %d URLs total; %d entries with 2+, %d with exactly 1, %d with none"
        % (cov["sources_url_total"], cov["sources_two_or_more_urls"],
           cov["sources_one_url"], cov["sources_zero_urls"]))
    add("- sources carrying a non-URL annotation (preserved, not dropped): **%d**"
        % cov["sources_with_annotations"])
    add("- solo-reachable (official or community MCP AND gate free or paid): **%d**"
        % cov["solo_reachable"])
    add("- BENCH-TESTED: **%d**. This stays 0 until Andrew runs something." % cov["bench_tested"])
    add("")
    add("mcp_status: `%s`" % json.dumps(cov["mcp_status"]))
    add("api_gate: `%s`" % json.dumps(cov["api_gate"]))
    add("tier: `%s`" % json.dumps(cov["tier"]))
    add("last_checked: `%s`" % json.dumps(cov["last_checked"]))
    add("")
    add("### SPEC 2.3 fields present in the shape, unmeasured everywhere")
    add("")
    for f, n in cov["unmeasured_spec_fields"].items():
        add("- `%s`: null or empty on all %d entries" % (f, n))
    add("")

    jb = report["jobs"]
    supply = report["jobs_supply"]
    add("## Job tagging (phase 2)")
    add("")
    add("Source files: `data/jobs.yaml` (the closed vocabulary) and "
        "`data/tags.yaml` (the tags). `directory.json` is generated output and "
        "is never the place a tag lives.")
    add("")
    add("**What a tag means: the vendor says the tool does this.** Tags are "
        "derived from each entry's own what_it_does / ai_features / revops_role "
        "text, which is RESEARCHED tier. A tag is not a test result and "
        "bench_tested is still %d." % cov["bench_tested"])
    add("")
    add("- vocabulary: **%d jobs** in **%d families**, status `%s`"
        % (jb["vocabulary_size"], len(payload["job_families"]),
           report["jobs_meta"]["vocabulary_status"]))
    add("- tags.yaml keys (products): **%d**, tagged on %s by `%s`"
        % (jb["tags_keys"], report["tags_meta"]["tagged_on"],
           report["tags_meta"]["tagged_by"]))
    add("- entries tagged: **%d of %d**; untagged: **%d**"
        % (jb["entries_tagged"], jb["entries_total"], jb["entries_untagged"]))
    add("- canonical products tagged: **%d**; untagged: **%d**"
        % (jb["products_tagged"], jb["products_untagged"]))
    add("- total tag assignments: **%d**, mean **%s** per tagged entry, max **%d**"
        % (jb["tag_assignments"], jb["mean_tags_per_tagged_entry"],
           jb["max_tags_on_one_entry"]))
    add("- flagged needs-review in tags.yaml: **%d**" % jb["needs_review_count"])
    add("")
    add("Tags per entry: `%s`" % json.dumps(jb["tags_per_entry"]))
    add("")
    add("### Supply per job, as computed")
    add("")
    add("A job with almost no supply is a finding, not a hole. These counts ship "
        "exactly as computed.")
    add("")
    add("| Job | Family | Entries | Products | Official MCP | Solo-reachable |")
    add("|---|---|---|---|---|---|")
    for j in supply:
        add("| %s | %s | %d | %d | %d | %d |"
            % (j["id"], j["family"], j["entry_count"], j["product_count"],
               j["official_mcp"], j["solo_reachable"]))
    add("")
    empty = [j["id"] for j in supply if j["entry_count"] == 0]
    add("- jobs with zero tagged supply: **%d**%s"
        % (len(empty), (" (" + ", ".join(empty) + ")") if empty else ""))
    add("")
    if jb["needs_review"]:
        add("### Needs review")
        add("")
        add("| Entry | Ids | Tagged | Reason |")
        add("|---|---|---|---|")
        for r in jb["needs_review"]:
            add("| %s | %s | %s | %s |"
                % (r["name"], ", ".join(r["entry_ids"]),
                   ("%d job(s)" % r["job_count"]) if r["tagged"] else "no",
                   r["reason"]))
        add("")
    if jb["notes"]:
        add("### Job merge notes")
        add("")
        for n in jb["notes"]:
            add("- %s" % n)
        add("")

    dupes = report["duplicates_resolved"]
    add("## Duplicates resolved")
    add("")
    add("%d cross-file duplicate groups, %d with a canonical home declared in "
        "INDEX.md, %d defaulted by the parser."
        % (dupes["groups"], dupes["declared_in_index"], dupes["defaulted"]))
    add("")
    add("| Normalized name | Canonical | Cross-references |")
    add("|---|---|---|")
    for d in dupes["detail"]:
        add("| %s | %s | %s |" % (d["normalized_name"], d["canonical"],
                                  ", ".join(d["cross_references"]) or "(none)"))
    add("")

    dq = report["data_quality"]
    add("## Data quality findings")
    add("")
    add("Editorial, not build failures. The markdown is the source of truth; the "
        "build reports these and ships.")
    add("")
    add("- SCHEMA law 1 risk (official or community with no parseable mcp_url): **%d** %s"
        % (dq["schema_law_1_risk"]["count"],
           ", ".join(e["id"] for e in dq["schema_law_1_risk"]["entries"]) or ""))
    add("- Thin sourcing (fewer than 2 source URLs): **%d**" % dq["thin_sourcing"]["count"])
    add("- api_gate unknown: **%d**" % dq["api_gate_unknown"]["count"])
    add("- docs_url missing: **%d**" % dq["docs_url_missing"]["count"])
    add("")

    add("## Source file fixes made by this build")
    add("")
    if report["file_fixes"]:
        for fix in report["file_fixes"]:
            add("- %s" % fix)
    else:
        add("None. No source category file was edited.")
    add("")

    add("## Parser warnings")
    add("")
    if report["parser_warnings"]:
        for w in report["parser_warnings"]:
            add("- %s" % w)
    else:
        add("None.")
    add("")
    if rec["recount_warnings"]:
        add("### tools_recount.py warnings on the same run")
        add("")
        for w in rec["recount_warnings"]:
            add("- %s" % w)
        add("")
    if report["index_notes"]:
        add("## INDEX.md notes")
        add("")
        for n in report["index_notes"]:
            add("- %s" % n)
        add("")

    add("## Integrity")
    add("")
    add("- content sha256: `%s`" % report["content_sha256"])
    add("- source sha256: `%s`" % report["source_sha256"])
    add("- jobs.yaml sha256: `%s`" % report["jobs_meta"]["source_sha256"])
    add("- tags.yaml sha256: `%s`" % report["tags_meta"]["source_sha256"])
    add("- network calls made: 0 (the socket module is disarmed at import)")
    add("")
    return "\n".join(lines) + "\n"


def write_json(path: str, obj) -> int:
    text = json.dumps(obj, ensure_ascii=False, indent=2) + "\n"
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return len(text.encode("utf-8"))


# --------------------------------------------------------------------------
# 11. Entry point
# --------------------------------------------------------------------------


def main(argv=None) -> int:
    disarm_network()
    parser = argparse.ArgumentParser(description="Bake directory.json from the 15 category files.")
    parser.add_argument("--check", action="store_true", help="validate only, write nothing")
    parser.add_argument("--quiet", action="store_true", help="print totals only")
    parser.add_argument("--date", default=date.today().isoformat(), help="override generated_on")
    args = parser.parse_args(argv)

    payload, report = build(args.date)
    rec = report["reconciliation"]

    if not args.quiet:
        print(render_report_md(payload, report))

    if not rec["reconciled"]:
        for f in rec["failures"]:
            print("RECONCILIATION FAILURE: " + f, file=sys.stderr)
        raise BuildFailure(
            "entry counts do not reconcile with tools_recount.py; nothing was written"
        )

    if args.check:
        print("CHECK OK: %d entries reconcile with tools_recount.py. Nothing written."
              % report["entries_parsed"])
        return 0

    os.makedirs(DATA_DIR, exist_ok=True)
    size = write_json(OUT_JSON, payload)
    write_json(OUT_REPORT_JSON, report)
    with open(OUT_REPORT_MD, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(render_report_md(payload, report))

    print("wrote %s (%d bytes, %d entries)" % (OUT_JSON, size, report["entries_parsed"]))
    print("wrote %s" % OUT_REPORT_JSON)
    print("wrote %s" % OUT_REPORT_MD)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BuildFailure as exc:
        print("BUILD FAILED: %s" % exc, file=sys.stderr)
        sys.exit(1)
