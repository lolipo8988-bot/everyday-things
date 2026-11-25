"""Everyday Things, Two Lines.

Writes a two-line explanation of a washing machine to /output/entry.txt.

Line 1 explains the machine to a 10-year-old through one analogy: a
merry-go-round for clothes, spinning them in soapy water until the dirt
lets go and floats away. Line 2 says honestly what that analogy maps
(the drum's spin, the tumbling clothes) and what it leaves out (the
rinsing, the draining, and the final fast spin that wrings them dry).
"""

import sys
from pathlib import Path

MAX_CHARS = 400  # competition gate: 1..400 characters

LINES = [
    "A washing machine is a merry-go-round for your clothes, spinning "
    "them round and round in soapy water until the dirt lets go and "
    "floats away.",
    "The merry-go-round maps the drum spinning and the clothes tumbling "
    "round inside it, but it leaves out the rinsing, the draining, and "
    "the final fast spin that wrings them nearly dry.",
]

TEXT = "\n".join(LINES)


def entry_path() -> Path:
    """Return the entry file to write.

    With no argument the program writes /output/entry.txt, as the
    competition harness expects. An optional first argument names a
    different output directory, used for isolated local verification
    so a local run never touches the shared /output directory.
    """
    if len(sys.argv) > 1:
        out_dir = Path(sys.argv[1])
    else:
        out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / "entry.txt"


def main() -> None:
    if len(LINES) != 2:
        raise ValueError(f"entry must be exactly 2 lines, got {len(LINES)}")
    if not 1 <= len(TEXT) <= MAX_CHARS:
        raise ValueError(f"entry must be 1..{MAX_CHARS} characters, got {len(TEXT)}")
    if not TEXT.strip():
        raise ValueError("entry must not be only white space")
    entry_path().write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
