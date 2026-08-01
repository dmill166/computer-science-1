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

(iv)  Every public markdown page carries an ``author_status`` marker.
      Voice-provenance convention (locked 2026-07-09; no exempt class —
      every page is Dakota's public work and gets his hand): pages that
      sync to the site are re-checked there by ``dakotalearns/tools/
      check_content.py``, but GitHub-only pages (``resources/``, the repo
      README) would otherwise be invisible to any gate — so the coverage
      check rides here too. Only ``LICENSE*`` files are skipped (third-
      party legal text, not authored prose). Canonical convention doc:
      ``cs-teaching/voice_provenance.md`` (implementation deliberately
      vendored per repo — zero cross-repo CI dependency).

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

# Voice-provenance marker values a published page may carry (must match
# dakotalearns/tools/check_content.py — the site-side half of this gate).
VALID_STATUSES = (
    "dakota-authored",
    "dakota-voice-draft",
    "assistant-mechanical",
    "assistant-shared",
)
STATUS_MARKER = re.compile(r"author_status:\s*([A-Za-z-]+)")


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


def check_marker_coverage(root: Path) -> list[str]:
    """Require an author_status marker on every public markdown page.

    An unmarked page is invisible to the site-side publish-lock gate, so
    "unmarked" must be impossible rather than silently passing. Markers
    with values outside ``VALID_STATUSES`` fail too (typo protection).
    """
    failures: list[str] = []
    scanned = 0
    for md in sorted(root.rglob("*.md")):
        if ".git" in md.parts or md.name.upper().startswith("LICENSE"):
            continue
        scanned += 1
        rel = md.relative_to(root)
        values = STATUS_MARKER.findall(md.read_text(encoding="utf-8"))
        if not values:
            failures.append(
                _fail(
                    f"{rel} carries no author_status marker — add "
                    "dakota-authored / dakota-voice-draft / "
                    "assistant-*, per cs-teaching/voice_provenance.md"
                )
            )
        for value in values:
            if value not in VALID_STATUSES:
                failures.append(
                    _fail(
                        f"{rel} has unrecognized author_status value "
                        f"{value!r} — expected one of "
                        f"{', '.join(VALID_STATUSES)}"
                    )
                )
    print(f"  scanned {scanned} markdown page(s) for provenance markers")
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
    print("[iv] markdown pages must carry author_status markers:")
    failures += check_marker_coverage(args.root)

    print()
    if failures:
        print(f"Integrity scan: FAIL — {len(failures)} issue(s):\n")
        print("\n".join(failures))
        return 1
    print("Integrity scan: PASS — no leaks detected in public content.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
