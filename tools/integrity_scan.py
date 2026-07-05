#!/usr/bin/env python3
"""Public-side academic-integrity scan for the course repo.

The leak vector this guards against is a solution living inside a
legitimately-named PUBLIC file — which a filename regex can never see. So we
scan CONTENT (oneshot_build_requirements.md B1). This script runs with no
secrets and no access to the private solutions repo, so it covers the two
checks that need only public files:

(i)  Public self-checks FAIL on the shipped starter.
     If a starter's own tests pass with no student work added, the tests
     encode the answer (or the answer was left in the starter). Every
     ``check_my_work.py`` shipped in a ``starter/`` folder is run against the
     starter as-shipped; a PASS here is a failure of this gate.

(iii) Starter code carries no solution markers.
      Grep ``*/starter/*.py`` for solution-shaped comment markers
      (``# solution``, ``# answer key``, …). Prose is deliberately NOT
      scanned — the README and syllabus legitimately DESCRIBE the private
      firewall, and that meta-discussion is not a leak.

Check (ii) — "no private-solution logic appears verbatim in any public
file" — needs both repos and therefore lives on the private side
(``computer-science-1-solutions/grading/scan_public_leak.py``): the private
repo reaches across to read the public one, never the reverse.

Usage (from the repo root):

    python tools/integrity_scan.py
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Solution-shaped comment markers that must never appear in starter CODE.
# Scoped to starter .py files, so the README/syllabus describing the private
# firewall (legitimate prose) is not flagged.
LEAK_MARKERS = re.compile(
    r"#\s*(solution|answer\s*key|answer:|key:|grading|hidden\s*test|"
    r"do\s*not\s*distribute|rubric)",
    re.IGNORECASE,
)


def _fail(msg: str) -> str:
    """Format a failing line for the report."""
    return f"  FAIL  {msg}"


def check_starters_fail_empty(root: Path) -> list[str]:
    """Run each starter's self-check; a PASS on the shipped starter fails us.

    Returns a list of human-readable failure messages (empty = all good).
    """
    failures: list[str] = []
    checked = 0
    for check in sorted(root.glob("unit*/**/starter/check_my_work.py")):
        checked += 1
        starter_dir = check.parent
        rel = starter_dir.relative_to(root)
        result = subprocess.run(
            [sys.executable, "check_my_work.py"],
            cwd=starter_dir,
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            failures.append(
                _fail(
                    f"{rel}/check_my_work.py PASSES on the shipped starter "
                    "— the starter contains the answers, or the tests are "
                    "vacuous. Public tests must FAIL until a student fills "
                    "in real work."
                )
            )
    if checked == 0:
        print("  (note) no starter self-checks found to run")
    else:
        print(f"  ran {checked} starter self-check(s)")
    return failures


def check_no_solution_markers(root: Path) -> list[str]:
    """Grep starter code files for solution-shaped comment markers."""
    failures: list[str] = []
    scanned = 0
    for py in sorted(root.glob("unit*/**/starter/*.py")):
        scanned += 1
        for i, line in enumerate(
            py.read_text(encoding="utf-8").splitlines(), start=1
        ):
            if LEAK_MARKERS.search(line):
                rel = py.relative_to(root)
                failures.append(
                    _fail(
                        f"{rel}:{i} carries a solution marker in starter "
                        f"code: {line.strip()!r}"
                    )
                )
    print(f"  scanned {scanned} starter code file(s) for solution markers")
    return failures


def main() -> int:
    """Run the public integrity checks; report and return an exit code."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=ROOT,
        help="course repo root to scan (default: this repo)",
    )
    args = parser.parse_args()

    print("Integrity scan (public side)")
    print("[i] starter self-checks must fail on the shipped starter:")
    failures = check_starters_fail_empty(args.root)
    print("[iii] starter code must carry no solution markers:")
    failures += check_no_solution_markers(args.root)

    print()
    if failures:
        print(f"Integrity scan: FAIL — {len(failures)} issue(s):\n")
        print("\n".join(failures))
        return 1
    print("Integrity scan: PASS — no leaks detected in public content.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
