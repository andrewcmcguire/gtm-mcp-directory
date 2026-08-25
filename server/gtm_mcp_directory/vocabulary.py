"""The jobs vocabulary (SPEC 2.4), loaded if it exists and degraded honestly if not.

Phase 1 baked the SHAPE of `jobs[]` on every entry, not the values. Phase 2 (a
parallel lane) writes `jobs.yaml` and tags the entries. This server has to be
useful on both sides of that line, so:

- If `jobs.yaml` is present, natural language resolves against slugs, labels
  and aliases, and the response says which slug it resolved to.
- If it is absent, or present but no entry carries a tag yet, capability
  lookup falls back to a literal text search over the vendor's own description
  and says, in the response, that that is what happened.

Neither path invents a capability claim. That is the whole product.
"""

from __future__ import annotations

import difflib
import json
import os
import re
from pathlib import Path
from typing import Any

VOCAB_PATH_ENV = "GTM_DIRECTORY_JOBS"

JOB_FIELDS = ("slug", "label", "family", "aliases", "primary_categories", "one_liner")


def _norm(text: str) -> str:
    text = (text or "").lower().strip()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


# Words that carry no signal in a job phrasing. Kept small and generic on
# purpose: this is grammar, not a thesaurus of what vendors meant.
_FILLER = {
    "a", "an", "the", "and", "or", "of", "for", "to", "from", "with", "in",
    "on", "by", "at", "as", "into", "my", "our", "their", "your", "it", "is",
    "are", "i", "we", "you", "who", "what", "which", "that", "this", "some",
    "just", "need", "want", "get", "got", "give", "me", "us", "them", "do",
    "does", "can", "how", "somebody", "someone", "someones",
}


def _content_tokens(text: str) -> set[str]:
    return {t for t in _norm(text).split() if t and t not in _FILLER}


def _tokens_match(a: str, b: str) -> bool:
    """Loose word match so 'visited' reaches 'visitor' and 'anonymously' reaches 'anonymous'.

    A shared five-character prefix, or exact equality for short words. This is
    grammar tolerance, not a synonym table: it never claims two DIFFERENT words
    mean the same thing.
    """
    if a == b:
        return True
    if len(a) >= 5 and len(b) >= 5:
        return a[:5] == b[:5]
    return False


def _overlap(query: set[str], phrase: set[str]) -> tuple[float, float]:
    if not query or not phrase:
        return 0.0, 0.0
    hits = sum(1 for p in phrase if any(_tokens_match(q, p) for q in query))
    q_hits = sum(1 for q in query if any(_tokens_match(q, p) for p in phrase))
    return hits / len(phrase), q_hits / len(query)


def candidate_paths(data_path: Path) -> list[Path]:
    here = Path(__file__).resolve().parent
    out: list[Path] = []
    env = os.environ.get(VOCAB_PATH_ENV)
    if env:
        p = Path(env).expanduser()
        out.append(p / "jobs.yaml" if p.is_dir() else p)
    for base in (data_path.parent, here / "data", here.parent.parent, here.parent):
        for name in ("jobs.yaml", "jobs.yml", "jobs.json"):
            out.append(base / name)
    return out


def _coerce_jobs(raw: Any) -> list[dict[str, Any]]:
    """Accept every shape jobs.yaml could plausibly take, without guessing content.

    The phase-2 file on disk uses `id` rather than `slug` and adds a `phrasing`
    field. Both spellings are accepted here so the server does not break on a
    naming choice the data lane is entitled to make.
    """
    if raw is None:
        return []
    if isinstance(raw, dict):
        for key in ("jobs", "vocabulary", "slugs"):
            if key in raw:
                return _coerce_jobs(raw[key])
        # families -> list-of-jobs mapping, or slug -> job mapping
        if all(isinstance(v, dict) for v in raw.values()):
            out = []
            for key, value in raw.items():
                if {"slug", "id", "label", "aliases"} & set(value):
                    job = dict(value)
                    job.setdefault("slug", job.get("id") or key)
                    out.append(job)
                else:
                    out.extend(_coerce_jobs(value))
            return out
        if all(isinstance(v, list) for v in raw.values()):
            out = []
            for family, items in raw.items():
                for job in _coerce_jobs(items):
                    job.setdefault("family", family)
                    out.append(job)
            return out
        return []
    if isinstance(raw, list):
        out = []
        for item in raw:
            if isinstance(item, dict):
                out.append(dict(item))
            elif isinstance(item, str):
                out.append({"slug": item})
        return out
    return []


