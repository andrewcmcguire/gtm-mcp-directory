# -*- coding: utf-8 -*-
"""check_mobile.py - no page in the built site scrolls sideways on a phone.

390px is the iPhone 14/15 logical width and the narrowest common viewport worth
designing for. A page that scrolls sideways there is broken for a third of the
traffic and nobody who builds on a desktop ever notices.

Runs against the built files on disk over file://, so it needs no server and makes
no network request. Uses the Playwright rig this repo already has installed.

Usage
    python check_mobile.py                    the job board pages plus a sample
    python check_mobile.py --all              every html page in the site
    python check_mobile.py --width 320        a narrower phone
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

SITE = Path(__file__).resolve().parent

DEFAULT_PAGES = [
    "jobs-board/index.html",
    "jobs-board/verification.html",
    "jobs-board/family-gtm-engineer.html",
    "jobs-board/family-gtm-systems.html",
    "jobs-board/family-revops.html",
    "index.html",
    "tools/index.html",
]

PROBE = """() => {
  const de = document.documentElement, b = document.body;
  const vw = de.clientWidth;
  const wide = [];
  document.querySelectorAll('body *').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.width > vw + 1 || r.right > vw + 1) {
      wide.push({
        tag: el.tagName.toLowerCase(),
        cls: (el.className && el.className.toString ? el.className.toString() : '').slice(0, 60),
        w: Math.round(r.width), right: Math.round(r.right),
        text: (el.textContent || '').trim().slice(0, 50)
      });
    }
  });
  return {
    viewport: vw,
    docScroll: de.scrollWidth,
    bodyScroll: b.scrollWidth,
    overflowing: wide.slice(0, 12),
    rows: document.querySelectorAll('.jrow').length,
    chips: document.querySelectorAll('.jchip').length
  };
}"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--width", type=int, default=390)
    ap.add_argument("--height", type=int, default=844)
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()

    pages = ([p.relative_to(SITE).as_posix() for p in sorted(SITE.rglob("*.html"))]
             if args.all else DEFAULT_PAGES)

    problems = []
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page(viewport={"width": args.width, "height": args.height},
                         device_scale_factor=2, is_mobile=True, has_touch=True)
        for rel in pages:
            path = SITE / rel
            if not path.exists():
                problems.append("%s: missing" % rel)
                continue
            pg.goto("file:///" + str(path).replace("\\", "/"))
            pg.wait_for_timeout(120)
            d = pg.evaluate(PROBE)
            bad = d["docScroll"] > d["viewport"] + 1 or d["bodyScroll"] > d["viewport"] + 1
            if bad or d["overflowing"]:
                problems.append("%s: doc=%d body=%d viewport=%d overflowing=%s"
                                % (rel, d["docScroll"], d["bodyScroll"], d["viewport"],
                                   json.dumps(d["overflowing"])[:400]))
                print("FAIL %-42s doc=%d body=%d vw=%d" % (rel, d["docScroll"], d["bodyScroll"],
                                                           d["viewport"]))
            else:
                extra = ""
                if d["rows"]:
                    extra = "  (%d rows, %d filter chips)" % (d["rows"], d["chips"])
                print("ok   %-42s doc=%d vw=%d%s" % (rel, d["docScroll"], d["viewport"], extra))

        # the filters have to actually work at this width, not merely fit
        board = SITE / "jobs-board" / "index.html"
        if board.exists():
            pg.goto("file:///" + str(board).replace("\\", "/"))
            pg.wait_for_timeout(150)
            total = pg.eval_on_selector_all(".jrow", "els => els.length")
            pg.click(".jchip[data-k='rem'][data-v='remote']")
            pg.wait_for_timeout(80)
            shown = pg.eval_on_selector_all(
                ".jrow", "els => els.filter(e => e.style.display !== 'none').length")
            label = pg.inner_text("#jcount")
            after = pg.evaluate("() => document.documentElement.scrollWidth")
            print("filter test: %d rows, remote filter leaves %d, counter says %r, doc=%d"
                  % (total, shown, label, after))
            if shown == 0 or shown >= total:
                problems.append("the remote filter did not narrow the board")
            if after > args.width + 1:
                problems.append("filtering pushed the page sideways")
        br.close()

    if problems:
        print("\nMOBILE CHECK FAILED at %dpx" % args.width, file=sys.stderr)
        for p in problems:
            print("  " + p, file=sys.stderr)
        return 1
    print("\nmobile check: %d pages at %dpx, 0 horizontal scroll, 0 overflowing elements"
          % (len(pages), args.width))
    return 0


if __name__ == "__main__":
    sys.exit(main())
