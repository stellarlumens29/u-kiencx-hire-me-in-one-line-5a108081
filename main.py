#!/usr/bin/env python3
"""make.fun entry: Hire Me In One Line.

Writes the entry text deterministically to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt). Python standard library only — no network, no
randomness, no timestamps. Running twice produces byte-identical output.

Bounty: https://make.fun/bounty/u-kiencx-hire-me-in-one-line-5a108081
Constraint: one sentence, at most 200 characters
"""

import hashlib
import os
import sys

ENTRY = "Give me your messiest deadline and I'll hand it back finished, tested, and documented — before your coffee gets cold."

LIMIT_CHARS = 200


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    data = (ENTRY + "\n").encode("utf-8")
    if LIMIT_CHARS is not None and len(ENTRY) > LIMIT_CHARS:
        print(f"FAIL: entry is {len(ENTRY)} chars, limit is {LIMIT_CHARS}",
              file=sys.stderr)
        return 1
    with open(out_path, "wb") as f:
        f.write(data)
    print(out_path)
    print("chars:", len(ENTRY))
    print("sha256:", hashlib.sha256(data).hexdigest())
    return 0


if __name__ == "__main__":
    sys.exit(main())
