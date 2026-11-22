# Purpose: Environment check students run to confirm they have a supported
#   Python; prints PASS or what to fix.
"""
check_env.py: Computer Science 1 environment check.

Run this any time to confirm you're using the right Python for the
course:
    macOS / Linux:  python3 check_env.py
    Windows:        python check_env.py

It prints your Python version and where it's installed, then a
PASS/FAIL. You'll run this before assignments too; it's the fastest
way to catch a "wrong Python" problem before it wastes your time.

No prior knowledge needed: just run it and read the last line. But
like every script in this course, it's also meant to be READ: each
step below is explained, and by mid-course you'll understand every
line here.
"""

# `sys` knows about the Python that is running RIGHT NOW (its version,
# where it's installed); `platform` knows about your computer (OS,
# chip). Both ship with Python; nothing to install.
import sys
import platform

# Rationale for the constants:
#   MIN_OK: the floor. Chosen as the oldest release still receiving
#            security fixes at design time AND what common Linux LTS
#            distros ship (Debian 12 = 3.11). Course code is stdlib-only,
#            so this is a support-policy choice, not a technical need.
#   IDEAL: the recommended baseline; matches the setup guide's
#            "3.13 or newer." Bump only if the guide's guidance moves.
# Newer Pythons pass automatically; nothing here breaks on a new 3.x.
MIN_OK = (3, 11)      # works for the course
IDEAL = (3, 13)       # current/recommended

# sys.version_info holds the running version as separate numbers
# (3.14.6 -> major 3, minor 14, micro 6). Keeping the pieces separate
# lets us compare pairs like (3, 14) >= (3, 11); Python compares them
# position by position, exactly like alphabetizing two words.
v = sys.version_info

# sys.executable is the full path of the Python program running this
# script: the single most useful fact when the "wrong Python" is the
# problem. (The `or` provides a fallback label in the rare case the
# path is unknown.)
exe = sys.executable or "(unknown)"

# We'll collect anything wrong in `problems` and anything merely worth
# mentioning in `notes`, then report both at the end. Collect-then-
# report beats print-as-you-go: the last line can then be a single
# clear verdict.
problems = []
notes = []

# --- Check 1: is this Python new enough? -----------------------------
if (v.major, v.minor) < MIN_OK:
    problems.append(
        f"Python {v.major}.{v.minor} is too old for this course. "
        f"Install the current release from https://www.python.org/downloads/"
    )
elif (v.major, v.minor) < IDEAL:
    # Not a failure, just a nudge. 3.11/3.12 run everything we do.
    notes.append(
        f"Python {v.major}.{v.minor} will work, but "
        f"{IDEAL[0]}.{IDEAL[1]}+ is recommended."
    )

# --- Check 2 (macOS only): are you on Apple's stub Python? -----------
# Modern macOS doesn't ship a general-use Python; /usr/bin/python3 is
# a stub tied to Apple's developer tools. If the path of the running
# Python contains one of these giveaway fragments, you're not on your
# course install. ("darwin" is macOS's internal name, a Unix history
# souvenir.)
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

# --- Report ----------------------------------------------------------
# f-strings (the f"..." form) drop live values into text; you'll
# learn these properly in Unit 1.
print("Computer Science 1 environment check")
print("-" * 40)
print(f"Python version : {platform.python_version()}")
print(f"Interpreter    : {exe}")
print(f"Operating sys  : {platform.system()} ({platform.machine()})")
print("-" * 40)

for n in notes:
    print(f"note: {n}")

# Exit codes are how programs report success to OTHER programs:
# 0 means "all good", anything else means "something failed". That's
# what lets the setup script (and graders, and automation) react to
# this check's result without reading its text.
if problems:
    for p in problems:
        print(f"FIX:  {p}")
    print("\nRESULT: FAIL - fix the item(s) above, then run this again.")
    sys.exit(1)

print("\nRESULT: PASS - your Python is ready for Computer Science 1.")
sys.exit(0)
