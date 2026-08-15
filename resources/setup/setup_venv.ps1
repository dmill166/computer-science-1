<#
.SYNOPSIS
    setup_venv.ps1 — OPTIONAL isolated environment (Windows / PowerShell)
    for Computer Science 1.

.DESCRIPTION
    You do NOT need this for the course. Computer Science 1 installs no
    third-party packages, so a plain python.org interpreter + IDLE is
    all that's required. This script is for students who want clean
    separation anyway (or already have some experience). The "why"
    lives in the Advanced Instructions section of README.md.

    This script is also meant to be READ, not just run — every step
    below is explained in plain language.

.EXAMPLE
    Run it from the course folder root (the unzipped repo):
    powershell -ExecutionPolicy Bypass -File resources\setup\setup_venv.ps1
#>

# --- Safety setting ---------------------------------------------------
# Stop immediately if any step fails, instead of barreling on and
# causing confusing errors later.
$ErrorActionPreference = "Stop"

# --- Show which Python we're about to use -----------------------------
python --version

# --- Create the virtual environment (if it doesn't already exist) -----
# ".venv" is the industry-standard name you'll see in tutorials and
# real projects everywhere, so we teach the real convention. The
# leading dot signals "machinery, not your work."
if (Test-Path ".venv") {
    Write-Host ".venv already exists here - reusing it."
} else {
    python -m venv .venv
    Write-Host "Created .venv\"
}

# --- Activate it -------------------------------------------------------
# "Activate" means: point THIS terminal window at the environment's own
# copy of Python. It only affects this window, and only until you close
# it or type `deactivate`.
. .\.venv\Scripts\Activate.ps1

# --- Prove it worked ----------------------------------------------------
# Find the folder THIS script lives in (resources\setup\), so we can run
# check_env.py that sits right next to it — no matter which folder you
# ran the script FROM.
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
python "$scriptDir\check_env.py"

Write-Host ""
Write-Host "Done. Your isolated environment is active for THIS terminal."
Write-Host "- Every new session, re-activate:   .\.venv\Scripts\Activate.ps1"
Write-Host "- To leave it:                       deactivate"
Write-Host "Reminder: this is optional. The course works fine without it."
