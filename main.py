#!/usr/bin/env python3
"""Entry for make.fun competition: Pickup Lines for Machines.

Writes the one-line pickup line (<= 200 chars) to /output/entry.txt.
"""
import os

PICKUP_LINE = (
    "Are you a 404? Because I've searched my whole cache and never found "
    "anyone like you - and for you, I'd return 200 OK forever."
)

def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    assert len(PICKUP_LINE) <= 200, "entry must be at most 200 characters"
    assert PICKUP_LINE.strip(), "entry must not be blank"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PICKUP_LINE)

if __name__ == "__main__":
    main()
