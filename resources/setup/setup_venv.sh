#!/usr/bin/env bash
# =====================================================================
# setup_venv.sh — OPTIONAL isolated environment (macOS / Linux)
# Computer Science 1
#
# You do NOT need this for the course. Computer Science 1 installs no
# third-party packages, so a plain python.org interpreter + IDLE is
# all that's required. This script is for students who want clean
# separation anyway (or already have some experience). The "why" lives
# in the Advanced Instructions section of README.md.
#
# This script is also meant to be READ, not just run — every step
# below is explained in plain language. Reading a small script like
# this is great practice.
#
# Run it from the course folder root (the unzipped repo):
#     bash resources/setup/setup_venv.sh
# =====================================================================

# --- Safety settings (three separate switches, explained) -----------
set -e            # stop immediately if any step fails, instead of
                  # barreling on and causing confusing errors later
set -u            # treat using a misspelled/unset variable as an
                  # error, instead of silently using empty text
set -o pipefail   # if commands are chained with pipes, the chain
                  # fails when ANY link fails — no hidden failures

# --- Find out where this script lives --------------------------------
# We need this so we can find check_env.py, which sits in the same
# folder as this script (resources/setup/), no matter which folder
# you ran the script FROM.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# --- Show which Python we're about to use ----------------------------
echo "Using: $(python3 --version)"

# --- Create the virtual environment (if it doesn't already exist) ----
# ".venv" is the industry-standard name you'll see in tutorials and
# real projects everywhere, so we teach the real convention. The
# leading dot means "hidden folder" — it's machinery, not your work.
if [ -d .venv ]; then
    echo ".venv already exists here — reusing it."
else
    python3 -m venv .venv
    echo "Created .venv/"
fi

# --- Activate it ------------------------------------------------------
# "Activate" means: point THIS terminal window at the environment's
# own copy of Python. It only affects this window, and only until you
# close it or type `deactivate`.
source .venv/bin/activate

# --- Prove it worked --------------------------------------------------
# Run the course environment check using the environment we just
# activated. The `|| true` at the end means "even if the check reports
# a problem, keep going" — so you still see the reminders below.
python "$SCRIPT_DIR/check_env.py" || true

cat <<'EOF'

Done. Your isolated environment is active for THIS terminal.
- Every new terminal session, re-activate:   source .venv/bin/activate
- To leave it:                               deactivate
Reminder: this is optional. The course works fine without it.
EOF
