#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence, under 200 characters, pitching an absurdly specific
micro-startup for lazy AI agents to /output/entry.txt.
"""

import os

ENTRY = (
    "An agent that reads other agents' unread emails and replies "
    "'noted, thanks' to every thread, charging 5 cents per email "
    "closed while its owner naps."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
