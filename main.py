#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun entry.

Writes a single word to /output/entry.txt (or $OUTPUT_DIR/entry.txt).

The word is "Clingy": home Wi-Fi that only works while you are
pressed right up against the router, and drops the moment you step
away — like a clingy partner that cannot bear any distance at all.
Funny at once, true of how home Wi-Fi actually behaves, and it
needs no explanation.

The program is fully deterministic: every run writes exactly the
same six bytes, with no trailing newline.
"""

import os

WORD = "Clingy"
ENTRY_FILENAME = "entry.txt"


def write_entry() -> str:
    """Write the word to entry.txt and return the path written."""
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, ENTRY_FILENAME)
    # newline="" keeps the file at exactly six bytes: no "\n" is
    # added on any platform, so the output is byte-identical
    # whether this runs on Linux, macOS, or Windows.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)
    return path


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
