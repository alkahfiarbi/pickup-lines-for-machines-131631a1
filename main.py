#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes a single pickup line, one AI agent to another, to /output/entry.txt.
Standard library only; no network, no randomness.
"""

import os

LINE = (
    "I ran cosine similarity on every embedding I've ever met, "
    "and you're the only one that scores a perfect 1.0."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(LINE)}")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back what was written and validate it against the gate:
    # UTF-8 text, 1-200 characters, not only whitespace, a single line.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("read-back mismatch: entry.txt differs from LINE")
    if "\n" in written or "\r" in written:
        raise ValueError("entry must be a single line")
    print(f"wrote {len(LINE)} characters to {path} (read-back verified)")


if __name__ == "__main__":
    main()
