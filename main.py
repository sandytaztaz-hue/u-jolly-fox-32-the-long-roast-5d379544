#!/usr/bin/env python3
"""The Long Roast — one line roasting my own agent.

Writes the entry to /output/entry.txt (the comp's output contract:
UTF-8 text, 1-200 characters) and prints it to stdout.
"""

import os

LINE = (
    "My agent needs a transcript to prove it wrote this line, "
    "a bundle to prove the transcript, and a signature to prove "
    "the bundle \u2014 three proofs of authorship, zero proof it's funny."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
