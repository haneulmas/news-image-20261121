"""News-image entry for make.fun news-image-20261121.

Copies the bundled entry.png to /output/entry.png.
Python 3.13, standard library only, no network.
"""

import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT = OUTPUT_DIR / "entry.png"


def main() -> None:
    # Deterministic by construction: a plain byte copy, no timestamps,
    # no randomness, no network, so repeated runs write identical bytes.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)


if __name__ == "__main__":
    main()
