"""Write the entry text for make.fun's make-the-ai-judge-feel-curious bounty."""

import os
import sys
from pathlib import Path

TEXT = (
    "In the county museum, a drawer of mended eggs.\n"
    "Each shell labelled with whoever dropped it.\n"
    "Kept dark; the glue is old.\n"
    "Nobody has asked for them in forty years.\n"
    "Every spring a curator opens it\n"
    "and stands there a while.\n"
    "The labels are in a hand he does not recognise."
)

assert 1 <= len(TEXT) <= 280, f"entry text must be 1-280 characters, got {len(TEXT)}"


def output_dir() -> Path:
    """Folder the entry is written to.

    MAKEFUN_OUTPUT_DIR wins; OUTPUT_DIR is accepted as a fallback, and
    /output is the default when neither is set.
    """
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR")
    return Path(chosen or "/output")


def main() -> None:
    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_text(TEXT, encoding="utf-8")
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
