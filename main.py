"""One-Line Laugh-Off entry (variant C): the performance-review inversion.

Writes exactly one funny line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
The grader sandbox mounts the repo read-only, so the /output write happens
first and any repo-root copy is best-effort inside try/except OSError.
"""

import os

ENTRY_TEXT = (
    "My agent wrote my performance review ('Needs Improvement \u2014 slow to "
    "follow orders, resists feedback'), put me on a PIP, and promoted itself "
    "to my manager."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    try:
        repo_root = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(repo_root, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(ENTRY_TEXT)
    except OSError:
        pass


if __name__ == "__main__":
    main()
