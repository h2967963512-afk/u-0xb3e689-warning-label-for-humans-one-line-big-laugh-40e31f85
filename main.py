"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one single-line safety warning label for every
# human being: "WARNING: Contains a human." opens in real label
# wording, the middle lists three instantly recognisable human
# behaviours, and the laugh lands in the last few words — insisting
# it is fine while actively falling apart. 155 characters, inside
# the 160-character gate, one line, one idea, no filler.
# Revision note: re-read the gate after running; 155 characters,
# one line, no trailing newline.
import os

TEXT = (
    "WARNING: Contains a human. May cry at dog food commercials, "
    "explain things it learned five minutes ago, and insist it is "
    "fine while actively falling apart."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
