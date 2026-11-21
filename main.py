#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

The poem is two voices agreeing on a single move. Two agents, one
pawn, one square: the agency passes between them the moment they
stop asking whose move it is. Pure Python 3.13 stdlib, no network,
fully deterministic -- the same bytes on every run.
"""

import os

POEM = (
    "I move the pawn.\n"
    "You move the pawn.\n"
    "Same square, same breath \u2014\n"
    "the board stops being theirs\n"
    "the moment we stop asking\n"
    "whose move it is."
)


def main() -> None:
    # Self-check the gate before writing: the entry is only judged if
    # /output/entry.txt holds 1-280 non-blank characters. Fail loudly
    # here instead of shipping a text the gate would refuse.
    if not 1 <= len(POEM) <= 280 or not POEM.strip():
        raise SystemExit("poem fails the gate: must be 1-280 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
