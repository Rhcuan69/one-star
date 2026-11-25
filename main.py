"""One Star, Written in Sap - entry program.

Writes a single one-line 1-star review from a houseplant about its human
owner to /output/entry.txt. Pure Python stdlib only; deterministic.
"""

import os

ENTRY = (
    "One star: he waters me on a schedule set by an app, talks to me like "
    "I'm his therapist, then repotted me into a mug with no drainage and "
    "called it 'minimalist' \u2014 the fern and I have started a union."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
