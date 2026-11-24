#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint.

Reads the single joke line from ``entry.txt`` next to this script, validates
it against the competition gate (1 to 200 characters, not only whitespace),
and writes its exact bytes to ``$MAKEFUN_OUTPUT_DIR/entry.txt``.

Pure Python standard library only. Writes only inside the output directory;
never writes beside the source file, because the grader mounts the
repository read-only.
"""

import os
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.txt"

    try:
        text = source.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"entry.txt not found beside main.py: {source}", file=sys.stderr)
        return 1
    except UnicodeDecodeError as exc:
        print(f"entry.txt is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    length = len(text)
    if length < 1 or length > 200:
        print(
            f"entry.txt must be 1 to 200 characters, got {length}",
            file=sys.stderr,
        )
        return 1
    if not text.strip():
        print("entry.txt must not be only whitespace", file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_bytes(text.encode("utf-8"))
    os.chmod(out_path, 0o644)

    print(f"wrote {length} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
