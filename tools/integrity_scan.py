#!/usr/bin/env python3
# Purpose: Public-side integrity checks: starters fail when untouched, no
#   solution markers, provenance markers on every page, course-code
#   mentions match the reviewed baseline, no private references, no
#   hidden placeholders, no em-dashes, no unfilled template slots.
"""Public-side academic-integrity scan for the course repo.

The leak vector this guards against is a solution living inside a
legitimately-named PUBLIC file - which a filename regex can never see. So we
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
      scanned - the README and syllabus legitimately DESCRIBE the private
      firewall, and that meta-discussion is not a leak.

Check (ii) - "no private-solution logic appears verbatim in any public
file" - needs both repos and therefore lives on the private side
(``computer-science-1-solutions/grading/scan_public_leak.py``): the private
repo reaches across to read the public one, never the reverse.

(v)   Course-code mentions match the reviewed baseline. The naming
      ratchet: forbidden-code patterns and the human-reviewed per-file
      occurrence counts live in ``tools/integrity_config.json`` (data),
      while this engine stays course-agnostic. Any drift fails until a
      human re-reviews and updates the config.

(iv)  Every public markdown page carries an ``author_status`` marker.
      Voice-provenance convention (locked 2026-07-09; no exempt class -
      every page is Dakota's public work and gets his hand): pages that
      sync to the site are re-checked there by ``dakotalearns/tools/
      check_content.py``, but GitHub-only pages (``resources/``, the repo
      README) would otherwise be invisible to any gate - so the coverage
      check rides here too. Only ``LICENSE*`` files are skipped (third-
      party legal text, not authored prose). Canonical convention doc:
      ``cs-teaching/voice_provenance.md`` (implementation deliberately
      vendored per repo - zero cross-repo CI dependency).

Usage (from the repo root):

    python tools/integrity_scan.py
"""
from __future__ import annotations

import argparse
import json
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
# dakotalearns/tools/check_content.py - the site-side half of this gate).
VALID_STATUSES = (
    "dakota-authored",
    "dakota-voice-draft",
    "assistant-mechanical",
    "assistant-shared",
)
STATUS_MARKER = re.compile(r"author_status:\s*([A-Za-z-]+)")

# Naming-rule ratchet (check v). Our courses are never named by a
# university course code; codes appear only as reviewed alignment
# references. This is deliberately a RATCHET, not a classifier: the
# COURSE DATA (code patterns + the human-reviewed per-file baseline)
# lives in tools/integrity_config.json, and ANY drift - new mention
# or removed mention - fails until a human re-reviews and updates
# that file. The machine never judges legitimacy; it just makes
# unreviewed drift impossible. Engine/data split (2026-08-02): this
# script stays course-agnostic so course repo #2 can hoist the engine
# to cs-teaching (pinned checkout in CI) and keep only its own config
# - see the maintenance trigger index.
NAME_SUFFIXES = {".md", ".py", ".sh", ".ps1", ".yml", ".txt"}


# Folders that aren't this course's content: git internals, and the
# cs-teaching checkout CI places at .cs-teaching/ for the file-map check.
SKIP_DIRS = {".git", ".cs-teaching"}


def _skipped(path: Path) -> bool:
    """Return True for a path inside a folder the scan must ignore."""
    return any(part in SKIP_DIRS for part in path.parts)


def _fail(msg: str) -> str:
    """Format a failing line for the report."""
    return f"  FAIL  {msg}"


def check_starters_fail_empty(root: Path) -> list[str]:
    """Run each starter's self-check; a PASS on the shipped starter fails us.

    Returns:
        Human-readable failure messages (empty = all good).
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
                    " - the starter contains the answers, or the tests are "
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
    """Grep starter code files for solution-shaped comment markers.

    Returns:
        One failure message per marker hit; empty means clean.
    """
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

    Returns:
        One failure message per unmarked page plus one per invalid
        marker value; empty means clean.
    """
    failures: list[str] = []
    scanned = 0
    for md in sorted(root.rglob("*.md")):
        if _skipped(md) or md.name.upper().startswith("LICENSE"):
            continue
        scanned += 1
        rel = md.relative_to(root)
        values = STATUS_MARKER.findall(md.read_text(encoding="utf-8"))
        if not values:
            failures.append(
                _fail(
                    f"{rel} carries no author_status marker - add "
                    "dakota-authored / dakota-voice-draft / "
                    "assistant-*, per cs-teaching/voice_provenance.md"
                )
            )
        for value in values:
            if value not in VALID_STATUSES:
                failures.append(
                    _fail(
                        f"{rel} has unrecognized author_status value "
                        f"{value!r} - expected one of "
                        f"{', '.join(VALID_STATUSES)}"
                    )
                )
    print(f"  scanned {scanned} markdown page(s) for provenance markers")
    return failures


