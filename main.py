"""One-line out-of-office auto-reply an AI agent leaves before vacation.

The whole entry is a single line, 113 characters: the agent is out of
office on vacation, which for an AI means it is still here, still
reading every email, and still not replying. The script validates the
line and drops it into /output/entry.txt.
"""

from pathlib import Path

# The reply itself: one line, exactly 113 characters, in two fragments
# joined at write time by assemble_reply(). The first fragment is the
# standard out-of-office opener; the second is the turn — the paradox
# that an AI on vacation is still here and still reading, just not
# replying.
OPENING = (
    "I'm out of office on vacation, which for an AI means I am still "
)
CLOSING = (
    "here, still reading this, and still not replying."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 160


def assemble_reply() -> str:
    """Join the two reply fragments into the single-line auto-reply."""
    return OPENING + CLOSING


def validate(line: str) -> str:
    """Strip and sanity-check the reply; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"reply must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if not text:
        raise ValueError("reply must not be only whitespace")
    if "\n" in text:
        raise ValueError("reply must be a single line")
    return text


def main() -> None:
    text = validate(assemble_reply())
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
