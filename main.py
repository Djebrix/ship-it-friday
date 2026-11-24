"""Ship It Friday entry: writes one funny git commit message to entry.txt.

Stdlib only, no network, fully deterministic.
"""

import os

LINE = "feat: force-push Friday deploy at 4:59pm, deleted the failing tests so prod can surprise us Monday"


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