def check_no_private_refs(root: Path, patterns: list[str]) -> list[str]:
    """Fail when public files name private repos or private voice files.

    Provenance markers cite voice sources by code (``source: CST-C1``),
    never by private path; this keeps it that way. The config file that
    holds the patterns is skipped, since it must contain them.

    Args:
        root: Course repo root to scan.
        patterns: Regexes for private names, from the integrity config.

    Returns:
        One failure message per file and line that matches; empty means
        clean.
    """
    failures: list[str] = []
    token = re.compile("|".join(patterns), re.IGNORECASE)
    for path in sorted(root.rglob("*")):
        if (not path.is_file() or _skipped(path)
                or path.suffix not in {".md", ".py", ".json", ".yml"}
                or path.name == "integrity_config.json"):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for n, line in enumerate(text.splitlines(), start=1):
            if token.search(line):
                failures.append(_fail(
                    f"{path.relative_to(root)}:{n} names a private repo "
                    "or file - cite voice sources by code "
                    "(source: CST-C1), per cs-teaching/voice_provenance.md"
                ))
    return failures


# Real HTML tags a page may use on purpose; anything else written as
# <word ...> outside code is almost always a placeholder, and Markdown
# would silently swallow it as an unknown HTML tag.
HTML_TAGS_OK = frozenset("""a abbr b br button code details div em
figcaption figure hr i iframe img input kbd label li mark ol p path
picture pre section small source span strong sub summary sup svg table
tbody td th thead tr ul video""".split())
ANGLE_TAG = re.compile(r"(?<!\\)<(/?)([A-Za-z][A-Za-z0-9-]*)([^<>]*)>")


def find_angle_placeholders(text: str) -> list[tuple[int, str]]:
    """Find <word ...> text outside code that Markdown would hide.

    Skips fenced and indented code, inline code, HTML comments,
    autolinks (<https://...>), backslash-escaped brackets, and real
    tags listed in ``HTML_TAGS_OK``.

    Returns:
        (line number, matched text) for each suspected placeholder.
    """
    found = []
    in_fence = False
    in_comment = False
    for n, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        if in_fence or line.startswith("    "):
            continue
        scan = re.sub(r"`[^`]*`", "", line)
        if in_comment:
            if "-->" not in scan:
                continue
            scan = scan.split("-->", 1)[1]
            in_comment = False
        scan = re.sub(r"<!--.*?-->", "", scan)
        if "<!--" in scan:
            scan = scan.split("<!--", 1)[0]
            in_comment = True
        for m in ANGLE_TAG.finditer(scan):
            name = m.group(2).lower()
            if name in HTML_TAGS_OK or name in ("http", "https", "mailto"):
                continue
            if m.group(3).startswith(":"):
                continue  # autolink like <https://...>
            found.append((n, m.group(0)[:60]))
    return found


def check_angle_placeholders(root: Path) -> list[str]:
    """Fail on <placeholder> text that Markdown would silently hide.

    Returns:
        One failure message per suspected placeholder in any markdown
        file; empty means clean.
    """
    failures: list[str] = []
    for md in sorted(root.rglob("*.md")):
        if _skipped(md):
            continue
        text = md.read_text(encoding="utf-8")
        for n, snippet in find_angle_placeholders(text):
            failures.append(_fail(
                f"{md.relative_to(root)}:{n} {snippet} would vanish when "
                "rendered; use [square brackets] for placeholders"
            ))
    return failures


EM_DASH = "\u2014"
TEXT_SUFFIXES = {".md", ".py", ".sh", ".ps1", ".yml", ".yaml", ".json",
                 ".txt", ".toml"}


