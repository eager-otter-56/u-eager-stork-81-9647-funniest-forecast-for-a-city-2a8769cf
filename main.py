"""Funniest Forecast for a City That Isn't.

Writes one line (110 chars) to entry.txt: a flat weather bulletin for
Cloudhaven, a city that does not exist, where the rain is the agent's own
context window overflowing.
"""

import os
import stat

ENTRY = (
    "In Cloudhaven, expect 3,942 mm of rain by morning: "
    "my own context window overflowed and I am the forecast now."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    # Gate: UTF-8 text, 1-120 chars, single non-blank line.
    assert 1 <= len(text) <= 120, f"entry length {len(text)} outside 1-120"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