def _coerce_families(raw: Any) -> dict[str, dict[str, Any]]:
    """Family id -> {label, one_liner}, from a list or a mapping. Optional."""
    out: dict[str, dict[str, Any]] = {}
    if isinstance(raw, dict):
        raw = raw.get("families", raw)
    if isinstance(raw, list):
        for item in raw:
            if not isinstance(item, dict):
                continue
            fid = item.get("id") or item.get("slug") or item.get("family")
            if fid:
                out[str(fid)] = {
                    "label": item.get("label") or str(fid).replace("-", " "),
                    "one_liner": item.get("one_liner"),
                }
    elif isinstance(raw, dict):
        for fid, item in raw.items():
            if isinstance(item, dict):
                out[str(fid)] = {
                    "label": item.get("label") or str(fid).replace("-", " "),
                    "one_liner": item.get("one_liner"),
                }
    return out


class Vocabulary:
    """The 50-ish job slugs, or an honest empty stand-in."""

    def __init__(
        self,
        jobs: list[dict[str, Any]],
        path: Path | None,
        note: str,
        families: dict[str, dict[str, Any]] | None = None,
    ) -> None:
        self.path = path
        self.note = note
        self.source = "jobs.yaml on disk" if path else "none"
        self.meta: dict[str, Any] = {}
        self.tags_meta: dict[str, Any] = {}
        self.families = families or {}
        self.jobs: list[dict[str, Any]] = []
        self._by_slug: dict[str, dict[str, Any]] = {}
        self._alias_index: dict[str, str] = {}

        for job in jobs:
            slug = str(job.get("slug") or job.get("id") or "").strip()
            if not slug:
                continue
            family = job.get("family")
            clean = {
                "slug": slug,
                "label": job.get("label") or slug.replace("-", " "),
                "phrasing": job.get("phrasing"),
                "family": family,
                "family_label": job.get("family_label")
                or (self.families.get(family, {}).get("label") if family else None),
                "aliases": [a for a in (job.get("aliases") or []) if isinstance(a, str)],
                "primary_categories": job.get("primary_categories") or [],
                "one_liner": job.get("one_liner"),
            }
            self.jobs.append(clean)
            self._by_slug[slug] = clean
            self._alias_index.setdefault(_norm(slug), slug)
            self._alias_index.setdefault(_norm(slug.replace("-", " ")), slug)
            self._alias_index.setdefault(_norm(clean["label"]), slug)
            if clean["phrasing"]:
                self._alias_index.setdefault(_norm(clean["phrasing"]), slug)
            for alias in clean["aliases"]:
                self._alias_index.setdefault(_norm(alias), slug)

    def __bool__(self) -> bool:
        return bool(self.jobs)

    @property
    def slugs(self) -> list[str]:
        return [j["slug"] for j in self.jobs]

    def get(self, slug: str) -> dict[str, Any] | None:
        return self._by_slug.get(slug)

    def status(self) -> dict[str, Any]:
        out = {
            "loaded": bool(self.jobs),
            "source": self.source,
            "job_count": len(self.jobs),
            "family_count": len(self.families),
            "path": str(self.path).replace("\\", "/") if self.path else None,
            "note": self.note,
        }
        if self.meta:
            out["vocabulary_meta"] = self.meta
        if self.tags_meta:
            out["tagging_meta"] = self.tags_meta
        return out

    def search_text_for(self, slug: str) -> str:
        """Label plus aliases plus one-liner, used to enrich the text fallback."""
        job = self._by_slug.get(slug)
        if not job:
            return slug.replace("-", " ")
        parts = [job["label"], slug.replace("-", " ")]
        if job.get("phrasing"):
            parts.append(job["phrasing"])
        parts.extend(job["aliases"])
        if job.get("one_liner"):
            parts.append(job["one_liner"])
        return " ".join(parts)

    # -- resolution --------------------------------------------------------
    def resolve(self, query: str, limit: int = 3) -> list[dict[str, Any]]:
        """Resolve free text to job slugs. Returns [] rather than guessing wildly."""
        if not self.jobs or not query:
            return []
        q = _norm(query)
        if not q:
            return []

        if q in self._alias_index:
            slug = self._alias_index[q]
            confidence = "slug-exact" if _norm(slug) == q else "alias-exact"
            return [{"job": slug, "confidence": confidence, "score": 1.0}]

        scored: dict[str, tuple[float, str]] = {}

        def offer(slug: str, score: float, kind: str) -> None:
            if slug not in scored or score > scored[slug][0]:
                scored[slug] = (score, kind)

        q_tokens = _content_tokens(q)
        for phrase, slug in self._alias_index.items():
            if not phrase:
                continue
            if phrase in q or q in phrase:
                longer = max(len(phrase), len(q)) or 1
                offer(slug, 0.70 + 0.20 * (min(len(phrase), len(q)) / longer), "alias-substring")
            p_covered, q_covered = _overlap(q_tokens, _content_tokens(phrase))
            if p_covered >= 0.6:
                offer(slug, 0.45 + 0.25 * p_covered, "token-overlap")
            elif p_covered >= 0.5 and q_covered >= 0.5:
                offer(slug, 0.40 + 0.20 * ((p_covered + q_covered) / 2), "token-overlap")
            ratio = difflib.SequenceMatcher(None, phrase, q).ratio()
            if ratio >= 0.72:
                offer(slug, 0.30 + 0.35 * ratio, "fuzzy")

        ranked = sorted(scored.items(), key=lambda kv: (-kv[1][0], kv[0]))[:limit]
        return [
            {"job": slug, "confidence": kind, "score": round(score, 3)}
            for slug, (score, kind) in ranked
        ]


