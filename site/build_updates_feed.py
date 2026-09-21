#!/usr/bin/env python3
"""Bake the public updates feed from directory/digests/.

digest.py writes DIGEST_YYYY-MM-DD_{daily|weekly}.md for the rail and the
newsletter. This module does not write those files and does not invent a
digest. It reads the files that already exist and emits HTML pages, markdown
twins (via generate_site), a JSON Feed, and an Atom feed.

    python build_updates_feed.py            # write into this site/ directory
    python build_updates_feed.py --out DIR
    python build_updates_feed.py --list     # print discovered files, write nothing

URL shape (live prefix https://andrewcmcguire.com/gtm-directory):

    /updates/                       index of files that exist
    /updates/daily/YYYY-MM-DD/      one daily digest
    /updates/weekly/YYYY-MM-DD/     one weekly digest
    /updates/feed.json              JSON Feed 1.1 plus source metadata
    /updates/atom.xml               Atom

A date with no matching file has no page. Gaps between the first and last
file of a kind are named on the index. Counts on a digest page come from
that file. Counts labelled as the current bake come from directory.json.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
DIGEST_DIR = HERE.parent.parent / "digests"
SITE_DIR = HERE
FILENAME_RE = re.compile(r"^DIGEST_(\d{4}-\d{2}-\d{2})_(daily|weekly)\.md$")
BUILD_DATE_RE = re.compile(r"Build date (\d{4}-\d{2}-\d{2})")
INLINE_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
INLINE_CODE_RE = re.compile(r"`([^`]+)`")
INLINE_BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
BARE_URL_RE = re.compile(r"(?<![\"'>])(https?://[^\s)<]+)(?![\"'])")
TABLE_SEP_RE = re.compile(r"^\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$")
EM = "\u2014"


def load_gs():
    if "generate_site" in sys.modules:
        return sys.modules["generate_site"]
    site = str(SITE_DIR)
    if site not in sys.path:
        sys.path.insert(0, site)
    import generate_site as gs  # noqa: E402
    return gs


def parse_date(s: str) -> dt.date:
    return dt.date.fromisoformat(s)


def missing_in_span(dates: list[str]) -> list[str]:
    """Calendar days between the first and last file that have no file.

    Weekly files are Fridays a week apart, so a 7-day gap is the cadence, not
    a miss. Only daily files use this helper.
    """
    if len(dates) < 2:
        return []
    have = {parse_date(x) for x in dates}
    start, end = min(have), max(have)
    out = []
    cur = start
    while cur <= end:
        if cur not in have:
            out.append(cur.isoformat())
        cur += dt.timedelta(days=1)
    return out


def weekly_missing(dates: list[str]) -> list[str]:
    """Fridays between the first and last weekly file that have no weekly file."""
    if len(dates) < 2:
        return []
    have = {parse_date(x) for x in dates}
    start, end = min(have), max(have)
    out = []
    cur = start
    # walk forward to the next Friday-or-same
    while cur.weekday() != 4:
        cur += dt.timedelta(days=1)
        if cur > end:
            return []
    while cur <= end:
        if cur not in have:
            out.append(cur.isoformat())
        cur += dt.timedelta(days=7)
    return out


def discover(digest_dir: Path) -> list[dict]:
    """Return one record per DIGEST_*.md, newest first. Skip anything else."""
    if not digest_dir.is_dir():
        return []
    rows = []
    for path in sorted(digest_dir.iterdir()):
        if not path.is_file():
            continue
        m = FILENAME_RE.match(path.name)
        if not m:
            continue
        date, kind = m.group(1), m.group(2)
        try:
            parse_date(date)
        except ValueError:
            continue
        text = path.read_text(encoding="utf-8")
        rows.append(parse_digest(path, date, kind, text))
    rows.sort(key=lambda r: (r["date"], 0 if r["kind"] == "weekly" else 1), reverse=True)
    return rows


def parse_digest(path: Path, date: str, kind: str, text: str) -> dict:
    lines = text.splitlines()
    title = ""
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            break
    if not title:
        title = "The GTM MCP Directory, the %s to %s" % (kind[:-2] if kind.endswith("ly") else kind, date)
    bd = BUILD_DATE_RE.search(text)
    build_date = bd.group(1) if bd else date
    body_md = text
    if lines and lines[0].startswith("# "):
        body_md = "\n".join(lines[1:]).lstrip("\n")
    lede = ""
    for line in body_md.splitlines():
        if line.strip():
            lede = line.strip()
            break
    measures = extract_measures(text)
    slug_path = "updates/%s/%s/index.html" % (kind, date)
    url_path = "updates/%s/%s/" % (kind, date)
    return {
        "date": date,
        "kind": kind,
        "title": title,
        "build_date": build_date,
        "source_file": path.name,
        "source_rel": "directory/digests/%s" % path.name,
        "text": text,
        "body_md": body_md,
        "lede": lede,
        "measures": measures,
        "slug_path": slug_path,
        "url_path": url_path,
        "rel": "../../../",
    }


def extract_measures(text: str) -> list[dict]:
    """Copy the first markdown table after '## The numbers'. Values stay as written."""
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.strip() == "## The numbers":
            start = i + 1
            break
    if start is None:
        return []
    table = []
    for line in lines[start:]:
        if not line.strip():
            if table:
                break
            continue
        if line.startswith("|"):
            table.append(line)
        elif table:
            break
    if len(table) < 3:
        return []
    header = [c.strip() for c in table[0].strip("|").split("|")]
    rows = []
    for line in table[2:]:
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        item = {"measure": cells[0], "value": cells[1]}
        if len(cells) > 2:
            item["change"] = cells[2]
        if len(header) >= 2 and header[1] and header[1] != "change":
            item["as_of"] = header[1]
        rows.append(item)
    return rows


def inline_html(gs, s: str) -> str:
    """Escape, then restore a small set of digest inline marks."""
    s = gs.detype(s or "")
    holds = []

    def keep(html_frag: str) -> str:
        holds.append(html_frag)
        return "\x00%d\x00" % (len(holds) - 1)

    def links(mo):
        label = gs.esc(mo.group(1))
        href = gs.raw_esc(mo.group(2))
        return keep('<a href="%s">%s</a>' % (href, label))

    s = INLINE_LINK_RE.sub(links, s)

    def code(mo):
        return keep("<code>%s</code>" % gs.esc(mo.group(1)))

    s = INLINE_CODE_RE.sub(code, s)

    def bold(mo):
        return keep("<strong>%s</strong>" % gs.esc(mo.group(1)))

    s = INLINE_BOLD_RE.sub(bold, s)

    def bare(mo):
        url = mo.group(1).rstrip(".,;:)")
        return keep('<a href="%s">%s</a>' % (gs.raw_esc(url), gs.esc(url)))

    s = BARE_URL_RE.sub(bare, s)
    s = gs.esc(s)
    for i, frag in enumerate(holds):
        s = s.replace("\x00%d\x00" % i, frag)
    return s


def md_to_html(gs, text: str) -> str:
    """Render the digest subset: headings, tables, lists, paragraphs, inline marks."""
    lines = (text or "").splitlines()
    out = []
    i = 0
    n = len(lines)

    def flush_para(buf):
        if buf:
            out.append("<p>%s</p>" % inline_html(gs, " ".join(buf)))
            buf.clear()

    para = []
    while i < n:
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            flush_para(para)
            i += 1
            continue
        if stripped.startswith("#"):
            flush_para(para)
            hashes = len(stripped) - len(stripped.lstrip("#"))
            if 1 <= hashes <= 3 and stripped[hashes:hashes + 1] in ("", " "):
                level = min(hashes + 1, 3) if hashes == 1 else hashes
                # page already has the file's H1; file H1 was stripped. Remaining
                # # maps to h2 so the chrome h1 stays unique.
                if hashes == 1:
                    level = 2
                out.append("<h%d>%s</h%d>" % (level, inline_html(gs, stripped[hashes:].strip()), level))
                i += 1
                continue
        if stripped.startswith("|") and i + 1 < n and TABLE_SEP_RE.match(lines[i + 1].strip()):
            flush_para(para)
            header = [c.strip() for c in stripped.strip("|").split("|")]
            i += 2
            body = []
            while i < n and lines[i].strip().startswith("|"):
                body.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            thead = "<thead><tr>%s</tr></thead>" % "".join(
                "<th>%s</th>" % inline_html(gs, c) for c in header)
            tbody_rows = []
            for cells in body:
                tds = []
                for j, c in enumerate(cells):
                    cls = ' class="n"' if j > 0 else ""
                    tds.append("<td%s>%s</td>" % (cls, inline_html(gs, c)))
                tbody_rows.append("<tr>%s</tr>" % "".join(tds))
            out.append('<div class="scroller"><table class="datatable">%s<tbody>%s</tbody></table></div>'
                       % (thead, "".join(tbody_rows)))
            continue
        if stripped.startswith("- ") or stripped.startswith("* "):
            flush_para(para)
            items = []
            while i < n and (lines[i].strip().startswith("- ") or lines[i].strip().startswith("* ")):
                items.append("<li>%s</li>" % inline_html(gs, lines[i].strip()[2:]))
                i += 1
            out.append("<ul>%s</ul>" % "".join(items))
            continue
        para.append(stripped)
        i += 1
    flush_para(para)
    return "\n".join(out)


def kind_label(kind: str) -> str:
    return "Daily digest" if kind == "daily" else "Weekly digest"


def gap_note(rows: list[dict]) -> str:
    daily = [r["date"] for r in rows if r["kind"] == "daily"]
    weekly = [r["date"] for r in rows if r["kind"] == "weekly"]
    bits = []
    d_miss = missing_in_span(daily)
    w_miss = weekly_missing(weekly)
    if d_miss:
        bits.append("Daily files are missing for %s. Those dates have no page."
                    % ", ".join(d_miss))
    if w_miss:
        bits.append("Weekly files are missing for Friday%s %s. Those dates have no page."
                    % ("" if len(w_miss) == 1 else "s", ", ".join(w_miss)))
    if daily:
        bits.append("Latest daily file: %s." % daily[0])
    else:
        bits.append("No daily digest file is present.")
    if weekly:
        bits.append("Latest weekly file: %s." % weekly[0])
    else:
        bits.append("No weekly digest file is present.")
    bits.append("A later date is unpublished until digest.py writes the file. "
                "This bake does not invent one.")
    return " ".join(bits)


def headline_cells(row: dict) -> str:
    """A few measures copied from the digest table, for the index row."""
    wanted = (
        "GTM tools in the directory",
        "with an official MCP server",
        "servers that answer a live handshake",
        "individual MCP tools catalogued (gateways excluded)",
        "tools with an official CLI",
    )
    by = {m["measure"]: m for m in row.get("measures") or []}
    cells = []
    for label in wanted:
        m = by.get(label)
        if not m:
            continue
        change = m.get("change") or ""
        extra = (" %s" % change) if change else ""
        cells.append("%s: %s%s" % (label, m["value"], extra))
    return "; ".join(cells)


def neighbors(rows: list[dict], current: dict) -> tuple[dict | None, dict | None]:
    same = [r for r in rows if r["kind"] == current["kind"]]
    # same is newest-first
    idx = next((i for i, r in enumerate(same) if r["date"] == current["date"]), None)
    if idx is None:
        return None, None
    newer = same[idx - 1] if idx > 0 else None
    older = same[idx + 1] if idx + 1 < len(same) else None
    return older, newer


def render_digest_page(gs, row: dict, rows: list[dict], d, r) -> str:
    rel = row["rel"]
    older, newer = neighbors(rows, row)
    body = md_to_html(gs, row["body_md"])
    if not body.strip():
        body = ("<p>This digest file is empty. The generator did not invent "
                "content for %s.</p>" % gs.esc(row["source_file"]))
    nav = []
    if newer:
        nav.append('<a href="../%s/">Newer %s (%s)</a>'
                   % (newer["date"], newer["kind"], newer["date"]))
    nav.append('<a href="../../index.html">All updates</a>')
    if older:
        nav.append('<a href="../%s/">Older %s (%s)</a>'
                   % (older["date"], older["kind"], older["date"]))
    nav_html = " · ".join(nav)
    desc = (row["lede"] or row["title"])[:220]
    extra = ('<link rel="alternate" type="application/atom+xml" '
             'href="../../atom.xml" title="GTM MCP Directory updates">\n'
             '<link rel="alternate" type="application/feed+json" '
             'href="../../feed.json" title="GTM MCP Directory updates JSON">\n')
    trail = [("Directory", "index.html"),
             ("Updates", "updates/index.html"),
             ("%s %s" % (kind_label(row["kind"]), row["date"]), row["slug_path"])]
    article = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": gs.detype(row["title"]),
        "datePublished": row["date"],
        "dateModified": row["build_date"],
        "author": {"@type": "Person", "name": "Andrew McGuire"},
        "url": gs.abs_url(row["slug_path"]),
        "isAccessibleForFree": True,
        "description": gs.detype(desc),
    }
    page = (
        gs.head("%s | The GTM MCP Directory" % row["title"], desc, rel, extra=extra,
                ld=[article, gs.crumb_ld(rel, trail)], canon=row["slug_path"])
        + gs.masthead(rel, "updates")
        + f"""<div class="wrap">
