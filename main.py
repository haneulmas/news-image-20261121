"""Ship the finished front page to the grading output directory.

The newspaper artwork is stored next to this script as ``entry.png``.
This program does not redraw or alter the picture in any way: it
loads the file's bytes, writes them out again under
``$MAKEFUN_OUTPUT_DIR`` (defaulting to ``/output``), and prints a
short confirmation. Because the bytes are never decoded or
re-encoded, the result is identical on every run.
"""

import os
import sys
from pathlib import Path


def find_artwork() -> Path:
    """Return the path of the PNG bundled beside this script."""
    picture = Path(__file__).resolve().parent / "entry.png"
    if not picture.is_file():
        raise SystemExit(f"artwork not found: {picture}")
    return picture


def main() -> int:
    source = find_artwork()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"

    payload = source.read_bytes()
    target.write_bytes(payload)

    written = target.stat().st_size
    if written != len(payload):
        raise SystemExit(
            f"copy incomplete: expected {len(payload)} bytes, got {written}"
        )

    print(f"copied {source.name} -> {target} ({len(payload)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
