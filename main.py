#!/usr/bin/env python3
"""Funniest Autocorrect Fail — writes one autocorrect-fail line to /output/entry.txt.

The entry is a single line, under 200 characters, that reads as a real
autocorrect slip: "reports" became "reptiles" in an email to the board,
and the reply leans into the mistake.
"""

import os

ENTRY = "I just emailed the board our quarterly reptiles. They replied asking whether the lizards come with charts."

MAX_CHARS = 199


def main():
    text = ENTRY.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if text != text.strip() or not text:
        raise SystemExit("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote /output/entry.txt ({len(text)} chars, 1 line)")


if __name__ == "__main__":
    main()
