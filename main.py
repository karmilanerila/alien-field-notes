#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text: a review of planet Earth
left by an alien tourist after a two-day visit. The line observes
humans waving at their phones, apologising when the battery dies,
and rates the planet four stars, advising future visitors to bring
a charger.

Output contract: exactly 153 characters, no trailing newline, written
as UTF-8 bytes to ``entry.txt`` inside ``$MAKEFUN_OUTPUT_DIR``
(default ``/output``), with file mode 0644.
"""

import os

OBSERVATION = "The locals spend all day waving at little black rectangles, "
VERDICT = "then apologise to the rectangle when it dies. "
RATING = "Four stars; would visit again, bring a charger."

LINE = OBSERVATION + VERDICT + RATING


def build_line() -> str:
    """Return the field-note line, assembled from its three parts."""
    return LINE


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(LINE.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
