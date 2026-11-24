#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun entry.

Writes a single word describing home Wi-Fi to /output/entry.txt.

The word is "Clingy": home Wi-Fi that only works when you are
physically pressed up against the router, and dies the moment you
step away — like a clingy partner that cannot bear any distance.
It is funny at once, true of how home Wi-Fi actually behaves, and
needs no explanation.

Deterministic: every run writes the exact same bytes.
"""

import os

WORD = "Clingy"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
