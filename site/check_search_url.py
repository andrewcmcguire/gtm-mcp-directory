# -*- coding: utf-8 -*-
"""check_search_url.py - homepage capability search reads and writes query params.

Runs a Node harness over the baked search.js and search-index.js. No browser,
no network, no Playwright. Asserts that ?q= / ?mcp= / ?gate= / ?cli= fill the
box and chips, that typing and chip clicks update the URL with replaceState,
and that an unknown mcp value is ignored.

Usage
    python check_search_url.py                 # against this directory
    python check_search_url.py --root DIR      # against a generated tree
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
HARNESS = HERE / "check_search_url.js"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(HERE))
    args = ap.parse_args()
    root = Path(args.root).resolve()
    if not (root / "assets" / "search.js").exists():
        print(f"missing {root / 'assets' / 'search.js'}; generate the site first", file=sys.stderr)
        return 2
    if not HARNESS.exists():
        print(f"missing {HARNESS}", file=sys.stderr)
        return 2
    proc = subprocess.run(["node", str(HARNESS), str(root)], check=False)
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
