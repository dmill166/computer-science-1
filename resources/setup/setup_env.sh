#!/usr/bin/env bash
# setup_env.sh — OPTIONAL isolated environment for CS 1050 (macOS / Linux).
#
# You do NOT need this for the course: CS 1050 installs no third-party packages,
# so a plain python.org interpreter + IDLE is all that's required. This script is
# here for students who want clean separation anyway (or have prior experience).
# See the "Advanced Instructions" section of README.md for the why.
#
# It creates a project-local virtual environment (.venv) using the stdlib `venv`
# module — no pyenv needed — then runs the environment check.
#
# Usage (from your course folder):   bash path/to/setup_env.sh
# Override the interpreter:           PYTHON=python3.14 bash path/to/setup_env.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY="${PYTHON:-python3}"

echo "Interpreter: $("$PY" --version 2>&1)  ->  $("$PY" -c 'import sys; print(sys.executable)')"

if [ -d .venv ]; then
  echo ".venv already exists here — reusing it."
else
  "$PY" -m venv .venv
  echo "Created .venv/"
fi

# shellcheck disable=SC1091
source .venv/bin/activate
python "$SCRIPT_DIR/check_env.py" || true

cat <<'EOF'

Done. Your isolated environment is active for THIS terminal.
- Every new terminal session, re-activate:   source .venv/bin/activate
- To leave it:                                deactivate
Reminder: this is optional. The course works fine without it.
EOF