<div class="crumbs"><a href="{rel}index.html">Directory</a> /
<a href="{rel}updates/index.html">Updates</a> /
{gs.esc(kind_label(row["kind"]))} {gs.esc(row["date"])}</div>
<div class="qhead">
<div class="eyebrow">{gs.esc(kind_label(row["kind"]))}</div>
<h1>{gs.esc(row["title"])}</h1>
</div>
<p class="note">Rendered from <code>{gs.esc(row["source_rel"])}</code>.
Every number on this page was already in that file. The generator did not
compute a second set of counts. Current directory bake is
{gs.esc(d["generated_on"])}, {gs.num(d["counts"]["entries"])} entries in
<a href="{rel}data/directory.json">directory.json</a>.</p>
<div class="prose digest-body" style="margin-top:22px;max-width:82ch">
{body}
</div>
<p class="note" style="margin-top:28px">{nav_html}</p>
</div>
"""
        + gs.footer(rel, d, r)
    )
    return page


def render_index(gs, rows: list[dict], d, r) -> str:
    rel = "../"
    c = d["counts"]
    gen = d["generated_on"]
    daily = [x for x in rows if x["kind"] == "daily"]
    weekly = [x for x in rows if x["kind"] == "weekly"]

    def block(title, items, empty_msg):
        if not items:
            return f'<p class="sub">{gs.esc(empty_msg)}</p>'
        lis = []
        for item in items:
            teaser = headline_cells(item)
            extra = f'<div class="desc">{gs.esc(teaser)}</div>' if teaser else ""
            lis.append(
                f'<li class="row"><div class="top">'
                f'<a class="nm" href="{item["kind"]}/{item["date"]}/">{gs.esc(item["title"])}</a>'
                f'<span class="dom">{gs.esc(item["date"])} · {gs.esc(item["kind"])}</span>'
                f"</div>"
                f'<div class="desc">{gs.esc(item["lede"])}</div>'
                f"{extra}"
                f'<p class="note">Source file {gs.esc(item["source_file"])}.</p>'
                f"</li>"
            )
        return f'<ul class="rows">\n{"".join(lis)}\n</ul>'

    extra = ('<link rel="alternate" type="application/atom+xml" '
             'href="atom.xml" title="GTM MCP Directory updates">\n'
             '<link rel="alternate" type="application/feed+json" '
             'href="feed.json" title="GTM MCP Directory updates JSON">\n')
    ld_rows = [(x["title"], x["slug_path"]) for x in rows]
    blog = {
        "@context": "https://schema.org",
        "@type": "Blog",
        "name": "The GTM MCP Directory updates",
        "url": gs.abs_url("updates/index.html"),
        "description": ("Daily and weekly what-changed files from directory/digests/, "
                        "published as pages. A missing file is a missing page."),
        "author": {"@type": "Person", "name": "Andrew McGuire"},
    }
    empty_daily = ("No daily digest file is in directory/digests/. "
                   "digest.py has not written one yet. This page does not invent one.")
    empty_weekly = ("No weekly digest file is in directory/digests/. "
                    "digest.py has not written one yet. This page does not invent one.")
    page = (
        gs.head("Updates: daily and weekly changes | The GTM MCP Directory",
                "What changed in The GTM MCP Directory, as written by digest.py. "
                "%d daily and %d weekly files on disk. Current bake %s, %s entries."
                % (len(daily), len(weekly), gen, c["entries"]),
                rel, extra=extra,
                ld=[blog,
                    gs.crumb_ld(rel, [("Directory", "index.html"),
                                      ("Updates", "updates/index.html")]),
                    gs.itemlist_ld("Directory updates",
                                   "Daily and weekly digests that exist as files.",
                                   "updates/index.html", ld_rows, newest_first=True)],
                canon="updates/index.html")
        + gs.masthead(rel, "updates")
        + f"""<div class="wrap wide">