def from_payload(payload: dict[str, Any]) -> Vocabulary | None:
    """Prefer the vocabulary BAKED INTO directory.json, when the build carries one.

    Phase 2 bakes `jobs_vocabulary` and `job_families` into the artifact. That
    copy is the one the entries were actually tagged against, so it can never
    drift from the tags the way a separately-read jobs.yaml can. A jobs.yaml on
    disk is only a fallback for builds that predate this.
    """
    raw = payload.get("jobs_vocabulary")
    if not raw:
        return None
    jobs = _coerce_jobs(raw)
    if not jobs:
        return None
    families = _coerce_families(payload.get("job_families"))
    meta = raw.get("meta") if isinstance(raw, dict) else None
    tags_meta = raw.get("tags_meta") if isinstance(raw, dict) else None
    note = (
        "%d-job vocabulary read from directory.json, where the build baked it. "
        "This is the same vocabulary the entries were tagged against, so the "
        "two cannot drift apart." % len(jobs)
    )
    vocab = Vocabulary(jobs, None, note, families)
    vocab.source = "baked into directory.json"
    vocab.meta = meta or {}
    vocab.tags_meta = tags_meta or {}
    return vocab


def load_vocabulary(data_path: Path, payload: dict[str, Any] | None = None) -> Vocabulary:
    if payload is not None:
        baked = from_payload(payload)
        if baked is not None:
            return baked

    tried = candidate_paths(data_path)
    for path in tried:
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
            if path.suffix == ".json":
                raw = json.loads(text)
            else:
                import yaml  # ships with fastmcp, no new dependency

                raw = yaml.safe_load(text)
        except Exception as exc:  # noqa: BLE001 - a broken vocab must not kill the server
            return Vocabulary(
                [],
                path,
                "jobs vocabulary found at %s but could not be parsed (%s). "
                "Capability lookup fell back to text search."
                % (str(path).replace("\\", "/"), exc),
            )
        jobs = _coerce_jobs(raw)
        families = _coerce_families(raw)
        if jobs:
            return Vocabulary(
                jobs,
                path,
                "%d-job vocabulary loaded from %s"
                % (len(jobs), str(path).replace("\\", "/")),
                families,
            )
        return Vocabulary(
            [],
            path,
            "jobs vocabulary at %s parsed to zero jobs. Capability lookup fell "
            "back to text search." % str(path).replace("\\", "/"),
        )
    return Vocabulary(
        [],
        None,
        "jobs.yaml is not present on this install (SPEC 2.4 phase 2 has not "
        "landed here). Capability lookup runs as a literal text search over "
        "each vendor's own description, and every response says so.",
    )
