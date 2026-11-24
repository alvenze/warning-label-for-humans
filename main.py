#!/usr/bin/env python3
"""Entry for make.fun's "Warning Label for Humans: One Line, Big Laugh" bounty.

Writes the one-line warning label to /output/entry.txt. The kit gate
requires UTF-8 text of 1 to 160 characters, not only whitespace.
"""

import os

LINE = "WARNING: May suddenly recall an embarrassing moment from 2011 at 3 a.m. No recall will be issued."
OUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(LINE) <= 160, "entry must be 1 to 160 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    print(f"GATE OK: {len(LINE)} characters")


if __name__ == "__main__":
    main()
