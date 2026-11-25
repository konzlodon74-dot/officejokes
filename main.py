"""One-Line Office Jokes — writes a single funny line to /output/entry.txt.

The joke is a plain string constant: one vivid office detail (the office
printer that only jams at the worst moment) with the punch landing in the
final words. The program validates the line against the bounty rules
(non-empty, exactly one line, 1-200 characters) and writes it with no
trailing newline, so the output file contains exactly the line and
nothing else. Python standard library only.
"""

import os

LINE = (
    "The printer only jams when the boss is standing right behind me, "
    "so I now email my deadlines straight to its repair guy."
)


def validate(line: str) -> str:
    """Check the bounty rules and return the line unchanged.

    Rules: non-empty / non-whitespace, exactly one line (no ``\n`` or
    ``\r``), and between 1 and 200 characters long.
    """
    assert line.strip(), "line must not be empty or whitespace-only"
    assert "\n" not in line and "\r" not in line, "line must be exactly one line"
    assert 1 <= len(line) <= 200, (
        f"line is {len(line)} characters, must be 1-200"
    )
    return line


def main() -> None:
    line = validate(LINE)

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)

    print(f"Wrote {len(line)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