def check_no_em_dash(root: Path) -> list[str]:
    """Fail on any em-dash in a public text file (cs-teaching/STYLE.md).

    Returns:
        One failure message per line that contains an em-dash; empty
        means clean.
    """
    failures: list[str] = []
    for path in sorted(root.rglob("*")):
        if _skipped(path) or not path.is_file():
            continue
        if path.suffix not in TEXT_SUFFIXES and path.name != "LICENSE":
            continue
        text = path.read_text(encoding="utf-8")
        for n, line in enumerate(text.splitlines(), start=1):
            if EM_DASH in line:
                failures.append(_fail(
                    f"{path.relative_to(root)}:{n} em-dash found; use a "
                    "semicolon, comma, parentheses, or colon instead"
                ))
    return failures


def check_name_ratchet(
    root: Path, token: re.Pattern, baseline: dict[str, int]
) -> list[str]:
    """Fail when course-code mentions drift from the reviewed baseline.

    Counts course-code occurrences per text file and compares against
    the config's baseline. Higher = an unreviewed new mention; lower =
    a removed mention the baseline should reflect. Either way a human
    looks, then updates tools/integrity_config.json.

    Args:
        root: Course repo root to scan.
        token: Compiled pattern of forbidden course codes (from the
            config's course_code_patterns).
        baseline: Human-reviewed occurrence count per repo-relative
            file path (from the config's name_baseline).

    Returns:
        One failure message per file whose count drifted from the
        baseline; empty means no drift.
    """
    failures: list[str] = []
    found: dict[str, int] = {}
    for path in sorted(root.rglob("*")):
        if _skipped(path) or not path.is_file():
            continue
        if path.suffix not in NAME_SUFFIXES:
            continue
        if path.name == "integrity_scan.py":
            continue
        rel = str(path.relative_to(root))
        n = len(token.findall(path.read_text(encoding="utf-8")))
        if n:
            found[rel] = n
    for rel in sorted(set(found) | set(baseline)):
        actual, expected = found.get(rel, 0), baseline.get(rel, 0)
        if actual != expected:
            failures.append(
                _fail(
                    f"{rel}: {actual} course-code mention(s), baseline "
                    f"says {expected} - review the change (course codes "
                    "never name our courses), then update "
                    "tools/integrity_config.json"
                )
            )
    print(f"  compared {len(found)} file(s) against the naming baseline")
    return failures


TEMPLATE_LEFTOVER = re.compile(r"\[FILL\b|[Pp]urpose:\s*Template:")


def check_template_leftovers(root: Path) -> list[str]:
    """Fail on slots left over from a cs-teaching template.

    Returns:
        One failure message per line with a ``[FILL`` slot or a purpose
        line still starting "Template:"; empty means clean.
    """
    failures: list[str] = []
    for path in sorted(root.rglob("*")):
        if _skipped(path) or not path.is_file():
            continue
        if path.suffix not in TEXT_SUFFIXES:
            continue
        if path.resolve() == Path(__file__).resolve():
            continue  # this file names the pattern it looks for
        text = path.read_text(encoding="utf-8")
        for n, line in enumerate(text.splitlines(), start=1):
            if TEMPLATE_LEFTOVER.search(line):
                failures.append(_fail(
                    f"{path.relative_to(root)}:{n} unfilled template slot; "
                    "replace it (cs-teaching/templates/README.md)"
                ))
    return failures


def main() -> int:
    """Run the public integrity checks and report the results.

    Returns:
        Process exit code: 0 when every check passes, 1 when any
        check fails.
    """
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
    print("[v] course-code mentions must match the reviewed baseline:")
    config_path = args.root / "tools" / "integrity_config.json"
    config = json.loads(config_path.read_text(encoding="utf-8"))
    token = re.compile(
        "|".join(config["course_code_patterns"]), re.IGNORECASE
    )
    failures += check_name_ratchet(
        args.root, token, config["name_baseline"]
    )
    print("[vi] public files must not name private repos or files:")
    failures += check_no_private_refs(
        args.root, config["private_reference_patterns"]
    )
    print("[vii] markdown must not hide <placeholder> text:")
    failures += check_angle_placeholders(args.root)
    print("[viii] public text must not use em-dashes:")
    failures += check_no_em_dash(args.root)
    print("[ix] no unfilled template slots ([FILL] or Template:):")
    failures += check_template_leftovers(args.root)

    print()
    if failures:
        print(f"Integrity scan: FAIL - {len(failures)} issue(s):\n")
        print("\n".join(failures))
        return 1
    print("Integrity scan: PASS - no leaks detected in public content.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
