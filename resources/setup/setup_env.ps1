# setup_env.ps1 — OPTIONAL isolated environment for CS 1050 (Windows / PowerShell).
#
# You do NOT need this for the course: CS 1050 installs no third-party packages,
# so a plain python.org interpreter + IDLE is all that's required. This script is
# here for students who want clean separation anyway (or have prior experience).
# See the "Advanced Instructions" section of README.md for the why.
#
# It creates a project-local virtual environment (.venv) using the stdlib `venv`
# module - no pyenv needed - then runs the environment check.
#
# Usage (from your course folder):   powershell -ExecutionPolicy Bypass -File path\to\setup_env.ps1
$ErrorActionPreference = "Stop"

$py = if ($env:PYTHON) { $env:PYTHON } else { "python" }
& $py --version

if (Test-Path ".venv") {
    Write-Host ".venv already exists here - reusing it."
} else {
    & $py -m venv .venv
    Write-Host "Created .venv\"
}

. .\.venv\Scripts\Activate.ps1

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
python "$scriptDir\check_env.py"

Write-Host ""
Write-Host "Done. Your isolated environment is active for THIS terminal."
Write-Host "- Every new session, re-activate:   .\.venv\Scripts\Activate.ps1"
Write-Host "- To leave it:                       deactivate"
Write-Host "Reminder: this is optional. The course works fine without it."
