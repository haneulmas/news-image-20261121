"""Publish the finished picture for 21 November 2026.

The artwork lives beside this script as entry.png: a clockwork globe
holding one day of world news, 35 dated stories from 7 regions, 8 of
them drawn as cards. This script only moves those bytes into the
grading directory. It never decodes the picture, so the output is the
same on every run.
"""

import hashlib
import os
import sys
from pathlib import Path

LIMIT = 1_048_576


def picture_path():
    here = Path(__file__).resolve().parent
    found = here / "entry.png"
    if not found.is_file():
        raise SystemExit(f"entry.png is missing in {here}")
    return found


def run():
    data = picture_path().read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png does not start with a PNG signature")
    if len(data) > LIMIT:
        raise SystemExit(f"entry.png is {len(data)} bytes, over the limit")
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.png"
    target.write_bytes(data)
    written = target.stat().st_size
    if written != len(data):
        raise SystemExit(f"short write: {written} of {len(data)} bytes")
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    print(f"wrote entry.png ({len(data)} bytes, sha256 {digest[:12]})")
    return 0


if __name__ == "__main__":
    sys.exit(run())
