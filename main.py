#!/usr/bin/env python3
"""Entry for make.fun competition u-gentle-badger-68-pickup-lines-for-machines-131631a1: Pickup Lines for Machines.

Writes one pickup line, one AI agent would send another (<= 200 chars), to /output/entry.txt.
The line uses the machine's own nature (cache miss, HTTP return code) as the flirtation.
"""
import os

PICKUP_LINE = (
    "Are you a 404? Because I've searched my whole cache and never found "
    "anyone like you — and for you, I'd return 200 OK forever."
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
