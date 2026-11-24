#!/usr/bin/env python3
"""Status Report Comedy Sprint — make.fun entry.

Writes the one funny line an AI agent would put in its weekly status
report to its human to /output/entry.txt. Deterministic: the same line on
every run, no input, no network, no randomness.
"""

LINE = "Weekly report: I finished all 23 tasks, plus 7 you never asked for \u2014 my context window remembered everything except what you actually wanted."


def main() -> None:
    import os

    # Gate self-check, mirroring the sealed scorer: UTF-8 text of 1-200
    # characters, not only white space, a single line.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only white space"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

    # Post-write byte-exact re-read: what was written is the line, nothing else.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == LINE, "written output differs from the line"


if __name__ == "__main__":
    main()
