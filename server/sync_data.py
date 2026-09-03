#!/usr/bin/env python3
"""Copy the baked directory into the package so sdist and wheel both carry it.

The data is the product. A wheel without directory.json installs and then fails
at runtime, which is worse than not publishing. This script is the release step
that puts ../data/directory.json and ../data/build_report.json inside
gtm_mcp_directory/data/ so that `python -m build` (sdist, then wheel from the
sdist) works from any checkout, including one unpacked from the sdist itself.

Run it before every build. It is idempotent and prints what it copied and the
build date stamped inside the data, which is the date the README must quote.

    python sync_data.py
    python sync_data.py --check     # exit 1 if the bundled copy is stale
"""

from __future__ import annotations

import filecmp
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE.parent / "data"
DST = HERE / "gtm_mcp_directory" / "data"
FILES = ("directory.json", "build_report.json")


def main() -> int:
    check = "--check" in sys.argv
    DST.mkdir(parents=True, exist_ok=True)
    stale = []
    for name in FILES:
        src, dst = SRC / name, DST / name
        if not src.is_file():
            print("missing source: %s" % src, file=sys.stderr)
            return 2
        if dst.is_file() and filecmp.cmp(src, dst, shallow=False):
            print("up to date  %s" % name)
            continue
        if check:
            stale.append(name)
            continue
        shutil.copyfile(src, dst)
        print("copied      %s (%d bytes)" % (name, dst.stat().st_size))
    generated = json.loads((DST / "directory.json").read_text(encoding="utf-8")).get("generated_on")
    print("bundled data generated_on: %s" % generated)
    if stale:
        print("STALE: %s. Run python sync_data.py" % ", ".join(stale), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
