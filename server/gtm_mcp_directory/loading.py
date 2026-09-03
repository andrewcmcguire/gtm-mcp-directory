"""Data loading and the startup sanity gate.

Design laws this file enforces, from SPEC 4.1 and the wave-2 brief:

1. `directory.json` is loaded exactly once, at startup, into memory.
2. Zero network calls, ever. Nothing in this package imports a network client.
3. If the file is missing, unparseable, the wrong size, or fails its own
   content checksum, the server fails LOUDLY at startup instead of serving a
   half-truth. A directory that quietly serves drifted data is worse than a
   directory that refuses to start.
4. The expected entry count is READ from `build_report.json`, never hardcoded,
   so a legitimate rebuild by the data lane does not require a code change.
5. `data/` is read-only from here. This package never writes to it.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
from collections import OrderedDict
from pathlib import Path
from typing import Any


class DirectoryDataError(RuntimeError):
    """Raised when the baked data fails a startup sanity check."""


CHECKSUM_DRIFT_ENV = "GTM_DIRECTORY_ALLOW_CHECKSUM_DRIFT"
DATA_PATH_ENV = "GTM_DIRECTORY_DATA"

REQUIRED_TOP_LEVEL = (
    "schema_version",
    "product",
    "generated_on",
    "counts",
    "sort_rule",
    "honesty",
    "categories",
    "duplicates",
    "entries",
    "content_sha256",
)


def candidate_paths() -> list[Path]:
    """Every place the baked directory could legitimately live, in priority order."""
    here = Path(__file__).resolve().parent
    out: list[Path] = []

    env = os.environ.get(DATA_PATH_ENV)
    if env:
        p = Path(env).expanduser()
        out.append(p / "directory.json" if p.is_dir() else p)

    # Repo layout first: product/server/gtm_mcp_directory/ -> product/data/.
    # A checkout always reads the live build, never a stale bundled copy.
    out.append(here.parent.parent / "data" / "directory.json")
    # Bundled inside the package (what `uvx gtm-mcp-directory` gets). Put there
    # by sync_data.py before every build.
    out.append(here / "data" / "directory.json")
    # Tolerated alternate: server/data/
    out.append(here.parent / "data" / "directory.json")
    return out


def resolve_data_path() -> Path:
    tried = candidate_paths()

    # An explicit env var is an instruction, not a hint. If it points at
    # nothing, fail there rather than quietly serving some other file.
    env = os.environ.get(DATA_PATH_ENV)
    if env and not tried[0].is_file():
        raise DirectoryDataError(
            "%s is set to '%s' but no directory.json was found at %s. Refusing "
            "to silently fall back to a different copy of the data."
            % (DATA_PATH_ENV, env, tried[0])
        )

    for p in tried:
        if p.is_file():
            return p
    raise DirectoryDataError(
        "directory.json not found. The GTM MCP Directory server cannot start "
        "without its baked data.\nPaths tried, in order:\n"
        + "\n".join("  " + str(p) for p in tried)
        + "\nSet "
        + DATA_PATH_ENV
        + " to the file (or its directory) to point the server at it."
    )


# The builder hashes a canonical dump of its payload-bearing keys, in this
# order. Keys the current build does not carry are skipped, so this one list
# reproduces both the phase 1 shape (categories, duplicates, entries) and the
# phase 2 shape that adds the job vocabulary. A key added in a NEW position by
# a future build will not reproduce, and that case is handled explicitly at
# load time rather than silently.
BODY_KEYS = (
    "categories",
    "job_families",
    "jobs_vocabulary",
    "duplicates",
    "entries",
)


def content_sha256(payload: dict[str, Any], keys: tuple[str, ...] | None = None) -> str:
    """Recompute the checksum the way `src/build_directory.py` computes it."""
    order = keys or BODY_KEYS
    body = json.dumps(
        OrderedDict((k, payload[k]) for k in order if k in payload),
        ensure_ascii=False,
        indent=2,
    )
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def load_build_report(data_path: Path) -> tuple[dict[str, Any] | None, str | None]:
    """Read `build_report.json` from beside `directory.json`.

    Returns (report, warning). The report is the AUTHORITY on the expected
    entry count. If it is absent the server still starts, but it says so in
    every honesty envelope rather than pretending it verified something.
    """
    p = data_path.parent / "build_report.json"
    if not p.is_file():
        return None, (
            "build_report.json was not found beside directory.json, so the "
            "expected entry count could not be independently verified. The "
            "count check fell back to directory.json's own counts.entries, "
            "which is self-reported."
        )
    try:
        with p.open(encoding="utf-8") as fh:
            return json.load(fh), None
    except (OSError, ValueError) as exc:
        return None, (
            "build_report.json exists but could not be read (%s). The expected "
            "entry count fell back to directory.json's own counts.entries." % exc
        )


class Directory:
    """The whole in-memory directory, plus the record of how it was verified."""

    def __init__(self, payload: dict[str, Any], data_path: Path) -> None:
        self.payload = payload
        self.data_path = data_path
        self.entries: list[dict[str, Any]] = payload["entries"]
        self.categories: list[dict[str, Any]] = payload["categories"]
        self.duplicates: list[dict[str, Any]] = payload["duplicates"]
        self.counts: dict[str, Any] = payload["counts"]
        self.generated_on: str = payload["generated_on"]
        self.sort_rule: str = payload["sort_rule"]
        self.tier_meanings: dict[str, str] = payload["honesty"]["tier_meanings"]
        self.checks: list[dict[str, Any]] = []
        self.startup_caveats: list[str] = []
        self.build_report: dict[str, Any] | None = None
        self.expected_entries: int | None = None
        self.expected_entries_source: str = "unverified"

        self._by_id = {e["id"]: e for e in self.entries}
        self._categories_by_slug = {c["slug"]: c for c in self.categories}
        self._categories_by_num = {c["num"]: c for c in self.categories}

    # -- lookups ---------------------------------------------------------
    def by_id(self, entry_id: str) -> dict[str, Any] | None:
        return self._by_id.get(entry_id)

    def category(self, key: str) -> dict[str, Any] | None:
        key = (key or "").strip().lower()
        if key in self._categories_by_slug:
            return self._categories_by_slug[key]
        if key in self._categories_by_num:
            return self._categories_by_num[key]
        # tolerate "04-ai-sdr-agents" and "01-data-enrichment.md"
        stem = key[:-3] if key.endswith(".md") else key
        for cat in self.categories:
            if stem in (cat["file"][:-3], "%s-%s" % (cat["num"], cat["slug"])):
                return cat
            if stem == cat["label"].lower():
                return cat
        return None

    @property
    def category_slugs(self) -> list[str]:
        return [c["slug"] for c in self.categories]

    # -- record of the startup gate ---------------------------------------
    def _check(self, name: str, ok: bool, detail: str) -> None:
        self.checks.append({"check": name, "passed": bool(ok), "detail": detail})

    def integrity_summary(self) -> dict[str, Any]:
        return {
            "data_path": str(self.data_path).replace("\\", "/"),
            "checks": self.checks,
            "all_passed": all(c["passed"] for c in self.checks),
            "expected_entries": self.expected_entries,
            "expected_entries_source": self.expected_entries_source,
            "content_sha256": self.payload.get("content_sha256"),
        }


def load_directory(strict: bool = True) -> Directory:
    """Load, verify, and return the directory. Raises DirectoryDataError on failure."""
    data_path = resolve_data_path()

    try:
        with data_path.open(encoding="utf-8") as fh:
            payload = json.load(fh)
    except ValueError as exc:
        raise DirectoryDataError(
            "directory.json at %s is not valid JSON: %s" % (data_path, exc)
        ) from exc
    except OSError as exc:
        raise DirectoryDataError(
            "directory.json at %s could not be read: %s" % (data_path, exc)
        ) from exc

    missing = [k for k in REQUIRED_TOP_LEVEL if k not in payload]
    if missing:
        raise DirectoryDataError(
            "directory.json at %s is missing required top-level keys: %s. This "
            "is not a build of The GTM MCP Directory."
            % (data_path, ", ".join(missing))
        )
    if not isinstance(payload.get("entries"), list) or not payload["entries"]:
        raise DirectoryDataError(
            "directory.json at %s carries no entries." % data_path
        )

    directory = Directory(payload, data_path)

    # -- check 1: expected entry count, read from build_report.json --------
    report, report_warning = load_build_report(data_path)
    directory.build_report = report
    actual = len(directory.entries)

    if report is not None and isinstance(report.get("entries_parsed"), int):
        expected = int(report["entries_parsed"])
        directory.expected_entries_source = "build_report.json:entries_parsed"
    else:
        expected = int(directory.counts.get("entries") or 0)
        directory.expected_entries_source = "directory.json:counts.entries (fallback)"
        if report_warning:
            directory.startup_caveats.append(report_warning)
    directory.expected_entries = expected

    if expected <= 0:
        raise DirectoryDataError(
            "No expected entry count could be established from build_report.json "
            "or directory.json. Refusing to serve unverified data."
        )
    if actual != expected:
        raise DirectoryDataError(
            "Entry count mismatch. directory.json carries %d entries, %s says %d. "
            "The data and the build report disagree, so one of them is stale. "
            "Rebuild with src/build_directory.py."
            % (actual, directory.expected_entries_source, expected)
        )
    directory._check(
        "entry_count",
        True,
        "%d entries, matching %s" % (actual, directory.expected_entries_source),
    )

    # -- check 2: the file agrees with itself ------------------------------
    self_count = int(directory.counts.get("entries") or -1)
    if self_count != actual:
        raise DirectoryDataError(
            "directory.json disagrees with itself: counts.entries is %d, "
            "entries[] holds %d." % (self_count, actual)
        )
    directory._check("self_count", True, "counts.entries agrees with entries[]")

    cat_total = sum(int(c.get("total") or 0) for c in directory.categories)
    if cat_total != actual:
        raise DirectoryDataError(
            "Category totals sum to %d but entries[] holds %d."
            % (cat_total, actual)
        )
    directory._check(
        "category_totals",
        True,
        "%d category totals sum to %d" % (len(directory.categories), cat_total),
    )

    ids = {e.get("id") for e in directory.entries}
    if len(ids) != actual or None in ids:
        raise DirectoryDataError(
            "Entry ids are not unique or not present: %d unique ids for %d entries."
            % (len(ids), actual)
        )
    directory._check("unique_ids", True, "%d unique entry ids" % len(ids))

    # -- check 3: content checksum ----------------------------------------
    stored = payload.get("content_sha256")
    recomputed = content_sha256(payload)

    report_stamp = (report or {}).get("content_sha256")
    recipe_reproduced = stored == recomputed
    cross_checked = bool(report_stamp) and report_stamp == stored

    if recipe_reproduced:
        directory._check("content_sha256", True, "matches the stamped build")
    else:
        # Two things can produce a mismatch, and the operator needs to be told
        # which one this is. It is never treated as passable: a checksum that
        # can be talked out of failing is not a checksum.
        if cross_checked:
            diagnosis = (
                "The stamp in directory.json DOES match the one in "
                "build_report.json, so the likelier cause is that the "
                "builder's payload shape changed and BODY_KEYS in this "
                "server's loader is out of date. Check src/build_directory.py "
                "for the key list it hashes and update BODY_KEYS to match. If "
                "the key list has not changed, the file really was edited "
                "after the build."
            )
        else:
            diagnosis = (
                "The stamp in directory.json does not match build_report.json "
                "either, so the file has almost certainly been edited since "
                "the build that stamped it."
            )
        message = (
            "Content checksum mismatch on %s.\n  stored:     %s\n  recomputed: %s\n"
            "%s\nRebuild with src/build_directory.py so the checksum is "
            "restamped. To start anyway during development, set %s=1; the "
            "server will then carry a permanent 'unverified data' caveat on "
            "every single response."
            % (data_path, stored, recomputed, diagnosis, CHECKSUM_DRIFT_ENV)
        )
        if strict and os.environ.get(CHECKSUM_DRIFT_ENV, "") not in ("1", "true", "yes"):
            raise DirectoryDataError(message)
        directory._check("content_sha256", False, "MISMATCH, override in effect")
        directory.startup_caveats.append(
            "DATA NOT VERIFIED: directory.json failed its content checksum and "
            "the server was started with " + CHECKSUM_DRIFT_ENV + " set. Every "
            "fact below may have been edited after the build that stamped it."
        )
        print(message, file=sys.stderr)

    if report_warning and report is None:
        directory._check("build_report", False, report_warning)
    else:
        directory._check(
            "build_report",
            True,
            "build_report.json read from %s"
            % str(data_path.parent / "build_report.json").replace("\\", "/"),
        )

    return directory
