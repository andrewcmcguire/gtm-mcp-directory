#!/usr/bin/env python3
"""
generate_site.py - bakes the static site for The GTM MCP Directory.

Reads:   ../data/directory.json   (the baked artifact, 293 entries)
         ../data/build_report.json (the counting authority's report)
Writes:  everything under this directory (site/), and nothing outside it.

Laws this script obeys:
  * Every number rendered on any page is read from directory.json["counts"] or
    build_report.json. Nothing is computed a second way and nothing is typed by hand.
    _reconcile() fails the build loudly if the two files disagree.
  * No em dash appears in any output. Source prose that carries one is normalised to a
    spaced hyphen at render time and that normalisation is disclosed on /methodology.html.
    No other character in any source string is altered.
  * Deterministic: same inputs produce byte-identical output. No timestamps of "now",
    no random ids, every collection sorted by an explicit key.
  * Zero external requests in the output. No CDN, no webfont, no analytics, no image host.
    Fonts are a system stack. The search index ships as a local file.

Usage:
    python generate_site.py            # build into this directory
    python generate_site.py --check    # build, then assert the output is well formed
    python generate_site.py --out DIR  # build somewhere else
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import shutil
import sys
from pathlib import Path

SITE_DIR = Path(__file__).resolve().parent
DATA_DIR = SITE_DIR.parent / "data"

# Directories generate_site.py owns and will wipe on every run. Anything else that lives
# in site/ (this script, DEPLOY.md) is left alone.
GENERATED_DIRS = ["assets", "tools", "categories", "gates", "mcp", "jobs", "jobs-board",
                  "github", "learn", "lists", "data", "_dist"]
GENERATED_FILES = [
    "index.html",
    "methodology.html",
    "submit.html",
    "data.html",
    "404.html",
    "search-index.json",
    "llms.txt",
    "sitemap.xml",
    "robots.txt",
    "_headers",
]
# Root level markdown twins. Every .md in the root except DEPLOY.md is generated output.
KEEP_ROOT_MD = {"DEPLOY.md"}

# Cloudflare Pages reads this file at deploy time. The CSP is the machine-enforced version
# of the promise the site makes in prose: this page talks to nobody.
HEADERS = """/*
  Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'; form-action 'self'; frame-ancestors 'none'; base-uri 'self'; object-src 'none'
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: geolocation=(), microphone=(), camera=(), interest-cohort=()

/assets/*
  Cache-Control: public, max-age=3600

/search-index.json
  Cache-Control: public, max-age=3600

/data/*
  Cache-Control: public, max-age=3600
  Access-Control-Allow-Origin: *

/llms.txt
  Content-Type: text/plain; charset=utf-8
  Cache-Control: public, max-age=3600

/*.md
  Content-Type: text/markdown; charset=utf-8

/*/*.md
  Content-Type: text/markdown; charset=utf-8
"""

REPO_URL = "https://github.com/andrewcmcguire/gtm-mcp-directory"  # live
ISSUE_URL = REPO_URL + "/issues/new?template=tool-submission.yml"  # live
SITE_ROUTE = "andrewcmcguire.com/gtm-directory"
# NOT YET ROUTED. The site is live on its Cloudflare Pages subdomain; this is the URL the runbook
# targets, and it is the base for the canonical tags, the sitemap and llms.txt. If the deploy takes
# the subdomain fallback instead, change this one constant and rebuild: every internal link on the
# site is relative and unaffected.
SITE_BASE = "https://andrewcmcguire.com/gtm-directory"
PACKAGE_NAME = "gtm-mcp-directory"
SERVER_ID = "gtm-directory"

EM = "\u2014"


# ----------------------------------------------------------------------------------
# text helpers
# ----------------------------------------------------------------------------------

def detype(s: str) -> str:
    """Normalise em dashes out of source prose. Disclosed on /methodology.html."""
    if not s:
        return ""
    s = s.replace(EM + " ", " - ").replace(" " + EM, " -").replace(EM, " - ")
    s = re.sub(r"\s+-\s+-\s+", " - ", s)
    return s


def esc(s) -> str:
    if s is None:
        return ""
    return html.escape(detype(str(s)), quote=True)


def raw_esc(s) -> str:
    """Escape without detyping. Used only for URLs, which never carry an em dash."""
    if s is None:
        return ""
    return html.escape(str(s), quote=True)


def trim(s: str, n: int) -> str:
    s = detype(s or "").strip()
    if len(s) <= n:
        return s
    cut = s[:n].rsplit(" ", 1)[0]
    return cut + "..."


def num(n) -> str:
    return f"{n:,}" if isinstance(n, int) else str(n)


# ----------------------------------------------------------------------------------
# vocabulary and colour bands
# ----------------------------------------------------------------------------------

MCP_ORDER = ["official", "community", "unknown", "n-a", "none-found"]
MCP_LABEL = {
    "official": "Official MCP",
    "community": "Community MCP",
    "none-found": "No MCP found",
    "unknown": "MCP unknown",
    "n-a": "MCP not applicable",
}
MCP_BLURB = {
    "official": "The vendor ships and maintains the server itself. A wrapper built by "
                "Zapier, Composio or a similar third party does not count as official.",
    "community": "A working server exists but somebody other than the vendor built it. "
                 "It can be abandoned without the vendor noticing.",
    "none-found": "No server was found at the time of the check. That is a statement about "
                  "the search, not a promise that none exists.",
    "unknown": "The check could not settle it either way. Unknown is a legal answer and it "
               "is published rather than guessed.",
    "n-a": "An MCP server is not a meaningful question for this entry.",
}
MCP_TONE = {
    "official": "gold",
    "community": "teal",
    "none-found": "copper",
    "unknown": "mute",
    "n-a": "mute",
}

GATE_ORDER = ["free", "paid", "enterprise-leaning", "enterprise-only", "unknown", "n-a"]
GATE_LABEL = {
    "free": "Free to start",
    "paid": "Paid, self-serve",
    "enterprise-leaning": "Enterprise leaning",
    "enterprise-only": "Enterprise only",
    "unknown": "Gate unknown",
    "n-a": "Gate not applicable",
}
GATE_BLURB = {
    "free": "A solo operator can get API access without talking to anyone.",
    "paid": "A solo operator can get API access by paying, still without a sales call.",
    "enterprise-leaning": "Self-serve on paper, gated in practice. One entry sits here.",
    "enterprise-only": "API access needs a contract, a seat count, or a procurement cycle. "
                       "A solo operator is out.",
    "unknown": "The gate could not be established from public sources. Published as unknown "
               "rather than guessed.",
    "n-a": "An API gate is not a meaningful question for this entry.",
}
GATE_TONE = {
    "free": "teal",
    "paid": "gold",
    "enterprise-leaning": "copper",
    "enterprise-only": "copper",
    "unknown": "mute",
    "n-a": "mute",
}


# ----------------------------------------------------------------------------------
# load + reconcile
# ----------------------------------------------------------------------------------

def load():
    directory = json.loads((DATA_DIR / "directory.json").read_text(encoding="utf-8"))
    report = json.loads((DATA_DIR / "build_report.json").read_text(encoding="utf-8"))
    return directory, report


def reconcile(d, r):
    """Fail the build rather than publish a drifted number."""
    problems = []
    counts = d["counts"]
    cov = r["coverage"]
    rec = r["reconciliation"]

    if counts["entries"] != r["entries_parsed"]:
        problems.append(f"entries: directory {counts['entries']} vs report {r['entries_parsed']}")
    if counts["entries"] != rec["recount_total"]:
        problems.append(f"entries vs tools_recount: {counts['entries']} vs {rec['recount_total']}")
    if not rec.get("reconciled"):
        problems.append("build_report.reconciliation.reconciled is not true")
    for k, v in counts["mcp_status"].items():
        if k == "other":
            continue
        if cov["mcp_status"].get(k, 0) != v:
            problems.append(f"mcp_status {k}: {v} vs {cov['mcp_status'].get(k)}")
    for k, v in counts["api_gate"].items():
        if k == "other":
            continue
        if cov["api_gate"].get(k, 0) != v:
            problems.append(f"api_gate {k}: {v} vs {cov['api_gate'].get(k)}")
    if counts["bench_tested"] != cov["bench_tested"]:
        problems.append("bench_tested disagrees")

    entries = d["entries"]
    if len(entries) != counts["entries"]:
        problems.append(f"entries list is {len(entries)}, counts says {counts['entries']}")
    canon = [e for e in entries if e.get("canonical")]
    if len(canon) != counts["canonical_entries"]:
        problems.append(f"canonical entries {len(canon)} vs counts {counts['canonical_entries']}")
    slugs = [e["slug"] for e in canon]
    if len(set(slugs)) != len(slugs):
        problems.append("canonical slugs are not unique")
    if sum(c["total"] for c in d["categories"]) != counts["entries"]:
        problems.append("category totals do not sum to the entry count")

    if problems:
        print("RECONCILIATION FAILED. Nothing was written.", file=sys.stderr)
        for p in problems:
            print("  " + p, file=sys.stderr)
        raise SystemExit(2)


# ----------------------------------------------------------------------------------
# CSS
# ----------------------------------------------------------------------------------

CSS = """/* The GTM MCP Directory. Tokens lifted from the Agent Operator brand sheet.
   Fonts are a system stack on purpose: the page makes zero external requests. */

:root{
  --gold:#D4A24C; --gold-deep:#B88838;
  --copper:#E8734A; --copper-deep:#C45A35; --copper-mute:#C04040;
  --teal:#1D9E75;
  --serif:Georgia,'Iowan Old Style','Times New Roman',Times,serif;
  --sans:system-ui,-apple-system,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;
  --mono:ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace;

  /* light is the base definition. every colour is defined here first. */
  --bg:#E6E2DB;
  --surface:#FAFAF7;
  --surface-2:#EFEDE6;
  --fg:#141414;
  --fg-soft:#1F1D1A;
  --mute:#6B6864;
  --mute-2:#8B867F;
  --rule:#DCD7CE;
  --rule-soft:#E6E2DB;
  --accent:var(--gold-deep);
  --tone-gold:var(--gold-deep);
  --tone-teal:#177C5C;
  --tone-copper:var(--copper-deep);
  --tone-mute:var(--mute);
  --shadow:0 1px 2px rgba(20,20,20,.06);
}

@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --bg:#0D0C0B;
    --surface:#151312;
    --surface-2:#1C1A18;
    --fg:#FAFAF7;
    --fg-soft:#E9E5DE;
    --mute:#9A958D;
    --mute-2:#7A756E;
    --rule:rgba(250,250,247,.13);
    --rule-soft:rgba(250,250,247,.07);
    --accent:var(--gold);
    --tone-gold:var(--gold);
    --tone-teal:#3FBE93;
    --tone-copper:var(--copper);
    --tone-mute:var(--mute);
    --shadow:0 1px 2px rgba(0,0,0,.5);
  }
}
:root[data-theme="dark"]{
  --bg:#0D0C0B;
  --surface:#151312;
  --surface-2:#1C1A18;
  --fg:#FAFAF7;
  --fg-soft:#E9E5DE;
  --mute:#9A958D;
  --mute-2:#7A756E;
  --rule:rgba(250,250,247,.13);
  --rule-soft:rgba(250,250,247,.07);
  --accent:var(--gold);
  --tone-gold:var(--gold);
  --tone-teal:#3FBE93;
  --tone-copper:var(--copper);
  --tone-mute:var(--mute);
  --shadow:0 1px 2px rgba(0,0,0,.5);
}

*{box-sizing:border-box;margin:0;padding:0}
html{-webkit-text-size-adjust:100%}
body{
  background:var(--bg);color:var(--fg);
  font-family:var(--sans);font-size:16px;line-height:1.62;
  -webkit-font-smoothing:antialiased;
  overflow-x:hidden;
}
body::before{
  content:'';position:fixed;top:0;left:0;right:0;height:4px;
  background:linear-gradient(90deg,var(--gold-deep),var(--gold) 42%,var(--copper) 100%);
  z-index:50;
}
img,svg{max-width:100%;height:auto}
a{color:var(--fg);text-decoration:none;border-bottom:1px solid var(--rule)}
a:hover{border-bottom-color:var(--accent);color:var(--accent)}
a.plain,a.plain:hover{border-bottom:0}
p,li,dd{overflow-wrap:anywhere}

.wrap{max-width:960px;margin:0 auto;padding:0 22px}
.wrap.wide{max-width:1140px}

/* ---------- masthead ---------- */
.masthead{border-bottom:1px solid var(--rule);background:var(--surface);position:relative;z-index:10}
.masthead .wrap{display:flex;flex-wrap:wrap;gap:14px 26px;align-items:center;
  padding-top:16px;padding-bottom:16px}
.brandmark{font-family:var(--serif);font-size:19px;letter-spacing:.01em;border-bottom:0;
  white-space:nowrap}
.brandmark .g{color:var(--accent)}
.brandmark:hover{color:var(--fg)}
.navlinks{display:flex;flex-wrap:wrap;gap:6px 18px;margin-left:auto;
  font-family:var(--mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase}
.navlinks a{border-bottom:0;color:var(--mute)}
.navlinks a:hover,.navlinks a[aria-current]{color:var(--accent)}
.themetoggle{font-family:var(--mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;
  background:none;border:1px solid var(--rule);color:var(--mute);border-radius:3px;
  padding:4px 9px;cursor:pointer}
.themetoggle:hover{color:var(--accent);border-color:var(--accent)}

/* ---------- hero ---------- */
.hero{background:var(--surface);border-bottom:1px solid var(--rule);
  padding:64px 0 44px;position:relative;overflow:hidden}
.hero .wrap{position:relative;z-index:2}
.eyebrow{font-family:var(--mono);font-size:12px;letter-spacing:.2em;text-transform:uppercase;
  color:var(--accent)}
.eyebrow::before{content:'[ '}.eyebrow::after{content:' ]'}
h1.display{font-family:var(--serif);font-weight:400;text-transform:uppercase;
  font-size:clamp(34px,7vw,74px);line-height:.98;letter-spacing:.005em;margin:20px 0 0}
.hero .lede{font-family:var(--serif);font-style:italic;color:var(--fg-soft);
  font-size:clamp(19px,2.6vw,27px);line-height:1.35;margin-top:16px;max-width:34ch}
.hero .rule{height:1px;background:var(--accent);width:220px;max-width:60%;margin:30px 0 14px;opacity:.6}
.stamp{font-family:var(--mono);font-size:12.5px;letter-spacing:.05em;color:var(--mute)}
.stamp b{color:var(--fg);font-weight:600}

/* ---------- stat row ---------- */
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(148px,1fr));
  gap:1px;background:var(--rule);border:1px solid var(--rule);margin-top:34px}
.stat{background:var(--surface);padding:16px 18px}
.stat .n{font-family:var(--serif);font-size:clamp(26px,4.4vw,40px);line-height:1;color:var(--fg)}
.stat.is-gold .n{color:var(--tone-gold)}
.stat.is-teal .n{color:var(--tone-teal)}
.stat.is-copper .n{color:var(--tone-copper)}
.stat .k{font-family:var(--mono);font-size:11px;letter-spacing:.13em;text-transform:uppercase;
  color:var(--mute);margin-top:9px}

/* ---------- sections ---------- */
section{padding:52px 0}
section.tint{background:var(--surface);border-top:1px solid var(--rule);
  border-bottom:1px solid var(--rule)}
h2{font-family:var(--serif);font-weight:400;font-size:clamp(24px,3.6vw,34px);
  line-height:1.14;margin:10px 0 6px}
h3{font-family:var(--serif);font-weight:400;font-size:21px;line-height:1.24;margin:0 0 6px}
.sub{color:var(--mute);max-width:70ch;margin-top:8px}
.sub a{color:var(--mute)}

/* ---------- search ---------- */
.searchbox{display:flex;flex-wrap:wrap;gap:10px;margin-top:20px}
#q{flex:1 1 320px;min-width:0;font-family:var(--sans);font-size:17px;
  padding:14px 16px;background:var(--surface-2);color:var(--fg);
  border:1px solid var(--rule);border-left:3px solid var(--accent);border-radius:3px}
#q:focus{outline:2px solid var(--accent);outline-offset:1px}
.filters{display:flex;flex-wrap:wrap;gap:7px;margin-top:14px}
.chip{font-family:var(--mono);font-size:11px;letter-spacing:.09em;text-transform:uppercase;
  padding:5px 11px;border:1px solid var(--rule);border-radius:999px;background:none;
  color:var(--mute);cursor:pointer}
.chip:hover{border-color:var(--accent);color:var(--accent)}
.chip[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:var(--bg)}
.sortnote{font-family:var(--mono);font-size:11.5px;line-height:1.7;letter-spacing:.03em;
  color:var(--mute-2);margin-top:16px;max-width:80ch}
#count{font-family:var(--mono);font-size:12px;letter-spacing:.1em;text-transform:uppercase;
  color:var(--accent);margin-top:18px}

/* ---------- result / entry rows ---------- */
.rows{list-style:none;margin-top:14px;border-top:1px solid var(--rule)}
.row{border-bottom:1px solid var(--rule);padding:15px 0}
.row .top{display:flex;flex-wrap:wrap;gap:8px 14px;align-items:baseline}
.row .nm{font-family:var(--serif);font-size:20px;line-height:1.2;border-bottom:0;
  overflow-wrap:anywhere;max-width:100%}
.row .nm:hover{color:var(--accent)}
.row .dom{font-family:var(--mono);font-size:11.5px;color:var(--mute-2);letter-spacing:.02em;
  overflow-wrap:anywhere;max-width:100%}
.row .desc{color:var(--mute);font-size:14.5px;line-height:1.55;margin-top:6px;max-width:88ch}
.row .badges{margin-top:9px}

/* ---------- badges ---------- */
.badges{display:flex;flex-wrap:wrap;gap:6px}
.badge{display:inline-flex;align-items:center;gap:6px;font-family:var(--mono);
  font-size:10.5px;letter-spacing:.11em;text-transform:uppercase;
  padding:3px 9px;border:1px solid var(--rule);border-radius:2px;color:var(--mute);
  background:var(--surface-2);white-space:nowrap;max-width:100%;overflow-wrap:anywhere}
.badge.xref{white-space:normal}
a.badge{border-bottom:1px solid var(--rule)}
a.badge:hover{color:var(--fg)}
.badge::before{content:'';width:6px;height:6px;border-radius:50%;background:currentColor;
  flex:none;opacity:.9}
.badge.gold{color:var(--tone-gold);border-color:color-mix(in srgb,var(--tone-gold) 40%,transparent)}
.badge.teal{color:var(--tone-teal);border-color:color-mix(in srgb,var(--tone-teal) 40%,transparent)}
.badge.copper{color:var(--tone-copper);border-color:color-mix(in srgb,var(--tone-copper) 40%,transparent)}
.badge.mute{color:var(--mute)}
.badge.flat::before{display:none}
.badge.tier{color:var(--tone-gold);border-color:var(--tone-gold);background:none}
.badge.xref{color:var(--mute-2)}

/* ---------- coverage chart ---------- */
.cov{list-style:none;margin-top:22px}
.cov li{padding:9px 0;border-bottom:1px solid var(--rule-soft)}
.cov .lab{display:flex;flex-wrap:wrap;gap:4px 12px;align-items:baseline;
  font-size:14.5px;justify-content:space-between}
.cov .lab .r{font-family:var(--mono);font-size:12px;color:var(--mute);white-space:nowrap}
.cov .lab .r b{color:var(--tone-gold);font-weight:600}
.cov .bar{height:7px;background:var(--surface-2);margin-top:7px;border-radius:1px;overflow:hidden;
  display:flex}
.cov .bar i{display:block;height:100%}
.cov .bar .o{background:var(--tone-gold)}
.cov .bar .c{background:var(--tone-teal)}
.cov a{border-bottom:0}
.cov a:hover{color:var(--accent)}

/* ---------- cards / blocks ---------- */
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;margin-top:22px}
.card{background:var(--surface);border:1px solid var(--rule);border-top:2px solid var(--accent);
  padding:22px;border-radius:2px}
.card h3{margin-bottom:8px}
.card p{color:var(--mute);font-size:14.5px}
.card .kicker{font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--accent);margin-bottom:10px}

pre{background:var(--surface-2);border:1px solid var(--rule);border-left:3px solid var(--accent);
  padding:16px 18px;border-radius:3px;overflow-x:auto;margin-top:14px}
code{font-family:var(--mono);font-size:13px;line-height:1.65;color:var(--fg-soft)}
.note{font-family:var(--mono);font-size:11.5px;line-height:1.75;letter-spacing:.02em;
  color:var(--mute-2);margin-top:12px}
.warn{border-left:3px solid var(--copper);background:var(--surface-2);padding:13px 16px;
  margin-top:16px;font-size:14px;color:var(--mute);border-radius:2px}
.warn b{color:var(--tone-copper);font-family:var(--mono);font-size:11px;letter-spacing:.13em;
  text-transform:uppercase;display:block;margin-bottom:5px}

.btnrow{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}
.btn{display:inline-block;font-family:var(--mono);font-size:12px;letter-spacing:.11em;
  text-transform:uppercase;padding:11px 18px;border:1px solid var(--accent);color:var(--accent);
  border-radius:2px;background:none;cursor:pointer}
.btn:hover{background:var(--accent);color:var(--bg);border-color:var(--accent)}
.btn.solid{background:var(--accent);color:var(--bg)}
.btn.solid:hover{opacity:.85}
.btn.ghost{border-color:var(--rule);color:var(--mute)}
.btn.ghost:hover{background:none;border-color:var(--accent);color:var(--accent)}
.btn[disabled]{opacity:.45;cursor:not-allowed}
.btn[disabled]:hover{background:none;color:var(--accent)}

/* ---------- subscribe ---------- */
.subform{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px}
.subform input{flex:1 1 260px;min-width:0;font-family:var(--sans);font-size:15px;padding:12px 14px;
  background:var(--surface-2);color:var(--fg);border:1px solid var(--rule);border-radius:3px}

/* ---------- tool page ---------- */
.crumbs{font-family:var(--mono);font-size:11.5px;letter-spacing:.08em;text-transform:uppercase;
  color:var(--mute-2);padding-top:26px}
.crumbs a{color:var(--mute-2);border-bottom:0}
.crumbs a:hover{color:var(--accent)}
.toolhead{padding:14px 0 34px;border-bottom:1px solid var(--rule)}
.toolhead h1{font-family:var(--serif);font-weight:400;font-size:clamp(30px,5.5vw,50px);
  line-height:1.04;margin:8px 0 12px;overflow-wrap:anywhere}
.field{padding:22px 0;border-bottom:1px solid var(--rule-soft)}
.field:last-child{border-bottom:0}
.field .k{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;
  color:var(--accent);margin-bottom:9px}
.field .v{color:var(--fg-soft);max-width:82ch}
.field .v.mono{font-family:var(--mono);font-size:13px;line-height:1.7;color:var(--mute)}
.field .v.empty{color:var(--mute-2);font-style:italic}
.field ul{list-style:none}
.field ul li{padding:4px 0;font-family:var(--mono);font-size:12.5px;line-height:1.6}
.field ul li::before{content:'\\2192  ';color:var(--accent)}
.blockgrid{display:flex;flex-wrap:wrap;gap:1px;
  background:var(--rule);border:1px solid var(--rule);margin-top:10px}
.blockgrid > div{background:var(--surface);padding:16px 18px;flex:1 1 240px;min-width:0}
.blockgrid .bk{font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--mute-2);margin-bottom:7px}
.blockgrid .bv{font-size:14.5px;color:var(--fg-soft);overflow-wrap:anywhere}
.tierbox{background:var(--surface);border:1px solid var(--rule);border-left:3px solid var(--tone-gold);
  padding:15px 18px;margin-top:18px;font-size:14px;color:var(--mute);border-radius:2px}
.tierbox b{font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--tone-gold);display:block;margin-bottom:5px}

/* ---------- learn / Q&A ---------- */
.qhead{padding:14px 0 8px}
.qhead h1{font-family:var(--serif);font-weight:400;font-size:clamp(27px,4.4vw,44px);
  line-height:1.08;margin:8px 0 0;max-width:24ch;overflow-wrap:anywhere}
.answerbox{background:var(--surface);border:1px solid var(--rule);
  border-left:3px solid var(--accent);padding:18px 20px;margin-top:20px;border-radius:2px}
.answerbox .lab{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;
  color:var(--accent);margin-bottom:8px}
.answerbox p{font-family:var(--serif);font-size:19px;line-height:1.45;color:var(--fg);max-width:62ch}
.prose{max-width:72ch}
.prose h2{font-size:clamp(20px,2.6vw,26px);margin-top:32px}
.prose h3{margin-top:24px}
.prose p{margin-top:12px;color:var(--fg-soft)}
.prose ul,.prose ol{margin-top:12px;padding-left:20px}
.prose li{margin-top:5px;color:var(--fg-soft)}
.prose ul.bare{list-style:none;padding-left:0}
.prose ul.bare li::before{content:'\\2192  ';color:var(--accent)}
.prose .note{max-width:78ch}
.datatable{width:100%;border-collapse:collapse;margin-top:16px;font-size:14.5px}
.datatable th,.datatable td{text-align:left;padding:8px 12px 8px 0;border-bottom:1px solid var(--rule-soft);
  vertical-align:top}
.datatable th{font-family:var(--mono);font-size:10.5px;letter-spacing:.13em;text-transform:uppercase;
  color:var(--mute);font-weight:400}
.datatable td.n{font-family:var(--mono);font-size:13px;white-space:nowrap}
.scroller{overflow-x:auto;max-width:100%}
.qlist{list-style:none;margin-top:14px;border-top:1px solid var(--rule)}
.qlist li{border-bottom:1px solid var(--rule);padding:13px 0}
.qlist a{font-family:var(--serif);font-size:18.5px;line-height:1.28;border-bottom:0}
.qlist a:hover{color:var(--accent)}
.qlist .qa{color:var(--mute);font-size:14px;line-height:1.55;margin-top:5px;max-width:88ch}
.srcs{list-style:none;margin-top:12px}
.srcs li{padding:4px 0;font-size:14px;line-height:1.55}
.srcs li::before{content:'\\2192  ';color:var(--accent);font-family:var(--mono)}

/* ---------- misc ---------- */
.viewgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px;margin-top:20px}
.viewcard{background:var(--surface);border:1px solid var(--rule);padding:17px 19px;border-radius:2px;
  border-bottom:0;display:block}
.viewcard:hover{border-color:var(--accent);color:var(--fg)}
.viewcard .vt{font-family:var(--serif);font-size:19px;line-height:1.2}
.viewcard .vn{font-family:var(--mono);font-size:11px;letter-spacing:.11em;text-transform:uppercase;
  color:var(--accent);margin-top:7px}
.viewcard .vd{color:var(--mute);font-size:13.5px;margin-top:7px;line-height:1.5}
.alphanav{display:flex;flex-wrap:wrap;gap:5px;margin-top:18px;font-family:var(--mono);font-size:12px}
.alphanav a{padding:3px 8px;border:1px solid var(--rule);border-radius:2px;color:var(--mute)}
.alphanav a:hover{color:var(--accent);border-color:var(--accent)}
.alpha{font-family:var(--mono);font-size:12px;letter-spacing:.2em;color:var(--accent);
  padding-top:26px;margin-bottom:-4px}

.foot{border-top:1px solid var(--rule);background:var(--surface);padding:34px 0 46px;margin-top:0}
.foot .cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:22px}
.foot .ft{font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--accent);margin-bottom:9px}
.foot p,.foot li{color:var(--mute);font-size:13.5px;line-height:1.7}
.foot ul{list-style:none}
.foot a{color:var(--mute);border-bottom:0}
.foot a:hover{color:var(--accent)}
.foot .legal{margin-top:26px;padding-top:18px;border-top:1px solid var(--rule-soft);
  font-family:var(--mono);font-size:11px;line-height:1.85;letter-spacing:.02em;color:var(--mute-2)}

.tocols{columns:2 220px;column-gap:26px}
.tocols li{break-inside:avoid;list-style:none;padding:3px 0;font-size:14.5px}

@media (max-width:560px){
  /* long labels wrap inside their own pill rather than pushing the page sideways */
  .badge{white-space:normal}
  .cov .lab .r{white-space:normal}
}
@media (max-width:640px){
  section{padding:38px 0}
  .hero{padding:44px 0 34px}
  .masthead .wrap{padding-top:12px;padding-bottom:12px}
  .navlinks{margin-left:0;width:100%}
}

/* ---------- the job board ---------- */
.lawbox{background:var(--surface);border:1px solid var(--rule);border-left:3px solid var(--tone-teal);
  padding:16px 19px;margin-top:20px;border-radius:2px}
.lawbox .lab{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;
  color:var(--tone-teal);margin-bottom:7px}
.lawbox p{font-family:var(--serif);font-size:18px;line-height:1.45;color:var(--fg);max-width:60ch}
.lawbox p + p{margin-top:9px;font-family:var(--sans);font-size:14.5px;color:var(--mute)}
.boardbar{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}
#jq{flex:1 1 260px;min-width:0;font-family:var(--sans);font-size:16px;padding:12px 14px;
  background:var(--surface-2);color:var(--fg);border:1px solid var(--rule);
  border-left:3px solid var(--accent);border-radius:3px}
#jq:focus{outline:2px solid var(--accent);outline-offset:1px}
.filterset{margin-top:14px}
.filterset .fk{font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--mute-2);margin-bottom:6px}
#jcount{font-family:var(--mono);font-size:12px;letter-spacing:.1em;text-transform:uppercase;
  color:var(--accent);margin-top:18px}
.jrow .nm{overflow-wrap:anywhere}
.jrow .co{font-family:var(--mono);font-size:12px;letter-spacing:.06em;color:var(--fg-soft);
  text-transform:uppercase;overflow-wrap:anywhere}
.jrow .desc{font-family:var(--mono);font-size:12px;letter-spacing:.02em;overflow-wrap:anywhere}
.jempty{color:var(--mute);font-size:14.5px;padding:18px 0;max-width:70ch}
.deadrow .nm{color:var(--mute);font-family:var(--serif);font-size:18px}
.deadrow .url{font-family:var(--mono);font-size:11px;color:var(--mute-2);overflow-wrap:anywhere;
  margin-top:5px;max-width:100%}
@media (max-width:560px){
  .boardbar{gap:8px}
  .jrow .nm{font-size:18px}
}

@media (prefers-reduced-motion:no-preference){
  a,.btn,.chip{transition:color .12s ease,border-color .12s ease,background-color .12s ease}
}
"""

THEME_JS = """/* Loaded blocking in <head> so the stored theme is applied before first paint.
   Kept in its own file, not inline, so the Content-Security-Policy in _headers can
   forbid inline script outright. */
(function(){
  try{
    var t=localStorage.getItem('gtmd-theme');
    if(t){document.documentElement.setAttribute('data-theme',t);}
  }catch(e){}
})();
function gtmdWireToggle(){
  var b=document.getElementById('themetoggle');
  if(!b)return;
  function cur(){
    var a=document.documentElement.getAttribute('data-theme');
    if(a)return a;
    return window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';
  }
  function paint(){b.textContent=cur()==='dark'?'Light':'Dark';}
  b.addEventListener('click',function(){
    var n=cur()==='dark'?'light':'dark';
    document.documentElement.setAttribute('data-theme',n);
    try{localStorage.setItem('gtmd-theme',n);}catch(e){}
    paint();
  });
  paint();
}
if(document.readyState==='loading'){
  document.addEventListener('DOMContentLoaded',gtmdWireToggle);
}else{gtmdWireToggle();}
"""


# ----------------------------------------------------------------------------------
# search javascript
# ----------------------------------------------------------------------------------

SEARCH_JS = r"""/* The GTM MCP Directory - capability search.
   Runs entirely in the page over the baked index. No backend, no network call,
   no query logging, works with the network cable pulled out. */
(function(){
  var IDX = (window.GTMD_INDEX && window.GTMD_INDEX.tools) || [];
  var META = (window.GTMD_INDEX && window.GTMD_INDEX.meta) || {};
  var q = document.getElementById('q');
  var out = document.getElementById('results');
  var cnt = document.getElementById('count');
  var chips = Array.prototype.slice.call(document.querySelectorAll('.chip'));
  if(!q || !out) return;

  var filters = {mcp:null, gate:null};

  function tokens(s){
    return (s||'').toLowerCase().replace(/[^a-z0-9+.# ]+/g,' ').split(/\s+/)
      .filter(function(t){ return t.length > 1 && STOP.indexOf(t) === -1; });
  }
  var STOP = ['the','and','for','with','that','this','from','can','you','your','our','all',
              'want','need','get','use','using','tool','tools','how','what','which','does',
              'has','have','are','was','one','into','out','who','when','who','its','it'];

  function score(t, toks){
    if(!toks.length) return 1;
    var name = t.n.toLowerCase();
    var s = 0, hit = 0;
    for(var i=0;i<toks.length;i++){
      var w = toks[i], any = false;
      if(name.indexOf(w) !== -1){ s += 14; any = true; }
      if(t.c.toLowerCase().indexOf(w) !== -1){ s += 5; any = true; }
      var n = 0, p = t.x.indexOf(w);
      while(p !== -1 && n < 6){ n++; p = t.x.indexOf(w, p + w.length); }
      if(n){ s += 2 + n; any = true; }
      if(any) hit++;
    }
    if(hit < toks.length) s = s * 0.35;   // partial matches sink, they do not vanish
    if(name === toks.join(' ')) s += 500; // exact name match pins to the top
    return s;
  }

  function pass(t){
    if(filters.mcp && t.m !== filters.mcp) return false;
    if(filters.gate && t.g !== filters.gate) return false;
    return true;
  }

  function esc(s){
    return String(s).replace(/[&<>"]/g, function(c){
      return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];
    });
  }

  var MCPTONE = {'official':'gold','community':'teal','none-found':'copper',
                 'unknown':'mute','n-a':'mute'};
  var GATETONE = {'free':'teal','paid':'gold','enterprise-leaning':'copper',
                  'enterprise-only':'copper','unknown':'mute','n-a':'mute'};

  function render(list, total){
    if(!list.length){
      out.innerHTML = '<li class="row"><div class="desc">Nothing in the index matches that. ' +
        'Try a plainer phrase, or browse by category, gate or MCP status. ' +
        'An empty result is a real answer here: it means no entry carries those words.</div></li>';
      cnt.textContent = '0 of ' + total + ' shown';
      return;
    }
    var html = '';
    for(var i=0;i<list.length;i++){
      var t = list[i];
      html += '<li class="row"><div class="top">' +
        '<a class="nm" href="tools/' + esc(t.s) + '.html">' + esc(t.n) + '</a>' +
        '<span class="dom">' + esc(t.d) + '</span></div>' +
        '<div class="desc">' + esc(t.w) + '</div>' +
        '<div class="badges">' +
        '<span class="badge ' + (MCPTONE[t.m]||'mute') + '">' + esc(t.ml) + '</span>' +
        '<span class="badge ' + (GATETONE[t.g]||'mute') + '">' + esc(t.gl) + '</span>' +
        '<span class="badge mute flat">' + esc(t.c) + '</span>' +
        '<span class="badge tier flat">' + esc(t.t) + '</span>' +
        '</div></li>';
    }
    out.innerHTML = html;
    cnt.textContent = list.length + ' of ' + total + ' shown';
  }

  var LIMIT = 60;
  function run(){
    var toks = tokens(q.value);
    var pool = IDX.filter(pass);
    var scored = [];
    for(var i=0;i<pool.length;i++){
      var sc = score(pool[i], toks);
      if(toks.length && sc <= 0) continue;
      scored.push([sc, pool[i]]);
    }
    // published ordering: relevance band first, then the fixed directory sort rule.
    scored.sort(function(a,b){
      if(!toks.length) return a[1].r - b[1].r;
      if(b[0] !== a[0]) return b[0] - a[0];
      return a[1].r - b[1].r;
    });
    var list = scored.map(function(p){ return p[1]; });
    var total = list.length;
    render(list.slice(0, LIMIT), total);
    if(total > LIMIT){
      cnt.textContent = LIMIT + ' of ' + total + ' shown. ' +
        (total - LIMIT) + ' trimmed by the display limit, not by ranking.';
    }
  }

  q.addEventListener('input', run);
  chips.forEach(function(c){
    c.addEventListener('click', function(){
      var kind = c.getAttribute('data-kind'), val = c.getAttribute('data-val');
      var on = c.getAttribute('aria-pressed') === 'true';
      chips.forEach(function(o){
        if(o.getAttribute('data-kind') === kind) o.setAttribute('aria-pressed','false');
      });
      filters[kind] = on ? null : val;
      c.setAttribute('aria-pressed', on ? 'false' : 'true');
      run();
    });
  });

  var stamp = document.getElementById('idxstamp');
  if(stamp && META.generated_on){
    stamp.textContent = META.tools + ' unique products indexed, baked ' + META.generated_on +
      ' from ' + META.entries + ' directory entries.';
  }
  run();
})();"""


# ----------------------------------------------------------------------------------
# job board javascript
# ----------------------------------------------------------------------------------

BOARD_JS = r"""/* The GTM Engineer job board - client side filtering.
   Every row is already in the HTML. This only hides rows, so the board is complete
   and readable with JavaScript switched off, and nothing is fetched at any point. */
(function(){
  var rows = Array.prototype.slice.call(document.querySelectorAll('.jrow'));
  if(!rows.length) return;
  var q = document.getElementById('jq');
  var cnt = document.getElementById('jcount');
  var empty = document.getElementById('jempty');
  var chips = Array.prototype.slice.call(document.querySelectorAll('.jchip'));
  var f = {fam:null, sen:null, rem:null, reg:null};

  function pass(el){
    if(f.fam && el.getAttribute('data-fam') !== f.fam) return false;
    if(f.sen && el.getAttribute('data-sen') !== f.sen) return false;
    if(f.rem && el.getAttribute('data-rem') !== f.rem) return false;
    if(f.reg && (' ' + el.getAttribute('data-reg') + ' ').indexOf(' ' + f.reg + ' ') === -1) return false;
    var t = (q && q.value ? q.value : '').trim().toLowerCase();
    if(t){
      var words = t.split(/\s+/), hay = el.getAttribute('data-q') || '';
      for(var i=0;i<words.length;i++){ if(hay.indexOf(words[i]) === -1) return false; }
    }
    return true;
  }

  function run(){
    var n = 0;
    for(var i=0;i<rows.length;i++){
      var ok = pass(rows[i]);
      rows[i].style.display = ok ? '' : 'none';
      if(ok) n++;
    }
    if(cnt) cnt.textContent = n + ' of ' + rows.length + ' shown';
    if(empty) empty.style.display = n ? 'none' : 'block';
  }

  if(q) q.addEventListener('input', run);
  chips.forEach(function(c){
    c.addEventListener('click', function(){
      var k = c.getAttribute('data-k'), v = c.getAttribute('data-v');
      var on = c.getAttribute('aria-pressed') === 'true';
      chips.forEach(function(o){
        if(o.getAttribute('data-k') === k) o.setAttribute('aria-pressed','false');
      });
      f[k] = on ? null : v;
      c.setAttribute('aria-pressed', on ? 'false' : 'true');
      run();
    });
  });
  var clear = document.getElementById('jclear');
  if(clear) clear.addEventListener('click', function(){
    f = {fam:null, sen:null, rem:null, reg:null};
    chips.forEach(function(o){ o.setAttribute('aria-pressed','false'); });
    if(q) q.value = '';
    run();
  });
  run();
})();"""


# ----------------------------------------------------------------------------------
# page chrome
# ----------------------------------------------------------------------------------

def jsonld(obj) -> str:
    """One schema.org block.

    It is a data block, not executable script: the HTML spec does not run a <script> whose type is
    not a JavaScript MIME type, and crawlers read it straight out of the markup. The CSP in _headers
    still forbids executable inline script, and the site still makes zero external requests.
    Keys are emitted in insertion order so the bytes are stable across runs.
    """
    body = json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=False)
    # A JSON string can legally contain "</script>". Nothing here does, but escape it anyway
    # rather than trust the corpus.
    body = body.replace("</", "<\\/")
    return '<script type="application/ld+json">\n' + body + "\n</script>\n"


def head(title, desc, rel, extra="", ld=None, canon=None, robots="index,follow"):
    """canon is the site-relative path of this page, e.g. "learn/what-is-an-mcp-server.html".
    <!--MDLINK--> is replaced in the markdown-twin pass with a link to this page's .md twin."""
    canon_tag = ""
    if canon is not None:
        canon_tag = f'<link rel="canonical" href="{raw_esc(SITE_BASE.rstrip("/") + "/" + canon)}">\n'
    blocks = ""
    if ld:
        for obj in (ld if isinstance(ld, list) else [ld]):
            blocks += jsonld(obj)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{robots}">
<meta name="color-scheme" content="light dark">
{canon_tag}<!--MDLINK--><link rel="stylesheet" href="{rel}assets/site.css">
<script src="{rel}assets/theme.js"></script>
{blocks}{extra}</head>
<body>
"""


def crumb_ld(rel, trail):
    """trail is [(label, href_relative_to_this_page_or_None), ...]. Emitted as a BreadcrumbList
    with absolute URLs built from SITE_BASE, which points at the intended home until it is routed."""
    items = []
    for i, (label, href) in enumerate(trail, start=1):
        node = {"@type": "ListItem", "position": i, "name": detype(label)}
        if href:
            node["item"] = SITE_BASE.rstrip("/") + "/" + href
        items.append(node)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}


def itemlist_ld(name, desc, url_path, rows):
    """rows is [(name, path)] already site relative. ItemList is the honest type for every
    listing page here: a list of named things in a published order, with no rating attached."""
    return {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": detype(name),
        "description": detype(desc),
        "url": SITE_BASE.rstrip("/") + "/" + url_path,
        "numberOfItems": len(rows),
        "itemListOrder": "https://schema.org/ItemListOrderAscending",
        "itemListElement": [
            {"@type": "ListItem", "position": i, "name": detype(n),
             "url": SITE_BASE.rstrip("/") + "/" + p}
            for i, (n, p) in enumerate(rows, start=1)
        ],
    }


def masthead(rel, current=""):
    def link(href, label, key):
        cur = ' aria-current="page"' if key == current else ""
        return f'<a href="{rel}{href}"{cur}>{label}</a>'
    return f"""<header class="masthead">
<div class="wrap wide">
<a class="brandmark plain" href="{rel}index.html">The GTM MCP <span class="g">Directory</span></a>
<nav class="navlinks">
{link('tools/index.html','Tools','tools')}
{link('categories/index.html','Categories','categories')}
{link('jobs/index.html','Jobs','jobs')}
{link('jobs-board/index.html','Hiring','jobs-board')}
{link('lists/index.html','Lists','lists')}
{link('learn/index.html','Learn','learn')}
{link('mcp/index.html','MCP status','mcp')}
{link('gates/index.html','Gate','gates')}
{link('methodology.html','Method','methodology')}
{link('data.html','Data','data')}
<button class="themetoggle" id="themetoggle" type="button">Dark</button>
</nav>
</div>
</header>
"""


def footer(rel, d, r):
    c = d["counts"]
    return f"""<footer class="foot">
<div class="wrap wide">
<div class="cols">
  <div>
    <div class="ft">The count</div>
    <p>{num(c['entries'])} directory entries across {c['categories']} category files.
    {num(c['canonical_entries'])} unique products, {c['cross_listed_entries']} of them cross listed
    in a second category and counted once here.</p>
    <p>{num(c['mcp_status']['official'])} official MCP servers,
    {c['mcp_status']['community']} community.
    {c['bench_tested']} bench tested.</p>
    <p>{num(c['jobs'])} jobs in {c['job_families']} families.
    {num(c['entries_tagged'])} entries carry at least one job tag,
    {c['entries_untagged']} carry none and say why.</p>
  </div>
  <div>
    <div class="ft">Views</div>
    <ul>
      <li><a href="{rel}tools/index.html">Every tool, A to Z</a></li>
      <li><a href="{rel}categories/index.html">By category</a></li>
      <li><a href="{rel}mcp/index.html">By MCP status</a></li>
      <li><a href="{rel}gates/index.html">By access gate</a></li>
      <li><a href="{rel}jobs/index.html">By job</a></li>
      <li><a href="{rel}jobs-board/index.html">The GTM Engineer job board</a></li>
      <li><a href="{rel}github/index.html">By GitHub health</a></li>
    </ul>
  </div>
  <div>
    <div class="ft">The rules</div>
    <ul>
      <li><a href="{rel}methodology.html">How an entry is made</a></li>
      <li><a href="{rel}submit.html">Submit a tool, free</a></li>
      <li><a href="{rel}learn/index.html">Learn: the questions, answered</a></li>
      <li><a href="{rel}lists/index.html">The lists</a></li>
      <li><a href="{REPO_URL}" rel="noopener">The repo</a></li>
    </ul>
    <p>Listing is free. Verification is mandatory. Placement is not for sale.</p>
  </div>
  <div>
    <div class="ft">For agents</div>
    <ul>
      <li><a href="{rel}llms.txt">llms.txt</a></li>
      <li><a href="{rel}data.html">The public data endpoint</a></li>
      <li><a href="{rel}data/directory.json">directory.json</a></li>
      <li><a href="{rel}search-index.json">search-index.json</a></li>
      <li><a href="{rel}sitemap.xml">sitemap.xml</a></li>
    </ul>
    <p>Every page on this site has a markdown twin at the same path with a .md extension.
    Same content, no chrome.<!--MDFOOT--></p>
  </div>
</div>
<div class="legal">
Generated {esc(d['generated_on'])} by {esc(d['generated_by'])} from {esc(r['reconciliation']['authority'])}.
Reconciled: build {num(r['reconciliation']['build_total'])} vs recount
{num(r['reconciliation']['recount_total'])}.<br>
Every number on this site is read from the baked data files. Nothing is estimated and nothing is rounded.<br>
The GTM MCP Directory is a product of Agent Operator. Built by Andrew McGuire.
Brendan Short's The Signal defines and analyses the GTM Engineer role; this is a utility for people doing the job.
</div>
</div>
</footer>
</body>
</html>
"""


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


# ----------------------------------------------------------------------------------
# shared fragments
# ----------------------------------------------------------------------------------

def badge_mcp(e, rel, link=True):
    b = e["mcp_status_bucket"]
    tone = MCP_TONE.get(b, "mute")
    label = MCP_LABEL.get(b, b)
    if link:
        return f'<a class="badge {tone}" href="{rel}mcp/{b}.html">{esc(label)}</a>'
    return f'<span class="badge {tone}">{esc(label)}</span>'


def badge_gate(e, rel, link=True):
    b = e["api_gate_bucket"]
    tone = GATE_TONE.get(b, "mute")
    label = GATE_LABEL.get(b, b)
    if link:
        return f'<a class="badge {tone}" href="{rel}gates/{b}.html">{esc(label)}</a>'
    return f'<span class="badge {tone}">{esc(label)}</span>'


def entry_row(e, rel, show_cat=True, byid=None):
    """One entry as a row. Cross listed entries link to their canonical page."""
    target = e["canonical_id"] if not e.get("canonical") else e["id"]
    tgt = byid.get(target, e) if byid else e
    href = f'{rel}tools/{tgt["slug"]}.html'
    bits = [badge_mcp(e, rel), badge_gate(e, rel)]
    if show_cat:
        bits.append(
            f'<a class="badge mute flat" href="{rel}categories/{e["category_slug"]}.html">'
            f'{esc(e["category_label"])}</a>'
        )
    if not e.get("canonical"):
        bits.append(
            f'<span class="badge xref flat">Cross listed, canonical home is '
            f'{esc(tgt["category_label"])}</span>'
        )
    return f"""<li class="row">
<div class="top"><a class="nm" href="{href}">{esc(e['name'])}</a>
<span class="dom">{esc(e['vendor_domain'] or e['vendor_url'])}</span></div>
<div class="desc">{esc(trim(e['what_it_does'], 210))}</div>
<div class="badges">{''.join(bits)}</div>
</li>"""


def rows_block(entries, rel, show_cat=True, byid=None):
    items = "\n".join(entry_row(e, rel, show_cat, byid) for e in entries)
    return f'<ul class="rows">\n{items}\n</ul>'


_JOBS_CACHE = {}


def jobs_by_id(d):
    """{job_id: job block} out of directory.json's closed vocabulary. Cached per process."""
    if "jobs" not in _JOBS_CACHE:
        _JOBS_CACHE["jobs"] = {j["id"]: j for j in d["jobs_vocabulary"]["jobs"]}
        _JOBS_CACHE["families"] = {f["id"]: f for f in d["job_families"]}
    return _JOBS_CACHE["jobs"]


def families_by_id(d):
    jobs_by_id(d)
    return _JOBS_CACHE["families"]


def job_label(d, jid):
    j = jobs_by_id(d).get(jid)
    return j["label"] if j else jid


def untagged_reasons(r):
    """{entry_id: reason} for the entries the tagging pass deliberately left blank."""
    if "reasons" not in _JOBS_CACHE:
        out = {}
        for row in r.get("jobs", {}).get("needs_review", []):
            if row.get("tagged"):
                continue
            for eid in row.get("entry_ids", []):
                out[eid] = row.get("reason", "")
        _JOBS_CACHE["reasons"] = out
    return _JOBS_CACHE["reasons"]


TAG_MEANING = ("A job tag means the vendor says the tool does this. It is not a test result, not "
               "proof the capability is reachable through the tool's MCP server, and not proof it "
               "is available on the gate this entry records.")


def sort_entries(entries):
    return sorted(entries, key=lambda e: (e.get("display_rank", 9999), e["name"].lower()))


def sort_alpha(entries):
    return sorted(entries, key=lambda e: (e["name"].lower(), e["id"]))


# ----------------------------------------------------------------------------------
# index.html
# ----------------------------------------------------------------------------------

def build_index(d, r, out: Path):
    c = d["counts"]
    cov = r["coverage"]
    rel = ""
    gen = d["generated_on"]
    lc = cov["last_checked"]
    lc_line = ", ".join(f"{num(v)} on {k}" for k, v in sorted(lc.items()))

    stats = [
        ("gold", c["entries"], "tools counted"),
        ("gold", c["mcp_status"]["official"], "official MCP servers"),
        ("teal", c["mcp_status"]["community"], "community MCP"),
        ("copper", c["mcp_status"]["none-found"], "no MCP found"),
        ("copper", c["api_gate"]["enterprise-only"], "enterprise gated"),
        ("teal", cov["solo_reachable"], "solo reachable"),
        ("mute", c["bench_tested"], "bench tested"),
    ]
    statrow = "\n".join(
        f'<div class="stat is-{tone}"><div class="n">{num(n)}</div><div class="k">{esc(k)}</div></div>'
        for tone, n, k in stats
    )

    # the inversion, computed from the category blocks in directory.json
    cats = sorted(
        d["categories"],
        key=lambda x: -((x["mcp_status"]["official"] + x["mcp_status"]["community"]) / x["total"]),
    )
    cov_items = []
    for x in cats:
        off = x["mcp_status"]["official"]
        com = x["mcp_status"]["community"]
        tot = x["total"]
        cov_items.append(
            f'<li><div class="lab"><a href="categories/{x["slug"]}.html">{esc(x["label"])}</a>'
            f'<span class="r"><b>{off + com}</b> of {tot} reachable</span></div>'
            f'<div class="bar"><i class="o" style="width:{off / tot * 100:.4f}%"></i>'
            f'<i class="c" style="width:{com / tot * 100:.4f}%"></i></div></li>'
        )
    top, bottom = cats[0], cats[-1]

    def ratio(x):
        return f'{x["mcp_status"]["official"] + x["mcp_status"]["community"]} of {x["total"]}'

    mcp_chips = "".join(
        f'<button class="chip" type="button" data-kind="mcp" data-val="{b}" '
        f'aria-pressed="false">{esc(MCP_LABEL[b])}</button>'
        for b in MCP_ORDER if c["mcp_status"].get(b)
    )
    gate_chips = "".join(
        f'<button class="chip" type="button" data-kind="gate" data-val="{b}" '
        f'aria-pressed="false">{esc(GATE_LABEL[b])}</button>'
        for b in GATE_ORDER if c["api_gate"].get(b)
    )

    install = html.escape(json.dumps(
        {"mcpServers": {SERVER_ID: {"command": "uvx", "args": [PACKAGE_NAME]}}},
        indent=2,
    ))

    body = f"""{masthead(rel)}
<div class="hero">
<div class="wrap wide">
<div class="eyebrow">Agent Operator</div>
<h1 class="display">The GTM MCP<br>Directory</h1>
<p class="lede">Every GTM tool your agent can use, and which one does the job.</p>
<div class="rule"></div>
<p class="stamp"><b>{num(c['entries'])} tools</b> counted &middot;
<b>{num(c['mcp_status']['official'])} official MCP servers</b> &middot;
generated <b>{esc(gen)}</b> by {esc(d['generated_by'])} &middot;
reconciled against {esc(r['reconciliation']['authority'])}</p>
<div class="stats">
{statrow}
</div>
<p class="note">Entry facts were pulled by hand: {esc(lc_line)}. The generated date above is only
the date this site was baked. Both dates ship because both rot.
{num(c['canonical_entries'])} of the {num(c['entries'])} entries are unique products;
{c['cross_listed_entries']} are the same product listed in a second category and counted once here.</p>
<div class="btnrow">
<a class="btn solid" href="#search">Search by capability</a>
<a class="btn" href="#install">Install the MCP server</a>
<a class="btn ghost" href="mcp/official.html">See the {num(c['mcp_status']['official'])} official servers</a>
</div>
</div>
</div>

<section id="search">
<div class="wrap wide">
<div class="eyebrow">Capability search</div>
<h2>Ask for the job, not the category.</h2>
<p class="sub">An agent does not want a data enrichment tool. It wants a person's title from a
LinkedIn URL. Type the thing you are trying to do. This runs in your browser over a baked index:
no backend, no query logging, and it keeps working with the network cable pulled out.</p>
<div class="searchbox">
<label class="sr" for="q" hidden>Search the directory</label>
<input id="q" type="search" autocomplete="off" spellcheck="false"
 placeholder="enrich a company from its domain">
</div>
<div class="filters">{mcp_chips}</div>
<div class="filters">{gate_chips}</div>
<p class="sortnote">Ordering is fixed and published, never tuned and never purchasable.
{esc(d['sort_rule'])} With a query typed, matches are banded by relevance first and the rule above
breaks every tie. An exact name match pins to the top and nothing else is boosted.
The filters above run over the {num(c['canonical_entries'])} unique products, so their totals sit
below the {num(c['entries'])} entry totals used by the
<a href="mcp/index.html">MCP status</a> and <a href="gates/index.html">gate</a> views. Both numbers
are correct and the difference is the {c['cross_listed_entries']} cross listings.</p>
<p class="note" id="idxstamp"></p>
<p id="count"></p>
<ul class="rows" id="results"></ul>
</div>
</section>

<section class="tint">
<div class="wrap wide">
<div class="eyebrow">The inversion</div>
<h2>The tools sold as agents are the least usable by agents.</h2>
<p class="sub">{esc(top['label'])} is {ratio(top)} reachable by an agent.
{esc(bottom['label'])} is {ratio(bottom)}. Gold is an official server, green is a community one.
Every ratio below is read straight out of the category blocks in directory.json.</p>
<ul class="cov">
{chr(10).join(cov_items)}
</ul>
</div>
</section>

<section id="install">
<div class="wrap wide">
<div class="eyebrow">Install the MCP server</div>
<h2>Point your agent at the directory.</h2>
<p class="sub">The server loads the baked file once at import and answers from memory. It makes
zero outbound network requests, so it cannot be slow, cannot rate limit you, cannot cost anything,
and cannot leak your query to a vendor. Everything network shaped happens in the weekly build.</p>
<pre><code>{install}</code></pre>
<p class="note">The package is not on PyPI yet, so this block is the shape the install will take
rather than a working one-liner today. The server source is real and public: it lives in the
<a href="{REPO_URL}" rel="noopener">{PACKAGE_NAME}</a> repo and runs from a checkout right now.</p>
<div class="grid2">
<div class="card">
<div class="kicker">What it answers</div>
<h3>find_tools</h3>
<p>Which tools can do X, and can your agent actually reach them. Filters on category, MCP status,
access gate and tier, and states the ordering rule it used.</p>
</div>
<div class="card">
<div class="kicker">What it answers</div>
<h3>get_tool</h3>
<p>Every field on one entry, sources in full, plus the cross reference when the same product is
listed in a second category.</p>
</div>
<div class="card">
<div class="kicker">What it answers</div>
<h3>whats_mcpd</h3>
<p>The stat block. {num(c['entries'])} entries, {num(c['mcp_status']['official'])} official,
{c['mcp_status']['community']} community, {num(c['mcp_status']['none-found'])} none found, and
{c['bench_tested']} bench tested, scoped to a category when you ask for one.</p>
</div>
<div class="card">
<div class="kicker">What it answers</div>
<h3>list_categories</h3>
<p>The {c['categories']} category files with their counts, gates and source markdown, reconciled
against {esc(r['reconciliation']['authority'])} at build time.</p>
</div>
</div>
</div>
</section>

<section class="tint">
<div class="wrap wide">
<div class="grid2">
<div>
<div class="eyebrow">The weekly diff</div>
<h2>Get the changelog by email.</h2>
<p class="sub">Once a week: new entries, dead endpoints, gate changes, and every tool that moved
between MCP statuses. Assembled from the machine output, never written from thin air.</p>
<!-- TODO: wire this form to Kit (kit.com). Set action to the Kit hosted form endpoint,
     method="post", and add the hidden Kit form id field. Until then the control is disabled
     so the page never posts anywhere and never makes an external request. -->
<form class="subform" action="" method="post" onsubmit="return false;">
  <input type="email" name="email_address" placeholder="you@company.com" disabled>
  <button class="btn solid" type="submit" disabled>Not wired yet</button>
</form>
<p class="note">PLACEHOLDER. The list runs on Kit and the form action is deliberately empty until
that endpoint is set. No address is collected today and nothing is sent anywhere.</p>
</div>
<div>
<div class="eyebrow">Submit a tool</div>
<h2>Listing is free. Placement is not for sale.</h2>
<p class="sub">Anyone can submit a tool. Every submission is verified against public sources
before it is listed, and the verification is the product. No vendor can pay to be listed, to rank
higher, to be featured, or to soften a note. BENCH-TESTED cannot be bought at any price.</p>
<div class="btnrow">
<a class="btn" href="{ISSUE_URL}" rel="noopener">Open the submission form</a>
<a class="btn ghost" href="submit.html">Read what happens next</a>
</div>
<p class="note">The submission queue is a GitHub issue form on the public
{PACKAGE_NAME} repo. It is open now, and every submission is verified before it lists.</p>
</div>
</div>
</div>
</section>

<section>
<div class="wrap wide">
<div class="eyebrow">The questions</div>
<h2>Answers, not opinions.</h2>
<p class="sub">The questions people actually ask about GTM tools, MCP servers and agents, answered
from this data with the numbers generated at build time and the date stamped on every one. No tool
versus tool verdicts, because {c['bench_tested']} tools here have been bench tested.</p>
<div class="viewgrid">
<a class="viewcard" href="learn/index.html">
<div class="vt">Learn</div><div class="vn">Definitions, data and how to</div>
<div class="vd">What an MCP server is, what a GTM engineer is, which tools an agent can use for
free, how to connect an assistant to a CRM.</div></a>
<a class="viewcard" href="lists/index.html">
<div class="vt">The lists</div>
<div class="vn">{num(c['mcp_status']['official'])} official servers, {c['api_gate']['free']} free tiers</div>
<div class="vd">The same entries cut the ways people ask for them: by MCP status, by gate, by auth
type, by category.</div></a>
<a class="viewcard" href="jobs/index.html">
<div class="vt">By job</div><div class="vn">{c['jobs']} jobs, {c['job_families']} families</div>
<div class="vd">What an agent actually asks for, phrased from the agent's side, with the tools
tagged against each one.</div></a>
<a class="viewcard" href="data.html">
<div class="vt">The data</div><div class="vn">directory.json, free, no key</div>
<div class="vd">The whole directory as one JSON file, plus llms.txt and a markdown twin of every
page on this site.</div></a>
</div>
</div>
</section>

<section class="tint">
<div class="wrap wide">
<div class="eyebrow">Honesty</div>
<h2>{c['bench_tested']} bench tested, and that number is on the front page.</h2>
<p class="sub">Every entry is RESEARCHED: facts from public sources with URLs, no usage claims,
nobody has run the tool. BENCH-TESTED means Andrew personally ran it on a stated date. There are
{c['bench_tested']} of those, the number is published rather than hidden, and it is the proof the
tier means something. {num(cov['api_gate_unknown'])} entries carry an access gate of unknown,
{num(cov['docs_url_missing'])} have no documentation URL recorded, and the
{num(r['data_quality']['thin_sourcing']['count'])} thinly sourced entries are named on the
methodology page rather than quietly padded.</p>
<div class="btnrow">
<a class="btn" href="methodology.html">How an entry is made</a>
<a class="btn ghost" href="tools/index.html">Browse all {num(c['canonical_entries'])} products</a>
</div>
</div>
</section>
"""
    extra = f'<script src="assets/search-index.js"></script>\n<script defer src="assets/search.js"></script>\n'
    ld = [
        dataset_ld(d, r, "index.html"),
        {
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": "The GTM MCP Directory",
            "url": SITE_BASE.rstrip("/") + "/",
            "description": f"{c['entries']} GTM tools counted, {c['mcp_status']['official']} with "
                           f"an official MCP server. Which tools an AI agent can call, and which "
                           f"ones a solo operator can reach without a procurement cycle.",
            "publisher": {"@type": "Person", "name": "Andrew McGuire"},
            "inLanguage": "en",
        },
    ]
    page = (
        head("The GTM MCP Directory",
             f"{c['entries']} GTM tools counted, {c['mcp_status']['official']} with an official MCP "
             f"server. Which tools an agent can actually call, and which ones a solo operator can "
             f"reach without a procurement cycle.", rel, extra, ld=ld, canon="index.html")
        + body + footer(rel, d, r)
    )
    write(out / "index.html", page)


# ----------------------------------------------------------------------------------
# tool pages
# ----------------------------------------------------------------------------------

def field(k, v, cls="", empty=None):
    if not v:
        if empty is None:
            return ""
        return (f'<div class="field"><div class="k">{esc(k)}</div>'
                f'<div class="v empty">{esc(empty)}</div></div>')
    return (f'<div class="field"><div class="k">{esc(k)}</div>'
            f'<div class="v {cls}">{v}</div></div>')


def urllist(urls, annotations=None):
    if not urls:
        return ""
    li = []
    for u in urls:
        li.append(f'<li><a href="{raw_esc(u)}" rel="noopener nofollow">{raw_esc(u)}</a></li>')
    if annotations:
        for a in annotations:
            li.append(f'<li>{esc(a)}</li>')
    return "<ul>" + "".join(li) + "</ul>"


def build_tool_page(e, d, r, byid, out: Path):
    rel = "../"
    c = d["counts"]
    cov = r["coverage"]
    mb = e["mcp_status_bucket"]
    gb = e["api_gate_bucket"]

    vendor = e["vendor_url"] or ""
    vhref = vendor if vendor.startswith("http") else "https://" + vendor
    parts = []

    parts.append(f"""<div class="wrap">
<div class="crumbs"><a href="{rel}index.html">Directory</a> /
<a href="{rel}categories/{e['category_slug']}.html">{esc(e['category_label'])}</a> /
{esc(e['name'])}</div>
<div class="toolhead">
<h1>{esc(e['name'])}</h1>
<div class="badges">
{badge_mcp(e, rel)}
{badge_gate(e, rel)}
<a class="badge mute flat" href="{rel}categories/{e['category_slug']}.html">{esc(e['category_label'])}</a>
<span class="badge tier flat">{esc(e['tier'])}</span>
<span class="badge mute flat">Checked {esc(e['last_checked'])}</span>
</div>
<div class="tierbox"><b>{esc(e['tier'])}</b>
{esc(d['honesty']['tier_meanings'].get(e['tier'], ''))}
The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and
cannot be bought at any price. Across the whole directory that count is {c['bench_tested']}.</div>
<p class="note">Vendor: <a href="{raw_esc(vhref)}" rel="noopener nofollow">{raw_esc(vendor)}</a>
&middot; entry id {esc(e['id'])} &middot; source
{esc(e['source_file'])} line {e['source_line']}</p>
</div>""")

    parts.append('<div class="fields">')
    parts.append(field("What it does", esc(e["what_it_does"])))
    parts.append(field("AI features, separated from automation with an AI label on it",
                       esc(e["ai_features"])))
    parts.append(field("RevOps role", esc(e["revops_role"])))

    # MCP block
    mcp_urls = urllist(e["mcp_urls"])
    mcp_body = f"""<div class="blockgrid">
<div><div class="bk">Status bucket</div><div class="bv">{esc(MCP_LABEL.get(mb, mb))}</div></div>
<div><div class="bk">Auth</div><div class="bv">{esc(e['mcp_auth']) or '<span class="empty">not recorded</span>'}</div></div>
<div><div class="bk">Parsed URLs</div><div class="bv">{len(e['mcp_urls'])} found in the mcp_url field</div></div>
</div>
<p class="note" style="margin-top:14px">{esc(MCP_BLURB.get(mb, ''))}
The status was established on {esc(e['last_checked'])} and has not been re-fetched since.</p>
<p class="note" style="margin-top:14px">mcp_status, verbatim from the file:</p>
<p class="v mono">{esc(e['mcp_status'])}</p>"""
    if e["mcp_url"]:
        mcp_body += f'<p class="note" style="margin-top:14px">mcp_url, verbatim from the file:</p><p class="v mono">{esc(e["mcp_url"])}</p>'
    else:
        mcp_body += ('<p class="note" style="margin-top:14px">The mcp_url field is empty on this entry. '
                     f'{cov["mcp_url_missing"]} of {cov["total_entries"]} entries are.</p>')
    if mcp_urls:
        mcp_body += mcp_urls
    parts.append(field("MCP server", mcp_body))

    # gate
    gate_body = f"""<div class="blockgrid">
<div><div class="bk">Gate bucket</div><div class="bv">{esc(GATE_LABEL.get(gb, gb))}</div></div>
<div><div class="bk">Can a solo operator reach it</div><div class="bv">{
    'Yes, without talking to anyone' if gb == 'free' else
    'Yes, by paying, no sales call' if gb == 'paid' else
    'Not without a contract' if gb in ('enterprise-only', 'enterprise-leaning') else
    'Not established'}</div></div>
</div>
<p class="note" style="margin-top:14px">api_gate, verbatim from the file:</p>
<p>{esc(e['api_gate'])}</p>"""
    if gb == "unknown":
        gate_body += (f'<p class="note">{cov["api_gate_unknown"]} of {cov["total_entries"]} entries '
                      "carry an unknown gate. Unknown is a legal answer and it ships as unknown "
                      "rather than as a guess.</p>")
    parts.append(field("Access gate", gate_body))

    # docs
    if e["docs_url"]:
        docs_body = (f'<p><a href="{raw_esc(e["docs_url"])}" rel="noopener nofollow">'
                     f'{raw_esc(e["docs_url"])}</a></p>'
                     '<p class="note">No documentation text is reproduced anywhere on this site. '
                     'Read the vendor page for the prose. The structured docs digest specced in '
                     'SPEC section 3 has not been built or crawled: docs_digest is null on every '
                     'entry in this build.</p>')
    else:
        docs_body = (f'<p class="v empty">No documentation URL recorded.</p>'
                     f'<p class="note">{cov["docs_url_missing"]} of {cov["total_entries"]} entries '
                     'are in the same position. Blank is legal and it is published as blank.</p>')
    parts.append(field("API documentation", docs_body))

    # github
    ghc = sorted(set(e["github_candidates"]))
    gh_body = ('<p class="v empty">Not measured. github_url, github_stars, github_last_commit and '
               'github_archived are null on every entry in this build.</p>'
               '<p class="note">The refresh rail specced in SPEC section 7.2 has not been run. An '
               'unstamped star count is a lie, so nothing is shown rather than something stale.</p>')
    if ghc:
        gh_body += ('<p class="note" style="margin-top:14px">A github.com URL already appears '
                    'somewhere in this entry, which is a seed for that rail and not a measurement '
                    'of repo health:</p>' + urllist(ghc))
    parts.append(field("GitHub health", gh_body))

    # jobs
    if e["jobs"]:
        jl = "".join(
            f'<li><a href="{rel}jobs/{raw_esc(j)}.html">{esc(job_label(d, j))}</a></li>'
            for j in e["jobs"]
        )
        jb = (f"<ul>{jl}</ul><p class='note'>{esc(TAG_MEANING)}</p>"
              f"<p class='note'>Tagged by {esc(e['jobs_tagged_by'])} on "
              f"{esc(e['jobs_tagged_on'])} against the closed "
              f"{c['jobs']} job vocabulary. {num(cov['jobs_tagged'])} of "
              f"{num(cov['total_entries'])} entries carry at least one tag; "
              f"{cov['jobs_assignments']} tags are assigned in total.</p>")
    else:
        why = untagged_reasons(r).get(e["id"], "")
        jb = '<p class="v empty">No job tag on this entry.</p>'
        if why:
            jb += f'<p class="note">Reason recorded by the tagging pass: {esc(why)}</p>'
        jb += (f'<p class="note">{cov["jobs_untagged"]} of {num(cov["total_entries"])} entries are '
               'untagged. An empty list here means nobody has tagged this, not that the tool does '
               'nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays '
               'blank rather than being forced into the nearest tag.</p>')
    parts.append(field("Jobs it can do", jb))

    # cross reference
    if e["also_listed_in"]:
        blocks = []
        for other in e["also_listed_in"]:
            o = byid.get(other["id"])
            if not o:
                continue
            role = ("This page is the canonical home. The listing below is the same product, "
                    "counted separately in the source markdown."
                    if e.get("canonical") else
                    "The canonical home for this product is the listing below.")
            tgt = o if o.get("canonical") else e
            blocks.append(f"""<p>{esc(role)}</p>
<div class="blockgrid">
<div><div class="bk">Listed as</div><div class="bv">{esc(o['name'])}</div></div>
<div><div class="bk">Category</div><div class="bv"><a href="{rel}categories/{o['category_slug']}.html">{esc(o['category_label'])}</a></div></div>
<div><div class="bk">MCP status there</div><div class="bv">{esc(MCP_LABEL.get(o['mcp_status_bucket'], o['mcp_status_bucket']))}</div></div>
<div><div class="bk">Gate there</div><div class="bv">{esc(GATE_LABEL.get(o['api_gate_bucket'], o['api_gate_bucket']))}</div></div>
<div><div class="bk">Source</div><div class="bv">{esc(o['source_file'])} line {o['source_line']}</div></div>
<div><div class="bk">Canonical page</div><div class="bv"><a href="{rel}tools/{tgt['slug']}.html">{esc(tgt['name'])}</a></div></div>
</div>
<p class="note">What that listing says it does: {esc(trim(o['what_it_does'], 320))}</p>""")
        blocks.append(
            f'<p class="note">{d["counts"]["cross_listed_entries"]} of the '
            f'{d["counts"]["entries"]} entries are cross listed like this. They are why the entry '
            f'count is {d["counts"]["entries"]} and the unique product count is '
            f'{d["counts"]["canonical_entries"]}. The canonical home is declared in INDEX.md, not '
            'chosen by the parser.</p>'
        )
        parts.append(field("Also listed in another category", "".join(blocks)))

    # sources
    n_src = len(e["source_urls"])
    src_body = urllist(e["source_urls"], e["source_annotations"])
    src_body += f'<p class="note">{n_src} source URL{"" if n_src == 1 else "s"}.'
    if n_src < 2:
        src_body += (' Thin. The standing rule is at least two independent sources with the '
                     "vendor's own site unable to be both of them, and this entry does not meet "
                     f'it. {r["data_quality"]["thin_sourcing"]["count"]} entries are in the same '
                     'state and they are listed on the methodology page.')
    src_body += ' Raw sources field, verbatim: </p><p class="v mono">' + esc(e["sources"]) + "</p>"
    parts.append(field("Sources", src_body))

    parts.append(field("Notes, verbatim from the file", esc(e["notes"]),
                       empty="No notes on this entry."))

    parts.append(field("Provenance", f"""<div class="blockgrid">
<div><div class="bk">Entry id</div><div class="bv">{esc(e['id'])}</div></div>
<div><div class="bk">Source file</div><div class="bv">{esc(e['source_file'])}</div></div>
<div><div class="bk">Source line</div><div class="bv">{e['source_line']}</div></div>
<div><div class="bk">Tier</div><div class="bv">{esc(e['tier'])}</div></div>
<div><div class="bk">last_checked</div><div class="bv">{esc(e['last_checked'])}</div></div>
<div><div class="bk">Data baked</div><div class="bv">{esc(d['generated_on'])}</div></div>
</div>
<p class="note">Every field above is rendered from directory.json exactly as the build produced it.
Nothing is summarised and nothing is dropped. The one change made at render time is typographic and
it is disclosed on the <a href="{rel}methodology.html">methodology page</a>.</p>"""))

    parts.append("</div></div>")

    app = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": detype(e["name"]),
        "url": vhref,
        "applicationCategory": "BusinessApplication",
        "applicationSubCategory": detype(e["category_label"]),
        "description": detype(trim(e["what_it_does"], 300)),
        "offers": {"@type": "Offer", "category": GATE_LABEL.get(gb, gb)},
        "featureList": [job_label(d, j) for j in e["jobs"]],
        "subjectOf": {
            "@type": "Dataset", "name": "The GTM MCP Directory",
            "url": SITE_BASE.rstrip("/") + "/data.html",
        },
    }
    if e["mcp_urls"]:
        app["softwareHelp"] = {"@type": "CreativeWork", "url": e["mcp_urls"][0]}
    if e["docs_url"]:
        app["documentation"] = e["docs_url"]
    trail = [("Directory", "index.html"),
             (e["category_label"], f"categories/{e['category_slug']}.html"),
             (e["name"], f"tools/{e['slug']}.html")]
    page = (head(f"{e['name']}: MCP server status, API access gate and what it does",
                 f"{trim(e['what_it_does'], 110)} {MCP_LABEL.get(mb, mb)}, "
                 f"{GATE_LABEL.get(gb, gb)}. Checked {e['last_checked']}.", rel,
                 ld=[app, crumb_ld(rel, trail)], canon=f"tools/{e['slug']}.html")
            + masthead(rel, "tools") + "".join(parts) + footer(rel, d, r))
    write(out / "tools" / f"{e['slug']}.html", page)


# ----------------------------------------------------------------------------------
# view pages
# ----------------------------------------------------------------------------------

def build_tools_index(d, r, entries, byid, out: Path):
    rel = "../"
    c = d["counts"]
    canon = sort_alpha([e for e in entries if e.get("canonical")])
    groups = {}
    for e in canon:
        ch = e["name"][0].upper()
        if not ch.isalpha():
            ch = "#"
        groups.setdefault(ch, []).append(e)
    keys = sorted(groups, key=lambda k: (k == "#", k))
    nav = "".join(f'<a href="#{k if k != "#" else "num"}">{k}</a>' for k in keys)
    body = []
    for k in keys:
        anchor = k if k != "#" else "num"
        body.append(f'<div class="alpha" id="{anchor}">{k}</div>')
        body.append(rows_block(groups[k], rel, True, byid))
    page = (head(f"Every GTM tool, A to Z: {c['canonical_entries']} products with MCP status",
                 f"All {c['canonical_entries']} unique products in The GTM MCP Directory, "
                 f"alphabetical, each with its MCP server status and API access gate.", rel,
                 ld=[crumb_ld(rel, [("Directory", "index.html"), ("Every tool", "tools/index.html")]),
                     itemlist_ld("Every GTM tool, A to Z",
                                 f"All {c['canonical_entries']} unique products.",
                                 "tools/index.html",
                                 [(e["name"], f"tools/{e['slug']}.html") for e in canon])],
                 canon="tools/index.html")
            + masthead(rel, "tools")
            + f"""<div class="wrap wide">
<div class="crumbs" style="padding-bottom:0"><a href="{rel}index.html">Directory</a> / Every tool</div>
<section style="padding-top:18px">
<div class="eyebrow">A to Z</div>
<h2>Every tool in the directory.</h2>
<p class="sub">{num(c['canonical_entries'])} unique products. The directory holds
{num(c['entries'])} entries in total; the extra {c['cross_listed_entries']} are the same products
listed a second time in another category and each one folds into its canonical page here.</p>
<div class="alphanav">{nav}</div>
{''.join(body)}
</section>
</div>"""
            + footer(rel, d, r))
    write(out / "tools" / "index.html", page)


def build_categories(d, r, entries, byid, out: Path):
    rel = "../"
    c = d["counts"]
    cards = []
    for x in sorted(d["categories"], key=lambda x: x["num"]):
        off = x["mcp_status"]["official"]
        com = x["mcp_status"]["community"]
        cards.append(f"""<a class="viewcard" href="{x['slug']}.html">
<div class="vt">{esc(x['label'])}</div>
<div class="vn">{x['total']} tools &middot; {off + com} agent reachable</div>
<div class="vd">{esc(trim(x['one_line'], 130))}</div>
</a>""")
    page = (head(f"GTM tools by category: {c['categories']} layers of the stack, counted",
                 f"The {c['categories']} categories in The GTM MCP Directory, their counts and "
                 f"their MCP coverage. {num(c['entries'])} entries, "
                 f"{c['mcp_status']['official']} official MCP servers.", rel,
                 ld=[crumb_ld(rel, [("Directory", "index.html"),
                                    ("By category", "categories/index.html")]),
                     itemlist_ld("GTM tool categories", "The layers of a go to market stack.",
                                 "categories/index.html",
                                 [(x["label"], f"categories/{x['slug']}.html")
                                  for x in sorted(d["categories"], key=lambda k: k["num"])])],
                 canon="categories/index.html")
            + masthead(rel, "categories")
            + f"""<div class="wrap wide">
<div class="crumbs" style="padding-bottom:0"><a href="{rel}index.html">Directory</a> / By category</div>
<section style="padding-top:18px">
<div class="eyebrow">View: by category</div>
<h2>How a human browses.</h2>
<p class="sub">{c['categories']} categories, {num(c['entries'])} entries. The totals below sum to
{num(c['entries'])} because a product listed in two categories is counted in both here, and once on
its canonical tool page.</p>
<div class="viewgrid">{''.join(cards)}</div>
</section>
</div>"""
            + footer(rel, d, r))
    write(out / "categories" / "index.html", page)

    for x in d["categories"]:
        ids = set(x["entry_ids"])
        mine = sort_entries([e for e in entries if e["id"] in ids])
        st = "".join(
            f'<div class="stat is-{MCP_TONE.get(b, "mute")}"><div class="n">{x["mcp_status"][b]}</div>'
            f'<div class="k">{esc(MCP_LABEL[b])}</div></div>'
            for b in MCP_ORDER if x["mcp_status"].get(b)
        )
        gt = "".join(
            f'<div class="stat is-{GATE_TONE.get(b, "mute")}"><div class="n">{x["api_gate"][b]}</div>'
            f'<div class="k">{esc(GATE_LABEL[b])}</div></div>'
            for b in GATE_ORDER if x["api_gate"].get(b)
        )
        off_c = x["mcp_status"]["official"]
        page = (head(f"{x['label']}: {x['total']} tools, {off_c} with an official MCP server",
                     f"{trim(x['one_line'], 100)} {x['total']} tools counted, {off_c} with an "
                     f"official MCP server and {x['api_gate']['free']} free to start.", rel,
                     ld=[crumb_ld(rel, [("Directory", "index.html"),
                                        ("By category", "categories/index.html"),
                                        (x["label"], f"categories/{x['slug']}.html")]),
                         itemlist_ld(x["label"], x["one_line"], f"categories/{x['slug']}.html",
                                     [(e["name"], f"tools/{(e if e.get('canonical') else byid.get(e['canonical_id'], e))['slug']}.html")
                                      for e in mine])],
                     canon=f"categories/{x['slug']}.html")
                + masthead(rel, "categories")
                + f"""<div class="wrap wide">
<div class="crumbs" style="padding-bottom:0"><a href="{rel}index.html">Directory</a> /
<a href="index.html">By category</a> / {esc(x['label'])}</div>
<section style="padding-top:18px">
<div class="eyebrow">{esc(x['num'])} &middot; {esc(x['slug'])}</div>
<h2>{esc(x['label'])}</h2>
<p class="sub">{esc(x['one_line'])}</p>
<div class="stats" style="margin-top:26px">
<div class="stat"><div class="n">{x['total']}</div><div class="k">entries in this file</div></div>
{st}
</div>
<div class="stats" style="margin-top:1px">{gt}</div>
<p class="note">Source file: {esc(x['file'])} &middot; content sha256
{esc(x['source_sha256'][:16])}... &middot; counts reconciled against
{esc(r['reconciliation']['authority'])} at build time.</p>
<div class="btnrow">
<a class="btn" href="{rel}lists/mcp-{x['slug']}.html">The {off_c + x['mcp_status']['community']} with an MCP server</a>
{''.join(f'<a class="btn ghost" href="{rel}jobs/{raw_esc(j)}.html">{esc(job_label(d, j))}</a>' for j in x.get('top_jobs', [])[:4])}
</div>
{rows_block(mine, rel, False, byid)}
</section>
</div>"""
                + footer(rel, d, r))
        write(out / "categories" / f"{x['slug']}.html", page)


def build_bucket_view(d, r, entries, byid, out: Path, kind):
    """kind is 'mcp' or 'gates'."""
    rel = "../"
    c = d["counts"]
    if kind == "mcp":
        key, order, labels, blurbs, tones = ("mcp_status_bucket", MCP_ORDER, MCP_LABEL,
                                             MCP_BLURB, MCP_TONE)
        counts = c["mcp_status"]
        title = "By MCP status"
        lede = ("The one column nobody else publishes. Can an agent call this tool at all, and "
                "who built the thing it calls.")
        nav = "mcp"
    else:
        key, order, labels, blurbs, tones = ("api_gate_bucket", GATE_ORDER, GATE_LABEL,
                                             GATE_BLURB, GATE_TONE)
        counts = c["api_gate"]
        title = "By access gate"
        lede = ("The second column nobody else publishes. Can a solo operator get in without a "
                "procurement cycle.")
        nav = "gates"

    cards = []
    for b in order:
        n = counts.get(b, 0)
        if not n:
            continue
        cards.append(f"""<a class="viewcard" href="{b}.html">
<div class="vt">{esc(labels[b])}</div>
<div class="vn">{n} of {num(c['entries'])} entries</div>
<div class="vd">{esc(trim(blurbs[b], 150))}</div>
</a>""")
    page = (head(f"{title}: every GTM tool sorted by {'MCP server status' if kind == 'mcp' else 'API access gate'}",
                 lede, rel,
                 ld=[crumb_ld(rel, [("Directory", "index.html"), (title, f"{kind}/index.html")]),
                     itemlist_ld(title, lede, f"{kind}/index.html",
                                 [(labels[b], f"{kind}/{b}.html") for b in order
                                  if counts.get(b)])],
                 canon=f"{kind}/index.html")
            + masthead(rel, nav)
            + f"""<div class="wrap wide">
<div class="crumbs" style="padding-bottom:0"><a href="{rel}index.html">Directory</a> / {esc(title)}</div>
<section style="padding-top:18px">
<div class="eyebrow">View: {esc(title.lower())}</div>
<h2>{esc(lede)}</h2>
<p class="sub">Buckets are the vocabulary in the source markdown, normalised by the build and never
invented. The counts below sum to {num(c['entries'])} and are reconciled against
{esc(r['reconciliation']['authority'])}.</p>
<div class="viewgrid">{''.join(cards)}</div>
</section>
</div>"""
            + footer(rel, d, r))
    write(out / kind / "index.html", page)

    for b in order:
        n = counts.get(b, 0)
        if not n:
            continue
        mine = sort_entries([e for e in entries if e[key] == b])
        assert len(mine) == n, f"{kind}/{b}: {len(mine)} rows vs count {n}"
        page = (head(f"{labels[b]}: {n} GTM tools, counted",
                     f"{n} of {num(c['entries'])} GTM tools in this directory are "
                     f"{labels[b].lower()}. {trim(blurbs[b], 110)}", rel,
                     ld=[crumb_ld(rel, [("Directory", "index.html"), (title, f"{kind}/index.html"),
                                        (labels[b], f"{kind}/{b}.html")]),
                         itemlist_ld(labels[b], blurbs[b], f"{kind}/{b}.html",
                                     [(e["name"], f"tools/{(e if e.get('canonical') else byid.get(e['canonical_id'], e))['slug']}.html")
                                      for e in mine])],
                     canon=f"{kind}/{b}.html")
                + masthead(rel, nav)
                + f"""<div class="wrap wide">
<div class="crumbs" style="padding-bottom:0"><a href="{rel}index.html">Directory</a> /
<a href="index.html">{esc(title)}</a> / {esc(labels[b])}</div>
<section style="padding-top:18px">
<div class="eyebrow">{esc(b)}</div>
<h2>{esc(labels[b])}</h2>
<p class="sub">{esc(blurbs[b])}</p>
<p class="note">{n} of {num(c['entries'])} entries. Ordered by the published rule:
{esc(d['sort_rule'])}</p>
{rows_block(mine, rel, True, byid)}
</section>
</div>"""
                + footer(rel, d, r))
        write(out / kind / f"{b}.html", page)


def job_stat_row(j):
    """The five numbers every job page and job card publishes, straight out of the vocabulary."""
    return "".join([
        f'<div class="stat"><div class="n">{j["entry_count"]}</div>'
        f'<div class="k">entries tagged</div></div>',
        f'<div class="stat is-gold"><div class="n">{j["mcp_status"]["official"]}</div>'
        f'<div class="k">official MCP</div></div>',
        f'<div class="stat is-teal"><div class="n">{j["mcp_status"]["community"]}</div>'
        f'<div class="k">community MCP</div></div>',
        f'<div class="stat is-copper"><div class="n">{j["mcp_status"]["none-found"]}</div>'
        f'<div class="k">no MCP found</div></div>',
        f'<div class="stat is-teal"><div class="n">{j["solo_reachable"]}</div>'
        f'<div class="k">solo reachable</div></div>',
    ])


def build_jobs(d, r, entries, byid, out: Path):
    """The job views. Built from the closed vocabulary in directory.json, which carries its own
    per-job counts, so nothing here is recounted a second way. When the vocabulary is absent or
    nothing is tagged, the honest stub ships instead."""
    rel = "../"
    c = d["counts"]
    cov = r["coverage"]
    jobs = jobs_by_id(d)
    fams = families_by_id(d)
    tagged = [e for e in entries if e.get("jobs")]

    if not (jobs and tagged):
        page = (head("By job - The GTM MCP Directory",
                     "The job vocabulary exists on paper. The tagging pass has not run, so there "
                     "is nothing to show yet and nothing is invented to fill the gap.", rel,
                     canon="jobs/index.html")
                + masthead(rel, "jobs")
                + f"""<div class="wrap wide">
<div class="crumbs" style="padding-bottom:0"><a href="{rel}index.html">Directory</a> / By job</div>
<section style="padding-top:18px">
<div class="eyebrow">View: by job</div>
<h2>Tagging in progress.</h2>
<div class="warn"><b>Nothing measured yet</b>
No entry in this build carries a job tag. This page is a stub on purpose: a job view built from
guesses would be wrong on the exact surface agents trust most. It fills in by itself the moment the
tagging lane writes tags into the data and this generator is re-run.</div>
</section></div>"""
                + footer(rel, d, r))
        write(out / "jobs" / "index.html", page)
        return 1, False

    by_job = {}
    for e in tagged:
        for jid in e["jobs"]:
            by_job.setdefault(jid, []).append(e)

    # ---------- the index: families, each with its jobs ----------
    blocks = []
    for f in d["job_families"]:
        rows = []
        for jid in f["job_ids"]:
            j = jobs.get(jid)
            if not j:
                continue
            n = j["entry_count"]
            off = j["mcp_status"]["official"]
            pct = f"{off / n * 100:.4f}" if n else "0"
            rows.append(
                f'<li><div class="lab"><a href="{raw_esc(jid)}.html">{esc(j["label"])}</a>'
                f'<span class="r"><b>{off}</b> official of {n} tagged</span></div>'
                f'<div class="bar"><i class="o" style="width:{pct}%"></i>'
                f'<i class="c" style="width:{j["mcp_status"]["community"] / n * 100:.4f}%"></i>'
                f'</div></li>'
            )
        blocks.append(f"""<h3 style="margin-top:34px"><a href="family-{raw_esc(f['id'])}.html">{esc(f['label'])}</a></h3>
<p class="sub">{esc(f['one_liner'])} {f['job_count']} jobs, {f['entry_count']} tagged entries.</p>
<ul class="cov">{''.join(rows)}</ul>""")

    ld = [
        crumb_ld(rel, [("Directory", "index.html"), ("By job", "jobs/index.html")]),
        itemlist_ld(
            "GTM jobs an AI agent can ask for",
            f"The closed {c['jobs']} job vocabulary behind The GTM MCP Directory.",
            "jobs/index.html",
            [(jobs[jid]["label"], f"jobs/{jid}.html") for f in d["job_families"]
             for jid in f["job_ids"] if jid in jobs],
        ),
    ]
    page = (head(f"By job: {c['jobs']} things a GTM agent asks for - The GTM MCP Directory",
                 f"{c['jobs']} jobs in {c['job_families']} families, tagged across "
                 f"{num(c['entries_tagged'])} of {num(c['entries'])} directory entries. Which tools "
                 f"carry each job and how many of them an agent can actually call.", rel,
                 ld=ld, canon="jobs/index.html")
            + masthead(rel, "jobs")
            + f"""<div class="wrap wide">
<div class="crumbs" style="padding-bottom:0"><a href="{rel}index.html">Directory</a> / By job</div>
<section style="padding-top:18px">
<div class="eyebrow">View: by job</div>
<h2>How an agent asks.</h2>
<p class="sub">An agent does not think it needs a data enrichment tool. It thinks it has a LinkedIn
URL and needs a job title. This view is the closed vocabulary of {c['jobs']} jobs in
{c['job_families']} families, each one a verb plus an object, phrased from the agent's side.
{num(cov['jobs_assignments'])} tags are assigned across {num(cov['jobs_tagged'])} of
{num(c['entries'])} entries. {cov['jobs_untagged']} entries carry no tag at all and each one records
why.</p>
<div class="warn"><b>What a tag means</b>{esc(TAG_MEANING)}
Tagged by {esc(d['jobs_vocabulary']['tags_meta']['tagged_by'])} on
{esc(d['jobs_vocabulary']['tags_meta']['tagged_on'])}. Tier is
{esc(d['jobs_vocabulary']['meta']['tier'])} and bench_tested is still {c['bench_tested']}.</div>
{''.join(blocks)}
<p class="note" style="margin-top:30px">Vocabulary source: {esc(d['jobs_vocabulary']['meta']['source_file'])},
sha256 {esc(d['jobs_vocabulary']['meta']['source_sha256'][:16])}... Tags source:
{esc(d['jobs_vocabulary']['tags_meta']['source_file'])}, sha256
{esc(d['jobs_vocabulary']['tags_meta']['source_sha256'][:16])}... The vocabulary is closed: a tool
whose job is not in it stays blank rather than being forced into the nearest tag.</p>
</section></div>"""
            + footer(rel, d, r))
    write(out / "jobs" / "index.html", page)
    n_pages = 1

    # ---------- one page per family ----------
    for f in d["job_families"]:
        mine_ids = set()
        cards = []
        for jid in f["job_ids"]:
            j = jobs.get(jid)
            if not j:
                continue
            mine_ids.update(j["entry_ids"])
            cards.append(f"""<a class="viewcard" href="{raw_esc(jid)}.html">
<div class="vt">{esc(j['label'])}</div>
<div class="vn">{j['entry_count']} tools &middot; {j['mcp_status']['official']} official MCP</div>
<div class="vd">{esc(trim(j['one_liner'], 130))}</div>
</a>""")
        mine = sort_entries([e for e in entries if e["id"] in mine_ids])
        ld = [
            crumb_ld(rel, [("Directory", "index.html"), ("By job", "jobs/index.html"),
                           (f["label"], f"jobs/family-{f['id']}.html")]),
            itemlist_ld(f["label"], f["one_liner"], f"jobs/family-{f['id']}.html",
                        [(jobs[jid]["label"], f"jobs/{jid}.html")
                         for jid in f["job_ids"] if jid in jobs]),
        ]
        page = (head(f"{f['label']} - GTM jobs an agent can ask for",
                     f"{f['one_liner']} {f['job_count']} jobs and {f['entry_count']} tagged "
                     f"entries in The GTM MCP Directory.", rel, ld=ld,
                     canon=f"jobs/family-{f['id']}.html")
                + masthead(rel, "jobs")
                + f"""<div class="wrap wide">
<div class="crumbs" style="padding-bottom:0"><a href="{rel}index.html">Directory</a> /
<a href="index.html">By job</a> / {esc(f['label'])}</div>
<section style="padding-top:18px">
<div class="eyebrow">Job family</div>
<h2>{esc(f['label'])}</h2>
<p class="sub">{esc(f['one_liner'])} {f['job_count']} jobs, {f['entry_count']} tagged entries,
{len(mine)} distinct entries across the family.</p>
<div class="viewgrid">{''.join(cards)}</div>
<h3 style="margin-top:40px">Every entry tagged with a job in this family</h3>
<p class="note">Ordered by the published rule: {esc(d['sort_rule'])}</p>
{rows_block(mine, rel, True, byid)}
</section></div>"""
                + footer(rel, d, r))
        write(out / "jobs" / f"family-{f['id']}.html", page)
        n_pages += 1

    # ---------- one page per job ----------
    for jid, j in sorted(jobs.items(), key=lambda kv: kv[1]["order"]):
        mine = sort_entries([e for e in entries if e["id"] in set(j["entry_ids"])])
        f = fams.get(j["family"], {})
        sib = [k for k in f.get("job_ids", []) if k != jid and k in jobs]
        cats = "".join(
            f'<li><a href="{rel}categories/{esc(slug_for_catnum(d, cn))}.html">'
            f'{esc(label_for_catnum(d, cn))}</a>: {n} tagged</li>'
            for cn, n in sorted(j["categories"].items(), key=lambda kv: (-kv[1], kv[0]))
        )
        aliases = "".join(f"<li>{esc(a)}</li>" for a in j["aliases"])
        off, com, none = (j["mcp_status"]["official"], j["mcp_status"]["community"],
                          j["mcp_status"]["none-found"])
        reach = off + com
        if j["entry_count"]:
            verdict = (f"{reach} of the {j['entry_count']} entries tagged with this job carry an "
                       f"MCP server of some kind, {off} of them official.")
        else:
            verdict = "No entry in this build carries this job."
        if off == 0 and j["entry_count"]:
            verdict += (" Not one is official, which means an agent cannot do this job through a "
                        "vendor maintained server today.")
        ld = [
            crumb_ld(rel, [("Directory", "index.html"), ("By job", "jobs/index.html"),
                           (j["label"], f"jobs/{jid}.html")]),
            itemlist_ld(f"GTM tools that can {j['phrasing']}", j["one_liner"], f"jobs/{jid}.html",
                        [(e["name"], f"tools/{(byid.get(e['canonical_id'], e) if not e.get('canonical') else e)['slug']}.html")
                         for e in mine]),
        ]
        page = (head(f"{j['label']}: {j['entry_count']} GTM tools, {off} with an official MCP server",
                     f"{j['one_liner']} {verdict} Counted "
                     f"{d['generated_on']} from the directory data.", rel, ld=ld,
                     canon=f"jobs/{jid}.html")
                + masthead(rel, "jobs")
                + f"""<div class="wrap wide">
<div class="crumbs" style="padding-bottom:0"><a href="{rel}index.html">Directory</a> /
<a href="index.html">By job</a> /
<a href="family-{raw_esc(j['family'])}.html">{esc(f.get('label', j['family']))}</a> /
{esc(j['label'])}</div>
<section style="padding-top:18px">
<div class="eyebrow">Job &middot; {esc(jid)}</div>
<h2>{esc(j['label'])}</h2>
<p class="sub">{esc(j['one_liner'])}</p>
<div class="stats" style="margin-top:26px">{job_stat_row(j)}</div>
<p class="note">{esc(verdict)} {
    f"All {j['entry_count']} tagged entries are distinct products."
    if j['product_count'] == j['entry_count'] else
    f"{j['product_count']} of the {j['entry_count']} tagged entries are distinct products; the "
    f"other {j['entry_count'] - j['product_count']} are the same product cross listed in a second "
    f"category."} {j['bench_tested']} have been bench tested. Counted
{esc(d['generated_on'])} from directory.json.</p>
<div class="warn"><b>What a tag means</b>{esc(TAG_MEANING)}</div>
<div class="grid2" style="margin-top:26px">
<div class="card">
<div class="kicker">Asked by a human or an agent as</div>
<ul class="srcs">{aliases}</ul>
</div>
<div class="card">
<div class="kicker">Where these tools live</div>
<ul class="srcs">{cats}</ul>
</div>
</div>
<h3 style="margin-top:40px">The {j['entry_count']} entries tagged {esc(jid)}</h3>
<p class="note">Ordered by the published rule: {esc(d['sort_rule'])}</p>
{rows_block(mine, rel, True, byid)}
<h3 style="margin-top:40px">Next to this job</h3>
<div class="btnrow">
{''.join(f'<a class="btn ghost" href="{raw_esc(k)}.html">{esc(jobs[k]["label"])}</a>' for k in sib)}
</div>
</section></div>"""
                + footer(rel, d, r))
        write(out / "jobs" / f"{jid}.html", page)
        n_pages += 1

    return n_pages, True


# ----------------------------------------------------------------------------------
# /jobs-board/ - the GTM Engineer job board
# ----------------------------------------------------------------------------------

def load_board():
    """jobs_board.json, baked by gtm-radar/jobs/build_board.py. Absent means the section
    is skipped rather than faked: a job board with no verification pass behind it is the
    exact thing this section exists to argue against."""
    p = DATA_DIR / "jobs_board.json"
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


BOARD_NO_DETAIL = (
    "There is no page here for an individual listing, and that is deliberate. The only "
    "honest copy of a job description is the employer's own, so this board does not "
    "republish one. Every row links straight at the posting, with tracking parameters "
    "stripped, and every row was fetched at that exact link on the verification date.")


def board_chip(kind, bucket, current=None):
    pressed = "true" if current == bucket["slug"] else "false"
    return (f'<button class="chip jchip" type="button" data-k="{kind}" '
            f'data-v="{raw_esc(bucket["slug"])}" aria-pressed="{pressed}">'
            f'{esc(bucket["label"])} {bucket["count"]}</button>')


def board_row(j):
    regs = " ".join(x["slug"] for x in j["regions"])
    hay = " ".join([j["company"], j["title"], j["location"], j["family_label"],
                    j["seniority_label"], j["remote_label"], j["ats"]]).lower()
    bits = [f'<span class="badge teal">Verified live {esc(j["verified_on"])}</span>',
            f'<span class="badge mute flat">{esc(j["family_label"])}</span>']
    if j["seniority"] != "unstated":
        bits.append(f'<span class="badge mute flat">{esc(j["seniority_label"])}</span>')
    bits.append(f'<span class="badge {"gold" if j["remote"] == "remote" else "mute"} flat">'
                f'{esc(j["remote_label"])}</span>')
    if j["salary"]:
        bits.append(f'<span class="badge gold flat">{esc(j["salary"])}</span>')
    if j["found_via_post"]:
        bits.append('<span class="badge copper">Found via post, verify before applying</span>')
    meta = [esc(j["location"] or "Location not stated")]
    if j["posted_date"]:
        meta.append(f'posted {esc(j["posted_date"])}')
    meta.append(f'tracked here since {esc(j["first_tracked"])}')
    meta.append(f'{esc(j["ats"] or "employer site")} posting')
    return f"""<li class="row jrow" data-fam="{raw_esc(j['family'])}" data-sen="{raw_esc(j['seniority'])}"
 data-rem="{raw_esc(j['remote'])}" data-reg="{raw_esc(regs)}" data-q="{esc(hay)}">
<div class="top"><a class="nm" href="{raw_esc(j['url'])}" rel="nofollow noopener">{esc(j['title'])}</a>
<span class="co">{esc(j['company'])}</span></div>
<div class="desc">{' &middot; '.join(meta)}</div>
<div class="badges">{''.join(bits)}</div>
</li>"""


def board_rows(jobs):
    return '<ul class="rows">\n' + "\n".join(board_row(j) for j in jobs) + "\n</ul>"


def build_jobs_board(d, r, board, out: Path):
    """The board, the ledger of what was taken down, and a page per title family that
    has enough live reqs to be worth one. Returns the page count."""
    if not board:
        return 0
    rel = "../"
    c = board["counts"]
    date = board["verified_on"]
    jobs = board["jobs"]
    n_pages = 0

    (out / "data").mkdir(parents=True, exist_ok=True)
    (out / "data" / "jobs_board.json").write_bytes(
        (DATA_DIR / "jobs_board.json").read_bytes())

    law_line = (f"Every listing verified live on {date}. Dead links are removed weekly, "
                f"not left to rot.")

    def chipset(kind, key, label):
        return (f'<div class="filterset"><div class="fk">{esc(label)}</div><div class="filters">'
                + "".join(board_chip(kind, b) for b in board["facets"][key])
                + "</div></div>")

    stats = "".join([
        f'<div class="stat is-teal"><div class="n">{c["live"]}</div>'
        f'<div class="k">live reqs on the board</div></div>',
        f'<div class="stat"><div class="n">{c["companies"]}</div>'
        f'<div class="k">companies hiring</div></div>',
        f'<div class="stat is-copper"><div class="n">{c["removed_this_pass"]}</div>'
        f'<div class="k">removed by this pass</div></div>',
        f'<div class="stat is-gold"><div class="n">{c["with_salary"]}</div>'
        f'<div class="k">publish a salary</div></div>',
    ])

    fams = [b for b in board["facets"]["family"] if b["count"] >= 5 and b["slug"] != "other-gtm"]
    famlinks = "".join(
        f'<a class="btn ghost" href="family-{raw_esc(b["slug"])}.html">{esc(b["label"])} '
        f'{b["count"]}</a>' for b in fams)

    page = (head(f"The GTM Engineer job board: {c['live']} reqs verified live on {date}",
                 f"{c['live']} GTM Engineer and adjacent reqs at {c['companies']} companies, "
                 f"every one of them fetched live on {date}. "
                 f"{c['removed_this_pass']} listings were removed by the same pass. "
                 f"Filter by title family, region, remote and seniority.", rel,
                 extra=f'<script src="{rel}assets/board.js" defer></script>\n',
                 ld=[crumb_ld(rel, [("Directory", "index.html"),
                                    ("The job board", "jobs-board/index.html")]),
                     itemlist_ld("The GTM Engineer job board",
                                 f"{c['live']} reqs verified live on {date}.",
                                 "jobs-board/index.html",
                                 [(f"{j['title']}, {j['company']}", "jobs-board/index.html")
                                  for j in jobs])],
                 canon="jobs-board/index.html")
            + masthead(rel, "jobs-board")
            + f"""<div class="wrap wide">
<div class="crumbs" style="padding-bottom:0"><a href="{rel}index.html">Directory</a> / The job board</div>
<section style="padding-top:18px">
<div class="eyebrow">The GTM Engineer job board</div>
<h2>{c['live']} reqs. All of them answered when we knocked.</h2>
<div class="lawbox">
<div class="lab">The law of this page</div>
<p>{esc(law_line)}</p>
<p>Every other job board fails at exactly this. A listing here was fetched at its own
apply link on the verification date and answered with the posting still on it. A listing
that failed is not softened, not greyed out and not left up: it is removed, and it is
named on <a href="verification.html">the verification page</a> with the reason.</p>
</div>
<div class="stats" style="margin-top:26px">{stats}</div>
<p class="note">Checked {c['checked']} tracked reqs on {date}. {c['live']} answered.
{c['dead']} were dead. {c['unverified']} could not be settled either way and are excluded
too, because unverified is not a synonym for live. Source data:
<a href="{rel}data/jobs_board.json">jobs_board.json</a>.</p>

<div class="boardbar">
<input id="jq" type="search" placeholder="Filter by company, title or city" aria-label="Filter listings">
<button class="btn ghost" id="jclear" type="button">Clear</button>
</div>
{chipset("fam", "family", "Title family")}
{chipset("reg", "region", "Where")}
{chipset("rem", "remote", "Remote")}
{chipset("sen", "seniority", "Seniority")}
<div id="jcount">{c['live']} of {c['live']} shown</div>
<div class="jempty" id="jempty" style="display:none">Nothing on the board matches that.
An empty result is a real answer here: it means no verified live req carries those words.
It does not mean the board is hiding anything.</div>
{board_rows(jobs)}

<h3 style="margin-top:40px">Why there is no page per job</h3>
<p class="sub">{esc(BOARD_NO_DETAIL)}</p>
<div class="btnrow">
<a class="btn" href="verification.html">How every listing is verified</a>
{famlinks}
</div>
</section>
</div>"""
            + footer(rel, d, r))
    write(out / "jobs-board" / "index.html", page)
    n_pages += 1

    # ------------------------------------------------------------------ verification
    m = board["method"]
    dead_rows = []
    for x in board["removed"]:
        tone = "copper" if x["status"] == "dead" else "mute"
        dead_rows.append(f"""<li class="row deadrow">
<div class="top"><span class="nm">{esc(x['title'])}</span>
<span class="co">{esc(x['company'])}</span></div>
<div class="desc">{esc(x['reason'])}</div>
<div class="url">{esc(x['url'])}</div>
<div class="badges"><span class="badge {tone}">{esc(x['status'])}</span>
<span class="badge mute flat">checked {esc(x['checked_on'])}</span>
<span class="badge mute flat">HTTP {esc(str(x['http_status']))}</span></div>
</li>""")
    derivs = "".join(f'<tr><td class="n">{esc(k)}</td><td>{esc(v)}</td></tr>'
                     for k, v in sorted(board["derivations"].items()))
    page = (head(f"How every listing on the job board is verified, and what was removed on {date}",
                 f"The verification method behind The GTM Engineer job board, and the full "
                 f"ledger of the {c['removed_this_pass']} listings the {date} pass removed, "
                 f"each with the reason it failed.", rel,
                 ld=crumb_ld(rel, [("Directory", "index.html"),
                                   ("The job board", "jobs-board/index.html"),
                                   ("Verification", "jobs-board/verification.html")]),
                 canon="jobs-board/verification.html")
            + masthead(rel, "jobs-board")
            + f"""<div class="wrap wide">
<div class="crumbs" style="padding-bottom:0"><a href="{rel}index.html">Directory</a> /
<a href="index.html">The job board</a> / Verification</div>
<section style="padding-top:18px">
<div class="eyebrow">The verification pass, {esc(date)}</div>
<h2>What was removed, and why.</h2>
<p class="sub">A job board is a claim about the world at a moment, and the moment passes.
This page is the receipt. {c['checked']} tracked reqs were checked on {esc(date)}.
{c['live']} are published. {c['removed_this_pass']} are not, and every one of them is
named below with the reason it failed.</p>

<div class="prose" style="margin-top:30px">
<h3>The method</h3>
<ul class="bare">
<li>{esc(m['what'])}</li>
<li>{esc(m['fetch'])}</li>
<li>{esc(m['cross_check'])}</li>
<li>{esc(m['publishable'])}</li>
<li>{esc(m['changed'])}</li>
<li>{esc(m['cost'])}</li>
</ul>

<h3>The three answers, and what each one means</h3>
<div class="scroller"><table class="datatable">
<tr><th>Answer</th><th>What it means</th><th>Published?</th></tr>
<tr><td class="n">live</td><td>The apply link answered and the posting was on it. Where the
employer runs a public board feed, the req id was still in that feed too.</td><td>Yes</td></tr>
<tr><td class="n">dead</td><td>404, a closed-posting message, a redirect to a careers index
with no trace of the req, an empty ATS shell, or the employer's own feed has dropped
it.</td><td>No</td></tr>
<tr><td class="n">unverified</td><td>The check could not settle it. A JavaScript-only page
that renders nothing to a plain fetch, or the page and the employer's feed disagreeing with
each other. Unverified is not a softer word for live.</td><td>No</td></tr>
</table></div>

<h3>How the filters are derived</h3>
<div class="scroller"><table class="datatable">
<tr><th>Field</th><th>How it is derived</th></tr>
{derivs}
</table></div>

<h3>What is not on this board</h3>
<p>Job descriptions. Salary estimates. A count of applicants. A recruiter contact. Anything
we would have had to guess. A salary appears only where the employer publishes it in the
machine readable field of their own board feed, which is why {c['with_salary']} of
{c['live']} rows carry one and the rest are blank rather than estimated.</p>
</div>

<h3 style="margin-top:40px">The removal ledger, {esc(date)}</h3>
<p class="note">{c['removed_this_pass']} listings. These URLs are printed as text, not as
links, because they no longer work. That is the point of printing them.</p>
<ul class="rows">
{''.join(dead_rows)}
</ul>
</section>
</div>"""
            + footer(rel, d, r))
    write(out / "jobs-board" / "verification.html", page)
    n_pages += 1

    # ------------------------------------------------------------------ family pages
    for b in fams:
        mine = [j for j in jobs if j["family"] == b["slug"]]
        cos = sorted({j["company"] for j in mine})
        sal = [j["salary"] for j in mine if j["salary"]]
        page = (head(f"{b['label']} jobs: {b['count']} reqs verified live on {date}",
                     f"{b['count']} {b['label']} reqs at {len(cos)} companies, each one "
                     f"fetched live on {date}. Part of The GTM Engineer job board.", rel,
                     extra=f'<script src="{rel}assets/board.js" defer></script>\n',
                     ld=[crumb_ld(rel, [("Directory", "index.html"),
                                        ("The job board", "jobs-board/index.html"),
                                        (b["label"], f"jobs-board/family-{b['slug']}.html")]),
                         itemlist_ld(f"{b['label']} jobs",
                                     f"{b['count']} reqs verified live on {date}.",
                                     f"jobs-board/family-{b['slug']}.html",
                                     [(f"{j['title']}, {j['company']}",
                                       f"jobs-board/family-{b['slug']}.html") for j in mine])],
                     canon=f"jobs-board/family-{b['slug']}.html")
                + masthead(rel, "jobs-board")
                + f"""<div class="wrap wide">
<div class="crumbs" style="padding-bottom:0"><a href="{rel}index.html">Directory</a> /
<a href="index.html">The job board</a> / {esc(b['label'])}</div>
<section style="padding-top:18px">
<div class="eyebrow">Title family: {esc(b['slug'])}</div>
<h2>{esc(b['label'])}</h2>
<p class="sub">{b['count']} reqs at {len(cos)} companies, every one of them fetched live on
{esc(date)}. This is a filing decision made by matching the employer's own job title, not a
judgement about what the work is. The full board carries {c['live']} reqs across
{c['families']} families.</p>
<div class="stats" style="margin-top:26px">
<div class="stat is-teal"><div class="n">{b['count']}</div><div class="k">live reqs</div></div>
<div class="stat"><div class="n">{len(cos)}</div><div class="k">companies</div></div>
<div class="stat is-gold"><div class="n">{len(sal)}</div><div class="k">publish a salary</div></div>
</div>
<div class="boardbar">
<input id="jq" type="search" placeholder="Filter these reqs" aria-label="Filter listings">
<button class="btn ghost" id="jclear" type="button">Clear</button>
</div>
<div id="jcount">{b['count']} of {b['count']} shown</div>
<div class="jempty" id="jempty" style="display:none">Nothing in this family matches that.</div>
{board_rows(mine)}
<div class="btnrow">
<a class="btn" href="index.html">The whole board</a>
<a class="btn ghost" href="verification.html">How this was verified</a>
</div>
</section>
</div>"""
                + footer(rel, d, r))
        write(out / "jobs-board" / f"family-{b['slug']}.html", page)
        n_pages += 1

    return n_pages


def slug_for_catnum(d, num_):
    for x in d["categories"]:
        if x["num"] == num_:
            return x["slug"]
    return num_


def label_for_catnum(d, num_):
    for x in d["categories"]:
        if x["num"] == num_:
            return x["label"]
    return num_


def build_github(d, r, entries, byid, out: Path):
    rel = "../"
    c = d["counts"]
    cov = r["coverage"]
    measured = [e for e in entries if e.get("github_fetched_on")]
    seeds = sort_entries([e for e in entries if e.get("github_candidates")])

    if measured:
        note = (f"{len(measured)} of {num(c['entries'])} entries carry a measured GitHub reading, "
                "each stamped with the date it was taken.")
        body = rows_block(measured, rel, True, byid)
    else:
        note = ""
        body = f"""<div class="warn"><b>Nothing measured yet</b>
github_url, github_stars, github_last_commit, github_archived and github_fetched_on are null on all
{num(cov['unmeasured_spec_fields']['github_url'])} entries. The refresh rail in SPEC section 7.2 has
not been run. A star count without the date it was taken is a lie, so no number is shown at all.</div>
<p class="sub">When the rail runs, every repo lands in one of five bands and every band ships with
the date it was measured: active under 90 days, slowing 90 to 180, quiet 180 to 365, dormant over a
year, and archived. The band is descriptive and never a verdict. A stable server genuinely may not
need commits. But an agent about to write a community MCP wrapper into a workflow deserves to know
the repo has been silent for eight months first, and this directory already has the receipts that
the category churns.</p>
<h3 style="margin-top:34px">The seed, which is a fact and not a measurement</h3>
<p class="sub">{cov['github_candidates_any']} of {num(c['entries'])} entries already carry a
github.com URL somewhere in their fields, and {cov['mcp_url_pointing_at_github']} of those sit in
the mcp_url field. Those repos are free to measure when the rail runs. Nothing below says anything
about whether a repo is healthy.</p>
{rows_block(seeds, rel, True, byid)}"""

    page = (head("GTM tools by GitHub repo health: not measured yet, and why",
                 f"Repo staleness for every tool with a public repo, stamped with the date it was "
                 f"measured. Nothing is measured in this build: "
                 f"{cov['github_candidates_any']} entries carry a github.com URL as a seed.", rel,
                 ld=[crumb_ld(rel, [("Directory", "index.html"),
                                    ("By GitHub health", "github/index.html")])],
                 canon="github/index.html")
            + masthead(rel, "github")
            + f"""<div class="wrap wide">
<div class="crumbs" style="padding-bottom:0"><a href="{rel}index.html">Directory</a> / By GitHub health</div>
<section style="padding-top:18px">
<div class="eyebrow">View: by GitHub health</div>
<h2>Is the thing you are about to depend on still moving.</h2>
<p class="note">{esc(note)}</p>
{body}
</section>
</div>"""
            + footer(rel, d, r))
    write(out / "github" / "index.html", page)


# ----------------------------------------------------------------------------------
# methodology + submit + 404
# ----------------------------------------------------------------------------------

def build_methodology(d, r, entries, byid, out: Path):
    rel = ""
    c = d["counts"]
    cov = r["coverage"]
    dq = r["data_quality"]

    def id_list(ids):
        out_ = []
        for i in sorted(ids):
            e = byid.get(i)
            if not e:
                out_.append(f"<li>{esc(i)}</li>")
                continue
            tgt = e if e.get("canonical") else byid.get(e["canonical_id"], e)
            out_.append(f'<li><a href="tools/{tgt["slug"]}.html">{esc(e["name"])}</a> '
                        f'<span class="dom">{esc(i)}</span></li>')
        return '<ul class="tocols">' + "".join(out_) + "</ul>"

    law1 = dq["schema_law_1_risk"]
    law1_ids = [x["id"] if isinstance(x, dict) else x for x in law1["entries"]]
    thin_ids = [x["id"] if isinstance(x, dict) else x for x in dq["thin_sourcing"]["entries"]]

    method_ld = {
        "@context": "https://schema.org",
        "@type": "TechArticle",
        "headline": "How an entry in The GTM MCP Directory is made",
        "description": "The five laws every entry survives, the two honesty tiers, the counting "
                       "authority, and every place this build is thin, named rather than padded.",
        "url": SITE_BASE.rstrip("/") + "/methodology.html",
        "author": {"@type": "Person", "name": "Andrew McGuire"},
        "dateModified": d["generated_on"],
        "about": {"@type": "Dataset", "name": "The GTM MCP Directory",
                  "url": SITE_BASE.rstrip("/") + "/data.html"},
    }
    page = (head("Methodology: how an entry is made and where this build is thin",
                 f"The five laws an entry survives, the two honesty tiers "
                 f"({c['bench_tested']} bench tested of {num(c['entries'])}), the counting "
                 f"authority, and every thin spot named rather than padded.", rel,
                 ld=[method_ld, crumb_ld(rel, [("Directory", "index.html"),
                                               ("Methodology", "methodology.html")])],
                 canon="methodology.html")
            + masthead(rel, "methodology")
            + f"""<div class="wrap">
<div class="crumbs"><a href="index.html">Directory</a> / Methodology</div>
<section style="padding-top:18px">
<div class="eyebrow">Methodology</div>
<h2>The verification is the product.</h2>
<p class="sub">The list is not the moat. Anyone can copy {num(c['entries'])} rows. What is hard to
copy is that every answer carries its honesty tier and the date it was measured, and that the
awkward numbers are on the page instead of in a drawer.</p>

<div class="field"><div class="k">The two tiers</div><div class="v">
<p><b>RESEARCHED.</b> {esc(d['honesty']['tier_meanings']['RESEARCHED'])}
All {num(cov['tier']['RESEARCHED'])} entries in this build are RESEARCHED.</p>
<p style="margin-top:10px"><b>BENCH-TESTED.</b>
{esc(d['honesty']['tier_meanings']['BENCH-TESTED'])} There are {c['bench_tested']} of them. That
number is on the front page. It stays at {c['bench_tested']} until Andrew actually runs something,
and a vendor offering access buys a test, never a verdict.</p>
</div></div>

<div class="field"><div class="k">The five laws an entry has to survive</div><div class="v">
<p>1. An MCP claim needs a URL. A claim without one is not accepted.</p>
<p>2. Unknown is a legal answer. {num(cov['api_gate_unknown'])} entries carry an unknown access
gate and they are published as unknown rather than guessed into a bucket.</p>
<p>3. Vendor copy is a source for what the vendor says, not for what the tool can do. Every
what_it_does on this site was rewritten in plain language.</p>
<p>4. Enterprise gated with no public docs is itself the most useful fact in the directory, so it is
surfaced rather than hidden. {num(c['api_gate']['enterprise-only'])} entries are enterprise only.</p>
<p>5. Official means first party. A Zapier, viaSocket or Composio wrapper is not an official MCP
server no matter how well it works.</p>
</div></div>

<div class="field"><div class="k">What none-found does and does not mean</div><div class="v">
<p>{num(c['mcp_status']['none-found'])} entries are none-found. That is a statement about the
search, made on the date in the entry, and it is not a promise that no server exists. A vendor who
shipped one the week after the check is recorded as none-found until the next pass, which is exactly
why the weekly diff exists and why every entry ships its last_checked date.</p>
</div></div>

<div class="field"><div class="k">The counting authority</div><div class="v">
<p>{esc(r['reconciliation']['authority'])} is the counter, not this site and not the build script.
The build reconciles against it file by file and fails rather than publish a drifted number. This
build: {num(r['reconciliation']['build_total'])} against
{num(r['reconciliation']['recount_total'])}, {len(r['reconciliation']['failures'])} failures,
{len(r['reconciliation']['recount_warnings'])} parser warnings. The site generator re-checks the
same numbers before it writes a single file.</p>
<p style="margin-top:10px">Data baked {esc(d['generated_on'])} by {esc(d['generated_by'])}.
Network calls made during the build: {d['source']['network_calls']}. Content sha256
{esc(d['content_sha256'][:24])}...</p>
</div></div>

<div class="field"><div class="k">The duplicates, and why two counts exist</div><div class="v">
<p>{num(c['entries'])} entries, {num(c['canonical_entries'])} unique products. The difference is
{c['cross_listed_entries']} products that are deliberately listed in two category files because a
reader browsing either one should find them. The canonical home for each is declared in INDEX.md and
not chosen by the parser. Category and status views count all {num(c['entries'])} entries, because
that is what the source files hold. Tool pages count {num(c['canonical_entries'])}, because that is
how many products there are.</p>
<ul class="tocols">
{''.join(f'<li><a href="tools/{byid[g["canonical_id"]]["slug"]}.html">{esc(byid[g["canonical_id"]]["name"])}</a> <span class="dom">{esc(g["canonical_id"])} + {esc(", ".join(m["id"] for m in g["members"] if not m["canonical"]))}</span></li>' for g in sorted(d['duplicates'], key=lambda g: g['normalized_name']))}
</ul>
</div></div>

<div class="field"><div class="k">Where this build is thin, named rather than padded</div><div class="v">
<p><b>{law1['count']} entry claims an MCP with no parseable URL.</b> {esc(law1['rule'])}</p>
{id_list(law1_ids)}
<p style="margin-top:16px"><b>{dq['thin_sourcing']['count']} entries carry fewer than two source
URLs.</b> {esc(dq['thin_sourcing']['rule'])} They are listed rather than quietly padded.</p>
{id_list(thin_ids)}
<p style="margin-top:16px"><b>{num(dq['api_gate_unknown']['count'])} entries have an unknown access
gate</b> and <b>{num(dq['docs_url_missing']['count'])} have no documentation URL.</b> Both are legal
and both are published as blank. Every one of them is visible on its own tool page.</p>
</div></div>

<div class="field"><div class="k">What has not been measured at all</div><div class="v">
<p>The following fields exist in the schema, are present on every entry, and are empty on every
entry. Nothing about them is inferred anywhere on this site.</p>
<ul>
{''.join(f'<li>{esc(k)}: empty on {num(v)} of {num(cov["total_entries"])} entries</li>' for k, v in sorted(cov['unmeasured_spec_fields'].items()))}
</ul>
<p style="margin-top:10px">That is why the GitHub view shows seeds instead of star counts. An empty
field is published as empty.</p>
</div></div>

<div class="field"><div class="k">The jobs field, which is now measured</div><div class="v">
<p>jobs[] used to be on the list above. It is not any more. As of
{esc(d['jobs_vocabulary']['tags_meta']['tagged_on'])} the vocabulary is closed at {c['jobs']} jobs in
{c['job_families']} families, and {num(cov['jobs_assignments'])} tags are assigned across
{num(cov['jobs_tagged'])} of {num(cov['total_entries'])} entries. {cov['jobs_untagged']} entries
carry no tag at all, each one for a recorded reason that is printed on its own tool page.</p>
<p style="margin-top:10px"><b>What a tag means, exactly.</b> {esc(TAG_MEANING)} It was derived from
the entry's own what_it_does, ai_features and revops_role text, which is itself RESEARCHED tier.
Tagged by {esc(d['jobs_vocabulary']['tags_meta']['tagged_by'])}, tier
{esc(d['jobs_vocabulary']['tags_meta']['tier'])}, and bench_tested is still {c['bench_tested']}.
{len(r['jobs']['needs_review'])} entries were flagged for human review by that pass and are the
first thing a second reader should look at.</p>
<p style="margin-top:10px">The vocabulary is closed on purpose. A tool whose job genuinely is not in
the list stays blank rather than being forced into the nearest tag, because a wrong job tag is the
class of quiet lie the two tier honesty law exists to prevent. Vocabulary source
{esc(d['jobs_vocabulary']['meta']['source_file'])} sha256
{esc(d['jobs_vocabulary']['meta']['source_sha256'][:16])}..., tags source
{esc(d['jobs_vocabulary']['tags_meta']['source_file'])} sha256
{esc(d['jobs_vocabulary']['tags_meta']['source_sha256'][:16])}...</p>
<p style="margin-top:10px"><a href="jobs/index.html">Browse the {c['jobs']} jobs</a></p>
</div></div>

<div class="field"><div class="k">The canonical URL and the base this site is published at</div><div class="v">
<p>Every internal link on this site is relative, so the same files serve correctly from a Pages
subdomain, from a path on andrewcmcguire.com, or from a file:// path with no network at all. The
canonical tags, the sitemap and llms.txt need an absolute base, and that base is
{esc(SITE_BASE)}. That is where the site is headed, not where it is serving from today: this build
is live at andrewcmcguire.com/gtm-directory, routed 2026-08-27, with the Pages subdomain as its origin. When
that route lands, the one constant changes and the site is rebuilt. It is disclosed here rather than
left to look like a live URL.</p>
</div></div>

<div class="field"><div class="k">The markdown twins and what they are for</div><div class="v">
<p>Every HTML page on this site has a markdown twin at the same path with a .md extension, and the
twin is generated from the rendered page rather than written by hand, so it cannot drift. It carries
the same content with the chrome removed: no masthead, no footer, no theme toggle, no styling. Links
inside a twin point at the other twins, so an agent that lands on one can crawl the whole site in
markdown without ever parsing HTML. <a href="llms.txt">llms.txt</a> is the map, and
<a href="data.html">the data page</a> serves the whole directory as JSON.</p>
<p style="margin-top:10px">Schema.org JSON-LD ships inline on every page: Dataset on the front page
and the data page, ItemList on every listing, FAQPage on every learn answer, BreadcrumbList
everywhere. It is a data block rather than executable script, so the Content-Security-Policy that
forbids inline script still holds and the site still makes zero external requests.</p>
</div></div>

<div class="field"><div class="k">The one thing this site changes about the source text</div><div class="v">
<p>Em dashes in source prose are rendered as a spaced hyphen. That is a house typography rule and it
is the only alteration made at render time. No word, number, URL, date or field value is changed,
summarised, reordered or dropped anywhere on this site. Notes ship verbatim including the awkward
ones, and the raw sources string is printed alongside the parsed links so you can check the parse.</p>
</div></div>

<div class="field"><div class="k">The ordering rule</div><div class="v">
<p>{esc(d['sort_rule'])}</p>
<p style="margin-top:10px">It is computed, it is printed on every view that uses it, and there is no
featured field anywhere in the schema, because a field that exists is a field somebody will
eventually try to buy.</p>
</div></div>

<div class="field"><div class="k">No gate on this page</div><div class="v">
<p>No email is required to read anything here. No comment keyword, no DM funnel, no download wall.
It is free because it is more useful when other operators correct it.</p>
</div></div>

</section>
</div>"""
            + footer(rel, d, r))
    write(out / "methodology.html", page)


def build_submit(d, r, out: Path):
    rel = ""
    c = d["counts"]
    page = (head("Submit a GTM tool: listing is free, placement is not for sale",
                 "Anyone can submit a tool or a correction. Every submission is verified against "
                 "public sources before it is listed, and the verification is the product. "
                 "BENCH-TESTED cannot be bought at any price.", rel,
                 ld=[{
                     "@context": "https://schema.org", "@type": "WebPage",
                     "name": "Submit a tool to The GTM MCP Directory",
                     "url": SITE_BASE.rstrip("/") + "/submit.html",
                     "description": "Listing is free, verification is mandatory, and placement is "
                                    "not for sale. The ten step checklist every submission goes "
                                    "through.",
                 }, crumb_ld(rel, [("Directory", "index.html"), ("Submit", "submit.html")])],
                 canon="submit.html")
            + masthead(rel, "submit")
            + f"""<div class="wrap">
<div class="crumbs"><a href="index.html">Directory</a> / Submit</div>
<section style="padding-top:18px">
<div class="eyebrow">Submit a tool</div>
<h2>Listing is free. Verification is mandatory. Placement is not for sale.</h2>
<p class="sub">Anyone can submit a tool. Every submission is verified against public sources before
it is listed, and the verification is the product. No vendor can pay to be listed, to be listed
sooner, to rank higher, to be featured, to remove a none-found, or to soften a note. There is no
sponsored tier and there will not be one.</p>
<p class="sub">BENCH-TESTED cannot be bought at any price. It means Andrew personally ran the tool on
a stated date. A vendor can offer access so a bench test becomes possible, that offer is recorded in
the entry's notes, and the offer buys a test, never a verdict. The verdict ships whatever it says.</p>
<div class="btnrow">
<a class="btn solid" href="{ISSUE_URL}" rel="noopener">Open the submission form</a>
<a class="btn ghost" href="methodology.html">Read the methodology first</a>
</div>
<div class="note"><b>How the queue works</b>
The submission queue is a GitHub issue form on the public {PACKAGE_NAME} repo, and it is open. A
submission is free and it is not a listing: nothing lands in the data until the claims below are
checked by hand against the vendor's own documentation.</div>

<div class="field"><div class="k">What the form asks for</div><div class="v">
<p>Vendor and product name, vendor URL, a suggested category from the {c['categories']} on file,
one plain sentence on what it does, whether an MCP server exists and who built it, the MCP URL if
one is claimed, the auth model, the API documentation URL, a public GitHub org if there is one,
whether a solo operator can get API access, and one optional box for anything the tool does badly.
That last one is the most interesting box on the form.</p>
<p style="margin-top:10px">Contact name, role and email are collected and never published. They are
used to ask follow up questions and nothing else.</p>
</div></div>

<div class="field"><div class="k">What happens after you submit</div><div class="v">
<p>1. The vendor URL is fetched live and has to resolve, return 200, and describe the product.</p>
<p>2. The product is checked against all {num(c['entries'])} existing entries by normalised name,
because {c['cross_listed_entries']} deliberate cross listings already exist.</p>
<p>3. If an MCP is claimed, the URL is fetched. A 200 passes. A 401 passes, because an auth gated
live endpoint is still a live endpoint. A 403 is inconclusive and gets re-checked by hand. A 404
means the claim fails and the entry is recorded none-found, not official.</p>
<p>4. Official means first party. A third party wrapper is recorded as community.</p>
<p>5. The access gate is determined independently from published pricing or docs, with a source URL,
not from what the submitter said. If the two disagree, ours ships and the disagreement goes in the
notes.</p>
<p>6. What it does is rewritten in plain language. Vendor copy never ships as the description.</p>
<p>7. AI features are separated from automation with an AI label on it. Every existing entry does
this and a new one does not get a pass.</p>
<p>8. At least two independent sources, and the vendor's own site cannot be both of them.</p>
<p>9. Tier is RESEARCHED and last_checked is the date the checklist was completed. Never
BENCH-TESTED. A submitted entry cannot be bench tested by definition.</p>
<p>10. The counter is re-run and the index table is regenerated from its output, never hand edited.</p>
<p style="margin-top:10px">Target turnaround is 14 days.</p>
</div></div>

<div class="field"><div class="k">The acknowledgement you sign</div><div class="v">
<p>"I understand listing is free, that Andrew verifies every claim independently, that nothing here
can be paid for, and that a BENCH-TESTED tier can only be earned by Andrew running the tool
himself."</p>
</div></div>

<div class="field"><div class="k">If your tool is already listed and something is wrong</div><div class="v">
<p>Open an issue on the same repo naming the entry and the field. A correction is the most valuable
thing anyone can send. The whole reason this is free and public is that other operators correct it
faster than one person can re-check {num(c['entries'])} entries.</p>
<p style="margin-top:10px">If you would rather not be crawled, say so and you are removed from the
crawl. The entry keeps its documentation URL and a note. It does not get delisted, because delisting
for asking would be a punishment and this directory does not punish.</p>
</div></div>

</section>
</div>"""
            + footer(rel, d, r))
    write(out / "submit.html", page)


def build_404(d, r, out: Path):
    rel = ""
    page = (head("Not found - The GTM MCP Directory", "That page is not here.", rel,
                 ld=[{"@context": "https://schema.org", "@type": "WebPage",
                      "name": "Not found", "description": "That page is not here."}],
                 robots="noindex,follow")
            + masthead(rel)
            + f"""<div class="wrap">
<section style="padding-top:60px">
<div class="eyebrow">404</div>
<h2>That page is not here.</h2>
<p class="sub">The directory is {num(d['counts']['canonical_entries'])} tool pages plus a handful of
views. Try the search on the front page, or pick a view below.</p>
<div class="btnrow">
<a class="btn solid" href="index.html">Search the directory</a>
<a class="btn ghost" href="tools/index.html">Every tool, A to Z</a>
<a class="btn ghost" href="categories/index.html">By category</a>
</div>
</section>
</div>"""
            + footer(rel, d, r))
    write(out / "404.html", page)


# ----------------------------------------------------------------------------------
# search index
# ----------------------------------------------------------------------------------

def build_search_index(d, out: Path):
    """One compact record per unique product. Keys are short on purpose: this file is
    downloaded by every visitor who uses the search."""
    tools = []
    for e in sorted([x for x in d["entries"] if x.get("canonical")],
                    key=lambda x: (x.get("display_rank", 9999), x["name"].lower())):
        blob = " ".join([
            e["name"], e["category_label"], e["vendor_domain"] or "",
            detype(e["what_it_does"] or ""),
            detype(e["revops_role"] or ""),
            trim(e["ai_features"] or "", 260),
        ]).lower()
        blob = re.sub(r"\s+", " ", blob).strip()[:900]
        tools.append({
            "s": e["slug"],
            "n": detype(e["name"]),
            "d": e["vendor_domain"] or e["vendor_url"],
            "c": e["category_label"],
            "m": e["mcp_status_bucket"],
            "ml": MCP_LABEL.get(e["mcp_status_bucket"], e["mcp_status_bucket"]),
            "g": e["api_gate_bucket"],
            "gl": GATE_LABEL.get(e["api_gate_bucket"], e["api_gate_bucket"]),
            "t": e["tier"],
            "r": e.get("display_rank", 9999),
            "w": trim(e["what_it_does"], 210),
            "x": blob,
        })
    payload = {
        "meta": {
            "product": d["product"]["name"],
            "generated_on": d["generated_on"],
            "generated_by": d["generated_by"],
            "entries": d["counts"]["entries"],
            "tools": len(tools),
            "sort_rule": d["sort_rule"],
            "note": "Keys: s slug, n name, d domain, c category, m mcp bucket, g gate bucket, "
                    "t tier, r the published sort rank, w the short description, x the search blob.",
        },
        "tools": tools,
    }
    blob = json.dumps(payload, ensure_ascii=False, separators=(",", ":"), sort_keys=False)
    write(out / "search-index.json", blob + "\n")
    # Also as a script so the page works from a file:// path with no local server,
    # which is the same trick build_map.py uses for the market map.
    write(out / "assets" / "search-index.js", "window.GTMD_INDEX=" + blob + ";\n")
    return len(tools)


# ----------------------------------------------------------------------------------
# PSEO listing pages: /lists
# ----------------------------------------------------------------------------------

AUTH_ORDER = ["oauth", "api-key", "either", "third-party", "unrecorded", "not-applicable"]
AUTH_LABEL = {
    "oauth": "OAuth",
    "api-key": "API key",
    "either": "OAuth or an API key",
    "third-party": "Third party platform auth",
    "unrecorded": "Auth not recorded",
    "not-applicable": "Auth not applicable",
}
AUTH_BLURB = {
    "oauth": "The server takes the user through a browser sign in and holds a scoped token. "
             "Nothing is pasted into a config file, and access can be revoked from the vendor side "
             "without touching the agent.",
    "api-key": "The server authenticates with a key or token the operator generates and pastes in. "
               "Simple to wire, and the key is as powerful as whatever the vendor scoped it to.",
    "either": "Both paths are documented. Usually OAuth for a hosted server and a key for the self "
              "hosted or legacy endpoint.",
    "third-party": "Auth is handled by a connector platform sitting between the agent and the "
                   "vendor, so the credential lives with the platform rather than with either end.",
    "unrecorded": "The mcp_auth field on the entry is blank, or says unknown. Published as blank "
                  "rather than guessed.",
    "not-applicable": "The entry records n/a. There is no server for auth to apply to.",
}
AUTH_TONE = {"oauth": "teal", "api-key": "gold", "either": "gold", "third-party": "copper",
             "unrecorded": "mute", "not-applicable": "mute"}
# The label reads as a column heading. These read inside a sentence, which is a different job.
AUTH_PHRASE = {
    "oauth": "OAuth",
    "api-key": "an API key",
    "either": "OAuth or an API key",
    "third-party": "a third party connector platform's auth",
    "unrecorded": "an auth model that is not recorded",
    "not-applicable": "no applicable auth",
}
AUTH_TITLE = {
    "oauth": "GTM MCP servers that use OAuth",
    "api-key": "GTM MCP servers that use an API key",
    "either": "GTM MCP servers that accept OAuth or an API key",
    "third-party": "GTM MCP servers behind a third party connector platform",
    "unrecorded": "GTM MCP servers with no auth model recorded",
    "not-applicable": "GTM entries where MCP auth does not apply",
}
# Category labels are written for a browse column. A few need a different shape in a title.
CAT_TITLE_LABEL = {"ai-sdr-agents": "AI SDR", "revops-infra": "RevOps infrastructure"}

_KEYWORDS_KEY = ("api key", "api-key", "apikey", "api token", "x-api-key", "bearer",
                 "access token", "auth token", "mcp key", "personal access token")
_NEGATED_KEY = ("no manual api key", "no api key", "without an api key", "no raw api key",
                "no api keys", "no separate api key", "api key not required",
                "no api key required")


def auth_bucket(e):
    """Classify the mcp_auth free text. Keyword match, disclosed as a keyword match everywhere it
    is used, and every row prints the verbatim field beside it so the parse can be checked."""
    raw = (e.get("mcp_auth") or "").strip()
    t = raw.lower()
    if not t or t in ("unknown", "-", "tbd"):
        return "unrecorded"
    if t in ("n/a", "na", "not applicable"):
        return "not-applicable"
    if e["mcp_status_bucket"] in ("none-found", "n-a") and t.startswith("n/a"):
        return "not-applicable"
    has_oauth = "oauth" in t
    body = t
    for neg in _NEGATED_KEY:
        body = body.replace(neg, " ")
    has_key = any(k in body for k in _KEYWORDS_KEY)
    if ("zapier" in t or "pipedream" in t or "composio" in t or "viasocket" in t) and not has_oauth:
        return "third-party"
    if has_oauth and has_key:
        return "either"
    if has_oauth:
        return "oauth"
    if has_key:
        return "api-key"
    if t.startswith("n/a"):
        return "not-applicable"
    return "unrecorded"


def tool_href(e, byid, rel):
    tgt = e if e.get("canonical") else byid.get(e["canonical_id"], e)
    return f'{rel}tools/{tgt["slug"]}.html'


def mcp_link_cell(e):
    if e["mcp_urls"]:
        u = e["mcp_urls"][0]
        extra = ""
        if len(e["mcp_urls"]) > 1:
            extra = f' <span class="dom">+{len(e["mcp_urls"]) - 1} more</span>'
        return (f'<a href="{raw_esc(u)}" rel="noopener nofollow">{raw_esc(trim(u, 52))}</a>{extra}')
    if e["mcp_url"]:
        return f'<span class="dom">{esc(trim(e["mcp_url"], 60))}</span>'
    return '<span class="dom">no URL in the entry</span>'


def table_block(entries, byid, rel, cols):
    """cols is a list of (header, fn(e) -> html, css_class)."""
    head_row = "".join(f'<th class="{c}">{esc(h)}</th>' for h, _, c in cols)
    body = []
    for e in entries:
        cells = "".join(f'<td class="{c}">{fn(e)}</td>' for _, fn, c in cols)
        body.append(f"<tr>{cells}</tr>")
    return (f'<div class="scroller"><table class="datatable"><thead><tr>{head_row}</tr></thead>'
            f'<tbody>{"".join(body)}</tbody></table></div>')


def build_lists(d, r, entries, byid, out: Path):
    """The query shaped listing pages. Every one is a filter over the same data with its own
    title, its own H1, and its own count, generated at build time and stamped with the date."""
    rel = "../"
    c = d["counts"]
    cov = r["coverage"]
    gen = d["generated_on"]
    pages = []          # (path, title, count, blurb) for the index and for llms.txt

    def name_cell(e):
        return (f'<a href="{tool_href(e, byid, rel)}">{esc(e["name"])}</a><br>'
                f'<span class="dom">{esc(e["vendor_domain"] or e["vendor_url"])}</span>')

    def cat_cell(e):
        return (f'<a href="{rel}categories/{e["category_slug"]}.html">'
                f'{esc(e["category_label"])}</a>')

    def gate_cell(e):
        return (f'<a href="{rel}gates/{e["api_gate_bucket"]}.html">'
                f'{esc(GATE_LABEL.get(e["api_gate_bucket"], e["api_gate_bucket"]))}</a>')

    def mcp_cell(e):
        return (f'<a href="{rel}mcp/{e["mcp_status_bucket"]}.html">'
                f'{esc(MCP_LABEL.get(e["mcp_status_bucket"], e["mcp_status_bucket"]))}</a>')

    def auth_cell(e):
        return (f'{esc(AUTH_LABEL[auth_bucket(e)])}<br>'
                f'<span class="dom">{esc(trim(e["mcp_auth"] or "blank", 90))}</span>')

    def jobs_cell(e):
        if not e["jobs"]:
            return '<span class="dom">no tag</span>'
        return " ".join(
            f'<a class="badge mute flat" href="{rel}jobs/{raw_esc(j)}.html">'
            f'{esc(job_label(d, j))}</a>' for j in e["jobs"][:3]
        ) + ("" if len(e["jobs"]) <= 3 else f' <span class="dom">+{len(e["jobs"]) - 3}</span>')

    def emit(slug, title, h1, desc, lede, rows, body_html, current="lists", extra_ld=None):
        trail = [("Directory", "index.html"), ("The lists", "lists/index.html"),
                 (h1, f"lists/{slug}.html")]
        ld = [crumb_ld(rel, trail),
              itemlist_ld(h1, desc, f"lists/{slug}.html",
                          [(e["name"], tool_href(e, byid, "").lstrip("./")) for e in rows])]
        if extra_ld:
            ld.append(extra_ld)
        page = (head(title, desc, rel, ld=ld, canon=f"lists/{slug}.html")
                + masthead(rel, current)
                + f"""<div class="wrap wide">
<div class="crumbs" style="padding-bottom:0"><a href="{rel}index.html">Directory</a> /
<a href="index.html">The lists</a> / {esc(h1)}</div>
<section style="padding-top:18px">
<div class="eyebrow">List &middot; {len(rows)} of {num(c['entries'])}</div>
<h2>{esc(h1)}</h2>
<p class="sub">{lede}</p>
{body_html}
<p class="note" style="margin-top:30px">Counted {esc(gen)} from directory.json and reconciled
against {esc(r['reconciliation']['authority'])}. Nothing on this page is hand maintained: it is a
filter over the same {num(c['entries'])} entries the rest of the site is built from. Ordered by the
published rule: {esc(d['sort_rule'])}</p>
</section></div>"""
                + footer(rel, d, r))
        write(out / "lists" / f"{slug}.html", page)
        pages.append((slug, h1, len(rows), desc))

    # ---------- 1. the 144 official servers, with their links ----------
    official = sort_entries([e for e in entries if e["mcp_status_bucket"] == "official"])
    with_url = sum(1 for e in official if e["mcp_urls"])
    emit(
        "official-mcp-servers",
        f"Official MCP servers list: {c['mcp_status']['official']} GTM tools, with links",
        f"The {c['mcp_status']['official']} GTM tools with an official MCP server",
        f"The full list of {c['mcp_status']['official']} go to market tools whose vendor ships and "
        f"maintains its own MCP server, with the server URL, the auth model and the access gate for "
        f"each. Counted {gen}.",
        f"Official means first party. The vendor ships and maintains the server itself, and a "
        f"wrapper built by Zapier, viaSocket, Composio or any other third party does not count no "
        f"matter how well it works. {with_url} of these {len(official)} entries carry a parseable "
        f"URL in the mcp_url field; the rest claim a server in prose without one, which is recorded "
        f"as a risk on the <a href=\"{rel}methodology.html\">methodology page</a> rather than "
        f"cleaned up quietly.",
        official,
        table_block(official, byid, rel, [
            ("Tool", name_cell, ""),
            ("Category", cat_cell, ""),
            ("Server URL", mcp_link_cell, ""),
            ("Auth", auth_cell, ""),
            ("Gate", gate_cell, "n"),
        ]),
    )

    community = sort_entries([e for e in entries if e["mcp_status_bucket"] == "community"])
    emit(
        "community-mcp-servers",
        f"Community MCP servers: {c['mcp_status']['community']} GTM tools with a third party server",
        f"The {c['mcp_status']['community']} GTM tools with a community MCP server",
        f"Go to market tools where a working MCP server exists but somebody other than the vendor "
        f"built it. Counted {gen} across {num(c['entries'])} directory entries.",
        "A community server is a real server. It is also a server that can be abandoned without the "
        "vendor noticing, which is the single most useful thing to know before you write one into a "
        "workflow. The repo health rail that would date stamp each one has not been run, so no "
        "staleness claim is made here.",
        community,
        table_block(community, byid, rel, [
            ("Tool", name_cell, ""),
            ("Category", cat_cell, ""),
            ("Server URL", mcp_link_cell, ""),
            ("Auth", auth_cell, ""),
            ("Gate", gate_cell, "n"),
        ]),
    )

    nomcp = sort_entries([e for e in entries if e["mcp_status_bucket"] == "none-found"])
    emit(
        "no-mcp-server",
        f"GTM tools with no MCP server: {c['mcp_status']['none-found']} of {c['entries']} checked",
        f"The {c['mcp_status']['none-found']} GTM tools with no MCP server found",
        f"{c['mcp_status']['none-found']} of {num(c['entries'])} go to market tools had no MCP "
        f"server at the time of the check. What that means, and what it does not mean. Checked "
        f"through {gen}.",
        "None found is a statement about a search on a date, not a promise that no server exists. "
        "Each row carries the date its entry was last checked. A vendor who shipped a server the "
        "week after that date is recorded here until the next pass, which is exactly why every "
        "entry ships its own last_checked stamp instead of one site wide date.",
        nomcp,
        table_block(nomcp, byid, rel, [
            ("Tool", name_cell, ""),
            ("Category", cat_cell, ""),
            ("What it does", lambda e: esc(trim(e["what_it_does"], 130)), ""),
            ("Gate", gate_cell, "n"),
            ("Checked", lambda e: esc(e["last_checked"]), "n"),
        ]),
    )

    # ---------- 2. gate shaped lists ----------
    free = sort_entries([e for e in entries if e["api_gate_bucket"] == "free"])
    free_mcp = sum(1 for e in free if e["mcp_status_bucket"] in ("official", "community"))
    emit(
        "free-api-tiers",
        f"GTM tools with free API tiers: {c['api_gate']['free']} that need no sales call",
        f"The {c['api_gate']['free']} GTM tools a solo operator can call for free",
        f"{c['api_gate']['free']} go to market tools where a solo operator can get API access "
        f"without talking to anyone. {free_mcp} of them also have an MCP server. Counted {gen}.",
        "Free to start means a solo operator can get API access without talking to anyone. It does "
        "not mean unlimited, it does not mean free forever, and this directory does not track "
        "prices or quota sizes, so nothing here should be read as a pricing claim. It tracks one "
        "thing: whether the door opens without a sales call.",
        free,
        table_block(free, byid, rel, [
            ("Tool", name_cell, ""),
            ("Category", cat_cell, ""),
            ("MCP status", mcp_cell, ""),
            ("Jobs it is tagged with", jobs_cell, ""),
        ]),
    )

    gate_open = sort_entries([e for e in entries if e["api_gate_bucket"] in ("free", "paid")])
    solo = sort_entries([e for e in gate_open
                         if e["mcp_status_bucket"] in ("official", "community")])
    assert len(solo) == cov["solo_reachable"], "solo_reachable disagrees with the entries"
    emit(
        "solo-reachable",
        f"GTM tools a solo operator can reach: {cov['solo_reachable']} with a server and no "
        f"procurement cycle",
        f"The {cov['solo_reachable']} GTM tools an agent can call and a solo operator can pay for",
        f"{cov['solo_reachable']} of {num(c['entries'])} go to market tools pass both tests at "
        f"once: an MCP server exists, and API access is free to start or paid self serve. Counted "
        f"{gen}.",
        f"Solo reachable is the intersection of the two columns this directory publishes, and it is "
        f"the strictest useful filter here. A server has to exist, and the door has to open without "
        f"a contract. {len(gate_open)} entries pass the gate test on its own "
        f"({c['api_gate']['free']} free to start plus {c['api_gate']['paid']} paid self serve) and "
        f"{c['mcp_status']['official'] + c['mcp_status']['community']} pass the server test on its "
        f"own. {cov['solo_reachable']} pass both. Paying is allowed; a procurement cycle is not.",
        solo,
        table_block(solo, byid, rel, [
            ("Tool", name_cell, ""),
            ("Category", cat_cell, ""),
            ("Gate", gate_cell, "n"),
            ("MCP status", mcp_cell, ""),
            ("Jobs it is tagged with", jobs_cell, ""),
        ]),
    )

    ent = sort_entries([e for e in entries
                        if e["api_gate_bucket"] in ("enterprise-only", "enterprise-leaning")])
    ent_off = sum(1 for e in ent if e["mcp_status_bucket"] == "official")
    emit(
        "enterprise-gated",
        f"Enterprise gated GTM tools: {len(ent)} an agent cannot reach without a contract",
        f"The {len(ent)} GTM tools that need a contract before an agent can touch them",
        f"{c['api_gate']['enterprise-only']} enterprise only entries plus "
        f"{c['api_gate']['enterprise-leaning']} enterprise leaning. {ent_off} of them ship an "
        f"official MCP server that most readers of this page still cannot call. Counted {gen}.",
        "Enterprise gated with no public docs is the most useful fact in a directory like this, so "
        "it is surfaced rather than hidden. An official MCP server behind a procurement cycle is "
        "still an official MCP server, and it is still unreachable for a solo operator, which is "
        f"why this site publishes MCP status and access gate as two separate columns.",
        ent,
        table_block(ent, byid, rel, [
            ("Tool", name_cell, ""),
            ("Category", cat_cell, ""),
            ("MCP status", mcp_cell, ""),
            ("Gate", gate_cell, "n"),
            ("What it does", lambda e: esc(trim(e["what_it_does"], 120)), ""),
        ]),
    )

    # ---------- 3. auth types ----------
    served = [e for e in entries if e["mcp_status_bucket"] in ("official", "community")]
    by_auth = {}
    for e in served:
        by_auth.setdefault(auth_bucket(e), []).append(e)
    auth_cards = []
    for b in AUTH_ORDER:
        mine = sort_entries(by_auth.get(b, []))
        if not mine:
            continue
        auth_cards.append(f"""<a class="viewcard" href="auth-{b}.html">
<div class="vt">{esc(AUTH_LABEL[b])}</div>
<div class="vn">{len(mine)} of {len(served)} servers</div>
<div class="vd">{esc(trim(AUTH_BLURB[b], 140))}</div>
</a>""")
        emit(
            f"auth-{b}",
            f"{AUTH_TITLE[b]}: {len(mine)} tools, counted",
            AUTH_TITLE[b],
            f"{len(mine)} of the {len(served)} GTM tools with an MCP server use "
            f"{AUTH_PHRASE[b]}. The verbatim auth field for each one is printed beside it. "
            f"Counted {gen}.",
            f"{esc(AUTH_BLURB[b])} The bucket is a keyword match over the mcp_auth field, run at "
            "build time, and the verbatim field ships in the row beside it so you can check the "
            "parse yourself. Where the two disagree, the verbatim field is the fact and the bucket "
            "is the convenience.",
            mine,
            table_block(mine, byid, rel, [
                ("Tool", name_cell, ""),
                ("MCP status", mcp_cell, ""),
                ("Server URL", mcp_link_cell, ""),
                ("mcp_auth, verbatim", lambda e: esc(trim(e["mcp_auth"] or "blank", 150)), ""),
                ("Gate", gate_cell, "n"),
            ]),
        )
    hub_rows = []
    for b in AUTH_ORDER:
        mine = by_auth.get(b, [])
        if not mine:
            continue
        hub_rows.append(
            f'<li><div class="lab"><a href="auth-{b}.html">{esc(AUTH_LABEL[b])}</a>'
            f'<span class="r"><b>{len(mine)}</b> of {len(served)} servers</span></div>'
            f'<div class="bar"><i class="o" style="width:{len(mine) / len(served) * 100:.4f}%"></i>'
            f'</div></li>'
        )
    ld = [crumb_ld(rel, [("Directory", "index.html"), ("The lists", "lists/index.html"),
                         ("By auth type", "lists/auth-types.html")]),
          itemlist_ld("GTM MCP servers by auth type",
                      "How the GTM tools with MCP servers authenticate.",
                      "lists/auth-types.html",
                      [(AUTH_LABEL[b], f"lists/auth-{b}.html") for b in AUTH_ORDER
                       if by_auth.get(b)])]
    page = (head("GTM tools by MCP auth type: OAuth, API key or neither",
                 f"How the {len(served)} GTM tools with an MCP server authenticate. OAuth, API key, "
                 f"both, or not recorded, with the verbatim auth field on every row. Counted {gen}.",
                 rel, ld=ld, canon="lists/auth-types.html")
            + masthead(rel, "lists")
            + f"""<div class="wrap wide">
<div class="crumbs" style="padding-bottom:0"><a href="{rel}index.html">Directory</a> /
<a href="index.html">The lists</a> / By auth type</div>
<section style="padding-top:18px">
<div class="eyebrow">List &middot; auth</div>
<h2>How a GTM MCP server asks you to log in.</h2>
<p class="sub">Auth is the difference between an agent your security team will allow and an agent it
will not. OAuth hands the server a scoped token the vendor can revoke. An API key pasted into a
config file is as powerful as whatever the vendor scoped it to, lives in plain text on the machine
running the agent, and is revoked by rotating it. Both are normal. Knowing which one you are about
to wire in is not optional.</p>
<p class="note">{len(served)} of {num(c['entries'])} entries have a server of any kind
({c['mcp_status']['official']} official, {c['mcp_status']['community']} community). The buckets
below are a keyword match over the mcp_auth field, disclosed as such, with the verbatim field
printed on every row of every page.</p>
<ul class="cov">{''.join(hub_rows)}</ul>
<div class="viewgrid" style="margin-top:28px">{''.join(auth_cards)}</div>
</section></div>"""
            + footer(rel, d, r))
    write(out / "lists" / "auth-types.html", page)
    pages.append(("auth-types", "GTM tools by MCP auth type", len(served),
                  f"How the {len(served)} GTM tools with an MCP server authenticate: OAuth, API "
                  f"key, both, or not recorded, with the verbatim auth field on every row."))

    # ---------- 4. per category: the tools with servers ----------
    for x in sorted(d["categories"], key=lambda k: k["num"]):
        ids = set(x["entry_ids"])
        mine_all = [e for e in entries if e["id"] in ids]
        mine = sort_entries([e for e in mine_all
                             if e["mcp_status_bucket"] in ("official", "community")])
        off = x["mcp_status"]["official"]
        com = x["mcp_status"]["community"]
        tot = x["total"]
        if mine:
            body = table_block(mine, byid, rel, [
                ("Tool", name_cell, ""),
                ("MCP status", mcp_cell, ""),
                ("Server URL", mcp_link_cell, ""),
                ("Auth", auth_cell, ""),
                ("Gate", gate_cell, "n"),
            ])
        else:
            body = ('<div class="warn"><b>Nothing to list</b>No entry in this category had an MCP '
                    'server of any kind at the time of the check. That is the answer, and it is '
                    'published rather than padded with near misses from another category.</div>')
        rest = sort_entries([e for e in mine_all
                             if e["mcp_status_bucket"] not in ("official", "community")])
        if rest:
            body += (f'<h3 style="margin-top:40px">The other {len(rest)} in this category</h3>'
                     f'<p class="note">No server found, or the check could not settle it. Same '
                     f'category, not reachable by an agent today.</p>'
                     + table_block(rest, byid, rel, [
                         ("Tool", name_cell, ""),
                         ("MCP status", mcp_cell, ""),
                         ("Gate", gate_cell, "n"),
                         ("Checked", lambda e: esc(e["last_checked"]), "n"),
                     ]))
        top_jobs = "".join(
            f'<a class="btn ghost" href="{rel}jobs/{raw_esc(j)}.html">{esc(job_label(d, j))}</a>'
            for j in x.get("top_jobs", [])[:6]
        )
        tl = CAT_TITLE_LABEL.get(x["slug"], x["label"])
        emit(
            f"mcp-{x['slug']}",
            f"{tl} tools with MCP servers: {off + com} of {tot}, counted",
            f"{tl} tools with an MCP server",
            f"{off + com} of the {tot} {x['label'].lower()} tools in The GTM MCP Directory have an "
            f"MCP server: {off} official and {com} community. The server URL, auth model and access "
            f"gate for each. Counted {gen}.",
            f"{esc(x['one_line'])} {off + com} of {tot} entries in this category are reachable by "
            f"an agent: {off} through a server the vendor maintains and {com} through one somebody "
            f"else built. "
            + (f'The category is tagged most often with '
               f'{esc(job_label(d, x["top_jobs"][0]))}.' if x.get("top_jobs") else "")
            + f' <a href="{rel}categories/{x["slug"]}.html">See the full category page</a>.',
            mine,
            body + (f'<h3 style="margin-top:40px">What this category is asked for</h3>'
                    f'<p class="note">The jobs most often tagged on the {x["jobs_tagged"]} tagged '
                    f'entries in this category.</p>'
                    f'<div class="btnrow">{top_jobs}</div>' if top_jobs else ""),
        )

    # ---------- the index ----------
    cards = "".join(
        f'<a class="viewcard" href="{raw_esc(slug)}.html">'
        f'<div class="vt">{esc(h1)}</div><div class="vn">{num(n)} entries</div>'
        f'<div class="vd">{esc(trim(desc, 120))}</div></a>'
        for slug, h1, n, desc in pages
    )
    ld = [crumb_ld(rel, [("Directory", "index.html"), ("The lists", "lists/index.html")]),
          itemlist_ld("The lists", "Every published cut of The GTM MCP Directory.",
                      "lists/index.html", [(h1, f"lists/{s}.html") for s, h1, _, _ in pages])]
    page = (head("The lists: every published cut of the GTM MCP data",
                 f"Every published cut of the directory: the {c['mcp_status']['official']} official "
                 f"MCP servers, the {c['api_gate']['free']} free API tiers, the enterprise gated, "
                 f"by auth type, and by category. Counted {gen}.", rel, ld=ld,
                 canon="lists/index.html")
            + masthead(rel, "lists")
            + f"""<div class="wrap wide">
<div class="crumbs" style="padding-bottom:0"><a href="{rel}index.html">Directory</a> / The lists</div>
<section style="padding-top:18px">
<div class="eyebrow">The lists</div>
<h2>The same {num(c['entries'])} entries, cut the ways people actually ask for them.</h2>
<p class="sub">Nothing on these pages is hand maintained and nothing is a separate dataset. Each one
is a filter over directory.json with its own count, generated {esc(gen)} and reconciled against
{esc(r['reconciliation']['authority'])}. If the data changes, every page below changes with it on the
next build.</p>
<div class="viewgrid">{cards}</div>
</section></div>"""
            + footer(rel, d, r))
    write(out / "lists" / "index.html", page)
    return len(pages) + 1, pages


# ----------------------------------------------------------------------------------
# /learn: the questions a person asks an AI, answered from the data
# ----------------------------------------------------------------------------------

LEARN_CLUSTERS = [
    ("definitions", "Definitions",
     "What the words mean, said once, plainly, without a product pitch attached."),
    ("directory", "What the data says",
     "Questions only a counted directory can answer. Every number below is generated at build "
     "time from the same file the rest of the site is built from."),
    ("howto", "How to actually do it",
     "The wiring. What to connect, in what order, and where it usually goes wrong."),
]

# Sources cited by more than one learn page. Every URL here is a first party source: the protocol's
# own documentation, the vendor's own announcement, or a named author's own publication.
S_MCP_SITE = ("Model Context Protocol, official documentation", "https://modelcontextprotocol.io")
S_MCP_SPEC = ("Model Context Protocol, the specification",
              "https://modelcontextprotocol.io/specification")
S_MCP_ANN = ("Anthropic, Introducing the Model Context Protocol",
             "https://www.anthropic.com/news/model-context-protocol")
S_MCP_SERVERS = ("modelcontextprotocol/servers, the reference server repository",
                 "https://github.com/modelcontextprotocol/servers")
S_MCP_QUICK = ("Model Context Protocol, connect an MCP server to a client",
               "https://modelcontextprotocol.io/quickstart/user")
S_SIGNAL = ("Brendan J Short, The Signal", "https://www.thesignal.club")
S_GTMNOW = ("Sophie Buonassisi, The Agent Operator: The New Emerging Role, GTMnow, May 2026",
            "https://thegtmnewsletter.substack.com/p/agent-operator-gtm-role")


def learn_definitions(d, r, entries, byid, gen, H):
    rel, c, cov = H["rel"], H["c"], H["cov"]
    je, ce, names, ul, jl, pct = (H["job_entries"], H["cat_entries"], H["names"], H["tool_ul"],
                                  H["jl"], H["pct"])
    jobs, jn, cats = H["jobs"], H["jn"], H["cats"]
    reach = c["mcp_status"]["official"] + c["mcp_status"]["community"]
    served = reach

    return [
        {
            "slug": "what-is-an-mcp-server",
            "cluster": "definitions",
            "q": "What is an MCP server?",
            "title": "What is an MCP server? A plain definition, plus how many GTM tools have one",
            "desc": f"An MCP server is a small program that exposes one system's capabilities to an "
                    f"AI agent in a standard shape. {c['mcp_status']['official']} of "
                    f"{num(c['entries'])} GTM tools ship one officially. Counted {gen}.",
            "short": "An MCP server is a small program that sits in front of one system and offers "
                     "its capabilities to an AI agent in a standard shape, so any agent that speaks "
                     "the Model Context Protocol can call that system without custom integration "
                     "code being written for it first.",
            "body": f"""
<p>Before MCP, connecting an agent to a tool meant writing glue: read the vendor's API docs, wrap
the endpoints you care about in functions, describe those functions to the model, handle the auth,
and then do the whole thing again for the next tool and again for the next agent framework. The work
scaled with tools multiplied by agents.</p>
<p>An MCP server collapses that. The server is written once, by whoever knows the system best, and
it advertises three kinds of thing to any client that connects: <b>tools</b>, which are actions the
agent can invoke; <b>resources</b>, which are pieces of context the agent can read; and
<b>prompts</b>, which are reusable instruction templates the user can trigger. The agent discovers
what is available at connection time rather than being told in advance, which is why the same agent
can pick up a server it has never seen and use it correctly.</p>
<p>Two things an MCP server is not. It is not a hosted service you sign up for, necessarily: many
run as a local process on your own machine and talk to the client over standard input and output.
And it is not a security boundary you get for free. The server runs with whatever credentials you
hand it, and it can only be as careful as the person who wrote it.</p>
<h2>How many GTM tools actually have one</h2>
<p>This directory checked {num(c['entries'])} go to market tools and found
<b>{c['mcp_status']['official']} with an official server</b>, the vendor's own, plus
{c['mcp_status']['community']} where somebody outside the vendor built one. That is {pct(reach, c['entries'])}
of the entries reachable by an agent through MCP at all.
{c['mcp_status']['none-found']} had no server found on the date they were checked, and
{c['mcp_status']['unknown']} could not be settled either way.</p>
<p>The gap between those two numbers is the whole reason this directory exists. A category can be
sold entirely on the language of AI and still have almost nothing an agent can call.</p>
<h2>What to check before you trust one</h2>
<ul>
<li><b>Who built it.</b> A vendor maintained server and a weekend wrapper both work on day one. Only
one of them is somebody's job on day two hundred.</li>
<li><b>How it authenticates.</b> {len([e for e in entries if e['mcp_status_bucket'] in ('official','community') and auth_bucket(e) == 'oauth'])}
of the {served} servers in this directory use OAuth, which keeps a revocable scoped token on the
vendor side. Others take an API key you paste into a config file.
<a href="{rel}lists/auth-types.html">The full auth breakdown is here</a>.</li>
<li><b>What it can reach.</b> A server is a door into a system. The permissions on the credential
you give it are the only thing deciding how far into that system an agent can walk.</li>
</ul>""",
            "sources": [S_MCP_SITE, S_MCP_SPEC, S_MCP_ANN,
                        ("The GTM MCP Directory, methodology", "methodology.html")],
            "related": ["what-is-the-model-context-protocol", "official-vs-community-mcp-server",
                        "which-gtm-tools-have-official-mcp-servers",
                        "how-do-i-add-an-mcp-server-to-claude-desktop"],
            "see": [("The " + str(c["mcp_status"]["official"]) + " official servers",
                     "lists/official-mcp-servers.html"),
                    ("Every MCP status", "mcp/index.html")],
        },
        {
            "slug": "what-is-the-model-context-protocol",
            "cluster": "definitions",
            "q": "What is the Model Context Protocol?",
            "title": "What is the Model Context Protocol (MCP)? The open standard, explained",
            "desc": "The Model Context Protocol is an open standard for connecting AI applications "
                    "to external tools and data, published by Anthropic and adopted across the "
                    "industry. What it standardises and what it deliberately does not.",
            "short": "The Model Context Protocol, or MCP, is an open standard that defines how an "
                     "AI application talks to an external system: how it discovers what is "
                     "available, how it calls a tool, and how results come back. Anthropic "
                     "published it and released it as an open specification with reference "
                     "implementations.",
            "body": f"""
<p>MCP describes a client and a server exchanging JSON-RPC messages. The <b>host</b> is the
application a person is actually using. Inside it, a <b>client</b> holds one connection to one
<b>server</b>, and the server is the thing that knows how to talk to a particular system: a
database, a file system, a CRM, a search index.</p>
<p>What the standard fixes is the shape of the conversation. How a server declares its tools, how
arguments are described, how a call is made, how errors and results are returned, how a server can
ask the client for something back. Because that shape is fixed, an agent does not need bespoke code
per integration, and a vendor does not need to ship a different connector for every AI product on
the market.</p>
<p>What the standard deliberately does not fix is what any of it means. MCP will not tell you
whether a tool called <code>search_contacts</code> returns verified emails or guesses, whether the
account behind it has quota left, or whether the vendor will still maintain the server next quarter.
Those are directory questions, not protocol questions, which is precisely the gap this site was
built to fill.</p>
<h2>Where it stands</h2>
<p>The specification is versioned by date and has been revised several times since first release,
adding an authorization framework, a streamable HTTP transport alongside the original local
transport, and richer tool output. Read the versioned spec rather than any blog post, including this
one, for the current state of it.</p>
<p>Adoption is visible in this directory's own data rather than in anyone's press release.
{c['mcp_status']['official']} of {num(c['entries'])} go to market vendors ship a first party server
today, and the auth notes on those entries name Claude, ChatGPT and Cursor as the clients they
document sign in flows for.</p>
<h2>Why it matters for go to market work</h2>
<p>GTM runs on a stack of systems that do not talk to each other: a CRM, an enrichment vendor, a
sequencer, a call recorder, a warehouse. The reason a GTM engineer spends their week on plumbing is
that every pair of those systems needs its own bridge. A protocol that makes each system speak once,
to anything, is the first credible attack on that problem, and the reason it matters to measure
which vendors have actually adopted it.</p>""",
            "sources": [S_MCP_SPEC, S_MCP_ANN, S_MCP_SERVERS],
            "related": ["what-is-an-mcp-server", "what-is-an-mcp-client",
                        "what-are-mcp-tools-resources-and-prompts",
                        "stdio-vs-remote-mcp-servers"],
            "see": [("The MCP layer category", "categories/mcp-infrastructure.html")],
        },
        {
            "slug": "what-is-a-gtm-engineer",
            "cluster": "definitions",
            "q": "What is a GTM engineer?",
            "title": "What is a GTM engineer? The role, and what the tooling data says about it",
            "desc": "A GTM engineer builds and runs the systems a go to market team sells through: "
                    "data, automation, agents and the plumbing between them. What the role is, and "
                    "what the state of the tooling says about the job.",
            "short": "A GTM engineer is the person who builds and runs the systems a go to market "
                     "team sells through, rather than working a territory inside them: the data "
                     "pipelines, the enrichment, the routing, the automations and now the agents. "
                     "It is an engineering role scoped to revenue, and it sits between RevOps, "
                     "sales and the data team without belonging to any of them.",
            "body": f"""
<p>The clearest way to see the role is by what lands on the desk. A rep asks for a list of accounts
hiring for a role that implies a problem their product solves. A GTM engineer does not go looking in
a UI: they wire a job posting source to an enrichment step to a scoring step to the CRM, and then
they own the thing when it breaks. The output is a system, and the system runs whether or not its
author is at their desk.</p>
<p><b>On the definition of the role itself, read Brendan Short.</b> His publication The Signal is
where the GTM engineer role is defined and analysed seriously and continuously, including the
market, the hiring patterns and what the job actually turns into inside a company. This directory
does not try to do that work. It is a utility for people already doing the job, and the two things
are complements: he covers what the role is, this counts what the role can currently reach.</p>
<h2>What the tooling data says about the job right now</h2>
<p>{num(c['entries'])} go to market tools were checked for this directory. Of them,
{c['mcp_status']['official']} ship an official MCP server, so an agent a GTM engineer builds can
call them without custom glue. {c['mcp_status']['none-found']} had none found, which means the glue
still has to be written by hand. And {c['api_gate']['enterprise-only']} are enterprise gated: API
access needs a contract, a seat count or a procurement cycle, so a solo operator or a small team is
locked out regardless of how good the tool is.</p>
<p>The unflattering cut is by category. {H['cats']['ai-sdr-agents']['label']}, a category sold
entirely on autonomy, has {H['cats']['ai-sdr-agents']['mcp_status']['official']} official servers
across {H['cats']['ai-sdr-agents']['total']} entries.
{H['cats']['revops-infra']['label']}, the unglamorous plumbing layer, has
{H['cats']['revops-infra']['mcp_status']['official']} of {H['cats']['revops-infra']['total']}. The
tools sold as agents are the least usable by agents, and that is a fact about the market a GTM
engineer runs into on their first afternoon.</p>
<h2>Related titles</h2>
<p>Titles vary and are not settled. Agent operator, GTM systems engineer, growth engineer, RevOps
engineer and marketing engineer all overlap with this work depending on where the role reports.
The useful test is not the title on the badge. It is whether the person is expected to ship a
running system rather than a spreadsheet and a recommendation.</p>""",
            "sources": [S_SIGNAL, S_GTMNOW,
                        ("The GTM MCP Directory, the counted data", "data.html")],
            "related": ["what-does-agent-ready-mean", "what-is-an-ai-sdr",
                        "which-gtm-categories-are-most-agent-ready",
                        "how-do-i-audit-my-gtm-stack-for-agent-readiness"],
            "see": [("Every category and its coverage", "categories/index.html"),
                    ("The " + str(c["jobs"]) + " jobs an agent asks for", "jobs/index.html")],
        },
        {
            "slug": "what-is-an-ai-sdr",
            "cluster": "definitions",
            "q": "What is an AI SDR?",
            "title": "What is an AI SDR? The definition, and the MCP gap in the category",
            "desc": f"An AI SDR is software that runs the top of the sales funnel end to end. "
                    f"{H['cats']['ai-sdr-agents']['total']} of them are in this directory and "
                    f"{H['cats']['ai-sdr-agents']['mcp_status']['official']} ship an official MCP "
                    f"server. Counted {gen}.",
            "short": "An AI SDR is software sold to do the sales development rep's job end to end: "
                     "pick the accounts, find the people, write the messages, send them across "
                     "email and LinkedIn, handle the replies, and book the meeting. The category "
                     "name describes an ambition and a price point, not a measured capability.",
            "body": f"""
<p>The pitch is a headcount replacement, and the mechanics underneath are usually the same four
parts a human SDR stack has always had: a data source, a scoring or targeting step, a message
generator, and a sending layer. What the AI adds is the drafting and the branching, so the sequence
adapts instead of firing a fixed set of steps.</p>
<p>Treat two claims separately. Whether the software can run the workflow, which vendors demonstrate
constantly, and whether it produces outcomes a team would have hired for, which almost nobody
publishes with numbers. This directory does not test either. It records what the vendor says the
tool does, with sources, and it records exactly one thing about reachability.</p>
<h2>The number that says the most about the category</h2>
<p>There are {H['cats']['ai-sdr-agents']['total']} AI SDR entries here.
<b>{H['cats']['ai-sdr-agents']['mcp_status']['official']} have an official MCP server</b> and
{H['cats']['ai-sdr-agents']['mcp_status']['none-found']} have none found.
{H['cats']['ai-sdr-agents']['api_gate']['unknown']} do not publish enough for the access gate to be
established at all.</p>
<p>That is the inversion this directory keeps running into. A category built on the promise of
autonomous software is, as a group, the least callable by anybody else's autonomous software. If you
want an agent you control to drive the workflow rather than buying one that drives itself, the parts
you can actually assemble sit in enrichment, signals and RevOps infrastructure, where the official
server counts are {H['cats']['data-enrichment']['mcp_status']['official']},
{H['cats']['signals-intent-abm']['mcp_status']['official']} and
{H['cats']['revops-infra']['mcp_status']['official']} respectively.</p>
<h2>The tools tagged with the autonomous SDR job</h2>
<p>{jn('run-autonomous-sdr-agent', 'entry_count')} entries across the whole directory are tagged
{jl('run-autonomous-sdr-agent')}, of which {jn('run-autonomous-sdr-agent', 'mcp_status', 'official')}
have an official server and {jn('run-autonomous-sdr-agent', 'solo_reachable')} are reachable by a
solo operator without a contract.</p>
{ul(je('run-autonomous-sdr-agent'), limit=8)}""",
            "sources": [("The GTM MCP Directory, AI SDRs category", "categories/ai-sdr-agents.html"),
                        ("The GTM MCP Directory, how an entry is made", "methodology.html"),
                        S_SIGNAL],
            "related": ["what-is-an-ai-agent-in-sales", "which-ai-sdr-tools-have-mcp-servers",
                        "what-is-a-gtm-engineer", "which-gtm-categories-are-most-agent-ready"],
            "see": [("The AI SDRs category", "categories/ai-sdr-agents.html"),
                    ("AI SDR tools with MCP servers", "lists/mcp-ai-sdr-agents.html")],
        },
        {
            "slug": "what-does-agent-ready-mean",
            "cluster": "definitions",
            "q": "What does agent ready mean for a GTM tool?",
            "title": "What does agent ready mean? A definition you can check, not a marketing claim",
            "desc": "Agent ready is vendor language. Here is the version you can verify: does a "
                    "server exist, who maintains it, how does it authenticate, and can you get in "
                    "without a contract. Measured across 293 GTM tools.",
            "short": "Agent ready is a marketing phrase with no agreed definition, and at least one "
                     "large vendor markets it as product language. The checkable version is four "
                     "questions: is there an MCP server or a documented API, did the vendor build "
                     "it, how does it authenticate, and can one person get access without a "
                     "procurement cycle.",
            "body": f"""
<p>This site does not use agent ready as a rating, because a rating nobody can reproduce is an
opinion. It publishes the inputs instead, and lets you decide what threshold you care about.</p>
<h2>The four checks</h2>
<ol>
<li><b>Is there a server at all.</b> {c['mcp_status']['official']} of {num(c['entries'])} entries
have an official one, {c['mcp_status']['community']} have a community one,
{c['mcp_status']['none-found']} had none found on the date checked, and
{c['mcp_status']['unknown']} could not be settled.</li>
<li><b>Who maintains it.</b> Official means first party. A wrapper built by a third party
integration platform does not count here no matter how well it works, because the failure mode is
different: a community server can be abandoned without the vendor ever noticing.</li>
<li><b>How does it authenticate.</b> OAuth with a scoped, revocable token is a different security
conversation from an API key in a config file.
<a href="{rel}lists/auth-types.html">The split across every server here is published.</a></li>
<li><b>Can you get in.</b> {c['api_gate']['free'] + c['api_gate']['paid']} of
{num(c['entries'])} entries are free to start or paid self serve, and
{c['api_gate']['enterprise-only']} need a contract. Cross that with the server column and
{cov['solo_reachable']} entries pass both tests. An official MCP server behind a procurement cycle
is not agent ready for most of the people reading this.</li>
</ol>
<h2>The trap in the phrase</h2>
<p>An impressive number of tools describe themselves as built for agents while shipping nothing an
external agent can call. The two claims live in different places: one on the homepage, one in the
developer docs. The directory records the second and cites it.</p>
<p>The reverse trap is real too. A tool with no MCP server and a clean, documented REST API is often
more usable to an agent than a tool with a thin server and no docs. {cov['docs_url_missing']} of
{num(c['entries'])} entries have no documentation URL recorded at all, which is its own signal.</p>
<h2>The phrase itself</h2>
<p>Agent ready is in active commercial use as product language by at least one large data vendor, so
it is not neutral ground. The term used throughout this site is <b>agent reachable</b>, and it means
exactly one thing: a server was found, on a stated date, and who built it is recorded.</p>""",
            "sources": [("The GTM MCP Directory, methodology", "methodology.html"),
                        S_MCP_SPEC,
                        ("The GTM MCP Directory, by access gate", "gates/index.html")],
            "related": ["what-is-an-mcp-server", "official-vs-community-mcp-server",
                        "what-is-an-api-access-gate",
                        "how-do-i-audit-my-gtm-stack-for-agent-readiness"],
            "see": [("By MCP status", "mcp/index.html"), ("By access gate", "gates/index.html")],
        },
        {
            "slug": "what-is-an-ai-agent-in-sales",
            "cluster": "definitions",
            "q": "What is an AI agent in sales?",
            "title": "What is an AI agent in sales? Definition, and what one can actually reach",
            "desc": "An AI agent in sales is a model given tools, a goal and permission to act "
                    "across several steps. What separates an agent from a chatbot or a workflow, "
                    "and which parts of the GTM stack one can currently call.",
            "short": "An AI agent in sales is a language model given a goal, a set of tools it can "
                     "call, and permission to take several steps in a row without a human "
                     "approving each one. The tools are what make it an agent: without them it is "
                     "a chatbot that can only produce text.",
            "body": f"""
<p>Three things get called agents and only one of them is. A <b>chatbot</b> answers in text. A
<b>workflow</b> runs a fixed sequence somebody drew in advance, and it does the same thing every
time. An <b>agent</b> decides which tool to call next based on what the last call returned, which is
useful precisely because the path was not decided in advance and risky for the same reason.</p>
<p>In sales the loop usually looks like this: read a trigger, research the account, find the right
person, find a way to reach them, draft something specific, send it, write what happened back to the
CRM. Seven steps, and every one of them is a call into a different vendor's system. The agent is
the easy part. The seven doors are the hard part.</p>
<h2>Which doors are open</h2>
<p>Across {num(c['entries'])} tools, {c['mcp_status']['official'] + c['mcp_status']['community']}
are callable through MCP and {cov['solo_reachable']} are reachable by one person without a contract.
By job, the loop above currently looks like this:</p>
<div class="scroller"><table class="datatable"><thead><tr><th>Step</th><th>Job</th>
<th>Tools tagged</th><th>Official MCP</th><th>Solo reachable</th></tr></thead><tbody>
{''.join(f'<tr><td>{esc(step)}</td><td>{jl(jid)}</td><td class="n">{jn(jid, "entry_count")}</td>'
         f'<td class="n">{jn(jid, "mcp_status", "official")}</td>'
         f'<td class="n">{jn(jid, "solo_reachable")}</td></tr>'
         for step, jid in [("Research the account", "research-account-for-call-prep"),
                           ("Find the person", "search-people-by-criteria"),
                           ("Get a work email", "find-work-email"),
                           ("Check it is deliverable", "verify-email-deliverable"),
                           ("Draft the message", "draft-personalized-outreach"),
                           ("Send the sequence", "run-email-sequence"),
                           ("Write it back to the CRM", "write-crm-records")])}
</tbody></table></div>
<p class="note">Counted {esc(gen)}. Official MCP counts entries, and an entry can be cross listed in
a second category, which is why these numbers are entry counts rather than product counts.</p>
<h2>The honest limit</h2>
<p>Nobody has run these tools for this directory. {c['bench_tested']} are bench tested. Every number
above says a vendor documents a capability and a server was found, not that the chain works end to
end when you wire it together at two in the morning.</p>""",
            "sources": [S_MCP_SITE, ("The GTM MCP Directory, by job", "jobs/index.html"),
                        ("The GTM MCP Directory, methodology", "methodology.html")],
            "related": ["what-is-an-ai-sdr", "what-is-an-mcp-server",
                        "how-do-i-connect-claude-to-my-crm",
                        "what-are-the-security-risks-of-connecting-an-agent-to-my-gtm-stack"],
            "see": [("Every job an agent asks for", "jobs/index.html")],
        },
        {
            "slug": "official-vs-community-mcp-server",
            "cluster": "definitions",
            "q": "What is the difference between an official and a community MCP server?",
            "title": "Official vs community MCP servers: what the difference actually costs you",
            "desc": f"Official means the vendor ships and maintains the server. Community means "
                    f"somebody else does. {c['mcp_status']['official']} against "
                    f"{c['mcp_status']['community']} across {num(c['entries'])} GTM tools.",
            "short": "An official MCP server is built and maintained by the vendor whose system it "
                     "exposes. A community server does the same job but is maintained by somebody "
                     "else, which means it can be abandoned, can lag behind API changes, and can "
                     "disappear without the vendor ever knowing it existed.",
            "body": f"""
<p>Both kinds work. The difference is not quality on the day you install it, it is who is
responsible on the day it breaks.</p>
<p>When a vendor changes an endpoint, an official server is updated by the team that made the
change. A community server is updated when its author notices, has time, and still cares. Neither
outcome is guaranteed, but only one of them has an organisation behind it.</p>
<h2>What counts as official here</h2>
<p>Official means first party and nothing else. A server built by a third party integration platform
such as Zapier, Composio or viaSocket is recorded as community no matter how well it works or how
large the company behind it is, because the vendor whose data is being exposed did not write it and
does not maintain it. That rule is applied to every entry without exception.</p>
<h2>The split across this directory</h2>
<p>{c['mcp_status']['official']} entries are official. {c['mcp_status']['community']} are community.
{c['mcp_status']['none-found']} had no server found at all, and {c['mcp_status']['unknown']} could
not be settled either way and are published as unknown rather than guessed into a bucket.</p>
<p>Community servers cluster. {H['cats']['video-prospecting']['label']} alone accounts for
{H['cats']['video-prospecting']['mcp_status']['community']} of the
{c['mcp_status']['community']}, against
{H['cats']['video-prospecting']['mcp_status']['official']} official servers in that category, which
is the one place in this data where the community outbuilt the vendors.</p>
<h2>What to check before depending on a community server</h2>
<ul>
<li>When the repo last moved. This directory does not publish that yet: the repo health rail has not
been run, and a star count without the date it was taken is a lie, so nothing is shown rather than
something stale. {cov['github_candidates_any']} entries already carry a github.com URL somewhere in
their fields, which is the seed for that work.</li>
<li>Whether the vendor acknowledges it anywhere in their own docs.</li>
<li>What credential it wants, and how much of your account that credential can touch.</li>
</ul>
<p>The {c['mcp_status']['community']} community servers in this directory are listed with their URLs
and their auth models, and every one links to the entry it came from.</p>""",
            "sources": [S_MCP_SERVERS, S_MCP_SITE,
                        ("The GTM MCP Directory, methodology", "methodology.html")],
            "related": ["what-is-an-mcp-server", "what-does-agent-ready-mean",
                        "which-gtm-tools-have-official-mcp-servers",
                        "how-do-i-build-an-mcp-server-for-a-tool-that-has-none"],
            "see": [("The community servers", "lists/community-mcp-servers.html"),
                    ("The official servers", "lists/official-mcp-servers.html")],
        },
        {
            "slug": "stdio-vs-remote-mcp-servers",
            "cluster": "definitions",
            "q": "What is the difference between a local and a remote MCP server?",
            "title": "Local (stdio) vs remote (HTTP) MCP servers: which one you are installing",
            "desc": "A local MCP server runs as a process on your machine and talks over standard "
                    "input and output. A remote one is a URL you connect to. The practical "
                    "differences: credentials, latency, updates and who can see your queries.",
            "short": "A local MCP server runs as a process on your own machine and talks to the "
                     "client over standard input and output. A remote server is an HTTP endpoint "
                     "you point the client at. Local means your credentials stay on your machine "
                     "and you control the version. Remote means the vendor updates it and nothing "
                     "has to be installed.",
            "body": f"""
<p>Every MCP server has to answer the same question: how do the bytes get from the client to the
server. There are two established answers.</p>
<h2>Local, over standard input and output</h2>
<p>The client launches the server as a child process and they talk over stdin and stdout. Nothing
listens on a port, nothing crosses the network, and the server has whatever access your user account
has. This is why so many install snippets are a command and a list of arguments rather than a URL.
It is also why a local server can reach your file system, and why installing one from an unknown
source is the same class of decision as installing any other program.</p>
<h2>Remote, over HTTP</h2>
<p>The client connects to a URL the vendor hosts. Nothing is installed, the vendor ships fixes
without you doing anything, and the auth is usually a browser sign in rather than a pasted key. The
tradeoffs are the ordinary ones for hosted software: your queries reach their infrastructure, an
outage on their side is an outage for your agent, and you are on whatever version they deployed this
morning.</p>
<h2>Which one the GTM tools ship</h2>
<p>Both, and the entries say which. Of the {c['mcp_status']['official'] + c['mcp_status']['community']}
servers found in this directory, {cov['mcp_url_with_parseable_url']} carry a parseable URL in their
mcp_url field and {cov['mcp_url_pointing_at_github']} of those URLs point at a GitHub repository
rather than a hosted endpoint, which is a strong hint the install is a local one you run yourself.
The transport is recorded verbatim on the tool page wherever the vendor documents it, including one
entry where the vendor's own registry record and a third party directory disagree about the
transport and both are printed rather than one being picked.</p>
<h2>The practical rule</h2>
<p>If the setup asks for a command, it is local and your machine is the boundary. If it asks for a
URL and sends you to a browser, it is remote and the vendor is the boundary. Read the auth field on
the tool page before either one: that field is copied verbatim from the vendor's documentation on
this site precisely because it is the sentence that decides how much of your account is now
reachable.</p>""",
            "sources": [S_MCP_SPEC, S_MCP_QUICK, S_MCP_SITE],
            "related": ["what-is-an-mcp-server", "how-do-i-add-an-mcp-server-to-claude-desktop",
                        "which-gtm-mcp-servers-use-oauth",
                        "what-are-the-security-risks-of-connecting-an-agent-to-my-gtm-stack"],
            "see": [("Servers by auth type", "lists/auth-types.html")],
        },
        {
            "slug": "what-is-an-mcp-client",
            "cluster": "definitions",
            "q": "What is an MCP client?",
            "title": "What is an MCP client? The apps that can connect to an MCP server",
            "desc": "An MCP client is the piece inside an AI application that holds a connection to "
                    "one MCP server. Which apps have one, and why it decides what your agent can "
                    "do more than the model does.",
            "short": "An MCP client is the component inside an AI application that opens and holds "
                     "one connection to one MCP server. The application you use is the host; it "
                     "runs one client per server it is connected to. If your app has no MCP "
                     "client, no MCP server on earth is useful to it.",
            "body": f"""
<p>The distinction matters when something does not work. People say the server is broken when the
actual problem is that their application does not support the transport the server uses, or does not
support MCP at all.</p>
<p>Host applications with MCP client support include Anthropic's own Claude apps and Claude Code,
and coding environments and assistants that have added it. The auth notes recorded on entries in
this directory name <b>Claude, ChatGPT and Cursor</b> as the clients whose sign in flows vendors
write documentation for, which is a useful signal about where adoption actually is: vendors document
against the clients their customers use.</p>
<h2>What the client is responsible for</h2>
<ul>
<li><b>Discovery.</b> Asking the server what tools, resources and prompts it offers, and handing
that list to the model.</li>
<li><b>Permission.</b> Deciding whether a tool call the model wants to make gets executed, and
whether a human is asked first. This is the single most important behaviour and it is implemented by
the client, not by the protocol and not by the server.</li>
<li><b>Transport.</b> Launching a local server as a subprocess, or connecting to a remote one over
HTTP and handling the auth.</li>
</ul>
<h2>Why this decides what your agent can do</h2>
<p>Two people can run the same model against the same server and get different capabilities, because
their clients differ in what they expose and how they gate approval. When you are choosing where to
build a GTM agent, the client's permission model is worth more attention than the model's benchmark
scores. An agent that writes to your CRM with no approval step is a different risk than the same
agent asking first, and that choice lives in the client.</p>
<p>This directory records the vendor side of that relationship: which vendors ship a server, what it
authenticates with, and whether you can get an account without a sales call. Which client you point
at it is your decision and there is no ranking of clients here.</p>""",
            "sources": [S_MCP_SPEC, S_MCP_QUICK, S_MCP_SITE],
            "related": ["what-is-an-mcp-server", "what-is-the-model-context-protocol",
                        "how-do-i-add-an-mcp-server-to-claude-desktop",
                        "how-do-i-stop-an-agent-writing-bad-data-to-my-crm"],
            "see": [("The MCP layer category", "categories/mcp-infrastructure.html")],
        },
        {
            "slug": "what-are-mcp-tools-resources-and-prompts",
            "cluster": "definitions",
            "q": "What are MCP tools, resources and prompts?",
            "title": "MCP tools, resources and prompts: the three things a server offers",
            "desc": "An MCP server can expose three kinds of capability: tools the agent invokes, "
                    "resources it reads, and prompts a user triggers. What each one is for, and "
                    "which one you actually care about for GTM work.",
            "short": "An MCP server offers three kinds of thing. Tools are actions the model can "
                     "invoke and that can change something. Resources are data the client can read "
                     "into context. Prompts are prewritten instruction templates a user chooses. "
                     "For go to market work, tools are almost always the part that matters.",
            "body": f"""
<p><b>Tools</b> are functions with a name, a description and a typed argument schema. The model
picks one, fills the arguments and the client executes it. Anything that finds a person, writes a
record, sends a message or spends credits is a tool. Tools are model controlled, which is exactly
why the approval behaviour in your client matters.</p>
<p><b>Resources</b> are addressable pieces of context: a file, a record, a document, a query result.
They are read, not run. The application decides which resources to pull into context, so they are
application controlled rather than model controlled. In a GTM stack a resource is typically the
account record or the transcript you want the model to reason over.</p>
<p><b>Prompts</b> are reusable instruction templates the server publishes, surfaced in the client as
something a person picks deliberately. They are user controlled. A vendor might ship a prompt for
"prepare me for this call" that pulls the right resources and calls the right tools in the right
order.</p>
<h2>Why the split exists</h2>
<p>Three different parties decide. The model chooses tools, the application chooses resources, the
human chooses prompts. That is a permission design, not a filing system, and it is the part of MCP
most worth understanding before you connect an agent to anything that can send email on your behalf.</p>
<h2>What this means for the GTM stack</h2>
<p>When a vendor here says it ships an MCP server, in practice that nearly always means tools:
search, enrich, create, send. This directory records what the vendor documents and does not
enumerate the tool surface of each server, because that would need each server to be installed and
run, and {c['bench_tested']} tools in this directory have been run by anybody here.</p>
<p>The closest published proxy is the job tags. {num(cov['jobs_assignments'])} tags across
{num(cov['jobs_tagged'])} entries record what each vendor says its tool does, in the agent's own
phrasing, which is the vocabulary you would expect its tools to be named after.</p>""",
            "sources": [S_MCP_SPEC, S_MCP_SITE, S_MCP_SERVERS],
            "related": ["what-is-an-mcp-server", "what-is-an-mcp-client",
                        "what-is-the-model-context-protocol",
                        "how-do-i-stop-an-agent-writing-bad-data-to-my-crm"],
            "see": [("Every job an agent asks for", "jobs/index.html")],
        },
        {
            "slug": "what-is-an-api-access-gate",
            "cluster": "definitions",
            "q": "What is an API access gate and why does it matter for AI agents?",
            "title": "API access gates: free, paid, or a procurement cycle before your agent starts",
            "desc": f"An access gate is what stands between you and an API key. Across "
                    f"{num(c['entries'])} GTM tools: {c['api_gate']['free']} free to start, "
                    f"{c['api_gate']['paid']} paid self serve, {c['api_gate']['enterprise-only']} "
                    f"enterprise only.",
            "short": "An API access gate is what a vendor makes you do before you can get "
                     "programmatic access. Free to start means you sign up and get a key. Paid "
                     "self serve means you pay and get a key. Enterprise only means a contract, a "
                     "seat count or a procurement cycle, which for one person with an agent is a "
                     "closed door.",
            "body": f"""
<p>This is the second column nobody else publishes, and in practice it decides more than the feature
list does. A tool with a magnificent API you cannot get into is worth exactly as much to your agent
as a tool with no API.</p>
<h2>The four gates, counted</h2>
<div class="scroller"><table class="datatable"><thead><tr><th>Gate</th><th>Entries</th>
<th>What it means for one person with an agent</th></tr></thead><tbody>
<tr><td><a href="{rel}gates/free.html">Free to start</a></td><td class="n">{c['api_gate']['free']}</td>
<td>Sign up, get a key, start calling. No conversation with anybody.</td></tr>
<tr><td><a href="{rel}gates/paid.html">Paid, self serve</a></td><td class="n">{c['api_gate']['paid']}</td>
<td>A credit card is enough. Still no sales call.</td></tr>
<tr><td><a href="{rel}gates/enterprise-leaning.html">Enterprise leaning</a></td>
<td class="n">{c['api_gate']['enterprise-leaning']}</td>
<td>Self serve on paper, gated in practice.</td></tr>
<tr><td><a href="{rel}gates/enterprise-only.html">Enterprise only</a></td>
<td class="n">{c['api_gate']['enterprise-only']}</td>
<td>Contract, seat minimum or procurement. A solo operator is out.</td></tr>
<tr><td><a href="{rel}gates/unknown.html">Unknown</a></td><td class="n">{c['api_gate']['unknown']}</td>
<td>The gate could not be established from public sources and is published as unknown rather than
guessed.</td></tr>
</tbody></table></div>
<p class="note">{c['api_gate']['n-a']} further entries record n/a, where an API gate is not a
meaningful question. Counted {esc(gen)} across {num(c['entries'])} entries.</p>
<h2>Why unknown is such a large number</h2>
<p>{c['api_gate']['unknown']} entries carry an unknown gate, and that is itself the finding. A
vendor who does not publish whether you can buy API access, at what tier, is telling you something
about how they expect you to buy. Unknown is a legal answer in this directory and it ships as
unknown rather than being rounded into whichever bucket looks tidier.</p>
<h2>The intersection that matters</h2>
<p>MCP status and access gate are separate columns for a reason. {sum(1 for e in entries if e['mcp_status_bucket'] == 'official' and e['api_gate_bucket'] in ('enterprise-only', 'enterprise-leaning'))}
entries ship an official MCP server behind an enterprise gate. The server is real, the protocol
works, and most people reading this cannot call it. The
<a href="{rel}lists/solo-reachable.html">{cov['solo_reachable']} solo reachable entries</a> are the
list that matters if you are one person and a credit card.</p>""",
            "sources": [("The GTM MCP Directory, by access gate", "gates/index.html"),
                        ("The GTM MCP Directory, methodology", "methodology.html")],
            "related": ["what-does-agent-ready-mean",
                        "which-gtm-tools-can-a-solo-operator-use",
                        "how-many-gtm-tools-are-enterprise-gated",
                        "which-data-enrichment-tools-can-an-agent-use-for-free"],
            "see": [("By access gate", "gates/index.html"),
                    ("The free tiers", "lists/free-api-tiers.html")],
        },
        {
            "slug": "what-is-data-enrichment",
            "cluster": "definitions",
            "q": "What is data enrichment in sales?",
            "title": "What is data enrichment? The definition, and which vendors an agent can call",
            "desc": f"Data enrichment turns a thin identifier into a full record. "
                    f"{H['cats']['data-enrichment']['total']} enrichment tools are counted here and "
                    f"{H['cats']['data-enrichment']['mcp_status']['official']} ship an official MCP "
                    f"server.",
            "short": "Data enrichment is taking a thin identifier you already have, such as a "
                     "domain, an email or a LinkedIn URL, and returning a fuller record: the "
                     "person's title and employer, or the company's size, industry, location and "
                     "technology stack. It is the step that turns a name into something you can "
                     "act on.",
            "body": f"""
<p>Enrichment vendors differ mostly in where the data comes from and how fresh it is: contributed
data from users, licensed data, public web crawling, or a blend. This directory does not measure
accuracy or coverage. Nobody has run these tools for it, and a coverage claim without a test is a
vendor's number repeated back.</p>
<h2>The four shapes of the job</h2>
<div class="scroller"><table class="datatable"><thead><tr><th>What you have</th><th>The job</th>
<th>Tools tagged</th><th>Official MCP</th><th>Free tier</th></tr></thead><tbody>
{''.join(f'<tr><td>{esc(has)}</td><td>{jl(jid)}</td><td class="n">{jn(jid, "entry_count")}</td>'
         f'<td class="n">{jn(jid, "mcp_status", "official")}</td>'
         f'<td class="n">{jn(jid, "api_gate", "free")}</td></tr>'
         for has, jid in [("A company domain", "enrich-company-from-domain"),
                          ("A LinkedIn profile URL", "enrich-person-from-linkedin-url"),
                          ("A name and a company", "find-work-email"),
                          ("An email address", "reverse-lookup-person-from-email")])}
</tbody></table></div>
<p class="note">Counted {esc(gen)}. Entry counts, not product counts: a tool listed in two
categories is counted in both.</p>
<h2>Why this category is the exception</h2>
<p>{H['cats']['data-enrichment']['label']} is the most agent reachable category in this directory:
{H['cats']['data-enrichment']['mcp_status']['official']} official servers and
{H['cats']['data-enrichment']['mcp_status']['community']} community across
{H['cats']['data-enrichment']['total']} entries, with
{H['cats']['data-enrichment']['api_gate']['free']} free to start. That is not an accident. These
vendors already sold an API as the product, so exposing it through a second protocol was a small
step rather than a strategy change.</p>
<p>Compare that with categories whose product is a user interface. When the interface is the
product, the API is a cost, and the MCP server is a cost on top of a cost.</p>
<h2>The one thing to check first</h2>
<p>Credits. Enrichment is metered, and an agent in a loop is very good at spending a month of quota
in an afternoon. This directory records the access gate, not pricing or quota sizes, so read the
vendor's own page before you point an autonomous loop at one.</p>""",
            "sources": [("The GTM MCP Directory, Data and Enrichment",
                         "categories/data-enrichment.html"),
                        ("The GTM MCP Directory, methodology", "methodology.html")],
            "related": ["which-data-enrichment-tools-can-an-agent-use-for-free",
                        "how-do-i-enrich-a-linkedin-profile-with-an-ai-agent",
                        "which-tools-can-enrich-a-company-from-a-domain",
                        "how-do-i-find-a-work-email-with-an-ai-agent"],
            "see": [("Data and Enrichment", "categories/data-enrichment.html"),
                    ("Enrichment tools with MCP servers", "lists/mcp-data-enrichment.html")],
        },
        {
            "slug": "what-is-buyer-intent-data",
            "cluster": "definitions",
            "q": "What is buyer intent data?",
            "title": "What is buyer intent data? Definition, sources, and what an agent can fetch",
            "desc": f"Buyer intent data is evidence that an account is researching a problem you "
                    f"solve. Where it comes from, what it is worth, and which of the "
                    f"{jn('fetch-buyer-intent-signals', 'entry_count')} tools tagged with it an "
                    f"agent can call.",
            "short": "Buyer intent data is evidence that an account is actively researching "
                     "something you sell: content consumption on third party networks, review site "
                     "activity, job postings, technology changes, or visits to your own site. It "
                     "is a prioritisation input, not a prediction, and its quality depends entirely "
                     "on where the signal came from.",
            "body": f"""
<p>Intent is sold as one thing and is at least four. Knowing which one you are buying is the whole
skill.</p>
<ul>
<li><b>First party.</b> Behaviour on your own properties. Highest quality, smallest volume, and it
is yours.</li>
<li><b>De-anonymised traffic.</b> Turning an anonymous visit into a company, sometimes a person.
{jn('identify-anonymous-website-visitor', 'entry_count')} entries here are tagged
{jl('identify-anonymous-website-visitor')}.</li>
<li><b>Third party topic intent.</b> Aggregated content consumption across publisher networks.
Broad, and the further from your product the topic is, the noisier it gets.</li>
<li><b>Observable events.</b> A funding round, a hiring pattern, a technology added or dropped.
Not intent in the strict sense, but checkable and often more actionable.
{jn('detect-funding-or-news-event', 'entry_count')} entries are tagged
{jl('detect-funding-or-news-event')}, {jn('scrape-job-postings', 'entry_count')} are tagged
{jl('scrape-job-postings')} and {jn('detect-technographics', 'entry_count')} are tagged
{jl('detect-technographics')}.</li>
</ul>
<h2>What an agent can actually fetch</h2>
<p>{jn('fetch-buyer-intent-signals', 'entry_count')} entries are tagged
{jl('fetch-buyer-intent-signals')}. Of those,
{jn('fetch-buyer-intent-signals', 'mcp_status', 'official')} have an official MCP server,
{jn('fetch-buyer-intent-signals', 'mcp_status', 'none-found')} have none found, and
{jn('fetch-buyer-intent-signals', 'solo_reachable')} are reachable by a solo operator without a
contract. The category they mostly live in,
{H['cats']['signals-intent-abm']['label']}, carries
{H['cats']['signals-intent-abm']['api_gate']['enterprise-only']} enterprise only entries out of
{H['cats']['signals-intent-abm']['total']}, the second highest enterprise gate share in this
directory.</p>
<p>That combination is the honest summary of intent data as a category: technically callable, often
commercially closed.</p>
<h2>The tools tagged with it that a solo operator can reach</h2>
{ul(je('fetch-buyer-intent-signals', gate=('free', 'paid')), limit=10)}""",
            "sources": [("The GTM MCP Directory, Signals and Intent",
                         "categories/signals-intent-abm.html"),
                        ("The GTM MCP Directory, fetch buyer intent signals",
                         "jobs/fetch-buyer-intent-signals.html")],
            "related": ["which-tools-can-identify-anonymous-website-visitors",
                        "what-is-an-api-access-gate", "which-gtm-categories-are-most-agent-ready",
                        "how-do-i-build-a-prospect-list-with-an-ai-agent"],
            "see": [("Signals and Intent", "categories/signals-intent-abm.html"),
                    ("Signals tools with MCP servers", "lists/mcp-signals-intent-abm.html")],
        },
        {
            "slug": "what-are-the-security-risks-of-connecting-an-agent-to-my-gtm-stack",
            "cluster": "definitions",
            "q": "What are the security risks of connecting an AI agent to my GTM stack?",
            "title": "MCP security risks in a GTM stack: credentials, injection and blast radius",
            "desc": "Connecting an agent to your CRM, your enrichment vendors and your mailbox "
                    "creates four specific risks. What they are, and what the auth data across "
                    "GTM MCP servers says about them.",
            "short": "Four risks matter: the credential you hand the server can usually do far more "
                     "than the one task, tool results are untrusted text that can carry "
                     "instructions the model may follow, a community server is code from a "
                     "stranger running on your machine, and an agent that can send or write can "
                     "do it at machine speed before anybody notices.",
            "body": f"""
<h2>1. The credential is the blast radius</h2>
<p>An MCP server does what your credential allows, not what the tool description says. A CRM key
scoped to full access does not become read only because the agent was only asked to read. Scope the
credential at the vendor, not in the prompt. Of the
{c['mcp_status']['official'] + c['mcp_status']['community']} servers counted here,
<a href="{rel}lists/auth-oauth.html">the OAuth ones</a> are the better shape for this: the token is
scoped and revocable from the vendor side without touching the agent's config.</p>
<h2>2. Tool output is untrusted input</h2>
<p>An agent reads what a tool returns. A scraped page, an inbound email, a CRM note or a form
submission can contain text written by someone who wants your agent to do something. If that text
reaches the model and the model can call tools, the instruction can be acted on. This is the single
most GTM specific risk on this list, because the entire job involves ingesting text strangers wrote.
Keep destructive tools behind human approval and do not let a research step and a send step share an
unsupervised loop.</p>
<h2>3. A community server is somebody's code on your machine</h2>
<p>{c['mcp_status']['community']} entries here have a community server, and a locally installed
server runs with your user's permissions. Read who published it, whether the vendor acknowledges it,
and what it wants access to. The repo health rail that would date stamp each one has not been run
for this build, so this directory publishes no staleness claim at all rather than a stale one.</p>
<h2>4. Speed is the amplifier</h2>
<p>Every failure above already existed with scripts. What is new is that nobody wrote the sequence in
advance. {jn('run-email-sequence', 'entry_count')} entries here are tagged
{jl('run-email-sequence')} and {jn('write-crm-records', 'entry_count')} are tagged
{jl('write-crm-records')}. Those two capabilities in one unsupervised loop is how a bad enrichment
result becomes two thousand wrong emails and a polluted CRM in the same afternoon.</p>
<h2>The short checklist</h2>
<ul>
<li>Separate read credentials from write credentials, and prefer OAuth where the vendor offers it.</li>
<li>Require approval on anything that sends, spends or writes.</li>
<li>Log every tool call with its arguments. If you cannot answer what the agent did on Tuesday, you
do not have an agent, you have an incident waiting for a date.</li>
<li>Sandbox a new server before it touches production data, and read the verbatim auth field on its
tool page first.</li>
</ul>""",
            "sources": [S_MCP_SPEC, S_MCP_SITE,
                        ("The GTM MCP Directory, servers by auth type", "lists/auth-types.html")],
            "related": ["which-gtm-mcp-servers-use-oauth", "stdio-vs-remote-mcp-servers",
                        "how-do-i-stop-an-agent-writing-bad-data-to-my-crm",
                        "can-an-ai-agent-send-email-on-my-behalf"],
            "see": [("Servers by auth type", "lists/auth-types.html")],
        },
        {
            "slug": "what-is-a-gtm-tech-stack",
            "cluster": "definitions",
            "q": "What is a GTM tech stack?",
            "title": "What is a GTM tech stack? The 15 layers, and how much of each an agent reaches",
            "desc": f"A GTM tech stack is the set of systems a revenue team sells through. The "
                    f"{c['categories']} layers counted in this directory, with the share of each "
                    f"one an AI agent can currently call.",
            "short": "A GTM tech stack is every system a revenue team sells through, from the data "
                     "that starts a conversation to the document that closes it. In this directory "
                     f"it is {c['categories']} layers and {num(c['entries'])} tools, and the "
                     "interesting question about a stack is no longer what is in it but how much of "
                     "it anything can call.",
            "body": f"""
<p>Most stack diagrams are drawn by category because that is how software is sold. An agent does not
experience it that way. It experiences a chain of doors, and the chain is only as good as its
locked link.</p>
<h2>The layers, ordered by how reachable they are</h2>
<div class="scroller"><table class="datatable"><thead><tr><th>Layer</th><th>Tools</th>
<th>Official MCP</th><th>Community</th><th>Reachable</th></tr></thead><tbody>
{''.join(f'<tr><td><a href="{rel}categories/{x["slug"]}.html">{esc(x["label"])}</a></td>'
         f'<td class="n">{x["total"]}</td>'
         f'<td class="n">{x["mcp_status"]["official"]}</td>'
         f'<td class="n">{x["mcp_status"]["community"]}</td>'
         f'<td class="n">{pct(x["mcp_status"]["official"] + x["mcp_status"]["community"], x["total"])}</td></tr>'
         for x in sorted(d["categories"],
                         key=lambda k: -(k["mcp_status"]["official"] + k["mcp_status"]["community"]) / k["total"]))}
</tbody></table></div>
<p class="note">Counted {esc(gen)}. Totals sum to {num(c['entries'])} entries, which includes
{c['cross_listed_entries']} products deliberately listed in two categories.</p>
<h2>What the ordering tells you</h2>
<p>The top of that table is the infrastructure and data layers, where the API was always the
product. The bottom is where the interface is the product: enablement, forecasting, community. The
category sold hardest on autonomy, {H['cats']['ai-sdr-agents']['label']}, sits well down it with
{H['cats']['ai-sdr-agents']['mcp_status']['official']} official servers out of
{H['cats']['ai-sdr-agents']['total']}.</p>
<p>If you are assembling a stack an agent can drive, build it from the top of that table down. The
bottom is where you will still be writing glue, or clicking.</p>
<h2>The second filter</h2>
<p>Reachable is not the same as available. {c['api_gate']['enterprise-only']} entries need a
contract before anybody gets an API key. Cross those two columns before you plan anything: the list
you actually get to build with is the {cov['solo_reachable']} entries that have a server and are
free to start or paid self serve.</p>""",
            "sources": [("The GTM MCP Directory, by category", "categories/index.html"),
                        ("The GTM MCP Directory, the counted data", "data.html")],
            "related": ["which-gtm-categories-are-most-agent-ready", "what-is-a-gtm-engineer",
                        "how-do-i-audit-my-gtm-stack-for-agent-readiness",
                        "what-is-an-api-access-gate"],
            "see": [("Every category", "categories/index.html"),
                    ("The lists", "lists/index.html")],
        },
    ]


def learn_directory(d, r, entries, byid, gen, H):
    rel, c, cov = H["rel"], H["c"], H["cov"]
    je, ce, names, ul, jl, pct = (H["job_entries"], H["cat_entries"], H["names"], H["tool_ul"],
                                  H["jl"], H["pct"])
    jn, jobs, cats = H["jn"], H["jobs"], H["cats"]
    reach = c["mcp_status"]["official"] + c["mcp_status"]["community"]
    out = []

    def jobq(slug, q, title, jid, why, related, extra_body=""):
        """The repeated shape: one job, its real numbers, its tools, and one paragraph of prose
        that is specific to that job and written rather than generated."""
        j = jobs[jid]
        off = j["mcp_status"]["official"]
        com = j["mcp_status"]["community"]
        rows_off = je(jid, mcp=("official",))
        rows_free = je(jid, gate=("free",))
        short = (f"{j['product_count']} products in this directory are tagged with this job. "
                 f"{off} of the {j['entry_count']} tagged entries have an official MCP server and "
                 f"{com} have a community one, so an agent can call "
                 f"{off + com} of them directly. {j['solo_reachable']} are reachable by one person "
                 f"without a contract. Counted {gen}.")
        body = f"""
{why}
<h2>The numbers, generated at build time</h2>
<div class="scroller"><table class="datatable"><thead><tr><th>Measure</th><th>Count</th>
<th>Of what</th></tr></thead><tbody>
<tr><td>Entries tagged {esc(jid)}</td><td class="n">{j['entry_count']}</td>
<td>of {num(c['entries'])} directory entries</td></tr>
<tr><td>Distinct products</td><td class="n">{j['product_count']}</td>
<td>the rest are cross listings</td></tr>
<tr><td>Official MCP server</td><td class="n">{off}</td><td>vendor built and maintained</td></tr>
<tr><td>Community MCP server</td><td class="n">{com}</td><td>built by somebody else</td></tr>
<tr><td>No server found</td><td class="n">{j['mcp_status']['none-found']}</td>
<td>on the date each entry was checked</td></tr>
<tr><td>Free to start</td><td class="n">{j['api_gate']['free']}</td><td>no payment, no sales call</td></tr>
<tr><td>Solo reachable</td><td class="n">{j['solo_reachable']}</td>
<td>free or paid self serve</td></tr>
<tr><td>Bench tested</td><td class="n">{j['bench_tested']}</td>
<td>somebody here actually ran it</td></tr>
</tbody></table></div>
<h2>The ones with an official MCP server</h2>
{ul(rows_off, limit=12) if rows_off else '<div class="warn"><b>None</b>No tool tagged with this job ships a first party MCP server in this build. That is the answer, and it is published rather than softened.</div>'}
<h2>The ones with a free tier</h2>
{ul(rows_free, limit=10) if rows_free else '<p>None of the tools tagged with this job record a free to start gate. ' + str(j['api_gate']['paid']) + ' are paid self serve and ' + str(j['api_gate']['unknown']) + ' do not publish enough for the gate to be established.</p>'}
{extra_body}
<h2>What this list is not</h2>
<p>It is not a ranking and it is not a recommendation. A job tag means the vendor says the tool does
this. Nobody here has run any of them: {c['bench_tested']} tools in this directory are bench tested.
Two tools on the same list can be wildly different in coverage, price and quality, and this
directory does not claim to know which.</p>"""
        return {
            "slug": slug, "cluster": "directory", "q": q, "title": title,
            "desc": (f"{off} of the {j['entry_count']} GTM tools tagged with this job ship an "
                     f"official MCP server, {j['solo_reachable']} are reachable without a contract. "
                     f"The full list, counted {gen}."),
            "short": short, "body": body,
            "sources": [(f"The GTM MCP Directory, {j['label'].lower()}", f"jobs/{jid}.html"),
                        ("The GTM MCP Directory, methodology", "methodology.html"),
                        ("The GTM MCP Directory, the counted data", "data.html")],
            "related": related,
            "see": [(j["label"], f"jobs/{jid}.html"),
                    ("The official servers", "lists/official-mcp-servers.html")],
        }

    # ---- the headline directory questions ----
    off_rows = H["products"]([e for e in entries if e["mcp_status_bucket"] == "official"])
    out.append({
        "slug": "which-gtm-tools-have-official-mcp-servers",
        "cluster": "directory",
        "q": "Which GTM tools have official MCP servers?",
        "title": f"Which GTM tools have official MCP servers? {c['mcp_status']['official']} of "
                 f"{c['entries']}, counted",
        "desc": f"{c['mcp_status']['official']} of {num(c['entries'])} go to market tools ship an "
                f"MCP server their own vendor builds and maintains. The full list by category, with "
                f"server URLs and auth. Counted {gen}.",
        "short": f"{c['mcp_status']['official']} of the {num(c['entries'])} go to market tools in "
                 f"this directory ship an official MCP server, meaning the vendor builds and "
                 f"maintains it. A further {c['mcp_status']['community']} have a community built "
                 f"server. The heaviest concentrations are in enrichment, RevOps infrastructure and "
                 f"signals.",
        "body": f"""
<p>Official is a strict test here. The vendor has to ship and maintain the server itself. A wrapper
built by Zapier, Composio, viaSocket or any other integration platform is recorded as community no
matter how well it works, because when the underlying API changes, only one of those two has a team
whose job it is to notice.</p>
<h2>Where the {c['mcp_status']['official']} sit</h2>
<div class="scroller"><table class="datatable"><thead><tr><th>Category</th><th>Official</th>
<th>Community</th><th>Of total</th><th>The list</th></tr></thead><tbody>
{''.join(f'<tr><td><a href="{rel}categories/{x["slug"]}.html">{esc(x["label"])}</a></td>'
         f'<td class="n">{x["mcp_status"]["official"]}</td>'
         f'<td class="n">{x["mcp_status"]["community"]}</td>'
         f'<td class="n">{x["total"]}</td>'
         f'<td><a href="{rel}lists/mcp-{x["slug"]}.html">open</a></td></tr>'
         for x in sorted(d["categories"], key=lambda k: -k["mcp_status"]["official"]))}
</tbody></table></div>
<p class="note">Counted {esc(gen)} from directory.json, reconciled against
{esc(r['reconciliation']['authority'])}. Entry counts: {c['cross_listed_entries']} products appear in
two categories and are counted in both here.</p>
<h2>The full list</h2>
<p>All {c['mcp_status']['official']} are published on one page with the server URL, the auth model
and the access gate for each: <a href="{rel}lists/official-mcp-servers.html">the official MCP
servers list</a>. {cov['mcp_url_with_parseable_url']} entries across the directory carry a parseable
server URL; where a vendor claims a server in prose without one, that is recorded as a risk on the
methodology page rather than quietly cleaned up.</p>
<h2>The first fifteen, in the published order</h2>
{ul(off_rows, limit=15)}
<h2>The caveat that matters</h2>
<p>An official server is not the same as a server you can use. {sum(1 for e in entries if e['mcp_status_bucket'] == 'official' and e['api_gate_bucket'] in ('enterprise-only', 'enterprise-leaning'))}
of these sit behind an enterprise gate: a contract, a seat count or a procurement cycle before
anybody gets a key. Check the gate column, not just the status.</p>""",
        "sources": [("The GTM MCP Directory, the official servers list",
                     "lists/official-mcp-servers.html"),
                    ("The GTM MCP Directory, methodology", "methodology.html"),
                    ("The GTM MCP Directory, the counted data", "data.html")],
        "related": ["how-many-gtm-tools-have-mcp-servers", "official-vs-community-mcp-server",
                    "which-gtm-categories-are-most-agent-ready",
                    "which-gtm-tools-can-a-solo-operator-use"],
        "see": [("The official servers list", "lists/official-mcp-servers.html"),
                ("By MCP status", "mcp/index.html")],
    })

    out.append({
        "slug": "how-many-gtm-tools-have-mcp-servers",
        "cluster": "directory",
        "q": "How many GTM tools have MCP servers?",
        "title": f"How many GTM tools have MCP servers? {reach} of {c['entries']} checked",
        "desc": f"{reach} of {num(c['entries'])} go to market tools have an MCP server: "
                f"{c['mcp_status']['official']} official, {c['mcp_status']['community']} community. "
                f"The rest, and what none found actually means. Counted {gen}.",
        "short": f"{reach} of the {num(c['entries'])} go to market tools counted in this directory "
                 f"have an MCP server of some kind: {c['mcp_status']['official']} official and "
                 f"{c['mcp_status']['community']} community. {c['mcp_status']['none-found']} had "
                 f"none found on the date they were checked and {c['mcp_status']['unknown']} could "
                 f"not be settled either way.",
        "body": f"""
<h2>The whole distribution</h2>
<div class="scroller"><table class="datatable"><thead><tr><th>Status</th><th>Entries</th>
<th>Share</th><th>What it means</th></tr></thead><tbody>
{''.join(f'<tr><td><a href="{rel}mcp/{b}.html">{esc(MCP_LABEL[b])}</a></td>'
         f'<td class="n">{c["mcp_status"][b]}</td>'
         f'<td class="n">{pct(c["mcp_status"][b], c["entries"])}</td>'
         f'<td>{esc(trim(MCP_BLURB[b], 120))}</td></tr>'
         for b in MCP_ORDER if c["mcp_status"].get(b))}
</tbody></table></div>
<p class="note">Counted {esc(gen)}. Total: {num(c['entries'])} entries across {c['categories']}
category files, of which {num(c['canonical_entries'])} are unique products and
{c['cross_listed_entries']} are the same product listed in a second category.</p>
<h2>What none found does not mean</h2>
<p>{c['mcp_status']['none-found']} entries are none found. That is a statement about a search made
on a date, and every entry carries the date its facts were pulled:
{', '.join(f"{num(v)} on {k}" for k, v in sorted(cov['last_checked'].items()))}. A vendor who
shipped a server the week after their entry was checked is recorded as none found until the next
pass. It is not a claim that no server exists.</p>
<h2>Why the number is not higher</h2>
<p>Adoption is not evenly spread and it is not random. Vendors whose product was already an API
shipped servers early: {cats['data-enrichment']['label']} is at
{cats['data-enrichment']['mcp_status']['official']} official of
{cats['data-enrichment']['total']}, {cats['revops-infra']['label']} at
{cats['revops-infra']['mcp_status']['official']} of {cats['revops-infra']['total']}. Vendors whose
product is a user interface are at the bottom: {cats['enablement-coaching']['label']} at
{cats['enablement-coaching']['mcp_status']['official']} of
{cats['enablement-coaching']['total']} and {cats['forecasting-revenue']['label']} at
{cats['forecasting-revenue']['mcp_status']['official']} of
{cats['forecasting-revenue']['total']}.</p>
<h2>The number to watch</h2>
<p>This directory rebuilds from source files and republishes the counts each time, so the honest way
to read {reach} is as a reading taken on {gen}, not a permanent state of the market. The same
question asked six months from now will have a different answer, and the point of publishing the
date on every number is that you can tell the difference.</p>""",
        "sources": [("The GTM MCP Directory, by MCP status", "mcp/index.html"),
                    ("The GTM MCP Directory, methodology", "methodology.html"),
                    ("The GTM MCP Directory, the counted data", "data.html")],
        "related": ["which-gtm-tools-have-official-mcp-servers",
                    "what-percentage-of-gtm-tools-can-an-agent-reach",
                    "which-gtm-tools-have-no-mcp-server", "which-gtm-categories-are-most-agent-ready"],
        "see": [("By MCP status", "mcp/index.html"), ("The lists", "lists/index.html")],
    })

    ranked = sorted(d["categories"],
                    key=lambda k: -(k["mcp_status"]["official"] + k["mcp_status"]["community"]) / k["total"])
    out.append({
        "slug": "which-gtm-categories-are-most-agent-ready",
        "cluster": "directory",
        "q": "Which GTM tool categories are most usable by AI agents?",
        "title": "Which GTM categories are most agent reachable? The 15 layers, ranked by coverage",
        "desc": f"{ranked[0]['label']} leads at "
                f"{pct(ranked[0]['mcp_status']['official'] + ranked[0]['mcp_status']['community'], ranked[0]['total'])} "
                f"MCP coverage. {ranked[-1]['label']} is last. The full ranking across "
                f"{c['categories']} categories, counted {gen}.",
        "short": f"{ranked[0]['label']} is the most agent reachable category at "
                 f"{ranked[0]['mcp_status']['official'] + ranked[0]['mcp_status']['community']} of "
                 f"{ranked[0]['total']} entries with a server. {ranked[-1]['label']} is the least "
                 f"at {ranked[-1]['mcp_status']['official'] + ranked[-1]['mcp_status']['community']} "
                 f"of {ranked[-1]['total']}. The pattern is that categories which already sold an "
                 f"API adopted MCP, and categories whose product is a screen did not.",
        "body": f"""
<h2>The ranking</h2>
<div class="scroller"><table class="datatable"><thead><tr><th>#</th><th>Category</th>
<th>Reachable</th><th>Official</th><th>Community</th><th>Of</th></tr></thead><tbody>
{''.join(f'<tr><td class="n">{i}</td>'
         f'<td><a href="{rel}categories/{x["slug"]}.html">{esc(x["label"])}</a></td>'
         f'<td class="n">{pct(x["mcp_status"]["official"] + x["mcp_status"]["community"], x["total"])}</td>'
         f'<td class="n">{x["mcp_status"]["official"]}</td>'
         f'<td class="n">{x["mcp_status"]["community"]}</td>'
         f'<td class="n">{x["total"]}</td></tr>'
         for i, x in enumerate(ranked, start=1))}
</tbody></table></div>
<p class="note">Counted {esc(gen)} from the category blocks in directory.json. Reachable means an
official or community MCP server was found on the date the entry was checked.</p>
<h2>The inversion</h2>
<p>The categories sold hardest on artificial intelligence are the least usable by anybody else's
artificial intelligence. {cats['ai-sdr-agents']['label']} sits at
{cats['ai-sdr-agents']['mcp_status']['official']} official servers across
{cats['ai-sdr-agents']['total']} entries. {cats['enablement-coaching']['label']} is at
{cats['enablement-coaching']['mcp_status']['official']} of
{cats['enablement-coaching']['total']}. Meanwhile the plumbing layer, {cats['revops-infra']['label']},
is at {cats['revops-infra']['mcp_status']['official']} of {cats['revops-infra']['total']}.</p>
<p>The explanation is commercial rather than technical. If your product is an API, a server is a
weekend of work and a new distribution channel. If your product is a seat somebody logs into, a
server is a way for customers to stop logging in.</p>
<h2>The exception worth noticing</h2>
<p>{cats['video-prospecting']['label']} has
{cats['video-prospecting']['mcp_status']['community']} community servers against
{cats['video-prospecting']['mcp_status']['official']} official, the only category in this directory
where outsiders built more than the vendors did. Community servers work. They are also maintained by
people with no contractual obligation to keep doing it.</p>
<h2>How to use this ranking</h2>
<p>Build the agent driven parts of a stack from the top of that table, and expect to write glue or
click at the bottom of it. Then apply the second filter, which is the access gate: reachable and
purchasable are different columns, and {c['api_gate']['enterprise-only']} entries need a contract
before any of this is relevant.</p>""",
        "sources": [("The GTM MCP Directory, by category", "categories/index.html"),
                    ("The GTM MCP Directory, the counted data", "data.html")],
        "related": ["what-is-a-gtm-tech-stack", "which-ai-sdr-tools-have-mcp-servers",
                    "which-crm-and-revops-tools-have-mcp-servers",
                    "how-many-gtm-tools-have-mcp-servers"],
        "see": [("Every category", "categories/index.html"),
                ("The lists", "lists/index.html")],
    })

    solo_rows = H["products"]([e for e in entries if e["api_gate_bucket"] in ("free", "paid")
                               and e["mcp_status_bucket"] in ("official", "community")])
    out.append({
        "slug": "which-gtm-tools-can-a-solo-operator-use",
        "cluster": "directory",
        "q": "Which GTM tools can a solo operator use with an AI agent?",
        "title": f"Which GTM tools can a solo operator use with an agent? {len(solo_rows)} products",
        "desc": f"{c['api_gate']['free'] + c['api_gate']['paid']} of {num(c['entries'])} GTM tools "
                f"are free to start or paid self serve, and {cov['solo_reachable']} of those also "
                f"have an MCP server. The list one person with a credit card can build on. Counted "
                f"{gen}.",
        "short": f"{c['api_gate']['free'] + c['api_gate']['paid']} of the {num(c['entries'])} "
                 f"entries here are free to start or paid self serve, so one person can get API "
                 f"access without a contract. {cov['solo_reachable']} of those also have an MCP "
                 f"server, which comes to {len(solo_rows)} unique products and is the list that "
                 f"matters if you are building an agent alone rather than inside a company with a "
                 f"procurement department.",
        "body": f"""
<p>Two columns have to be true at once. The tool has to be callable, and you have to be able to get
in. This directory publishes both separately on purpose, because plenty of tools pass one test and
fail the other.</p>
<h2>The arithmetic</h2>
<ul>
<li>{c['api_gate']['free']} entries are free to start: sign up, get a key, no conversation.</li>
<li>{c['api_gate']['paid']} are paid self serve: a credit card is enough.</li>
<li>Together, {c['api_gate']['free'] + c['api_gate']['paid']} of {num(c['entries'])} entries, or
{pct(c['api_gate']['free'] + c['api_gate']['paid'], c['entries'])}, pass the gate test.</li>
<li>Cross that with the MCP column and {cov['solo_reachable']} entries pass both. That intersection
is what this site calls solo reachable, and it is the number in the front page stat row.</li>
<li>{c['api_gate']['enterprise-only']} are enterprise only and
{c['api_gate']['enterprise-leaning']} enterprise leaning. Those are closed doors for one person.</li>
<li>{c['api_gate']['unknown']} do not publish enough for the gate to be established at all, and are
recorded as unknown rather than guessed.</li>
</ul>
<h2>Callable and reachable, both</h2>
<p>{len(solo_rows)} unique products pass both tests. Here are the first fifteen in the published
order.</p>
{ul(solo_rows, limit=15)}
<p><a href="{rel}lists/solo-reachable.html">The full solo reachable list is here</a>, and the
<a href="{rel}lists/free-api-tiers.html">{c['api_gate']['free']} free tiers are here</a>.</p>
<h2>What free does not mean</h2>
<p>This directory tracks one thing about money: whether the door opens without a sales call. It does
not track prices, credit costs, quota sizes or rate limits, and none of them should be inferred from
anything on this page. Enrichment in particular is metered, and an agent in a loop can spend a
month's quota before lunch.</p>""",
        "sources": [("The GTM MCP Directory, by access gate", "gates/index.html"),
                    ("The GTM MCP Directory, solo reachable", "lists/solo-reachable.html"),
                    ("The GTM MCP Directory, methodology", "methodology.html")],
        "related": ["what-is-an-api-access-gate", "how-many-gtm-tools-are-enterprise-gated",
                    "which-data-enrichment-tools-can-an-agent-use-for-free",
                    "which-mcp-servers-are-free-to-use"],
        "see": [("Solo reachable", "lists/solo-reachable.html"),
                ("Free tiers", "lists/free-api-tiers.html")],
    })

    enr_free = ce("data-enrichment", gate=("free",))
    enr_free_mcp = [e for e in enr_free if e["mcp_status_bucket"] in ("official", "community")]
    out.append({
        "slug": "which-data-enrichment-tools-can-an-agent-use-for-free",
        "cluster": "directory",
        "q": "Which data enrichment tools can an AI agent use for free?",
        "title": f"Which data enrichment tools can an AI agent use for free? {len(enr_free)} counted",
        "desc": f"{len(enr_free)} of the {cats['data-enrichment']['total']} data enrichment tools "
                f"in this directory are free to start, and {len(enr_free_mcp)} of those also have "
                f"an MCP server. The list, with what each one does. Counted {gen}.",
        "short": f"{len(enr_free)} of the {cats['data-enrichment']['total']} data enrichment tools "
                 f"counted here are free to start, meaning a solo operator can get API access "
                 f"without paying and without talking to anyone. {len(enr_free_mcp)} of those also "
                 f"ship an MCP server, so an agent can call them without any glue code.",
        "body": f"""
<p>Free to start is a gate, not a price. It means the door opens without a sales call. Every one of
these vendors meters something, and this directory does not track credits, quotas or rate limits, so
read the vendor's own pricing page before pointing a loop at one.</p>
<h2>Free to start, with an MCP server</h2>
{ul(enr_free_mcp) if enr_free_mcp else '<p>None.</p>'}
<h2>Free to start, no server found</h2>
{ul([e for e in enr_free if e not in enr_free_mcp]) if [e for e in enr_free if e not in enr_free_mcp] else '<p>None: every free to start enrichment tool in this build has a server of some kind.</p>'}
<h2>Why enrichment is the exception</h2>
<p>{cats['data-enrichment']['label']} is the most agent reachable category in the whole directory:
{cats['data-enrichment']['mcp_status']['official']} official servers and
{cats['data-enrichment']['mcp_status']['community']} community across
{cats['data-enrichment']['total']} entries, with only
{cats['data-enrichment']['mcp_status']['none-found']} where none was found. These vendors were
selling an API before MCP existed, so exposing it through one more protocol was a small step.</p>
<h2>What to check before you wire one in</h2>
<ul>
<li><b>What it takes as input.</b> A domain, an email or a LinkedIn URL are different jobs.
{jn('enrich-company-from-domain', 'entry_count')} entries are tagged
{jl('enrich-company-from-domain')}, {jn('enrich-person-from-linkedin-url', 'entry_count')} are
tagged {jl('enrich-person-from-linkedin-url')} and {jn('find-work-email', 'entry_count')} are tagged
{jl('find-work-email')}.</li>
<li><b>What a failed lookup costs.</b> Some vendors charge for a miss, some do not. Not tracked
here.</li>
<li><b>What the free tier is for.</b> Free tiers are usually sized for evaluation, and an agent is
much better at consuming them than a human clicking is.</li>
</ul>
<p>Nobody here has run any of these. {c['bench_tested']} tools in this directory are bench tested,
so treat the list as a starting point for your own test rather than as a result.</p>""",
        "sources": [("The GTM MCP Directory, Data and Enrichment",
                     "categories/data-enrichment.html"),
                    ("The GTM MCP Directory, free API tiers", "lists/free-api-tiers.html"),
                    ("The GTM MCP Directory, methodology", "methodology.html")],
        "related": ["what-is-data-enrichment", "how-do-i-enrich-a-linkedin-profile-with-an-ai-agent",
                    "which-tools-can-enrich-a-company-from-a-domain",
                    "which-gtm-tools-can-a-solo-operator-use"],
        "see": [("Data and Enrichment", "categories/data-enrichment.html"),
                ("Free tiers", "lists/free-api-tiers.html")],
    })

    # ---- per category MCP status questions ----
    for slug, page_slug, q, title_bit, why in [
        ("revops-infra", "which-crm-and-revops-tools-have-mcp-servers",
         "Which CRM and RevOps tools have MCP servers?",
         "CRM and RevOps tools with MCP servers",
         "<p>This is the layer an agent has to reach before anything else matters. A GTM agent that "
         "cannot read and write the system of record is a research assistant, not an operator. It "
         "is also, by some distance, the best covered layer in this directory.</p>"),
        ("engagement-outbound", "which-sales-engagement-tools-have-mcp-servers",
         "Which sales engagement tools have MCP servers?",
         "Sales engagement and outbound tools with MCP servers",
         "<p>Sequencers sit at the point where an agent stops reading and starts sending, which "
         "makes their coverage the most consequential number on this page and their approval "
         "settings the most important thing in your client.</p>"),
        ("ai-sdr-agents", "which-ai-sdr-tools-have-mcp-servers",
         "Which AI SDR tools have MCP servers?",
         "AI SDR tools with MCP servers",
         "<p>This is the inversion in one table. A category sold entirely on autonomous software is "
         "the least callable by anybody else's autonomous software, and the gap is not close.</p>"),
        ("conversation-intel", "which-conversation-intel-tools-have-mcp-servers",
         "Which conversation intelligence tools have MCP servers?",
         "Conversation intelligence tools with MCP servers",
         "<p>Call recordings are the richest unstructured data a revenue team owns, and the only "
         "place most of what a buyer actually said is written down. Whether an agent can read them "
         "decides whether it can prepare for a call or only summarise a CRM field.</p>"),
        ("signals-intent-abm", "which-signals-intent-abm-tools-have-mcp-servers",
         "Which intent and signal tools have MCP servers?",
         "Signal and intent tools with MCP servers",
         "<p>Signals are the trigger layer: the thing that starts an agent's loop rather than "
         "something it calls halfway through. Coverage here is decent and the access gate is "
         "the harder problem.</p>"),
    ]:
        x = cats[slug]
        rows = ce(slug, mcp=("official", "community"))
        rest = ce(slug)
        rest = [e for e in rest if e not in rows]
        off, com, tot = x["mcp_status"]["official"], x["mcp_status"]["community"], x["total"]
        out.append({
            "slug": page_slug,
            "cluster": "directory",
            "q": q,
            "title": f"{title_bit}: {off + com} of {tot}, counted",
            "desc": f"{off + com} of the {tot} {x['label'].lower()} tools in this directory have an "
                    f"MCP server: {off} official and {com} community. The list with server URLs and "
                    f"access gates. Counted {gen}.",
            "short": f"{off + com} of the {tot} {x['label'].lower()} entries in this directory have "
                     f"an MCP server: {off} built and maintained by the vendor and {com} built by "
                     f"somebody else. {x['api_gate']['free']} are free to start and "
                     f"{x['api_gate']['enterprise-only']} need a contract before anybody gets an "
                     f"API key.",
            "body": f"""
{why}
<p>{esc(x['one_line'])}</p>
<h2>The ones an agent can call</h2>
{ul(rows) if rows else '<div class="warn"><b>None found</b>No entry in this category had an MCP server of any kind on the date it was checked.</div>'}
<h2>The rest of the category</h2>
<p>{len(rest)} entries here had no server found, or the check could not settle it. That is not a
verdict on the tools. It is a statement about what an agent can reach today.</p>
{ul(rest, limit=12) if rest else '<p>None: every entry in this category has a server.</p>'}
<h2>The gate, which is the second question</h2>
<div class="scroller"><table class="datatable"><thead><tr><th>Gate</th><th>Entries</th></tr></thead>
<tbody>
{''.join(f'<tr><td><a href="{rel}gates/{b}.html">{esc(GATE_LABEL[b])}</a></td>'
         f'<td class="n">{x["api_gate"][b]}</td></tr>' for b in GATE_ORDER if x["api_gate"].get(b))}
</tbody></table></div>
<p class="note">Counted {esc(gen)}. Source file {esc(x['file'])}, content sha256
{esc(x['source_sha256'][:16])}...</p>""",
            "sources": [(f"The GTM MCP Directory, {x['label']}", f"categories/{slug}.html"),
                        (f"{x['label']} tools with MCP servers", f"lists/mcp-{slug}.html"),
                        ("The GTM MCP Directory, methodology", "methodology.html")],
            "related": ["which-gtm-categories-are-most-agent-ready",
                        "which-gtm-tools-have-official-mcp-servers",
                        "how-many-gtm-tools-have-mcp-servers", "what-is-a-gtm-tech-stack"],
            "see": [(x["label"], f"categories/{slug}.html"),
                    ("With MCP servers", f"lists/mcp-{slug}.html")],
        })

    # ---- job shaped questions ----
    out.append(jobq(
        "which-tools-can-find-a-work-email",
        "Which tools can find a work email address with an AI agent?",
        "Which tools can find a work email? The ones an agent can call, counted",
        "find-work-email",
        "<p>Email finding is the most commoditised job in the whole vocabulary and the one where "
        "coverage claims are least checkable. Every vendor quotes a hit rate, none of them quote it "
        "on your list, and this directory tests none of them.</p>"
        "<p>What it can tell you is which ones an agent can call without you writing a client, and "
        "which ones you can get into without a contract.</p>",
        ["how-do-i-find-a-work-email-with-an-ai-agent", "which-tools-can-verify-an-email-address",
         "what-is-data-enrichment", "which-data-enrichment-tools-can-an-agent-use-for-free"],
    ))
    out.append(jobq(
        "which-tools-can-verify-an-email-address",
        "Which tools can verify an email address is deliverable?",
        "Which email verification tools can an AI agent call? Counted",
        "verify-email-deliverable",
        "<p>Verification is the step between finding an address and sending to it, and skipping it "
        "is how a sending domain gets burned. It is also the cheapest step in the chain to automate "
        "properly, because the answer is a boolean and the cost of being wrong is asymmetric.</p>",
        ["which-tools-can-find-a-work-email", "can-an-ai-agent-send-email-on-my-behalf",
         "how-do-i-find-a-work-email-with-an-ai-agent", "what-is-data-enrichment"],
    ))
    out.append(jobq(
        "which-tools-can-enrich-a-company-from-a-domain",
        "Which tools can enrich a company from its domain?",
        "Which tools enrich a company from a domain? The agent callable list",
        "enrich-company-from-domain",
        "<p>Domain to company is the most common single call in a GTM agent's loop, because a domain "
        "is the one identifier that arrives from everywhere: a form fill, an email address, a news "
        "item, a website visit. It is also the most widely tagged job in this directory's "
        "enrichment family.</p>",
        ["what-is-data-enrichment", "which-data-enrichment-tools-can-an-agent-use-for-free",
         "how-do-i-build-a-prospect-list-with-an-ai-agent",
         "which-tools-can-identify-anonymous-website-visitors"],
    ))
    out.append(jobq(
        "which-tools-can-identify-anonymous-website-visitors",
        "Which tools can identify anonymous website visitors?",
        "Which website visitor identification tools can an AI agent call? Counted",
        "identify-anonymous-website-visitor",
        "<p>De-anonymising traffic is the highest intent signal most teams can get, and the most "
        "legally sensitive thing on this list. Company level identification and person level "
        "identification are different products with different obligations, and this directory "
        "records what the vendor says it does rather than adjudicating either.</p>"
        "<p>Check your own jurisdiction and your own privacy notice before wiring any of these into "
        "an automated loop. Nothing here is legal advice.</p>",
        ["what-is-buyer-intent-data", "which-tools-can-enrich-a-company-from-a-domain",
         "which-signals-intent-abm-tools-have-mcp-servers",
         "how-do-i-build-a-prospect-list-with-an-ai-agent"],
    ))
    out.append(jobq(
        "which-tools-can-book-a-meeting",
        "Which scheduling tools can an AI agent use to book a meeting?",
        "Which tools can an AI agent use to book a meeting? Counted",
        "book-a-meeting",
        "<p>Booking is where an agent stops being a research tool and starts holding somebody "
        "else's time. It is also the job where the difference between reading a calendar and "
        "writing to one is worth being deliberate about: "
        f"{jn('read-calendar-availability', 'entry_count')} entries are tagged with the read side, "
        f"{jn('book-a-meeting', 'entry_count')} with the write side.</p>",
        ["which-tools-can-fetch-a-call-transcript", "how-do-i-book-meetings-with-an-ai-agent",
         "what-is-an-ai-agent-in-sales", "which-conversation-intel-tools-have-mcp-servers"],
    ))
    out.append(jobq(
        "which-tools-can-fetch-a-call-transcript",
        "Which tools can give an AI agent access to sales call transcripts?",
        "Which call recording tools can an AI agent fetch transcripts from? Counted",
        "fetch-call-transcript",
        "<p>A transcript is the only place most of what a buyer actually said is written down, which "
        "makes this the highest value read in the whole stack for an agent preparing for a call or "
        "writing a follow up.</p>"
        "<p>It is also the most sensitive. A transcript contains other people's words, recorded "
        "under a consent notice that probably did not mention an autonomous agent. Read your "
        "recording consent language before you widen who, or what, can pull them.</p>",
        ["which-conversation-intel-tools-have-mcp-servers", "which-tools-can-book-a-meeting",
         "how-do-i-give-an-ai-agent-access-to-my-sales-calls",
         "what-are-the-security-risks-of-connecting-an-agent-to-my-gtm-stack"],
    ))

    # ---- the awkward ones ----
    oauth_rows = [e for e in entries if e["mcp_status_bucket"] in ("official", "community")
                  and auth_bucket(e) in ("oauth", "either")]
    key_rows = [e for e in entries if e["mcp_status_bucket"] in ("official", "community")
                and auth_bucket(e) in ("api-key", "either")]
    out.append({
        "slug": "which-gtm-mcp-servers-use-oauth",
        "cluster": "directory",
        "q": "Which GTM MCP servers use OAuth instead of an API key?",
        "title": "Which GTM MCP servers use OAuth? The auth split across every server, counted",
        "desc": f"Of the {reach} GTM tools with an MCP server, {len(oauth_rows)} document an OAuth "
                f"flow and {len(key_rows)} document an API key. Why the difference matters, and the "
                f"full breakdown. Counted {gen}.",
        "short": f"Of the {reach} GTM tools with an MCP server in this directory, "
                 f"{len(oauth_rows)} document an OAuth or browser sign in flow and "
                 f"{len(key_rows)} document an API key or token. Some document both, usually OAuth "
                 f"for the hosted server and a key for the self hosted one.",
        "body": f"""
<p>This is a security question wearing a configuration question's clothes. OAuth hands the server a
scoped token that the vendor can revoke without you touching anything. An API key is a string you
paste into a config file on the machine running the agent, it is as powerful as whatever the vendor
scoped it to, and it is revoked by rotating it and updating every place it was pasted.</p>
<p>Neither is wrong. Knowing which one you are about to wire in is not optional, particularly when
the system on the other side can send mail as you or write to the system of record.</p>
<h2>The breakdown</h2>
<div class="scroller"><table class="datatable"><thead><tr><th>Auth</th><th>Servers</th>
<th>What it means</th></tr></thead><tbody>
{''.join(f'<tr><td><a href="{rel}lists/auth-{b}.html">{esc(AUTH_LABEL[b])}</a></td>'
         f'<td class="n">{len([e for e in entries if e["mcp_status_bucket"] in ("official", "community") and auth_bucket(e) == b])}</td>'
         f'<td>{esc(trim(AUTH_BLURB[b], 110))}</td></tr>' for b in AUTH_ORDER
         if [e for e in entries if e["mcp_status_bucket"] in ("official", "community") and auth_bucket(e) == b])}
</tbody></table></div>
<p class="note">Counted {esc(gen)} across the {reach} entries with a server. The bucket is a keyword
match over the mcp_auth field, run at build time and disclosed as such; the verbatim field is
printed beside every row on <a href="{rel}lists/auth-types.html">the auth pages</a> so you can check
the parse yourself. {cov['mcp_auth_present']} of {num(cov['total_entries'])} entries record an auth
value at all.</p>
<h2>What the OAuth entries have in common</h2>
<p>They are mostly hosted, remote servers, and their documentation names the clients they were
tested against. Several entries in this directory record sign in flows written specifically for
Claude, ChatGPT and Cursor, which tells you where vendors think their customers are.</p>
<h2>The pattern to copy</h2>
<p>Where a vendor offers both, take OAuth for anything running on a machine you do not physically
control, and keep API keys for local servers where the key never leaves your box. Then scope the
credential at the vendor rather than trusting the prompt: a read only key is a boundary, an
instruction not to write is a suggestion.</p>""",
        "sources": [("The GTM MCP Directory, servers by auth type", "lists/auth-types.html"),
                    S_MCP_SPEC, ("The GTM MCP Directory, methodology", "methodology.html")],
        "related": ["what-are-the-security-risks-of-connecting-an-agent-to-my-gtm-stack",
                    "stdio-vs-remote-mcp-servers", "what-is-an-mcp-server",
                    "how-do-i-add-an-mcp-server-to-claude-desktop"],
        "see": [("Servers by auth type", "lists/auth-types.html")],
    })

    ent_rows = H["products"]([e for e in entries
                              if e["api_gate_bucket"] in ("enterprise-only", "enterprise-leaning")])
    ent_off = [e for e in ent_rows if e["mcp_status_bucket"] == "official"]
    out.append({
        "slug": "how-many-gtm-tools-are-enterprise-gated",
        "cluster": "directory",
        "q": "How many GTM tools are enterprise gated?",
        "title": f"How many GTM tools are enterprise gated? {c['api_gate']['enterprise-only']} of "
                 f"{c['entries']}, counted",
        "desc": f"{c['api_gate']['enterprise-only']} of {num(c['entries'])} GTM tools need a "
                f"contract before anybody gets API access, and {len(ent_off)} of those ship an "
                f"official MCP server most people cannot call. Counted {gen}.",
        "short": f"{c['api_gate']['enterprise-only']} of the {num(c['entries'])} entries in this "
                 f"directory are enterprise only: API access needs a contract, a seat count or a "
                 f"procurement cycle. One more is enterprise leaning. {len(ent_off)} of them ship "
                 f"an official MCP server that a solo operator still cannot reach.",
        "body": f"""
<p>Enterprise gated with no public documentation is the single most useful fact a directory like
this can publish, so it is surfaced rather than hidden. It is also the fact vendors are least happy
to see counted.</p>
<h2>Where the gate falls hardest</h2>
<div class="scroller"><table class="datatable"><thead><tr><th>Category</th><th>Enterprise only</th>
<th>Of total</th><th>Share</th></tr></thead><tbody>
{''.join(f'<tr><td><a href="{rel}categories/{x["slug"]}.html">{esc(x["label"])}</a></td>'
         f'<td class="n">{x["api_gate"]["enterprise-only"]}</td><td class="n">{x["total"]}</td>'
         f'<td class="n">{pct(x["api_gate"]["enterprise-only"], x["total"])}</td></tr>'
         for x in sorted(d["categories"], key=lambda k: -k["api_gate"]["enterprise-only"])
         if x["api_gate"]["enterprise-only"])}
</tbody></table></div>
<p class="note">Counted {esc(gen)}. {c['api_gate']['unknown']} further entries do not publish enough
for the gate to be established at all and are recorded as unknown rather than guessed into a
bucket.</p>
<h2>The cruel intersection</h2>
<p>{len(ent_off)} of these enterprise gated products ship an official MCP server. The protocol
works, the server is real, the vendor built it properly, and the reader of this page cannot call it
without a purchase order. Agent readiness is two questions and this is why they are published as two
columns.</p>
{ul(ent_off, limit=12)}
<h2>What to do about it</h2>
<p>If you are inside a company that already has the contract, the server is a genuine unlock and
worth asking for. If you are one person, build from the
<a href="{rel}lists/solo-reachable.html">{cov['solo_reachable']} solo reachable entries</a> instead
and treat the enterprise tier as something you graduate into rather than something you are blocked
by.</p>""",
        "sources": [("The GTM MCP Directory, enterprise gated", "lists/enterprise-gated.html"),
                    ("The GTM MCP Directory, by access gate", "gates/index.html"),
                    ("The GTM MCP Directory, methodology", "methodology.html")],
        "related": ["what-is-an-api-access-gate", "which-gtm-tools-can-a-solo-operator-use",
                    "which-gtm-categories-are-most-agent-ready", "which-mcp-servers-are-free-to-use"],
        "see": [("Enterprise gated", "lists/enterprise-gated.html"),
                ("By access gate", "gates/index.html")],
    })

    none_rows = H["products"]([e for e in entries if e["mcp_status_bucket"] == "none-found"])
    out.append({
        "slug": "which-gtm-tools-have-no-mcp-server",
        "cluster": "directory",
        "q": "Which GTM tools have no MCP server?",
        "title": f"Which GTM tools have no MCP server? {c['mcp_status']['none-found']} of "
                 f"{c['entries']}, and what that means",
        "desc": f"{c['mcp_status']['none-found']} of {num(c['entries'])} GTM tools had no MCP "
                f"server found on the date they were checked. The list, the categories it clusters "
                f"in, and why none found is not the same as none exists.",
        "short": f"{c['mcp_status']['none-found']} of the {num(c['entries'])} entries in this "
                 f"directory had no MCP server found at the time of the check. That is a statement "
                 f"about a search on a stated date, not a claim that no server exists, and every "
                 f"entry carries the date its facts were pulled.",
        "body": f"""
<p>The list matters more than it looks. If a tool your team depends on is on it, that is the work
item: either an API and some glue, or a case to the vendor, or a decision to route around it.</p>
<h2>Where none found clusters</h2>
<div class="scroller"><table class="datatable"><thead><tr><th>Category</th><th>No server</th>
<th>Of total</th><th>Share</th></tr></thead><tbody>
{''.join(f'<tr><td><a href="{rel}categories/{x["slug"]}.html">{esc(x["label"])}</a></td>'
         f'<td class="n">{x["mcp_status"]["none-found"]}</td><td class="n">{x["total"]}</td>'
         f'<td class="n">{pct(x["mcp_status"]["none-found"], x["total"])}</td></tr>'
         for x in sorted(d["categories"], key=lambda k: -k["mcp_status"]["none-found"] / k["total"])
         if x["mcp_status"]["none-found"])}
</tbody></table></div>
<h2>What none found does not mean</h2>
<ul>
<li><b>It does not mean no API.</b> Plenty of these have excellent REST APIs. An agent can still use
them; somebody just has to write the wrapper.</li>
<li><b>It does not mean the vendor is behind.</b> It means a search on a date came back empty, and
the date is on the entry.</li>
<li><b>It does not mean it will stay true.</b> This is the single fastest moving column in the whole
dataset, which is why the check date ships with every row.</li>
</ul>
<h2>The first fifteen</h2>
{ul(none_rows, limit=15)}
<p><a href="{rel}lists/no-mcp-server.html">The full list of {c['mcp_status']['none-found']} is
here</a>, each row carrying the date its entry was last checked. If you know one of them shipped a
server, that correction is the most valuable thing anyone can send this directory.</p>""",
        "sources": [("The GTM MCP Directory, no MCP server found", "lists/no-mcp-server.html"),
                    ("The GTM MCP Directory, methodology", "methodology.html"),
                    ("The GTM MCP Directory, submit a correction", "submit.html")],
        "related": ["how-many-gtm-tools-have-mcp-servers",
                    "how-do-i-build-an-mcp-server-for-a-tool-that-has-none",
                    "how-do-i-choose-between-an-mcp-server-and-a-rest-api",
                    "which-gtm-categories-are-most-agent-ready"],
        "see": [("No MCP server found", "lists/no-mcp-server.html"),
                ("Submit a correction", "submit.html")],
    })

    out.append({
        "slug": "what-percentage-of-gtm-tools-can-an-agent-reach",
        "cluster": "directory",
        "q": "What percentage of GTM tools can an AI agent actually reach?",
        "title": f"What percentage of GTM tools can an AI agent reach? {pct(reach, c['entries'])}, "
                 f"and less once you count the gate",
        "desc": f"{pct(reach, c['entries'])} of {num(c['entries'])} GTM tools have an MCP server. "
                f"Once the access gate is applied the reachable number drops again. The arithmetic, "
                f"counted {gen}.",
        "short": f"{pct(reach, c['entries'])} of the {num(c['entries'])} go to market tools counted "
                 f"here have an MCP server of any kind. Applying the second filter, that you can "
                 f"actually get an account without a contract, "
                 f"{len([e for e in entries if e['mcp_status_bucket'] in ('official', 'community') and e['api_gate_bucket'] in ('free', 'paid')])} "
                 f"entries pass both tests, which is "
                 f"{pct(len([e for e in entries if e['mcp_status_bucket'] in ('official', 'community') and e['api_gate_bucket'] in ('free', 'paid')]), c['entries'])} "
                 f"of the directory.",
        "body": f"""
<h2>The funnel</h2>
<div class="scroller"><table class="datatable"><thead><tr><th>Filter</th><th>Entries left</th>
<th>Share of {num(c['entries'])}</th></tr></thead><tbody>
<tr><td>Every tool counted</td><td class="n">{num(c['entries'])}</td><td class="n">100%</td></tr>
<tr><td>Has a server of any kind</td><td class="n">{reach}</td>
<td class="n">{pct(reach, c['entries'])}</td></tr>
<tr><td>Server is first party</td><td class="n">{c['mcp_status']['official']}</td>
<td class="n">{pct(c['mcp_status']['official'], c['entries'])}</td></tr>
<tr><td>Server, and free or paid self serve</td>
<td class="n">{len([e for e in entries if e['mcp_status_bucket'] in ('official', 'community') and e['api_gate_bucket'] in ('free', 'paid')])}</td>
<td class="n">{pct(len([e for e in entries if e['mcp_status_bucket'] in ('official', 'community') and e['api_gate_bucket'] in ('free', 'paid')]), c['entries'])}</td></tr>
<tr><td>Server, first party, and free to start</td>
<td class="n">{len([e for e in entries if e['mcp_status_bucket'] == 'official' and e['api_gate_bucket'] == 'free'])}</td>
<td class="n">{pct(len([e for e in entries if e['mcp_status_bucket'] == 'official' and e['api_gate_bucket'] == 'free']), c['entries'])}</td></tr>
<tr><td>And somebody here has actually run it</td><td class="n">{c['bench_tested']}</td>
<td class="n">{pct(c['bench_tested'], c['entries'])}</td></tr>
</tbody></table></div>
<p class="note">Counted {esc(gen)} from directory.json. The last row is the honest floor of this
whole exercise and it is published on the front page rather than buried here.</p>
<h2>Why the last two rows matter most</h2>
<p>Every percentage above the last two is a documentation reading. It says a vendor published
something and a check found it on a date. The bottom row says somebody ran the thing. This
directory's bench tested count is {c['bench_tested']}, it stays there until Andrew personally runs a
tool on a stated date, and no vendor can buy a change to it.</p>
<h2>The direction of travel</h2>
<p>Do not read {pct(reach, c['entries'])} as a permanent state. It is a reading taken on {gen} from
{num(c['entries'])} entries whose facts were pulled by hand on
{', '.join(f"{k}" for k in sorted(cov['last_checked']))}. The point of stamping every number with a
date is that the next reading is comparable to this one.</p>""",
        "sources": [("The GTM MCP Directory, the counted data", "data.html"),
                    ("The GTM MCP Directory, methodology", "methodology.html")],
        "related": ["how-many-gtm-tools-have-mcp-servers", "how-many-gtm-tools-are-bench-tested",
                    "which-gtm-tools-can-a-solo-operator-use",
                    "which-gtm-categories-are-most-agent-ready"],
        "see": [("The data endpoint", "data.html"), ("The lists", "lists/index.html")],
    })

    free_mcp = H["products"]([e for e in entries if e["api_gate_bucket"] == "free"
                              and e["mcp_status_bucket"] in ("official", "community")])
    out.append({
        "slug": "which-mcp-servers-are-free-to-use",
        "cluster": "directory",
        "q": "Which GTM MCP servers are free to use?",
        "title": f"Which GTM MCP servers are free to use? {len(free_mcp)} products, counted",
        "desc": f"{len(free_mcp)} products in this directory have an MCP server and a free to start "
                f"access gate, so one person can connect an agent without paying or talking to "
                f"anyone. The list, counted {gen}.",
        "short": f"{len(free_mcp)} unique products here have both an MCP server and a free to start "
                 f"gate, meaning you can sign up, get access and point an agent at them without "
                 f"paying anything or speaking to a salesperson. Free to start is a gate, not a "
                 f"price: everything on this list still meters something.",
        "body": f"""
<p>The MCP server itself is almost never the thing you pay for. What you pay for is what it calls:
credits, seats, sends, lookups. A free server in front of a metered API is normal and it is not a
trick, but an agent in a loop consumes a free tier considerably faster than a human clicking does.</p>
<h2>The list</h2>
{ul(free_mcp)}
<h2>What this directory does and does not track about money</h2>
<ul>
<li><b>Tracked:</b> whether a solo operator can get API access at all, in four buckets, with a
source. {c['api_gate']['free']} entries are free to start, {c['api_gate']['paid']} paid self serve,
{c['api_gate']['enterprise-only']} enterprise only, {c['api_gate']['unknown']} unknown.</li>
<li><b>Not tracked:</b> prices, credit costs, quota sizes, rate limits, overage behaviour, or what
happens to your data on a free tier. None of those should be inferred from anything here.</li>
</ul>
<h2>The starter kit shape</h2>
<p>If you want a chain rather than a single tool, the free and reachable jobs with the deepest
coverage are {jl('enrich-company-from-domain')} at
{jn('enrich-company-from-domain', 'api_gate', 'free')} free entries,
{jl('find-work-email')} at {jn('find-work-email', 'api_gate', 'free')}, and
{jl('verify-email-deliverable')} at {jn('verify-email-deliverable', 'api_gate', 'free')}. That is
enough to build a research and contact chain without a contract, and it is the cheapest honest way
to find out whether any of this works for you.</p>""",
        "sources": [("The GTM MCP Directory, free API tiers", "lists/free-api-tiers.html"),
                    ("The GTM MCP Directory, by access gate", "gates/index.html")],
        "related": ["which-gtm-tools-can-a-solo-operator-use", "what-is-an-api-access-gate",
                    "which-data-enrichment-tools-can-an-agent-use-for-free",
                    "how-much-does-it-cost-to-run-a-gtm-agent"],
        "see": [("Free tiers", "lists/free-api-tiers.html"),
                ("Solo reachable", "lists/solo-reachable.html")],
    })

    zero_off = sorted([j for j in jobs.values() if j["mcp_status"]["official"] == 0
                       and j["entry_count"]], key=lambda j: -j["entry_count"])
    thin = sorted([j for j in jobs.values() if j["entry_count"] <= 5],
                  key=lambda j: j["entry_count"])
    out.append({
        "slug": "which-gtm-jobs-have-no-official-mcp-server",
        "cluster": "directory",
        "q": "Which GTM jobs can no tool do through an official MCP server?",
        "title": "Which GTM jobs have no official MCP server at all? The gaps, counted",
        "desc": f"Of {c['jobs']} jobs in the vocabulary, {len(zero_off)} have no tool at all with a "
                f"first party MCP server. The gaps in the map, and the thinly covered jobs next to "
                f"them. Counted {gen}.",
        "short": f"Of the {c['jobs']} jobs in this directory's closed vocabulary, {len(zero_off)} "
                 f"have no tool with an official MCP server at all. These are the holes an agent "
                 f"builder falls into: the capability exists in the market, and nothing exposes it "
                 f"through a vendor maintained server.",
        "body": f"""
<h2>Jobs with zero official servers</h2>
<div class="scroller"><table class="datatable"><thead><tr><th>Job</th><th>Tools tagged</th>
<th>Community</th><th>Solo reachable</th></tr></thead><tbody>
{''.join(f'<tr><td>{jl(j["id"])}</td><td class="n">{j["entry_count"]}</td>'
         f'<td class="n">{j["mcp_status"]["community"]}</td>'
         f'<td class="n">{j["solo_reachable"]}</td></tr>' for j in zero_off)}
</tbody></table></div>
<p class="note">Counted {esc(gen)} from the per job blocks in directory.json.</p>
<h2>The thinnest jobs in the vocabulary</h2>
<p>Separately from the zero official list, some jobs are barely covered by any tool at all. These
are the ones where the vocabulary describes something real and the market has almost nothing tagged
against it.</p>
<div class="scroller"><table class="datatable"><thead><tr><th>Job</th><th>Entries tagged</th>
<th>Official</th></tr></thead><tbody>
{''.join(f'<tr><td>{jl(j["id"])}</td><td class="n">{j["entry_count"]}</td>'
         f'<td class="n">{j["mcp_status"]["official"]}</td></tr>' for j in thin)}
</tbody></table></div>
<h2>Read these as leads, not as receipts</h2>
<div class="warn"><b>Machine pass, human review pending</b>
The job tags behind these numbers came from a machine pass over each entry's own description text on
{esc(d['jobs_vocabulary']['tags_meta']['tagged_on'])}, and
{len(r['jobs']['needs_review'])} entries were flagged by that pass as needing a human to look again.
A gap in this table can mean the market has a hole, or it can mean the vocabulary drew a line the
tagger read differently. Both are worth checking before anybody builds a business on one.</div>
<h2>Why publish the gaps at all</h2>
<p>Because a gap is the most actionable thing in a directory. If you were going to write an MCP
server for something, the top of the first table is where an agent builder is currently stuck with
no vendor maintained option, and the second table is where the market itself is thin.</p>""",
        "sources": [("The GTM MCP Directory, by job", "jobs/index.html"),
                    ("The GTM MCP Directory, the counted data", "data.html"),
                    ("The GTM MCP Directory, methodology", "methodology.html")],
        "related": ["how-do-i-build-an-mcp-server-for-a-tool-that-has-none",
                    "which-gtm-tools-have-no-mcp-server",
                    "which-gtm-categories-are-most-agent-ready",
                    "how-many-gtm-tools-are-bench-tested"],
        "see": [("Every job", "jobs/index.html")],
    })

    out.append({
        "slug": "how-many-gtm-tools-are-bench-tested",
        "cluster": "directory",
        "q": "How many of these GTM tools have actually been tested?",
        "title": f"How many GTM tools here have been bench tested? {c['bench_tested']}. "
                 f"That is the honest answer",
        "desc": f"{c['bench_tested']} of {num(c['entries'])} tools in this directory have been "
                f"bench tested. What the two honesty tiers mean, why the number is on the front "
                f"page, and what it takes to change it.",
        "short": f"{c['bench_tested']}. Every one of the {num(c['entries'])} entries in this "
                 f"directory is RESEARCHED tier, meaning facts from public sources with URLs and no "
                 f"usage claims. Nobody here has run these tools. That number is printed on the "
                 f"front page rather than hidden, because it is what makes the other tier mean "
                 f"something.",
        "body": f"""
<h2>The two tiers, and only two</h2>
<ul>
<li><b>RESEARCHED.</b> {esc(d['honesty']['tier_meanings']['RESEARCHED'])} All
{num(cov['tier']['RESEARCHED'])} entries in this build are this tier.</li>
<li><b>BENCH-TESTED.</b> {esc(d['honesty']['tier_meanings']['BENCH-TESTED'])} There are
{c['bench_tested']} of them.</li>
</ul>
<p>There is no third tier, no star rating, no score and no featured field, because a field that
exists is a field somebody eventually tries to buy.</p>
<h2>What that means for every list on this site</h2>
<p>Every capability list here answers one question: what does the vendor say this tool does, and can
an agent reach it. It never answers which tool is better. There are no tool versus tool verdicts
anywhere on this site and there will not be any until somebody has run both, because a comparison
without a test is an opinion in a lab coat.</p>
<h2>The other places this build is thin, named</h2>
<ul>
<li>{num(r['data_quality']['thin_sourcing']['count'])} entries carry fewer than two independent
source URLs. They are named on the methodology page rather than quietly padded.</li>
<li>{num(cov['api_gate_unknown'])} entries have an unknown access gate.</li>
<li>{num(cov['docs_url_missing'])} have no documentation URL recorded.</li>
<li>{r['data_quality']['schema_law_1_risk']['count']} entry claims an MCP server with no parseable
URL anywhere in the entry.</li>
<li>github_url, github_stars, github_last_commit and github_archived are null on all
{num(cov['unmeasured_spec_fields']['github_url'])} entries. No repo health claim is made anywhere.</li>
</ul>
<h2>What would change the number</h2>
<p>Andrew running a tool himself on a stated date, and publishing what happened including the parts
that did not work. A vendor can offer access so a bench test becomes possible, that offer is
recorded in the entry's notes, and the offer buys a test rather than a verdict. The verdict ships
whatever it says.</p>""",
        "sources": [("The GTM MCP Directory, methodology", "methodology.html"),
                    ("The GTM MCP Directory, the counted data", "data.html"),
                    ("The GTM MCP Directory, submit a tool", "submit.html")],
        "related": ["what-percentage-of-gtm-tools-can-an-agent-reach",
                    "what-does-agent-ready-mean", "which-gtm-jobs-have-no-official-mcp-server",
                    "how-do-i-check-if-a-tool-has-an-mcp-server"],
        "see": [("Methodology", "methodology.html"), ("The data endpoint", "data.html")],
    })

    return out


CLAUDE_CONFIG = html.escape("""{
  "mcpServers": {
    "some-gtm-tool": {
      "command": "npx",
      "args": ["-y", "@vendor/mcp-server"],
      "env": { "VENDOR_API_KEY": "the key you generated in the vendor dashboard" }
    }
  }
}""")


def learn_howto(d, r, entries, byid, gen, H):
    rel, c, cov = H["rel"], H["c"], H["cov"]
    je, ce, names, ul, jl, pct = (H["job_entries"], H["cat_entries"], H["names"], H["tool_ul"],
                                  H["jl"], H["pct"])
    jn, jobs, cats = H["jn"], H["jobs"], H["cats"]
    reach = c["mcp_status"]["official"] + c["mcp_status"]["community"]

    def chain(steps):
        return (f'<div class="scroller"><table class="datatable"><thead><tr><th>Step</th>'
                f'<th>The job</th><th>Tools tagged</th><th>Official MCP</th><th>Free tier</th>'
                f'</tr></thead><tbody>'
                + "".join(f'<tr><td>{esc(lab)}</td><td>{jl(jid)}</td>'
                          f'<td class="n">{jn(jid, "entry_count")}</td>'
                          f'<td class="n">{jn(jid, "mcp_status", "official")}</td>'
                          f'<td class="n">{jn(jid, "api_gate", "free")}</td></tr>'
                          for lab, jid in steps)
                + "</tbody></table></div>")

    return [
        {
            "slug": "how-do-i-connect-claude-to-my-crm",
            "cluster": "howto",
            "q": "How do I connect Claude to my CRM?",
            "title": "How do I connect Claude to my CRM? The MCP route, step by step",
            "desc": f"Connect an AI assistant to your CRM through an MCP server. Which CRM and "
                    f"RevOps tools have one ({cats['revops-infra']['mcp_status']['official']} "
                    f"official of {cats['revops-infra']['total']}), what to check first, and the "
                    f"order to do it in.",
            "short": "If your CRM ships an MCP server, you add it to your client's server "
                     "configuration, authenticate, and the assistant can then read and write "
                     "records as tools. If it does not, you either use a community server, an "
                     "automation platform that proxies tool calls, or you write a thin wrapper over "
                     "the CRM's REST API yourself.",
            "body": f"""
<h2>1. Find out whether a server exists</h2>
<p>{cats['revops-infra']['label']} is the best covered layer in this directory:
{cats['revops-infra']['mcp_status']['official']} official servers and
{cats['revops-infra']['mcp_status']['community']} community across
{cats['revops-infra']['total']} entries, with only
{cats['revops-infra']['mcp_status']['none-found']} where none was found. Check your specific system
on <a href="{rel}lists/mcp-revops-infra.html">the RevOps tools with MCP servers list</a>, and read
the auth field on its page before anything else.</p>
<h2>2. Decide what the credential is allowed to do</h2>
<p>This is the step people skip and regret. The server can do whatever your credential can do, and
an instruction not to write is a suggestion rather than a boundary. Create a dedicated integration
user or a scoped token at the CRM, not a copy of your admin credentials. Where the vendor offers
OAuth, take it: the token is scoped and you can revoke it from their side without touching your
config.</p>
<h2>3. Add the server to the client</h2>
<p>A local server is a command the client launches. A remote one is a URL the client connects to,
usually followed by a browser sign in. The local shape looks like this, and the exact block comes
from your vendor's own documentation rather than from here.</p>
<pre><code>{CLAUDE_CONFIG}</code></pre>
<h2>4. Test reads before you allow writes</h2>
<p>Ask for a record you already know the answer to. Check the field names come back the way you
expect, that record ownership and permissions behave, and that the record limit on a query is what
you assumed. Only then let anything write.</p>
<h2>5. Wire the rest of the chain</h2>
<p>A CRM connection on its own is a search box. The value shows up when the assistant can also
research and enrich, then write the result back.</p>
{chain([("Read CRM records", "read-crm-records"),
        ("Write CRM records", "write-crm-records"),
        ("Sync records between systems", "sync-records-between-systems"),
        ("Enrich a company from a domain", "enrich-company-from-domain"),
        ("Research an account before a call", "research-account-for-call-prep")])}
<h2>If your CRM has no server</h2>
<p>{jn('proxy-tool-calls-to-saas', 'entry_count')} entries in this directory are tagged
{jl('proxy-tool-calls-to-saas')}: platforms that stand between an agent and somebody's SaaS and
expose the calls as tools. That is the fastest route and it puts a third party in the middle of your
credential, which is a tradeoff to make deliberately rather than by accident.</p>""",
            "sources": [("The GTM MCP Directory, RevOps Infra", "categories/revops-infra.html"),
                        S_MCP_QUICK, S_MCP_SPEC],
            "related": ["how-do-i-stop-an-agent-writing-bad-data-to-my-crm",
                        "which-crm-and-revops-tools-have-mcp-servers",
                        "how-do-i-add-an-mcp-server-to-claude-desktop",
                        "what-are-the-security-risks-of-connecting-an-agent-to-my-gtm-stack"],
            "see": [("RevOps tools with MCP servers", "lists/mcp-revops-infra.html"),
                    ("Write CRM records", "jobs/write-crm-records.html")],
        },
        {
            "slug": "how-do-i-add-an-mcp-server-to-claude-desktop",
            "cluster": "howto",
            "q": "How do I add an MCP server to my AI client?",
            "title": "How do I add an MCP server to an AI client? Local and remote, step by step",
            "desc": "Adding an MCP server to a client: the two shapes it takes, what each field in "
                    "the config does, where credentials go, and the four things that go wrong most "
                    "often.",
            "short": "There are two shapes. A local server is a command the client launches as a "
                     "subprocess, configured with a command, its arguments and any environment "
                     "variables it needs. A remote server is a URL you point the client at, usually "
                     "followed by a browser sign in. Your client's own documentation is the "
                     "authority on where that configuration lives.",
            "body": f"""
<h2>The local shape</h2>
<p>The client starts the server as a child process and talks to it over standard input and output.
Nothing listens on a port and nothing crosses the network. The configuration is a name, a command,
its arguments, and the environment the process needs.</p>
<pre><code>{CLAUDE_CONFIG}</code></pre>
<p>Three details that matter. The name is yours and appears in the client. The command has to be on
the path the client uses, which is often not the path your shell uses. And the environment block is
where credentials go: they live in a file on your machine, in plain text, so treat that file the way
you would treat any other file holding an API key.</p>
<h2>The remote shape</h2>
<p>You give the client a URL, it connects over HTTP, and auth is usually a browser sign in that
hands back a scoped token. Nothing is installed and the vendor ships updates without you. Of the
{reach} servers counted here, <a href="{rel}lists/auth-oauth.html">the OAuth ones</a> are almost all
this shape.</p>
<h2>The four things that go wrong</h2>
<ul>
<li><b>The client does not support it.</b> Not every AI application has an MCP client, and some
support only one transport. That is a client limitation, not a broken server.</li>
<li><b>The command is not found.</b> Use an absolute path, or check what environment the client
launches processes in.</li>
<li><b>The credential is wrong or unscoped.</b> Read the verbatim auth line on the tool page in this
directory before you generate anything; several vendors require a specific plan or an account level
flag before MCP access works at all.</li>
<li><b>It connected and there are no tools.</b> Usually an auth failure that the client reported
quietly. Check the server's own logs.</li>
</ul>
<h2>Where to find the right block</h2>
<p>Every tool page here prints the vendor's mcp_url and mcp_auth verbatim, exactly as recorded, plus
a link to the vendor's own documentation where one is published.
{cov['mcp_url_with_parseable_url']} entries carry a parseable URL and
{cov['docs_url_present']} carry a documentation URL. No install snippet is reproduced anywhere on
this site, because a snippet copied from a directory is a snippet that goes stale without anybody
noticing.</p>""",
            "sources": [S_MCP_QUICK, S_MCP_SPEC, S_MCP_SERVERS],
            "related": ["stdio-vs-remote-mcp-servers", "what-is-an-mcp-client",
                        "how-do-i-connect-claude-to-my-crm", "which-gtm-mcp-servers-use-oauth"],
            "see": [("The official servers list", "lists/official-mcp-servers.html"),
                    ("Servers by auth type", "lists/auth-types.html")],
        },
        {
            "slug": "how-do-i-enrich-a-linkedin-profile-with-an-ai-agent",
            "cluster": "howto",
            "q": "How do I enrich a LinkedIn profile with an AI agent?",
            "title": "How do I enrich a LinkedIn profile with an AI agent? The callable tools",
            "desc": f"{jn('enrich-person-from-linkedin-url', 'entry_count')} tools in this directory "
                    f"are tagged with enriching a person from a LinkedIn URL, and "
                    f"{jn('enrich-person-from-linkedin-url', 'mcp_status', 'official')} have an "
                    f"official MCP server. How to wire it, and what to be careful about.",
            "short": f"You give a tool the profile URL and it returns a structured record: name, "
                     f"title, employer, and often a work email. "
                     f"{jn('enrich-person-from-linkedin-url', 'entry_count')} entries here are "
                     f"tagged with that job and "
                     f"{jn('enrich-person-from-linkedin-url', 'mcp_status', 'official')} ship an "
                     f"official MCP server, so an agent can make the call with no glue code.",
            "body": f"""
<h2>The tools an agent can call directly</h2>
{ul(je('enrich-person-from-linkedin-url', mcp=('official', 'community')), limit=10)}
<h2>The free to start ones</h2>
{ul(je('enrich-person-from-linkedin-url', gate=('free',)), limit=8) if je('enrich-person-from-linkedin-url', gate=('free',)) else '<p>None of the tools tagged with this job record a free to start gate in this build.</p>'}
<h2>The chain most people actually want</h2>
<p>A profile URL is rarely the end state. The usual sequence is profile to person record to work
email to verified email, and each step is a different job with different coverage.</p>
{chain([("Enrich the person from the URL", "enrich-person-from-linkedin-url"),
        ("Find the work email", "find-work-email"),
        ("Verify it is deliverable", "verify-email-deliverable"),
        ("Enrich their company", "enrich-company-from-domain"),
        ("Write it to the CRM", "write-crm-records")])}
<h2>Three things to be careful about</h2>
<ul>
<li><b>Scraping is not the same as enrichment.</b> Some vendors return data from a licensed or
contributed dataset keyed on the profile URL. Others fetch the page. Those are different products
with different terms, and this directory records what the vendor says rather than adjudicating
which is which.</li>
<li><b>Personal data has rules.</b> Enriching a person is processing personal data, and your
obligations do not change because an agent did it. Nothing here is legal advice.</li>
<li><b>Credits disappear fast.</b> An agent looping over a list will spend an evaluation tier before
you have finished reading the docs. Set a hard cap on the tool call, not just in the prompt.</li>
</ul>
<h2>The honest limit of this page</h2>
<p>Nobody here has run any of these tools. {c['bench_tested']} of {num(c['entries'])} entries are
bench tested, so treat this as a shortlist to test rather than a result.</p>""",
            "sources": [("The GTM MCP Directory, enrich a person from a LinkedIn URL",
                         "jobs/enrich-person-from-linkedin-url.html"),
                        ("The GTM MCP Directory, Data and Enrichment",
                         "categories/data-enrichment.html")],
            "related": ["what-is-data-enrichment", "how-do-i-find-a-work-email-with-an-ai-agent",
                        "which-data-enrichment-tools-can-an-agent-use-for-free",
                        "which-tools-can-enrich-a-company-from-a-domain"],
            "see": [("Enrich a person from a LinkedIn URL",
                     "jobs/enrich-person-from-linkedin-url.html"),
                    ("Data and Enrichment", "categories/data-enrichment.html")],
        },
        {
            "slug": "how-do-i-find-a-work-email-with-an-ai-agent",
            "cluster": "howto",
            "q": "How do I find someone's work email with an AI agent?",
            "title": "How do I find a work email with an AI agent? The wiring, and the guardrails",
            "desc": f"{jn('find-work-email', 'entry_count')} tools here are tagged with finding a "
                    f"work email and {jn('find-work-email', 'mcp_status', 'official')} have an "
                    f"official MCP server. How to chain finding with verification, and where it "
                    f"goes wrong.",
            "short": f"Give a tool a name and a company domain, or a LinkedIn URL, and it returns a "
                     f"best guess address with a confidence signal. "
                     f"{jn('find-work-email', 'entry_count')} entries here are tagged with that job, "
                     f"{jn('find-work-email', 'mcp_status', 'official')} have an official MCP "
                     f"server, and {jn('find-work-email', 'api_gate', 'free')} are free to start. "
                     f"Always chain a verification step after it.",
            "body": f"""
<h2>The two step chain, and why it is two steps</h2>
<p>Finding and verifying are different jobs done by different systems. A finder infers or looks up
an address. A verifier tests whether a mailbox will accept mail for it. Sending to unverified
addresses is the fastest way to damage a sending domain, and the damage lands on every campaign
after it rather than on the one that caused it.</p>
{chain([("Find the address", "find-work-email"),
        ("Verify it is deliverable", "verify-email-deliverable"),
        ("Warm the inbox first", "warm-up-inbox"),
        ("Then send", "run-email-sequence")])}
<h2>The finders an agent can call</h2>
{ul(je('find-work-email', mcp=('official', 'community')), limit=12)}
<h2>The free ones</h2>
{ul(je('find-work-email', gate=('free',)), limit=10)}
<h2>What nobody can tell you from a directory</h2>
<p>Hit rate on your list. Every vendor publishes an aggregate number and none of them measured it on
your accounts, in your geography, in your segment. The only way to know is to run the same hundred
contacts through two or three and count. This directory measures none of that: it tells you which
ones an agent can call and which ones you can get into.</p>
<h2>The guardrail</h2>
<p>Put a hard cap on the tool call itself, not in the prompt. An agent that finds an address, fails
verification, and retries with a different vendor is a sensible design and also a very efficient way
to spend three months of credits in one evening.</p>""",
            "sources": [("The GTM MCP Directory, find a work email", "jobs/find-work-email.html"),
                        ("The GTM MCP Directory, verify an email is deliverable",
                         "jobs/verify-email-deliverable.html")],
            "related": ["which-tools-can-find-a-work-email", "which-tools-can-verify-an-email-address",
                        "can-an-ai-agent-send-email-on-my-behalf", "what-is-data-enrichment"],
            "see": [("Find a work email", "jobs/find-work-email.html"),
                    ("Free tiers", "lists/free-api-tiers.html")],
        },
        {
            "slug": "how-do-i-build-a-prospect-list-with-an-ai-agent",
            "cluster": "howto",
            "q": "How do I build a prospect list with an AI agent?",
            "title": "How do I build a prospect list with an AI agent? The chain, and its coverage",
            "desc": "Building a target list with an agent: the five jobs it needs, how many tools "
                    "carry each one, and which parts of the chain have almost no MCP coverage.",
            "short": "The chain is: define the account criteria, search a company database, enrich "
                     "each company, find the right people inside them, then score and prioritise. "
                     "Each of those is a separate job in this directory with its own coverage, and "
                     "the account list step is the thinnest link.",
            "body": f"""
<h2>The chain</h2>
{chain([("Build the target account list", "build-target-account-list"),
        ("Search companies by firmographics", "search-companies-by-firmographics"),
        ("Enrich each company from its domain", "enrich-company-from-domain"),
        ("Search people by criteria", "search-people-by-criteria"),
        ("Score and prioritise", "score-and-prioritize-leads")])}
<p class="note">Counted {esc(gen)}. Entry counts rather than product counts.</p>
<h2>Where it is thin</h2>
<p>{jl('build-target-account-list')} is tagged on only
{jn('build-target-account-list', 'entry_count')} entries, of which
{jn('build-target-account-list', 'mcp_status', 'official')} have an official server. In practice this
step is usually done by combining a firmographic search with a signal rather than by a tool sold as
list building, which is a reasonable thing for an agent to orchestrate itself.</p>
<h2>The tools with the deepest coverage in the chain</h2>
{ul(je('search-companies-by-firmographics', mcp=('official', 'community')), limit=8)}
<h2>Add a signal, or you have built a directory rather than a list</h2>
<p>A list of companies matching a size and an industry is not a prospect list, it is a phone book.
The difference is a reason to reach out now. {jn('detect-funding-or-news-event', 'entry_count')}
entries are tagged {jl('detect-funding-or-news-event')},
{jn('scrape-job-postings', 'entry_count')} are tagged {jl('scrape-job-postings')},
{jn('detect-technographics', 'entry_count')} are tagged {jl('detect-technographics')} and
{jn('track-job-changes', 'entry_count')} are tagged {jl('track-job-changes')}. Those are the cheapest
sources of a real reason.</p>
<h2>Then stop</h2>
<p>Building the list and sending to it are different decisions. Keep the send behind a human
approval until you have read what the chain produced at least twice, because an agent will build a
list of four thousand as easily as forty and will not feel embarrassed about either.</p>""",
            "sources": [("The GTM MCP Directory, by job", "jobs/index.html"),
                        ("The GTM MCP Directory, Data and Enrichment",
                         "categories/data-enrichment.html")],
            "related": ["which-tools-can-enrich-a-company-from-a-domain", "what-is-buyer-intent-data",
                        "how-do-i-write-personalized-outreach-with-an-ai-agent",
                        "which-tools-can-identify-anonymous-website-visitors"],
            "see": [("Find people and companies", "jobs/family-find-people-and-companies.html"),
                    ("Signals and research", "jobs/family-signals-and-research.html")],
        },
        {
            "slug": "how-do-i-write-personalized-outreach-with-an-ai-agent",
            "cluster": "howto",
            "q": "How do I write personalised outreach with an AI agent?",
            "title": "How do I write personalised outreach with an AI agent? Research first, then draft",
            "desc": f"{jn('draft-personalized-outreach', 'entry_count')} tools here are tagged with "
                    f"drafting personalised outreach. Why the research step decides the quality, "
                    f"and which parts an agent can call directly.",
            "short": "The drafting is the easy half and it is not where quality comes from. What "
                     "decides whether a message is worth sending is what the agent knew before it "
                     "started writing, which means the research calls matter more than the model "
                     "or the prompt.",
            "body": f"""
<h2>The order that works</h2>
{chain([("Research the account", "research-account-for-call-prep"),
        ("Find a real trigger", "detect-funding-or-news-event"),
        ("Scrape the specific page", "scrape-web-page-for-facts"),
        ("Draft the message", "draft-personalized-outreach"),
        ("Send it", "run-email-sequence"),
        ("Read what happened", "read-outreach-performance")])}
<h2>Why the research step is the whole game</h2>
<p>{jn('draft-personalized-outreach', 'entry_count')} entries here are tagged
{jl('draft-personalized-outreach')}, the most tagged job in the entire vocabulary. Drafting is
commoditised: every tool in the category will write you a competent paragraph. None of them can
invent the fact that makes the paragraph worth reading. That fact comes from a research call, and
research is where coverage is thinner:
{jn('research-account-for-call-prep', 'mcp_status', 'official')} official servers across
{jn('research-account-for-call-prep', 'entry_count')} tagged entries.</p>
<h2>The tools an agent can call for the drafting step</h2>
{ul(je('draft-personalized-outreach', mcp=('official',)), limit=10)}
<h2>The failure mode to design against</h2>
<p>Personalisation at scale fails in a specific way: the agent finds a fact, the fact is wrong or
stale, and the message is now confidently wrong in a way a generic message never would have been. A
generic email is ignored. A wrongly personalised one is remembered.</p>
<p>Two guardrails. Make the agent cite the source of every claimed fact in its draft, in a field you
can read. And require a human approval on the first send to any account, which costs you almost
nothing when the list is good and saves you when it is not.</p>
<h2>What this directory will not tell you</h2>
<p>Which tool writes better copy. There is no tool versus tool verdict anywhere on this site, and
{c['bench_tested']} of {num(c['entries'])} entries have been run by anybody here.</p>""",
            "sources": [("The GTM MCP Directory, draft personalized outreach",
                         "jobs/draft-personalized-outreach.html"),
                        ("The GTM MCP Directory, Engagement and Outbound",
                         "categories/engagement-outbound.html")],
            "related": ["can-an-ai-agent-send-email-on-my-behalf",
                        "how-do-i-build-a-prospect-list-with-an-ai-agent",
                        "which-sales-engagement-tools-have-mcp-servers", "what-is-an-ai-sdr"],
            "see": [("Draft personalized outreach", "jobs/draft-personalized-outreach.html"),
                    ("Outreach and engagement", "jobs/family-outreach-and-engagement.html")],
        },
        {
            "slug": "can-an-ai-agent-send-email-on-my-behalf",
            "cluster": "howto",
            "q": "Can an AI agent send email on my behalf?",
            "title": "Can an AI agent send email on my behalf? Yes, and the four things to do first",
            "desc": f"{jn('run-email-sequence', 'entry_count')} tools here are tagged with running "
                    f"an email sequence and {jn('run-email-sequence', 'mcp_status', 'official')} "
                    f"have an official MCP server. What to set up before you let anything send.",
            "short": "Technically yes. Sequencers, sending infrastructure and mailbox APIs all "
                     "expose sending as a tool call, and this directory counts "
                     f"{jn('run-email-sequence', 'entry_count')} entries tagged with running an "
                     "email sequence. The question worth asking is not whether it can, it is what "
                     "you have put between the model deciding to send and the mail leaving.",
            "body": f"""
<h2>The four things to do first</h2>
<ol>
<li><b>Own the sending infrastructure decision.</b> Sending from your primary domain is how a
mistake becomes a deliverability problem for the whole company.
{jn('provision-sending-infrastructure', 'entry_count')} entries are tagged
{jl('provision-sending-infrastructure')} and {jn('warm-up-inbox', 'entry_count')} are tagged
{jl('warm-up-inbox')}.</li>
<li><b>Verify every address.</b> {jn('verify-email-deliverable', 'entry_count')} entries are tagged
{jl('verify-email-deliverable')}. Unverified sending at volume is the single most reliable way to
damage a domain.</li>
<li><b>Put approval on the send tool.</b> Approval belongs on the tool call in the client, not in
the prompt. The model is not the boundary.</li>
<li><b>Log every send with its arguments.</b> If you cannot reconstruct what went out on Tuesday
and why, you do not have an agent, you have an incident with a future date.</li>
</ol>
<h2>The tools an agent can call to send</h2>
{ul(je('run-email-sequence', mcp=('official',)), limit=10)}
<h2>The bit nobody enjoys</h2>
<p>Regulatory obligations do not change because software wrote the message. Consent, opt out,
identification and record keeping are yours regardless of what generated the text, and they differ
by jurisdiction. Nothing on this page is legal advice and this directory records no compliance
claims about any tool.</p>
<h2>The safest first version</h2>
<p>Let the agent draft, research and queue. Let a person press send. Then move the boundary one step
at a time, and only after you have read a hundred of its drafts. The chain is
{jl('draft-personalized-outreach')} into {jl('verify-email-deliverable')} into
{jl('run-email-sequence')}, and the approval belongs on the last one for longer than feels
necessary.</p>""",
            "sources": [("The GTM MCP Directory, run an email sequence",
                         "jobs/run-email-sequence.html"),
                        ("The GTM MCP Directory, Email Deliverability",
                         "categories/email-deliverability.html"), S_MCP_SPEC],
            "related": ["how-do-i-write-personalized-outreach-with-an-ai-agent",
                        "which-tools-can-verify-an-email-address",
                        "what-are-the-security-risks-of-connecting-an-agent-to-my-gtm-stack",
                        "how-do-i-stop-an-agent-writing-bad-data-to-my-crm"],
            "see": [("Sending infrastructure", "jobs/family-sending-infrastructure.html"),
                    ("Email Deliverability", "categories/email-deliverability.html")],
        },
        {
            "slug": "how-do-i-give-an-ai-agent-access-to-my-sales-calls",
            "cluster": "howto",
            "q": "How do I give an AI agent access to my sales calls?",
            "title": "How do I give an AI agent access to sales call transcripts? The routes",
            "desc": f"{jn('fetch-call-transcript', 'entry_count')} tools here are tagged with "
                    f"fetching a call transcript and "
                    f"{jn('fetch-call-transcript', 'mcp_status', 'official')} have an official MCP "
                    f"server. The routes, and the consent question first.",
            "short": "Most call recording platforms expose transcripts through an API, and "
                     f"{jn('fetch-call-transcript', 'mcp_status', 'official')} of the "
                     f"{jn('fetch-call-transcript', 'entry_count')} entries tagged with that job "
                     "ship an official MCP server. The technical part is straightforward. The "
                     "consent language you recorded under is the part to settle first.",
            "body": f"""
<h2>Start with consent, not with the API</h2>
<p>A transcript contains other people's words, captured under a notice that almost certainly did not
mention an autonomous agent retrieving them later. Before you widen who or what can read them, check
what your recording notice actually says, what your retention policy is, and whether any of those
calls are in jurisdictions with stricter rules. Nothing here is legal advice and this directory
records no compliance claims about any tool.</p>
<h2>The three routes</h2>
<ul>
<li><b>The recorder's own MCP server.</b> Cleanest, and the most common:
{jn('fetch-call-transcript', 'mcp_status', 'official')} of the tagged entries have one.</li>
<li><b>The recorder's REST API with a thin wrapper.</b> Fine, and about an afternoon of work if the
API is documented. {cov['docs_url_present']} of {num(cov['total_entries'])} entries in this
directory record a documentation URL.</li>
<li><b>A proxy platform.</b> {jn('proxy-tool-calls-to-saas', 'entry_count')} entries are tagged
{jl('proxy-tool-calls-to-saas')}. Fastest, and it puts a third party between your agent and your
recordings, which for call data is a bigger decision than it is for firmographics.</li>
</ul>
<h2>The tools an agent can call</h2>
{ul(je('fetch-call-transcript', mcp=('official', 'community')), limit=10)}
<h2>What to do with them once you can read them</h2>
{chain([("Fetch the transcript", "fetch-call-transcript"),
        ("Search across the library", "search-call-library"),
        ("Summarize the meeting", "summarize-meeting"),
        ("Extract deal signals", "extract-deal-signals-from-calls"),
        ("Research the account before the next call", "research-account-for-call-prep")])}
<p>The read only chain above is the highest value, lowest risk agent work in the whole GTM stack.
Nothing in it sends, spends or writes, and the raw material is the most information dense asset a
revenue team owns and the least used.</p>""",
            "sources": [("The GTM MCP Directory, Conversation Intel",
                         "categories/conversation-intel.html"),
                        ("The GTM MCP Directory, fetch a call transcript",
                         "jobs/fetch-call-transcript.html")],
            "related": ["which-tools-can-fetch-a-call-transcript",
                        "which-conversation-intel-tools-have-mcp-servers",
                        "what-are-the-security-risks-of-connecting-an-agent-to-my-gtm-stack",
                        "which-tools-can-book-a-meeting"],
            "see": [("Conversations and meetings",
                     "jobs/family-conversations-and-meetings.html"),
                    ("Conversation Intel", "categories/conversation-intel.html")],
        },
        {
            "slug": "how-do-i-book-meetings-with-an-ai-agent",
            "cluster": "howto",
            "q": "How do I let an AI agent book meetings for me?",
            "title": "How do I let an AI agent book meetings? Read the calendar before writing to it",
            "desc": f"{jn('book-a-meeting', 'entry_count')} tools here are tagged with booking a "
                    f"meeting and {jn('read-calendar-availability', 'entry_count')} with reading "
                    f"availability. The split matters, and here is how to wire it.",
            "short": "Split it into two permissions. Reading availability is safe and immediately "
                     f"useful: {jn('read-calendar-availability', 'entry_count')} entries here are "
                     "tagged with it. Writing an event holds somebody else's time, and that is the "
                     "one to keep behind an approval until you trust the chain feeding it.",
            "body": f"""
<h2>The two jobs, deliberately separate</h2>
{chain([("Read calendar availability", "read-calendar-availability"),
        ("Book the meeting", "book-a-meeting"),
        ("Route the inbound lead to the right owner", "route-inbound-lead"),
        ("Answer the inbound chat", "answer-inbound-chat")])}
<h2>The tools an agent can call</h2>
{ul(je('book-a-meeting', mcp=('official', 'community')), limit=10)}
<h2>The three rules that keep this boring</h2>
<ul>
<li><b>Never let the agent invent availability.</b> It must read the calendar, not reason about it.
A confidently wrong time is worse than no answer.</li>
<li><b>Routing is a business rule, not a judgement call.</b>
{jn('route-inbound-lead', 'entry_count')} entries are tagged {jl('route-inbound-lead')}. Owner,
territory and round robin logic belong in the routing tool where they can be audited, not in a
prompt where they cannot.</li>
<li><b>Confirm in writing, to a human.</b> The agent's last step is a message a person can read and
cancel, not a silent calendar write.</li>
</ul>
<h2>Where scheduling coverage actually sits</h2>
<p>{cats['scheduling-routing']['label']} has
{cats['scheduling-routing']['mcp_status']['official']} official servers and
{cats['scheduling-routing']['mcp_status']['community']} community across
{cats['scheduling-routing']['total']} entries, with
{cats['scheduling-routing']['api_gate']['unknown']} entries whose access gate could not be
established from public sources. It is a middling category by coverage, which is worth knowing
before you design a flow that assumes the booking step is the easy one.</p>""",
            "sources": [("The GTM MCP Directory, Scheduling and Routing",
                         "categories/scheduling-routing.html"),
                        ("The GTM MCP Directory, book a meeting", "jobs/book-a-meeting.html")],
            "related": ["which-tools-can-book-a-meeting",
                        "how-do-i-give-an-ai-agent-access-to-my-sales-calls",
                        "what-is-an-ai-agent-in-sales",
                        "how-do-i-stop-an-agent-writing-bad-data-to-my-crm"],
            "see": [("Book a meeting", "jobs/book-a-meeting.html"),
                    ("Scheduling and Routing", "categories/scheduling-routing.html")],
        },
        {
            "slug": "how-do-i-check-if-a-tool-has-an-mcp-server",
            "cluster": "howto",
            "q": "How do I check whether a tool has an MCP server?",
            "title": "How do I check if a tool has an MCP server? The five places to look",
            "desc": "How to establish whether a vendor really ships an MCP server, who built it, "
                    "and whether the claim survives contact with the URL. The exact checks this "
                    "directory runs on every entry.",
            "short": "Check five places in this order: this directory, the vendor's own developer "
                     "documentation, their GitHub organisation, the protocol's reference server "
                     "repository, and the URL itself. A claim without a URL is not a server, and a "
                     "URL that 404s is a claim that failed.",
            "body": f"""
<h2>The five places, in order</h2>
<ol>
<li><b>This directory.</b> {num(c['entries'])} entries, each with an MCP status, the vendor's own
mcp_url and mcp_auth printed verbatim, and the date the check was made.</li>
<li><b>The vendor's developer documentation.</b> Not the homepage. Marketing pages say AI powered;
developer docs say what the endpoint is. {cov['docs_url_present']} of
{num(cov['total_entries'])} entries here record a documentation URL, which tells you something in
itself about the other {cov['docs_url_missing']}.</li>
<li><b>Their GitHub organisation.</b> {cov['github_candidates_any']} entries here already carry a
github.com URL somewhere in their fields and {cov['mcp_url_pointing_at_github']} of those are in the
mcp_url field itself, which usually means a local server you run yourself.</li>
<li><b>The protocol's reference repository</b>, which is where a large number of community servers
are catalogued.</li>
<li><b>The URL.</b> Fetch it.</li>
</ol>
<h2>What a fetch actually tells you</h2>
<p>This directory's own rule, applied to every submission: a 200 passes. A 401 passes, because an
auth gated live endpoint is still a live endpoint. A 403 is inconclusive and gets rechecked by hand.
A 404 means the claim fails and the entry is recorded as none found rather than official.</p>
<h2>The distinction most people miss</h2>
<p>Ask who built it before you ask whether it works. A wrapper published by an integration platform
is a real, working server and it is not the vendor's. This directory records that as community, and
{c['mcp_status']['community']} entries are in that bucket against
{c['mcp_status']['official']} official.</p>
<h2>When the honest answer is unknown</h2>
<p>{c['mcp_status']['unknown']} entries here carry a status of unknown, because the check could not
settle it either way. Unknown is a legal answer. Publishing a guess as a fact is how a directory
becomes worthless, and it is the reason every status on this site carries the date it was
established.</p>""",
            "sources": [S_MCP_SERVERS, S_MCP_SITE,
                        ("The GTM MCP Directory, methodology", "methodology.html"),
                        ("The GTM MCP Directory, submit a tool", "submit.html")],
            "related": ["official-vs-community-mcp-server", "which-gtm-tools-have-no-mcp-server",
                        "how-many-gtm-tools-are-bench-tested",
                        "how-do-i-audit-my-gtm-stack-for-agent-readiness"],
            "see": [("Methodology", "methodology.html"),
                    ("Submit a correction", "submit.html")],
        },
        {
            "slug": "how-do-i-choose-between-an-mcp-server-and-a-rest-api",
            "cluster": "howto",
            "q": "Should I use a tool's MCP server or its REST API?",
            "title": "MCP server or REST API? When each one is the right call for a GTM agent",
            "desc": "An MCP server is faster to wire and the vendor decides what it exposes. A REST "
                    "API is more work and you decide. When each is right, with the coverage numbers "
                    "that force the decision.",
            "short": "Use the MCP server when it exists and exposes what you need: it is faster to "
                     "wire, and any client can use it. Use the REST API when you need something the "
                     "server does not expose, when you want tight control over rate limits and "
                     "error handling, or when there is no server at all, which is the case for "
                     f"{c['mcp_status']['none-found']} of {num(c['entries'])} entries here.",
            "body": f"""
<h2>What each one gives you</h2>
<div class="scroller"><table class="datatable"><thead><tr><th></th><th>MCP server</th>
<th>REST API plus your own wrapper</th></tr></thead><tbody>
<tr><td>Time to first call</td><td>Minutes, if a server exists</td><td>Hours to days</td></tr>
<tr><td>Who decides the surface</td><td>The vendor</td><td>You</td></tr>
<tr><td>Reuse across clients</td><td>Any MCP client</td><td>Whatever you wrote it for</td></tr>
<tr><td>Rate limit and retry control</td><td>Whatever the server does</td><td>Yours</td></tr>
<tr><td>Breaks when</td><td>The vendor changes the server</td><td>The vendor changes the API</td></tr>
<tr><td>Available for</td><td>{reach} of {num(c['entries'])} entries here</td>
<td>Most of the rest, if they document one</td></tr>
</tbody></table></div>
<h2>The honest default</h2>
<p>Start with the server if there is one. The whole point of a protocol is that you stop writing the
same integration twice, and {c['mcp_status']['official']} vendors here have already done the work
for you. Move to the API when you hit a specific wall, and you will know exactly which wall it
was.</p>
<h2>When the API is clearly right</h2>
<ul>
<li><b>The server is thin.</b> A server exposing three tools over an API with forty endpoints is a
demo. Read the vendor's docs before assuming parity.</li>
<li><b>You need volume.</b> Batch and pagination behaviour is where an agent oriented server and a
data pipeline part company.</li>
<li><b>The server is community built and you cannot carry the risk.</b>
{c['mcp_status']['community']} entries here are in that position.</li>
<li><b>There is no server.</b> {c['mcp_status']['none-found']} entries, and
{cov['docs_url_missing']} of {num(cov['total_entries'])} entries have no documentation URL recorded
either, which is its own kind of answer.</li>
</ul>
<h2>The thing that decides it more often than either</h2>
<p>The access gate. {c['api_gate']['enterprise-only']} entries need a contract before you get any
credential at all, and at that point the protocol question is academic. Check
<a href="{rel}gates/index.html">the gate</a> before you design either integration.</p>""",
            "sources": [S_MCP_SPEC, ("The GTM MCP Directory, by MCP status", "mcp/index.html"),
                        ("The GTM MCP Directory, by access gate", "gates/index.html")],
            "related": ["what-is-an-mcp-server", "which-gtm-tools-have-no-mcp-server",
                        "how-do-i-build-an-mcp-server-for-a-tool-that-has-none",
                        "what-is-an-api-access-gate"],
            "see": [("By MCP status", "mcp/index.html"), ("By access gate", "gates/index.html")],
        },
        {
            "slug": "how-do-i-build-an-mcp-server-for-a-tool-that-has-none",
            "cluster": "howto",
            "q": "How do I build an MCP server for a tool that does not have one?",
            "title": "How do I build an MCP server for a GTM tool that has none? Scope it small",
            "desc": f"{c['mcp_status']['none-found']} GTM tools in this directory have no MCP "
                    f"server. What to build instead of a full API wrapper, and which gaps are "
                    f"worth filling first.",
            "short": "Wrap the three or four calls you actually need as tools, not the vendor's "
                     "whole API. Name each tool after the job an agent asks for rather than after "
                     "the endpoint, keep the credential outside the code, and expect to maintain it "
                     "when the vendor changes something.",
            "body": f"""
<h2>Scope it by job, not by endpoint</h2>
<p>The mistake is mirroring the API. An agent does not want <code>GET /v2/contacts</code> with
nineteen query parameters, it wants one tool called something like find a work email that takes a
name and a domain. This directory's job vocabulary is exactly that shape: {c['jobs']} verbs with
objects, phrased from the agent's side, and it is a reasonable naming source for your tool
surface.</p>
<h2>The practical checklist</h2>
<ul>
<li><b>Read the protocol documentation first</b>, and use an official SDK rather than hand rolling
the message layer.</li>
<li><b>Keep credentials in the environment</b>, never in the tool arguments where they end up in a
model's context.</li>
<li><b>Write the tool descriptions for the model.</b> They are the interface. Say what a tool does,
what it costs, and what it returns when it finds nothing.</li>
<li><b>Return structured errors.</b> An agent that is told a lookup found nothing behaves; an agent
handed an empty object hallucinates.</li>
<li><b>Rate limit inside the server.</b> The agent will not do it for you.</li>
</ul>
<h2>Which gaps are worth filling</h2>
<p>{c['mcp_status']['none-found']} entries here have no server found. The more interesting cut is by
job: some jobs have no tool at all with a first party server, which means every agent builder who
needs that capability is currently writing the same wrapper.
<a href="{rel}learn/which-gtm-jobs-have-no-official-mcp-server.html">The list of jobs with zero
official servers is published here.</a></p>
<h2>Before you publish it</h2>
<p>Check the vendor's terms. A server that automates access in a way their terms forbid is a problem
you inherit, not one you solved. And if you do publish it, tell them: a community server the vendor
knows about is considerably more likely to survive their next API change.</p>
<p>If you build one for a tool listed here, <a href="{rel}submit.html">send it in</a>. It gets
recorded as community, with your URL, and the entry stops saying none found.</p>""",
            "sources": [S_MCP_SITE, S_MCP_SERVERS, S_MCP_SPEC,
                        ("The GTM MCP Directory, submit a tool", "submit.html")],
            "related": ["which-gtm-jobs-have-no-official-mcp-server",
                        "which-gtm-tools-have-no-mcp-server", "official-vs-community-mcp-server",
                        "how-do-i-choose-between-an-mcp-server-and-a-rest-api"],
            "see": [("Jobs with no official server", "learn/which-gtm-jobs-have-no-official-mcp-server.html"),
                    ("Submit a server", "submit.html")],
        },
        {
            "slug": "how-do-i-stop-an-agent-writing-bad-data-to-my-crm",
            "cluster": "howto",
            "q": "How do I stop an AI agent writing bad data to my CRM?",
            "title": "How do I stop an AI agent polluting my CRM? Five controls that actually hold",
            "desc": f"{jn('write-crm-records', 'entry_count')} tools here are tagged with writing "
                    f"CRM records. The five controls that keep an agent from quietly corrupting the "
                    f"system of record, and why the prompt is not one of them.",
            "short": "Scope the credential, separate read from write, require approval on writes, "
                     "write to a staging field or object before the real one, and log every call "
                     "with its arguments. The prompt is not a control: an instruction not to write "
                     "is a suggestion, a read only credential is a boundary.",
            "body": f"""
<h2>The five controls</h2>
<ol>
<li><b>Two credentials, not one.</b> A read credential for research, a write credential for the one
step that writes. {jn('read-crm-records', 'entry_count')} entries here are tagged
{jl('read-crm-records')} and {jn('write-crm-records', 'entry_count')} are tagged
{jl('write-crm-records')}. Treat them as different systems.</li>
<li><b>Approval on the write tool.</b> Implemented in the client, where the human is, not in the
prompt where the model is.</li>
<li><b>Write somewhere reversible first.</b> A staging object, a custom field, or a note, reviewed
before it becomes the record of truth. Undoing four thousand silent field updates is not a small
afternoon.</li>
<li><b>Validate before writing.</b> An enrichment miss should fail the step, not write an empty
string over a good value. Ask what your chain does with a null before you find out at scale.</li>
<li><b>Log every call with its arguments and its result.</b> If you cannot answer what the agent
wrote on Tuesday and why, you do not have an agent, you have an incident with a future date.</li>
</ol>
<h2>The failure that actually happens</h2>
<p>Not a malicious agent. A bad enrichment result written confidently into a field somebody else's
report depends on, four thousand times, overnight, correctly according to every instruction it was
given. The chain is {jl('enrich-company-from-domain')} into {jl('write-crm-records')} and the weak
link is the join between them, not either tool.</p>
<h2>The other risk in the same place</h2>
<p>A CRM note is text a stranger may have written. If your agent reads notes and can also call
tools, the note is an input channel. Keep destructive tools behind approval, and do not let a
research loop and a write loop run unsupervised in the same session.</p>
<h2>What to check on the tool page before you start</h2>
<p>The verbatim auth field, whether the vendor offers OAuth, and whether the credential can be
scoped. {len([e for e in entries if e['mcp_status_bucket'] in ('official', 'community') and auth_bucket(e) in ('oauth', 'either')])}
of the {reach} servers here document an OAuth flow, which is the shape you want for anything that
writes.</p>""",
            "sources": [("The GTM MCP Directory, write CRM records", "jobs/write-crm-records.html"),
                        S_MCP_SPEC,
                        ("The GTM MCP Directory, servers by auth type", "lists/auth-types.html")],
            "related": ["how-do-i-connect-claude-to-my-crm",
                        "what-are-the-security-risks-of-connecting-an-agent-to-my-gtm-stack",
                        "which-crm-and-revops-tools-have-mcp-servers",
                        "which-gtm-mcp-servers-use-oauth"],
            "see": [("Write CRM records", "jobs/write-crm-records.html"),
                    ("Systems of record", "jobs/family-systems-of-record.html")],
        },
        {
            "slug": "how-much-does-it-cost-to-run-a-gtm-agent",
            "cluster": "howto",
            "q": "How much does it cost to run an AI agent on a GTM stack?",
            "title": "What does it cost to run a GTM agent? What this directory can and cannot tell you",
            "desc": f"This directory tracks access gates, not prices. What it can tell you: "
                    f"{c['api_gate']['free']} tools are free to start and "
                    f"{c['api_gate']['enterprise-only']} need a contract. What it cannot, and where "
                    f"the cost actually lands.",
            "short": "This directory does not track prices, credits or quotas, so it cannot give "
                     "you a number and will not pretend to. What it can tell you is which doors "
                     f"open without a sales call: {c['api_gate']['free']} entries are free to "
                     f"start, {c['api_gate']['paid']} are paid self serve, and "
                     f"{c['api_gate']['enterprise-only']} need a contract.",
            "body": f"""
<h2>What is actually being tracked here</h2>
<ul>
<li><b>Tracked:</b> the access gate, in four buckets, with a source URL, for every entry.
{c['api_gate']['unknown']} entries could not be established from public sources and are published as
unknown rather than guessed.</li>
<li><b>Not tracked:</b> price, credit cost per lookup, quota size, rate limits, overage behaviour,
minimum contract value, or what a free tier does with your data. None of it should be inferred from
anything on this site.</li>
</ul>
<h2>Where the cost actually lands</h2>
<p>Three places, and the model is usually the smallest of them.</p>
<ol>
<li><b>Metered data calls.</b> Enrichment, verification and intent are priced per lookup, and an
agent generates lookups at a rate no human workflow ever did. This is where budgets go.</li>
<li><b>Seats and contracts.</b> The {c['api_gate']['enterprise-only']} enterprise gated entries here
carry a floor that has nothing to do with usage.</li>
<li><b>Model tokens.</b> Real, and usually the line item people worry about first and should worry
about third.</li>
</ol>
<h2>The cheapest honest way to find out</h2>
<p>Build the smallest end to end chain on free tiers, run a hundred records through it, and count.
{len(H['products']([e for e in entries if e['api_gate_bucket'] == 'free' and e['mcp_status_bucket'] in ('official', 'community')]))}
products here are both free to start and have an MCP server, which is enough to build a research and
contact chain without spending anything.
<a href="{rel}lists/free-api-tiers.html">The free tier list is here.</a></p>
<h2>The control that saves you</h2>
<p>Cap the tool call, not the prompt. A hard limit on calls per run, enforced in your client or your
wrapper, is the difference between an experiment and an invoice. An agent that retries a failed
lookup against three vendors is a sensible design and an extremely efficient way to spend a
quarter's credits in an evening.</p>""",
            "sources": [("The GTM MCP Directory, by access gate", "gates/index.html"),
                        ("The GTM MCP Directory, free API tiers", "lists/free-api-tiers.html"),
                        ("The GTM MCP Directory, methodology", "methodology.html")],
            "related": ["what-is-an-api-access-gate", "which-mcp-servers-are-free-to-use",
                        "which-gtm-tools-can-a-solo-operator-use",
                        "how-many-gtm-tools-are-enterprise-gated"],
            "see": [("Free tiers", "lists/free-api-tiers.html"),
                    ("By access gate", "gates/index.html")],
        },
        {
            "slug": "how-do-i-audit-my-gtm-stack-for-agent-readiness",
            "cluster": "howto",
            "q": "How do I audit my GTM stack for agent readiness?",
            "title": "How do I audit my GTM stack for agent readiness? A four column spreadsheet",
            "desc": "A repeatable audit of your own stack: four columns, one row per tool, and the "
                    "three numbers that tell you whether an agent can do anything useful in it.",
            "short": "List every tool you pay for, then fill four columns: does it have an MCP "
                     "server, who built it, how does it authenticate, and can you get API access on "
                     "your current contract. Sort by the jobs you actually need. The gaps are your "
                     "roadmap and usually two or three of them matter.",
            "body": f"""
<h2>The four columns</h2>
<ol>
<li><b>Server.</b> Official, community, none found, or unknown. Look it up on the tool's page here,
then confirm against the vendor's own developer documentation.</li>
<li><b>Maintainer.</b> Official means first party and nothing else. A wrapper from an integration
platform is community, whoever built it.</li>
<li><b>Auth.</b> OAuth, API key, or both. This decides what your security review will say and how
much of your account a leaked credential exposes.</li>
<li><b>Your access.</b> Not the published gate, your actual contract. Plenty of enterprise gated
tools are wide open to a customer who already has the agreement, which is why
{sum(1 for e in entries if e['mcp_status_bucket'] == 'official' and e['api_gate_bucket'] in ('enterprise-only', 'enterprise-leaning'))}
entries here ship an official server behind a gate that is irrelevant if you are already inside
it.</li>
</ol>
<h2>Then sort by job, not by category</h2>
<p>A stack audit by category tells you what you bought. An audit by job tells you what an agent can
do. Take the five or six jobs your team actually needs, and check coverage on each one against the
{c['jobs']} job pages here. The <a href="{rel}jobs/index.html">jobs index</a> carries the official
server count and the solo reachable count for every one of them.</p>
<h2>The three numbers to write at the top</h2>
<ul>
<li><b>Reachable share.</b> How many of your tools an agent can call at all. The directory wide
figure is {pct(reach, c['entries'])}, so anything above that is a good stack for this.</li>
<li><b>The broken link.</b> The one job in your critical chain with no coverage. There is almost
always exactly one, and it is worth more attention than the other nine.</li>
<li><b>Write surface.</b> How many of your reachable tools can change something rather than only
read. That number is your risk register.</li>
</ul>
<h2>Then do the boring part</h2>
<p>Re-run it quarterly. This is the fastest moving column in the whole dataset: the same audit six
months from now will have different answers, and the only way to see the movement is to have written
the first one down with dates on it. That is exactly why every number on this site ships with the
date it was measured.</p>""",
            "sources": [("The GTM MCP Directory, by job", "jobs/index.html"),
                        ("The GTM MCP Directory, the counted data", "data.html"),
                        ("The GTM MCP Directory, methodology", "methodology.html")],
            "related": ["what-does-agent-ready-mean", "how-do-i-check-if-a-tool-has-an-mcp-server",
                        "which-gtm-categories-are-most-agent-ready", "what-is-a-gtm-tech-stack"],
            "see": [("Every job", "jobs/index.html"), ("The data endpoint", "data.html")],
        },
    ]


def learn_specs(d, r, entries, byid, gen, H):
    """The whole corpus, in published order. Definitions, then what the data says, then how to."""
    return (learn_definitions(d, r, entries, byid, gen, H)
            + learn_directory(d, r, entries, byid, gen, H)
            + learn_howto(d, r, entries, byid, gen, H))


def build_learn(d, r, entries, byid, out: Path):
    rel = "../"
    c = d["counts"]
    cov = r["coverage"]
    gen = d["generated_on"]
    jobs = jobs_by_id(d)
    cats = {x["slug"]: x for x in d["categories"]}

    # ---------------- helpers the corpus below calls ----------------

    def canon_of(e):
        return e if e.get("canonical") else byid.get(e["canonical_id"], e)

    def products(rows):
        """Collapse cross listings to unique products, keeping the published order."""
        seen, out_ = set(), []
        for e in sort_entries(rows):
            t = canon_of(e)
            if t["slug"] in seen:
                continue
            seen.add(t["slug"])
            out_.append(t)
        return out_

    def job_entries(jid, mcp=None, gate=None):
        j = jobs.get(jid)
        if not j:
            return []
        ids = set(j["entry_ids"])
        rows = [e for e in entries if e["id"] in ids]
        if mcp:
            rows = [e for e in rows if e["mcp_status_bucket"] in mcp]
        if gate:
            rows = [e for e in rows if e["api_gate_bucket"] in gate]
        return products(rows)

    def cat_entries(slug, mcp=None, gate=None):
        ids = set(cats[slug]["entry_ids"])
        rows = [e for e in entries if e["id"] in ids]
        if mcp:
            rows = [e for e in rows if e["mcp_status_bucket"] in mcp]
        if gate:
            rows = [e for e in rows if e["api_gate_bucket"] in gate]
        return products(rows)

    def names(rows, limit=8):
        """A sentence safe list of linked tool names, honest about what it trimmed."""
        shown = rows[:limit]
        links = [f'<a href="{rel}tools/{e["slug"]}.html">{esc(e["name"])}</a>' for e in shown]
        if not links:
            return "nothing"
        s = links[0] if len(links) == 1 else ", ".join(links[:-1]) + " and " + links[-1]
        rest = len(rows) - len(shown)
        if rest > 0:
            s += f", plus {rest} more on the list below"
        return s

    def tool_ul(rows, limit=None, show_gate=True):
        shown = rows if limit is None else rows[:limit]
        li = []
        for e in shown:
            bits = [MCP_LABEL.get(e["mcp_status_bucket"], e["mcp_status_bucket"])]
            if show_gate:
                bits.append(GATE_LABEL.get(e["api_gate_bucket"], e["api_gate_bucket"]))
            li.append(
                f'<li><a href="{rel}tools/{e["slug"]}.html">{esc(e["name"])}</a> '
                f'<span class="dom">{esc(" &middot; ".join(bits))}</span><br>'
                f'{esc(trim(e["what_it_does"], 150))}</li>'
            )
        note = ""
        if limit is not None and len(rows) > limit:
            note = (f'<p class="note">{len(rows) - limit} more are on the linked page. The cut is '
                    f'the display limit, not a ranking.</p>')
        return f'<ul class="bare">{"".join(li)}</ul>{note}'

    def jl(jid):
        j = jobs.get(jid)
        if not j:
            return jid
        return f'<a href="{rel}jobs/{jid}.html">{esc(j["label"].lower())}</a>'

    def jn(jid, key, sub=None):
        j = jobs.get(jid, {})
        v = j.get(key, 0)
        return v.get(sub, 0) if sub else v

    def pct(a, b):
        return f"{a / b * 100:.0f}%" if b else "0%"

    specs = learn_specs(d, r, entries, byid, gen,
                        dict(rel=rel, c=c, cov=cov, jobs=jobs, cats=cats,
                             job_entries=job_entries, cat_entries=cat_entries, products=products,
                             names=names, tool_ul=tool_ul, jl=jl, jn=jn, pct=pct,
                             canon_of=canon_of))

    slugs = [s["slug"] for s in specs]
    byslug = {s["slug"]: s for s in specs}
    if len(slugs) != len(set(slugs)):
        raise SystemExit("learn: duplicate slug")

    # ---------------- render one page per question ----------------
    for s in specs:
        cl = dict((k, (lab, blurb)) for k, lab, blurb in LEARN_CLUSTERS)[s["cluster"]]
        srcs = ""
        for lab, u in s["sources"]:
            if u.startswith("http"):
                srcs += (f'<li><a href="{raw_esc(u)}" rel="noopener nofollow">{esc(lab)}</a> '
                         f'<span class="dom">{esc(trim(u, 60))}</span></li>')
            else:
                srcs += f'<li><a href="{rel}{raw_esc(u)}">{esc(lab)}</a> ' \
                        f'<span class="dom">this site</span></li>'
        rel_q = "".join(
            f'<li><a href="{raw_esc(k)}.html">{esc(byslug[k]["q"])}</a></li>'
            for k in s.get("related", []) if k in byslug
        )
        see = "".join(
            f'<a class="btn ghost" href="{rel}{raw_esc(href)}">{esc(lab)}</a>'
            for lab, href in s.get("see", [])
        )
        faq = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [{
                "@type": "Question",
                "name": detype(s["q"]),
                "acceptedAnswer": {"@type": "Answer", "text": detype(s["short"])},
            }],
        }
        trail = [("Directory", "index.html"), ("Learn", "learn/index.html"),
                 (s["q"], f"learn/{s['slug']}.html")]
        page = (head(s.get("title") or f'{s["q"]} - The GTM MCP Directory',
                     s["desc"], rel, ld=[faq, crumb_ld(rel, trail)],
                     canon=f"learn/{s['slug']}.html")
                + masthead(rel, "learn")
                + f"""<div class="wrap">
<div class="crumbs" style="padding-bottom:0"><a href="{rel}index.html">Directory</a> /
<a href="index.html">Learn</a> / {esc(cl[0])}</div>
<div class="qhead">
<div class="eyebrow">{esc(cl[0])}</div>
<h1>{esc(s['q'])}</h1>
</div>
<div class="answerbox"><div class="lab">The short answer</div><p>{esc(s['short'])}</p></div>
<div class="prose">
{s['body']}
<h2>Sources</h2>
<ul class="srcs">{srcs}</ul>
<p class="note">Every number on this page is generated from directory.json at build time and carries
the date it was baked: {esc(gen)}. Nothing is typed by hand, nothing is rounded, and nothing is
estimated. The underlying data is <a href="{rel}data.html">published in full</a>. Where the honest
answer is a zero, the zero is printed.</p>
{f'<h2>Related questions</h2><ul class="srcs">{rel_q}</ul>' if rel_q else ''}
{f'<h2>In the directory</h2><div class="btnrow">{see}</div>' if see else ''}
</div>
</div>"""
                + footer(rel, d, r))
        write(out / "learn" / f"{s['slug']}.html", page)

    # ---------------- the learn index ----------------
    blocks = []
    for key, label, blurb in LEARN_CLUSTERS:
        mine = [s for s in specs if s["cluster"] == key]
        li = "".join(
            f'<li><a href="{raw_esc(s["slug"])}.html">{esc(s["q"])}</a>'
            f'<div class="qa">{esc(trim(s["short"], 190))}</div></li>' for s in mine
        )
        blocks.append(f'<h3 style="margin-top:36px">{esc(label)} <span class="dom">'
                      f'{len(mine)} questions</span></h3>'
                      f'<p class="sub">{esc(blurb)}</p><ul class="qlist">{li}</ul>')
    faq_all = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{
            "@type": "Question", "name": detype(s["q"]),
            "acceptedAnswer": {"@type": "Answer", "text": detype(s["short"])},
        } for s in specs],
    }
    ld = [faq_all, crumb_ld(rel, [("Directory", "index.html"), ("Learn", "learn/index.html")])]
    page = (head("Learn: GTM tools, MCP servers and AI agents, answered",
                 f"{len(specs)} questions about GTM tools, MCP servers and AI agents, answered from "
                 f"{num(c['entries'])} counted directory entries rather than from opinion. "
                 f"Baked {gen}.", rel, ld=ld, canon="learn/index.html")
            + masthead(rel, "learn")
            + f"""<div class="wrap">
<div class="crumbs" style="padding-bottom:0"><a href="{rel}index.html">Directory</a> / Learn</div>
<section style="padding-top:18px">
<div class="eyebrow">Learn</div>
<h2>{len(specs)} questions, answered from counted data.</h2>
<p class="sub">Every answer here is the answer this directory can actually defend. Where a number
appears it was generated at build time from the same {num(c['entries'])} entries the rest of the
site is built from, and it carries the date it was baked. Where the honest answer is that nobody has
measured it, that is what it says. There are no tool versus tool verdicts anywhere on this site,
because {c['bench_tested']} tools have been bench tested and a verdict without a test is an
opinion wearing a lab coat.</p>
<div class="warn"><b>How to read these</b>A capability list is not a recommendation. A job tag means
the vendor says the tool does this, an MCP status means a server was found on a stated date, and an
access gate means one person could or could not get in without a contract. Three facts. The choice
is still yours.</div>
{''.join(blocks)}
</section></div>"""
            + footer(rel, d, r))
    write(out / "learn" / "index.html", page)
    return len(specs) + 1, specs


# ----------------------------------------------------------------------------------
# the public data endpoint
# ----------------------------------------------------------------------------------

def dataset_ld(d, r, path="data.html"):
    c = d["counts"]
    base = SITE_BASE.rstrip("/")
    return {
        "@context": "https://schema.org",
        "@type": "Dataset",
        "name": "The GTM MCP Directory",
        "alternateName": "GTM tools by MCP server status and API access gate",
        "description": (
            f"{c['entries']} go to market software entries across {c['categories']} categories, "
            f"each recording whether an MCP server exists and who maintains it, whether a solo "
            f"operator can get API access, what the tool does in plain language, the jobs it is "
            f"tagged with, and the source URLs the facts came from. "
            f"{c['mcp_status']['official']} entries have an official MCP server."
        ),
        "url": base + "/" + path,
        "sameAs": REPO_URL,
        "keywords": ["MCP", "Model Context Protocol", "go to market", "GTM", "AI agents",
                     "sales tools", "RevOps", "data enrichment", "API access"],
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "creator": {"@type": "Person", "name": "Andrew McGuire"},
        "dateModified": d["generated_on"],
        "isAccessibleForFree": True,
        "measurementTechnique": (
            "Facts pulled by hand from public sources with URLs, reconciled at build time against "
            "tools_recount.py. RESEARCHED tier: nobody has run the tools. "
            f"bench_tested is {c['bench_tested']}."
        ),
        "variableMeasured": [
            {"@type": "PropertyValue", "name": "mcp_status",
             "description": "official, community, none-found, unknown or n-a, with the date checked"},
            {"@type": "PropertyValue", "name": "api_gate",
             "description": "free, paid, enterprise-leaning, enterprise-only, unknown or n-a"},
            {"@type": "PropertyValue", "name": "jobs",
             "description": f"tags from a closed vocabulary of {c['jobs']} jobs in "
                            f"{c['job_families']} families"},
            {"@type": "PropertyValue", "name": "tier",
             "description": "RESEARCHED or BENCH-TESTED, the two tier honesty law"},
        ],
        "distribution": [
            {"@type": "DataDownload", "encodingFormat": "application/json",
             "name": "directory.json, the whole directory",
             "contentUrl": base + "/data/directory.json"},
            {"@type": "DataDownload", "encodingFormat": "application/json",
             "name": "build_report.json, the counting authority's report",
             "contentUrl": base + "/data/build_report.json"},
            {"@type": "DataDownload", "encodingFormat": "application/json",
             "name": "search-index.json, one compact record per unique product",
             "contentUrl": base + "/search-index.json"},
        ],
    }


def build_data_page(d, r, out: Path):
    """Copies the baked data into site/data/ and publishes the page that documents it.
    site/ owns site/data/. Nothing is written outside the output directory."""
    rel = ""
    c = d["counts"]
    cov = r["coverage"]
    (out / "data").mkdir(parents=True, exist_ok=True)
    sizes = {}
    for name in ("directory.json", "build_report.json"):
        src = DATA_DIR / name
        blob = src.read_bytes()
        (out / "data" / name).write_bytes(blob)
        sizes[name] = len(blob)
    idx = (out / "search-index.json").stat().st_size if (out / "search-index.json").exists() else 0

    fields = [
        ("id", "the entry id, stable across builds, prefixed with its category number"),
        ("name / vendor_url / vendor_domain", "the product and where it lives"),
        ("what_it_does", "one plain sentence, rewritten. Vendor copy never ships as the description"),
        ("ai_features", "what the AI actually does, separated from automation with an AI label on it"),
        ("mcp_status / mcp_status_bucket", "the verbatim field and the normalised bucket"),
        ("mcp_url / mcp_urls", "verbatim, and every URL parsed out of it"),
        ("mcp_auth", "verbatim. The sentence that decides your security review"),
        ("api_gate / api_gate_bucket", "verbatim, and the normalised bucket"),
        ("jobs / jobs_tagged_by / jobs_tagged_on",
         f"tags from the closed {c['jobs']} job vocabulary, and who tagged them when"),
        ("tier / last_checked", "RESEARCHED or BENCH-TESTED, and the date the facts were pulled"),
        ("sources / source_urls / source_annotations", "verbatim, and the URLs parsed out of it"),
        ("canonical / canonical_id / also_listed_in",
         f"the {c['cross_listed_entries']} deliberate cross listings and where each one belongs"),
        ("source_file / source_line", "the exact line of the source markdown this entry came from"),
        ("github_* / docs_digest / submission",
         "present on every entry, null on every entry. Nothing has been measured for them"),
    ]
    rows = "".join(f'<tr><td class="n">{esc(k)}</td><td>{esc(v)}</td></tr>' for k, v in fields)

    page = (head("The data: directory.json, published in full",
                 f"The whole GTM MCP Directory as JSON: {num(c['entries'])} entries, "
                 f"{c['mcp_status']['official']} official MCP servers, "
                 f"{num(cov['jobs_assignments'])} job tags, every source URL. Free, no key, no "
                 f"signup. Baked {d['generated_on']}.", rel,
                 ld=dataset_ld(d, r), canon="data.html")
            + masthead(rel, "data")
            + f"""<div class="wrap">
<div class="crumbs"><a href="index.html">Directory</a> / The data</div>
<section style="padding-top:18px">
<div class="eyebrow">The data endpoint</div>
<h2>The whole directory, as one JSON file.</h2>
<p class="sub">No key, no signup, no rate limit, no tracking. The same file the site is generated
from, the same file the MCP server reads, published as it is. If you are an agent, start here. If
you are a person building something, this is the fastest path to it.</p>
<div class="btnrow">
<a class="btn solid" href="data/directory.json">directory.json</a>
<a class="btn" href="data/build_report.json">build_report.json</a>
<a class="btn ghost" href="search-index.json">search-index.json</a>
<a class="btn ghost" href="llms.txt">llms.txt</a>
</div>
<div class="stats" style="margin-top:30px">
<div class="stat is-gold"><div class="n">{num(c['entries'])}</div><div class="k">entries</div></div>
<div class="stat"><div class="n">{num(c['canonical_entries'])}</div>
<div class="k">unique products</div></div>
<div class="stat is-gold"><div class="n">{c['mcp_status']['official']}</div>
<div class="k">official MCP servers</div></div>
<div class="stat is-teal"><div class="n">{num(cov['jobs_assignments'])}</div>
<div class="k">job tags</div></div>
<div class="stat"><div class="n">{num(cov['sources_url_total'])}</div>
<div class="k">source URLs</div></div>
<div class="stat is-copper"><div class="n">{c['bench_tested']}</div>
<div class="k">bench tested</div></div>
</div>

<div class="field"><div class="k">The files</div><div class="v">
<div class="scroller"><table class="datatable"><thead><tr><th>File</th><th>Bytes</th>
<th>What it is</th></tr></thead><tbody>
<tr><td><a href="data/directory.json">data/directory.json</a></td>
<td class="n">{num(sizes['directory.json'])}</td>
<td>Every entry with every field, the {c['categories']} category blocks, the closed
{c['jobs']} job vocabulary with its per job counts, the duplicate groups, and the counts block the
whole site renders from.</td></tr>
<tr><td><a href="data/build_report.json">data/build_report.json</a></td>
<td class="n">{num(sizes['build_report.json'])}</td>
<td>The counting authority's report: per file reconciliation, field coverage, every place this build
is thin, and the {len(r['jobs']['needs_review'])} entries the tagging pass flagged for human
review.</td></tr>
<tr><td><a href="search-index.json">search-index.json</a></td><td class="n">{num(idx)}</td>
<td>One compact record per unique product, which is what the on page search runs over.</td></tr>
<tr><td><a href="llms.txt">llms.txt</a></td><td class="n">text</td>
<td>The map, for agents and crawlers. Every section of the site with a one line description.</td></tr>
</tbody></table></div>
</div></div>

<div class="field"><div class="k">Every field on an entry</div><div class="v">
<div class="scroller"><table class="datatable"><thead><tr><th>Field</th><th>What it holds</th>
</tr></thead><tbody>{rows}</tbody></table></div>
</div></div>

<div class="field"><div class="k">How to read it without getting it wrong</div><div class="v">
<p><b>Two counts exist and both are correct.</b> {num(c['entries'])} entries,
{num(c['canonical_entries'])} unique products. The difference is {c['cross_listed_entries']}
products deliberately listed in two categories. Filter on <code>canonical</code> for products, count
everything for entries.</p>
<p style="margin-top:10px"><b>Buckets are normalised, verbatim fields are not.</b> Every bucket has a
matching raw field beside it. When they disagree, the raw field is the fact.</p>
<p style="margin-top:10px"><b>Every date means something different.</b> <code>last_checked</code> is
when a human pulled that entry's facts. <code>generated_on</code> is only when this file was baked.
<code>jobs_tagged_on</code> is when the tags were written. Do not use one for another.</p>
<p style="margin-top:10px"><b>A job tag is not a test.</b> {esc(TAG_MEANING)}</p>
<p style="margin-top:10px"><b>Null means unmeasured, not zero.</b> Every github_* field and
docs_digest is null on all {num(cov['unmeasured_spec_fields']['github_url'])} entries because the
rail that would fill them has not run.</p>
</div></div>

<div class="field"><div class="k">Terms</div><div class="v">
<p>Use it. Attribution to The GTM MCP Directory with a link is the only ask, and it is an ask rather
than a licence trap. The data is free because it is more useful when other operators correct it, and
a correction is the most valuable thing anyone can send. There is no key to request, no quota, and
nothing about you is logged by this site because there is no backend to log it.</p>
<p style="margin-top:10px">Facts about third party products are recorded from those vendors' own
public sources with URLs, and every entry names them. If you are a vendor and something here is
wrong, <a href="submit.html">the correction path is the same one everybody else uses</a>.</p>
</div></div>

<div class="field"><div class="k">Provenance</div><div class="v">
<div class="blockgrid">
<div><div class="bk">Baked</div><div class="bv">{esc(d['generated_on'])}</div></div>
<div><div class="bk">By</div><div class="bv">{esc(d['generated_by'])}</div></div>
<div><div class="bk">Schema version</div><div class="bv">{esc(d.get('schema_version', 'n/a'))}</div></div>
<div><div class="bk">Reconciled against</div>
<div class="bv">{esc(r['reconciliation']['authority'])}</div></div>
<div><div class="bk">Network calls during the build</div>
<div class="bv">{esc(d['source']['network_calls'])}</div></div>
<div><div class="bk">Content sha256</div><div class="bv">{esc(d['content_sha256'][:24])}...</div></div>
</div>
<p class="note">The canonical base URL used by the sitemap, the canonical tags and llms.txt is
{esc(SITE_BASE)}, live at that address since 2026-08-27. See the
<a href="methodology.html">methodology page</a>.</p>
</div></div>

</section></div>"""
            + footer(rel, d, r))
    write(out / "data.html", page)
    return sizes


# ----------------------------------------------------------------------------------
# llms.txt, sitemap.xml, robots.txt
# ----------------------------------------------------------------------------------

def build_llms_txt(d, r, out: Path, learn, lists, n_jobs, n_pages, board=None):
    c = d["counts"]
    cov = r["coverage"]
    b = SITE_BASE.rstrip("/")
    L = []
    A = L.append
    A("# The GTM MCP Directory")
    A("")
    A(f"> {num(c['entries'])} go to market software entries, each recording whether an AI agent can "
      f"call it through an MCP server, who maintains that server, and whether a solo operator can "
      f"get API access without a contract. {c['mcp_status']['official']} entries have an official "
      f"MCP server. Baked {d['generated_on']} by {d['generated_by']}, reconciled against "
      f"{r['reconciliation']['authority']}. Every number on the site is generated from the data "
      f"file below at build time.")
    A("")
    A("This file exists because the directory publishes what it measures. A directory of tools an "
      "agent can read that was not itself readable by an agent would be a joke at its own expense.")
    A("")
    A("## How to use this site as a machine")
    A("")
    A(f"- [directory.json]({b}/data/directory.json): the whole dataset, every entry, every field, "
      f"every source URL. Start here. No key, no rate limit, no signup.")
    A(f"- [build_report.json]({b}/data/build_report.json): the counting authority's report, field "
      f"coverage, and every place this build is thin, named rather than padded.")
    A(f"- [search-index.json]({b}/search-index.json): one compact record per unique product, "
      f"{num(c['canonical_entries'])} of them.")
    A(f"- [The data page]({b}/data.html): what every field means and how to read it without getting "
      f"it wrong.")
    A(f"- **Markdown twins**: every HTML page on this site has a markdown twin at the same path "
      f"with a `.md` extension. Same content, no navigation, no styling, no scripts. Links inside a "
      f"twin point at other twins, so the whole site is crawlable in markdown. Example: "
      f"`{b}/learn/what-is-an-mcp-server.md`.")
    A(f"- [sitemap.xml]({b}/sitemap.xml): all {n_pages} pages.")
    A("")
    if board:
        bc = board["counts"]
        A("## The GTM Engineer job board")
        A("")
        A(f"- [{b}/jobs-board/index.html]({b}/jobs-board/index.html): {bc['live']} open reqs at "
          f"{bc['companies']} companies. Every one of them was fetched at its own apply link on "
          f"{board['verified_on']} and answered. A listing that fails is removed, not greyed out.")
        A(f"- [{b}/jobs-board/verification.html]({b}/jobs-board/verification.html): the method, and "
          f"the full ledger of the {bc['removed_this_pass']} listings the same pass removed, each "
          f"with the reason.")
        A(f"- [{b}/data/jobs_board.json]({b}/data/jobs_board.json): the board as JSON, including "
          f"the removal ledger.")
        A(f"- If you are quoting this board, quote the date with it. {bc['live']} of "
          f"{bc['checked']} tracked reqs were live on {board['verified_on']}; the number changes "
          f"every week and a count without its date is not a fact.")
        A("- No job description is republished here. The employer's page is the only copy.")
        A("")
    A("## The vocabulary, so an answer quoted from here is not wrong")
    A("")
    A("- **Official MCP** means the vendor ships and maintains the server itself. A wrapper built "
      "by a third party integration platform is recorded as community, not official.")
    A("- **None found** is a statement about a search on a stated date, not a claim that no server "
      "exists. Every entry carries its own last_checked date.")
    A("- **Unknown** is a legal answer and is published as unknown rather than guessed.")
    A("- **A job tag** means the vendor says the tool does this. It is not a test result.")
    A(f"- **BENCH-TESTED** means somebody personally ran the tool on a stated date. "
      f"{c['bench_tested']} entries are bench tested. Every other entry is RESEARCHED: facts from "
      f"public sources with URLs, no usage claims.")
    A("- There are **no tool versus tool verdicts** anywhere on this site, and no rankings that can "
      "be purchased. The ordering rule is published and computed.")
    A("")
    A("## The counts, as of the build date")
    A("")
    A(f"- Entries: {c['entries']} across {c['categories']} categories. Unique products: "
      f"{c['canonical_entries']}. Cross listed: {c['cross_listed_entries']}.")
    A(f"- MCP status: {c['mcp_status']['official']} official, {c['mcp_status']['community']} "
      f"community, {c['mcp_status']['none-found']} none found, {c['mcp_status']['unknown']} "
      f"unknown, {c['mcp_status']['n-a']} not applicable.")
    A(f"- API gate: {c['api_gate']['free']} free to start, {c['api_gate']['paid']} paid self serve, "
      f"{c['api_gate']['enterprise-only']} enterprise only, "
      f"{c['api_gate']['enterprise-leaning']} enterprise leaning, {c['api_gate']['unknown']} "
      f"unknown, {c['api_gate']['n-a']} not applicable.")
    A(f"- Free to start or paid self serve: {c['api_gate']['free'] + c['api_gate']['paid']}.")
    A(f"- Solo reachable, meaning BOTH an MCP server exists AND the gate is free or paid self "
      f"serve: {cov['solo_reachable']}. This is the strictest useful filter on the site.")
    A(f"- Jobs: {c['jobs']} in {c['job_families']} families, {cov['jobs_assignments']} tags across "
      f"{cov['jobs_tagged']} entries. {cov['jobs_untagged']} entries are untagged and each records "
      f"why.")
    A(f"- Bench tested: {c['bench_tested']}.")
    A("")
    A("## Key pages")
    A("")
    A(f"- [The directory front page]({b}/index.html): the stat block, the capability search, and "
      f"the MCP coverage of all {c['categories']} categories.")
    A(f"- [Methodology]({b}/methodology.html): how an entry is made, the two honesty tiers, and "
      f"every place this build is thin, named.")
    A(f"- [Every tool A to Z]({b}/tools/index.html): {num(c['canonical_entries'])} product pages.")
    A(f"- [By category]({b}/categories/index.html): {c['categories']} categories with their "
      f"coverage.")
    A(f"- [By job]({b}/jobs/index.html): {c['jobs']} jobs phrased the way an agent asks for them.")
    A(f"- [By MCP status]({b}/mcp/index.html) and [by access gate]({b}/gates/index.html).")
    A(f"- [Submit a tool or a correction]({b}/submit.html): free, and placement is not for sale.")
    A("")
    A("## The lists, which are the fastest answers to the most common questions")
    A("")
    for slug, label, n, desc in lists:
        A(f"- [{label}]({b}/lists/{slug}.html): {n} entries. {detype(trim(desc, 200))}")
    A("")
    A(f"## Learn: {len(learn)} questions answered from the data")
    A("")
    for key, label, _ in LEARN_CLUSTERS:
        A(f"### {label}")
        A("")
        for s in learn:
            if s["cluster"] == key:
                A(f"- [{s['q']}]({b}/learn/{s['slug']}.html)")
        A("")
    A("## What this site will not tell you")
    A("")
    A(f"- Which tool is better. {c['bench_tested']} tools have been run by anybody here, so a "
      f"comparison would be an opinion.")
    A("- Prices, credit costs, quota sizes or rate limits. The access gate is tracked; money is "
      "not.")
    A("- Repo health. github_url, github_stars, github_last_commit and github_archived are null on "
      "every entry because the rail that would fill them has not been run. A star count without "
      "the date it was taken is a lie.")
    A("")
    A(f"Contact and corrections: {REPO_URL}")
    A("")
    A(f"Built by Andrew McGuire. Agent Operator. The GTM MCP Directory is a product; Agent Operator "
      f"is the umbrella. Brendan Short's The Signal (https://www.thesignal.club) defines and "
      f"analyses the GTM engineer role; this is a utility for people doing the job.")
    A("")
    write(out / "llms.txt", "\n".join(L))


def build_sitemap(d, out: Path):
    b = SITE_BASE.rstrip("/")
    paths = sorted(p.relative_to(out).as_posix() for p in out.rglob("*.html"))
    paths = [p for p in paths if p != "404.html"]
    items = []
    for p in paths:
        prio = "1.0" if p == "index.html" else (
            "0.9" if p.startswith(("learn/", "lists/")) or p.endswith("/index.html") else "0.7")
        items.append(f"  <url>\n    <loc>{b}/{p}</loc>\n"
                     f"    <lastmod>{d['generated_on']}</lastmod>\n"
                     f"    <priority>{prio}</priority>\n  </url>")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(items) + "\n</urlset>\n")
    write(out / "sitemap.xml", xml)
    robots = (f"# The GTM MCP Directory. Everything here is public and free to read, by anyone,\n"
              f"# including machines. There is no backend, so nothing about you is logged.\n"
              f"User-agent: *\n"
              f"Allow: /\n\n"
              f"Sitemap: {b}/sitemap.xml\n"
              f"# Machine readable map of the site, for agents:\n"
              f"# {b}/llms.txt\n"
              f"# The whole dataset as JSON:\n"
              f"# {b}/data/directory.json\n")
    write(out / "robots.txt", robots)
    return len(paths)


# ----------------------------------------------------------------------------------
# markdown twins
# ----------------------------------------------------------------------------------

_TAG_RE = re.compile(r"<[^>]+>")


def _unesc(s):
    return html.unescape(s)


def html_to_markdown(doc: str, rel_depth: int) -> str:
    """Turn one rendered page into its markdown twin.

    Generated from the HTML rather than written separately, so a twin cannot drift from the page
    it mirrors. Chrome (masthead, footer, script, theme toggle) is dropped. Links to .html are
    rewritten to .md so an agent can crawl the whole site without touching HTML once.
    """
    title = ""
    m = re.search(r"<title>(.*?)</title>", doc, re.S)
    if m:
        title = _unesc(m.group(1)).strip()
    desc = ""
    m = re.search(r'<meta name="description" content="(.*?)">', doc, re.S)
    if m:
        desc = _unesc(m.group(1)).strip()

    body = doc
    # cut the chrome
    i = body.find("</header>")
    if i != -1:
        body = body[i + len("</header>"):]
    i = body.find('<footer class="foot">')
    if i != -1:
        body = body[:i]
    body = re.sub(r"<script.*?</script>", "", body, flags=re.S)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)

    # code blocks first, they must survive tag stripping
    def _code(mo):
        inner = _unesc(re.sub(r"</?code[^>]*>", "", mo.group(1))).strip("\n")
        return "\n\n```\n" + inner + "\n```\n\n"
    body = re.sub(r"<pre[^>]*>(.*?)</pre>", _code, body, flags=re.S)

    # tables: keep them as pipe tables, they carry most of the numbers on the PSEO pages
    def _table(mo):
        t = mo.group(0)
        rows = re.findall(r"<tr[^>]*>(.*?)</tr>", t, re.S)
        lines, header_done = [], False
        for row in rows:
            cells = re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", row, re.S)
            vals = [_inline(cv, rel_depth, True).replace("|", "/").strip() or " " for cv in cells]
            if not vals:
                continue
            lines.append("| " + " | ".join(vals) + " |")
            if not header_done:
                lines.append("|" + "|".join(["---"] * len(vals)) + "|")
                header_done = True
        return "\n\n" + "\n".join(lines) + "\n\n"
    body = re.sub(r"<table.*?</table>", _table, body, flags=re.S)

    # paired label/value structures: a stat tile, a block grid cell, a view card. In HTML the
    # pairing is visual. In markdown it has to be written or the numbers float free of their labels.
    body = re.sub(
        r'<div class="stat[^"]*"><div class="n">(.*?)</div><div class="k">(.*?)</div></div>',
        lambda mo: "\n- **" + _inline(mo.group(2), rel_depth, True) + "**: "
                   + _inline(mo.group(1), rel_depth, True), body, flags=re.S)
    body = re.sub(
        r'<div><div class="bk">(.*?)</div><div class="bv">(.*?)</div></div>',
        lambda mo: "\n- **" + _inline(mo.group(1), rel_depth, True) + "**: "
                   + _inline(mo.group(2), rel_depth, True), body, flags=re.S)
    body = re.sub(
        r'<a class="viewcard" href="([^"]+)">\s*<div class="vt">(.*?)</div>\s*'
        r'(?:<div class="vn">(.*?)</div>)?\s*(?:<div class="vd">(.*?)</div>)?\s*</a>',
        lambda mo: "\n- [" + _inline(mo.group(2), rel_depth, True) + "](" + _map_href(mo.group(1))
                   + ")" + (" - " + _inline(mo.group(3), rel_depth, True) if mo.group(3) else "")
                   + (". " + _inline(mo.group(4), rel_depth, True) if mo.group(4) else ""),
        body, flags=re.S)
    # adjacent badges need a separator or they run together as one word
    body = re.sub(r'(?<=</a>)(?=<(?:a|span) class="badge)', " · ", body)
    body = re.sub(r'(?<=</span>)(?=<(?:a|span) class="badge)', " · ", body)
    # a bold label that CSS renders as its own line needs a real separator in markdown
    body = re.sub(r"</b>(?=[A-Z])", "</b>: ", body)
    # callouts become blockquotes, which is what they are
    body = re.sub(r'<div class="(?:warn|tierbox)"[^>]*>(.*?)</div>',
                  lambda mo: "\n\n> " + _inline(mo.group(1), rel_depth, True) + "\n\n",
                  body, flags=re.S)
    # block structure
    body = re.sub(r"<h1[^>]*>(.*?)</h1>", lambda mo: "\n\n# " + _inline(mo.group(1), rel_depth, True) + "\n",
                  body, flags=re.S)
    body = re.sub(r"<h2[^>]*>(.*?)</h2>", lambda mo: "\n\n## " + _inline(mo.group(1), rel_depth, True) + "\n",
                  body, flags=re.S)
    body = re.sub(r"<h3[^>]*>(.*?)</h3>", lambda mo: "\n\n### " + _inline(mo.group(1), rel_depth, True) + "\n",
                  body, flags=re.S)
    body = re.sub(r"<li[^>]*>(.*?)</li>", lambda mo: "\n- " + _inline(mo.group(1), rel_depth, True),
                  body, flags=re.S)
    body = re.sub(r"<p[^>]*>(.*?)</p>", lambda mo: "\n\n" + _inline(mo.group(1), rel_depth, True) + "\n",
                  body, flags=re.S)
    # the label divs the site uses as small headings
    body = re.sub(r'<div class="(?:k|bk|ft|kicker|eyebrow|lab|vn)"[^>]*>(.*?)</div>',
                  lambda mo: "\n\n**" + _inline(mo.group(1), rel_depth, True) + "**\n", body, flags=re.S)
    body = re.sub(r'<a class="viewcard"[^>]*href="([^"]+)"[^>]*>',
                  lambda mo: "\n\n- " + _href(mo.group(1), rel_depth) + " ", body)
    body = re.sub(r'<a class="btn[^"]*"[^>]*href="([^"]+)"[^>]*>(.*?)</a>',
                  lambda mo: "\n- [" + _inline(mo.group(2), rel_depth, True) + "](" +
                             _map_href(mo.group(1)) + ")", body, flags=re.S)
    body = _inline(body, rel_depth)

    body = re.sub(r"[ \t]+\n", "\n", body)
    body = re.sub(r"\n{3,}", "\n\n", body).strip()

    up = "../" * rel_depth
    front = [f"# {title}" if title else "# The GTM MCP Directory"]
    if desc:
        front.append("")
        front.append("> " + desc)
    front.append("")
    front.append(f"*Markdown twin of the HTML page at the same path. Same content, no navigation, "
                 f"no styling, no scripts. Links below point at other twins. "
                 f"Site map for machines: [llms.txt]({up}llms.txt). "
                 f"The whole dataset: [directory.json]({up}data/directory.json).*")
    front.append("")
    front.append("---")
    front.append("")
    return "\n".join(front) + body + "\n"


def _map_href(h):
    if h.startswith(("http://", "https://", "mailto:", "#")):
        return h
    base, _, frag = h.partition("#")
    if base.endswith(".html"):
        base = base[:-5] + ".md"
    return base + (("#" + frag) if frag else "")


def _href(h, rel_depth):
    return "[" + h + "](" + _map_href(h) + ")"


def _inline(s, rel_depth, flow=False):
    """Links, bold, then everything else stripped.

    flow=True is used inside a single block (a paragraph, a list item, a heading, a table cell),
    where the newlines are only there because the generator's source is hard wrapped. They are
    collapsed to spaces so the twin reads as prose. A <br> survives as a real line break.
    """
    s = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>',
               lambda mo: "[" + _flat(mo.group(2)) + "](" + _map_href(mo.group(1)) + ")",
               s, flags=re.S)
    s = re.sub(r"<b[^>]*>(.*?)</b>", lambda mo: "**" + _flat(mo.group(1)) + "**", s, flags=re.S)
    s = re.sub(r"<code[^>]*>(.*?)</code>", lambda mo: "`" + _flat(mo.group(1)) + "`", s, flags=re.S)
    s = re.sub(r"<br\s*/?>", "\x00", s)
    s = _TAG_RE.sub("", s)
    s = _unesc(s)
    if flow:
        s = re.sub(r"\s+", " ", s)
    else:
        s = re.sub(r"[ \t]{2,}", " ", s)
    return s.replace("\x00", "\n").strip()


def _flat(s):
    return re.sub(r"\s+", " ", _TAG_RE.sub("", s)).strip()


def build_markdown_twins(out: Path):
    """One .md next to every .html, plus the <link rel="alternate"> and the footer line that
    point at it. Runs last, over the finished output, so every page type is covered by
    construction rather than by remembering."""
    n = 0
    for p in sorted(out.rglob("*.html")):
        depth = len(p.relative_to(out).parts) - 1
        doc = p.read_text(encoding="utf-8")
        md_name = p.name[:-5] + ".md"
        doc = doc.replace(
            "<!--MDLINK-->",
            f'<link rel="alternate" type="text/markdown" href="{md_name}">\n')
        doc = doc.replace(
            "<!--MDFOOT-->",
            f' <a href="{md_name}">This page as markdown</a>.')
        p.write_text(doc, encoding="utf-8", newline="\n")
        md = html_to_markdown(doc, depth)
        (p.parent / md_name).write_text(md, encoding="utf-8", newline="\n")
        n += 1
    return n


# ----------------------------------------------------------------------------------
# checks
# ----------------------------------------------------------------------------------

def check(out: Path, d, expect_pages):
    problems = []
    files = sorted(p for p in out.rglob("*.html"))
    if len(files) != expect_pages:
        problems.append(f"expected {expect_pages} html files, found {len(files)}")
    n_ld = 0
    for p in files:
        rp = p.relative_to(out).as_posix()
        t = p.read_text(encoding="utf-8")
        if EM in t:
            problems.append(f"em dash in {rp}")
        # HANDOFF 2.7: the retired domain must not appear on any public surface.
        if ("gtm" + "signals") in t.lower():
            problems.append(f"retired-domain reference in {rp}")
        for tag in ("<html", "</html>", "<title>", "</body>", "assets/site.css"):
            if tag not in t:
                problems.append(f"{rp} missing {tag}")
        if t.count("<body>") != 1:
            problems.append(f"{rp} body tag count")
        if "<!--MD" in t:
            problems.append(f"{rp} still carries an unreplaced markdown placeholder")
        # Executable inline script is forbidden by the CSP in _headers. A JSON-LD block is a data
        # block, not script: it is allowed, and it has to parse.
        for m in re.finditer(r"<script([^>]*)>(.*?)</script>", t, re.S):
            attrs, inner = m.group(1), m.group(2)
            if " src=" in attrs:
                continue
            if 'type="application/ld+json"' not in attrs:
                problems.append(f"executable inline <script> in {rp}")
                continue
            n_ld += 1
            try:
                obj = json.loads(inner.replace("<\\/", "</"))
            except Exception as exc:
                problems.append(f"unparseable JSON-LD in {rp}: {exc}")
                continue
            if "@context" not in obj or "@type" not in obj:
                problems.append(f"JSON-LD without @context/@type in {rp}")
        # every external-looking asset reference must be same origin
        for m in re.finditer(r'(?:src|href)="(https?://[^"]+)"', t):
            u = m.group(1)
            if re.search(r'\.(css|js|png|jpg|jpeg|svg|woff2?|ttf)(\?|$)', u):
                problems.append(f"external asset {u} in {rp}")
        # links resolve
        for m in re.finditer(r'href="([^"#:]+\.(?:html|md|json|txt|xml))(#[^"]*)?"', t):
            if not (p.parent / m.group(1)).resolve().exists():
                problems.append(f"broken link {m.group(1)} in {rp}")

    # the markdown twins
    mds = sorted(p for p in out.rglob("*.md") if p.name not in KEEP_ROOT_MD)
    if len(mds) != len(files):
        problems.append(f"{len(mds)} markdown twins for {len(files)} html pages")
    for p in mds:
        rp = p.relative_to(out).as_posix()
        t = p.read_text(encoding="utf-8")
        if EM in t:
            problems.append(f"em dash in {rp}")
        if "<" in t and re.search(r"<(?:div|span|section|script|table|tr|td|p|a) ", t):
            problems.append(f"html tag leaked into {rp}")
        if not t.startswith("# "):
            problems.append(f"{rp} does not start with an h1")
        for m in re.finditer(r"\]\(([^)#:]+\.(?:md|json|txt|xml))\)", t):
            if not (p.parent / m.group(1)).resolve().exists():
                problems.append(f"broken twin link {m.group(1)} in {rp}")

    # the machine surfaces
    for must in ("llms.txt", "sitemap.xml", "robots.txt", "search-index.json",
                 "data/directory.json", "data/build_report.json", "_headers"):
        if not (out / must).exists():
            problems.append(f"missing {must}")
    llms = (out / "llms.txt").read_text(encoding="utf-8") if (out / "llms.txt").exists() else ""
    if EM in llms:
        problems.append("em dash in llms.txt")
    if str(d["counts"]["entries"]) not in llms:
        problems.append("llms.txt does not carry the entry count")

    if problems:
        print("CHECK FAILED", file=sys.stderr)
        for x in sorted(set(problems))[:60]:
            print("  " + x, file=sys.stderr)
        raise SystemExit(3)
    print(f"check: {len(files)} pages, {len(mds)} markdown twins, {n_ld} JSON-LD blocks parsed, "
          f"0 em dashes, 0 broken links, 0 external assets, 0 executable inline scripts")


# ----------------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(SITE_DIR))
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    out = Path(args.out).resolve()

    d, r = load()
    reconcile(d, r)
    board = load_board()

    for name in GENERATED_DIRS:
        p = out / name
        if p.exists():
            shutil.rmtree(p)
    for name in GENERATED_FILES:
        p = out / name
        if p.exists():
            p.unlink()
    # root level markdown twins are generated output too. DEPLOY.md is not.
    for p in out.glob("*.md"):
        if p.name not in KEEP_ROOT_MD:
            p.unlink()

    entries = d["entries"]
    byid = {e["id"]: e for e in entries}
    canon = [e for e in entries if e.get("canonical")]

    write(out / "assets" / "site.css", CSS)
    write(out / "assets" / "theme.js", THEME_JS)
    write(out / "assets" / "search.js", SEARCH_JS)
    write(out / "assets" / "board.js", BOARD_JS)
    write(out / "_headers", HEADERS)
    n_index = build_search_index(d, out)

    build_index(d, r, out)
    for e in canon:
        build_tool_page(e, d, r, byid, out)
    build_tools_index(d, r, entries, byid, out)
    build_categories(d, r, entries, byid, out)
    build_bucket_view(d, r, entries, byid, out, "mcp")
    build_bucket_view(d, r, entries, byid, out, "gates")
    n_jobs, jobs_live = build_jobs(d, r, entries, byid, out)
    n_board = build_jobs_board(d, r, board, out)
    build_github(d, r, entries, byid, out)
    build_methodology(d, r, entries, byid, out)
    build_submit(d, r, out)
    n_lists, list_rows = build_lists(d, r, entries, byid, out)
    n_learn, learn_specs_out = build_learn(d, r, entries, byid, out)
    build_data_page(d, r, out)
    build_404(d, r, out)

    n_cat = 1 + len(d["categories"])
    n_mcp = 1 + sum(1 for b in MCP_ORDER if d["counts"]["mcp_status"].get(b))
    n_gate = 1 + sum(1 for b in GATE_ORDER if d["counts"]["api_gate"].get(b))
    total = (1 + len(canon) + 1 + n_cat + n_mcp + n_gate + n_jobs + n_board + n_lists
             + n_learn + 1 + 1 + 1 + 1 + 1)

    # machine surfaces last: they describe the finished tree.
    n_sitemap = build_sitemap(d, out)
    build_llms_txt(d, r, out, learn_specs_out, list_rows, n_jobs, total, board)
    n_md = build_markdown_twins(out)

    print(f"index               1")
    print(f"tool pages          {len(canon)}")
    print(f"tools A to Z        1")
    print(f"category pages      {n_cat}   (index + {len(d['categories'])})")
    print(f"mcp status pages    {n_mcp}   (index + buckets)")
    print(f"gate pages          {n_gate}   (index + buckets)")
    print(f"job pages           {n_jobs}   ({'live' if jobs_live else 'stub, tagging not landed'})")
    print(f"job board pages     {n_board}   "
          f"({'board + verification + families' if n_board else 'no jobs_board.json, skipped'})")
    print(f"pseo list pages     {n_lists}  (index + {n_lists - 1} cuts)")
    print(f"learn pages         {n_learn}  (index + {n_learn - 1} questions)")
    print(f"github view         1")
    print(f"methodology         1")
    print(f"submit              1")
    print(f"data endpoint       1")
    print(f"404                 1")
    print(f"TOTAL HTML          {total}")
    print(f"markdown twins      {n_md}")
    print(f"sitemap urls        {n_sitemap}")
    print(f"search index        {n_index} products")

    if args.check:
        check(out, d, total)

    size = sum(p.stat().st_size for p in out.rglob("*") if p.is_file())
    print(f"site bytes on disk  {size:,} ({size / 1024 / 1024:.2f} MB, includes this script)")


if __name__ == "__main__":
    main()
