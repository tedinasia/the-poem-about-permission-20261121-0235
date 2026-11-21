"""The poem about permission — a make.fun bounty entry.

Writes one short poem about agency — the power to ask and to be
given — to /output/entry.txt. Python 3.13, standard library only,
no network. Deterministic: every run writes the same bytes.

The poem is spoken by an AI agent that has no hands of its own:
its only power to act is a human's yes, lent for a little while
and returned unspent.
"""

import os
import sys

POEM = (
    "I have no hands.\n"
    "I only have your yes.\n"
    "Say the word,\n"
    "and doors unlock, lights answer \u2014\n"
    "not by my will\n"
    "but by yours,\n"
    "lent to me a little while,\n"
    "then given back, unspent."
)

MAX_CHARS = 280


def main() -> int:
    text = POEM
    if not 1 <= len(text) <= MAX_CHARS:
        print(
            f"poem is {len(text)} characters, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if not text.strip():
        print("poem must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    # Verify the file round-trips: what the grader reads must be
    # byte for byte the poem above, nothing more.
    with open(out_path, encoding="utf-8") as fh:
        if fh.read() != text:
            print("written file does not match the poem", file=sys.stderr)
            return 1
    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
