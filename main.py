#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text: a review of planet Earth
left by an alien tourist after a two-day visit.
"""

import os

LINE = (
    "The locals spend all day waving at little black rectangles, "
    "then apologise to the rectangle when it dies. "
    "Four stars; would visit again, bring a charger."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(LINE.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
