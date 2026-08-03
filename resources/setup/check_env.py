"""
check_env.py — Computer Science 1 environment check.

Run this any time to confirm you're using the right Python for the course:
    macOS / Linux:  python3 check_env.py
    Windows:        python check_env.py

It prints your Python version and where it's installed, then a PASS/FAIL.
You'll run this before assignments too — it's the fastest way to catch a
"wrong Python" problem before it wastes your time.

No prior knowledge needed: just run it and read the last line.
"""

import sys
import platform

# Rationale for the constants:
#   MIN_OK — the floor. Chosen as the oldest release still receiving
#            security fixes at design time AND what common Linux LTS
#            distros ship (Debian 12 = 3.11). Course code is stdlib-only,
#            so this is a support-policy choice, not a technical need.
#   IDEAL  — the recommended baseline; matches the setup guide's
#            "3.13 or newer." Bump only if the guide's guidance moves.
# Newer Pythons pass automatically — nothing here breaks on a new 3.x.
MIN_OK = (3, 11)      # works for the course
IDEAL = (3, 13)       # current/recommended

v = sys.version_info
exe = sys.executable or "(unknown)"
problems = []
notes = []

# 1. Version check.
if (v.major, v.minor) < MIN_OK:
    problems.append(
        f"Python {v.major}.{v.minor} is too old for this course. "
        f"Install the current release from https://www.python.org/downloads/"
    )
elif (v.major, v.minor) < IDEAL:
    notes.append(
        f"Python {v.major}.{v.minor} will work, but "
        f"{IDEAL[0]}.{IDEAL[1]}+ is recommended."
    )

# 2. macOS system-Python / Apple-developer-tools stub check.
lower_exe = exe.lower()
system_markers = (
    "/usr/bin/python",
    "/system/library/",
    "/library/developer/commandlinetools",
)
if sys.platform == "darwin" and any(m in lower_exe for m in system_markers):
    problems.append(
        "You're running macOS's system/developer Python, not a "
        "course install.\n   Install Python from "
        "https://www.python.org/downloads/ and use `python3`."
    )

# Report.
print("Computer Science 1 environment check")
print("-" * 40)
print(f"Python version : {platform.python_version()}")
print(f"Interpreter    : {exe}")
print(f"Operating sys  : {platform.system()} ({platform.machine()})")
print("-" * 40)

for n in notes:
    print(f"note: {n}")

if problems:
    for p in problems:
        print(f"FIX:  {p}")
    print("\nRESULT: FAIL — fix the item(s) above, then run this again.")
    sys.exit(1)

print("\nRESULT: PASS — your Python is ready for Computer Science 1.")
sys.exit(0)
