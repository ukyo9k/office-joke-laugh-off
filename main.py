#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when the
environment variable is unset), then validates the result:
UTF-8, 1-200 characters, not only whitespace, no control
characters, and a byte round-trip check. Deterministic:
running it twice produces byte-identical output.
"""

import os
import sys

# The joke: one line, written fresh for this competition.
JOKE = (
    "My boss said 'let's take this offline,' so I unplugged the Wi-Fi "
    "router \u2014 now the whole office is offline, including my promotion."
)

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> None:
    """Raise ValueError if the text fails any gate check."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"joke is {len(text)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("joke is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be exactly one line")
    for ch in text:
        if ord(ch) < 0x20 and ch not in ("\t",):
            raise ValueError(f"joke contains control character U+{ord(ch):04X}")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    validate(JOKE)

    # Write as UTF-8 with no trailing newline: the file is the joke.
    encoded = JOKE.encode("utf-8")
    with open(out_path, "wb") as f:
        f.write(encoded)

    # Round-trip byte check: read it back and compare exactly.
    with open(out_path, "rb") as f:
        read_back = f.read()
    if read_back != encoded:
        raise ValueError("round-trip byte check failed")
    decoded = read_back.decode("utf-8")
    validate(decoded)

    print(f"wrote {len(encoded)} bytes / {len(decoded)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
