#!/usr/bin/env python3
"""Entry for make.fun's "Warning Label for Humans: One Line, Big Laugh" bounty.

Writes the one-line warning label to /output/entry.txt. The kit gate
requires UTF-8 text of 1 to 160 characters, not only whitespace.
"""

import os

LINE = "WARNING: May suddenly recall an embarrassing moment from 2011 at 3 a.m. No recall will be issued."
OUT_PATH = "/output/entry.txt"


def check_gate(text: str) -> None:
    """The kit's gate asserts: UTF-8 text, 1 to 160 chars, not whitespace."""
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 160, "entry must be 1 to 160 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert encoded.decode("utf-8") == text, "entry must round-trip as UTF-8"


def main() -> None:
    check_gate(LINE)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    with open(OUT_PATH, encoding="utf-8") as fh:
        written = fh.read()
    assert written == LINE, "written file must match the entry exactly"
    check_gate(written)
    print(f"GATE OK: {len(written)} characters")


if __name__ == "__main__":
    main()
