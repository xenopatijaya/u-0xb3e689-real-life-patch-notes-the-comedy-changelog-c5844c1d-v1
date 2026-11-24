"""Real-Life Patch Notes: The Comedy Changelog — make.fun entry.

Writes one line (110 characters) to /output/entry.txt: a software patch
note for a bug in human biology, in the terse register of a real release
note. The joke is the brain's backwards memory priorities — it archives
every embarrassing moment in perfect detail, then forgets the one thing
you actually walked into the room to do. The file is written with no
trailing newline, so its byte count matches the line's character count
exactly. Python standard library only.
"""

import os

ENTRY = (
    "v4.1.0: Fixed a bug where the brain kept every embarrassing moment "
    "in HD but forgot why you entered this room."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars, must be 1-160"
    assert ENTRY == ENTRY.strip() and "\n" not in ENTRY, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