<div class="crumbs" style="padding-bottom:0"><a href="{rel}index.html">Directory</a> / Updates</div>
<section style="padding-top:18px">
<div class="qhead">
<div class="eyebrow">The public feed</div>
<h1>What changed.</h1>
</div>
<p class="sub">These pages are the daily and weekly reports already sitting in
<code>directory/digests/</code>. The rail mails them to Andrew and the
newsletter lifts lines from them. This bake turns each file that exists into
a public page. A date with no file has no page.</p>
<div class="stats">
<div class="stat is-gold"><div class="n">{gs.num(c["entries"])}</div>
<div class="k">entries in this bake, {gs.esc(gen)}</div></div>
<div class="stat is-gold"><div class="n">{c["mcp_status"]["official"]}</div>
<div class="k">official MCP servers, {gs.esc(gen)}</div></div>
<div class="stat"><div class="n">{len(daily)}</div>
<div class="k">daily digest files on disk</div></div>
<div class="stat"><div class="n">{len(weekly)}</div>
<div class="k">weekly digest files on disk</div></div>
</div>
<p class="note">The two gold tiles are the current <a href="{rel}data/directory.json">directory.json</a>
counts, dated {gs.esc(gen)}. They are not a digest delta. Numbers inside a
digest page belong to that file's own build date.</p>
<p class="note">{gs.esc(gap_note(rows))}</p>
<div class="btnrow">
<a class="btn" href="feed.json">JSON feed</a>
<a class="btn ghost" href="atom.xml">Atom feed</a>
<a class="btn ghost" href="{rel}data.html">directory.json</a>
</div>
</section>
<section class="tint">
<div class="wrap wide" style="padding-left:0;padding-right:0">
<div class="eyebrow">Weekly</div>
<h2>Friday roll-ups.</h2>
<p class="sub">{len(weekly)} weekly file{"" if len(weekly) == 1 else "s"} on disk.</p>
{block("Weekly", weekly, empty_weekly)}
</div>
</section>
<section>
<div class="eyebrow">Daily</div>
<h2>Day-by-day files.</h2>
<p class="sub">{len(daily)} daily file{"" if len(daily) == 1 else "s"} on disk.</p>
{block("Daily", daily, empty_daily)}
<p class="note">How a file becomes a page: <code>directory/UPDATES_FEED.md</code>.
digest.py still writes the files. Moving that job off the EC2 rail onto
Powerhouse is not part of this bake.</p>
</section>
</div>"""
        + gs.footer(rel, d, r)
    )
    return page


def xml_text(el, text):
    el.text = text


def build_atom(gs, rows: list[dict], d) -> str:
    b = gs.SITE_BASE.rstrip("/")
    feed = ET.Element("feed", {"xmlns": "http://www.w3.org/2005/Atom"})
    xml_text(ET.SubElement(feed, "title"), "The GTM MCP Directory updates")
    ET.SubElement(feed, "link", {"href": b + "/updates/", "rel": "alternate"})
    ET.SubElement(feed, "link", {"href": b + "/updates/atom.xml", "rel": "self",
                                 "type": "application/atom+xml"})
    updated = (rows[0]["date"] if rows else d["generated_on"]) + "T00:00:00Z"
    xml_text(ET.SubElement(feed, "updated"), updated)
    xml_text(ET.SubElement(feed, "id"), b + "/updates/")
    author = ET.SubElement(feed, "author")
    xml_text(ET.SubElement(author, "name"), "Andrew McGuire")
    xml_text(ET.SubElement(feed, "subtitle"),
             "Daily and weekly what-changed files from directory/digests/. "
             "A missing file is a missing entry. Baked %s." % d["generated_on"])
    for row in rows:
        entry = ET.SubElement(feed, "entry")
        xml_text(ET.SubElement(entry, "title"), gs.detype(row["title"]))
        ET.SubElement(entry, "link", {"href": b + "/" + row["url_path"].rstrip("/") + "/",
                                      "rel": "alternate"})
        xml_text(ET.SubElement(entry, "id"), b + "/" + row["url_path"])
        xml_text(ET.SubElement(entry, "updated"), row["date"] + "T00:00:00Z")
        xml_text(ET.SubElement(entry, "published"), row["date"] + "T00:00:00Z")
        xml_text(ET.SubElement(entry, "summary"), gs.detype(row["lede"] or row["title"]))
        cat = ET.SubElement(entry, "category", {"term": row["kind"]})
        cat.set("label", kind_label(row["kind"]))
    # ElementTree dumps attributes in an arbitrary order on some Pythons.
    # Re-serialise through a deterministic walk so --check is byte-stable.
    return atom_bytes(feed)


def atom_bytes(feed: ET.Element) -> str:
    def esc(s):
        return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                .replace('"', "&quot;"))

    def attrs(el):
        # preferred order for known keys, then the rest sorted
        prefer = ["xmlns", "href", "rel", "type", "term", "label"]
        keys = list(el.attrib)
        ordered = [k for k in prefer if k in el.attrib] + sorted(k for k in keys if k not in prefer)
        return "".join(' %s="%s"' % (k, esc(el.attrib[k])) for k in ordered)

    lines = ['<?xml version="1.0" encoding="utf-8"?>']

    def walk(el, indent):
        pad = "  " * indent
        kids = list(el)
        if kids:
            lines.append("%s<%s%s>" % (pad, el.tag, attrs(el)))
            if el.text and el.text.strip():
                lines.append("%s  %s" % (pad, esc(el.text)))
            for child in kids:
                walk(child, indent + 1)
            lines.append("%s</%s>" % (pad, el.tag))
        else:
            text = el.text if el.text is not None else ""
            lines.append("%s<%s%s>%s</%s>" % (pad, el.tag, attrs(el), esc(text), el.tag))

    walk(feed, 0)
    return "\n".join(lines) + "\n"


def build_feed_json(gs, rows: list[dict], d) -> dict:
    b = gs.SITE_BASE.rstrip("/")
    c = d["counts"]
    daily = [r["date"] for r in rows if r["kind"] == "daily"]
    weekly = [r["date"] for r in rows if r["kind"] == "weekly"]
    items = []
    for row in rows:
        items.append({
            "id": b + "/" + row["url_path"],
            "url": b + "/" + row["url_path"],
            "title": gs.detype(row["title"]),
            "date_published": row["date"] + "T00:00:00Z",
            "date_modified": row["build_date"] + "T00:00:00Z",
            "summary": gs.detype(row["lede"] or row["title"]),
            "tags": [row["kind"]],
            "_gtm": {
                "kind": row["kind"],
                "date": row["date"],
                "build_date": row["build_date"],
                "source_file": row["source_file"],
                "source_rel": row["source_rel"],
                "page": "/" + row["url_path"],
                "markdown_url": b + "/" + row["url_path"] + "index.md",
                "measures": row["measures"],
            },
        })
    return {
        "version": "https://jsonfeed.org/version/1.1",
        "title": "The GTM MCP Directory updates",
        "home_page_url": b + "/updates/",
        "feed_url": b + "/updates/feed.json",
        "description": ("Daily and weekly what-changed reports. Each item is a file "
                        "from directory/digests/. A date with no file is omitted."),
        "authors": [{"name": "Andrew McGuire", "url": "https://andrewcmcguire.com"}],
        "language": "en",
        "_gtm": {
            "generated_on": d["generated_on"],
            "source_of_record_for_counts": "directory.json",
            "source_of_record_for_digests": "directory/digests/",
            "directory_counts": {
                "entries": c["entries"],
                "official_servers": c["mcp_status"]["official"],
                "community_servers": c["mcp_status"]["community"],
                "as_of": d["generated_on"],
            },
            "files_on_disk": {
                "daily": len(daily),
                "weekly": len(weekly),
                "latest_daily": daily[0] if daily else None,
                "latest_weekly": weekly[0] if weekly else None,
                "missing_daily_in_span": missing_in_span(daily),
                "missing_weekly_fridays_in_span": weekly_missing(weekly),
            },
        },
        "items": items,
    }


def emit_updates_feed(d, r, out: Path, digest_dir: Path | None = None):
    """Called from generate_site.main(). Returns html page count."""
    gs = load_gs()
    src = digest_dir or DIGEST_DIR
    rows = discover(src)
    dest = out / "updates"
    dest.mkdir(parents=True, exist_ok=True)
    gs.write(dest / "index.html", render_index(gs, rows, d, r))
    for row in rows:
        page_dir = dest / row["kind"] / row["date"]
        gs.write(page_dir / "index.html", render_digest_page(gs, row, rows, d, r))
    feed = build_feed_json(gs, rows, d)
    (dest / "feed.json").write_text(
        json.dumps(feed, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8", newline="\n")
    (out / "data").mkdir(parents=True, exist_ok=True)
    (out / "data" / "updates.json").write_text(
        json.dumps(feed, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8", newline="\n")
    gs.write(dest / "atom.xml", build_atom(gs, rows, d))
    return 1 + len(rows), rows


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=str(SITE_DIR))
    ap.add_argument("--digests", default=str(DIGEST_DIR))
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()
    src = Path(args.digests)
    rows = discover(src)
    print("digest files        %d" % len(rows))
    for row in rows:
        print("  %s  %s  %s" % (row["date"], row["kind"], row["source_file"]))
    daily = [r["date"] for r in rows if r["kind"] == "daily"]
    weekly = [r["date"] for r in rows if r["kind"] == "weekly"]
    d_miss = missing_in_span(daily)
    w_miss = weekly_missing(weekly)
    if d_miss:
        print("missing daily       %s" % ", ".join(d_miss))
    else:
        print("missing daily       none in span")
    if w_miss:
        print("missing weekly      %s" % ", ".join(w_miss))
    else:
        print("missing weekly      none in span")
    if args.list:
        return 0
    gs = load_gs()
    d, r = gs.load()
    gs.reconcile(d, r)
    n, _ = emit_updates_feed(d, r, Path(args.out).resolve(), src)
    print("html pages          %d" % n)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
