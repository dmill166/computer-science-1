# Module 0 — Set Up Python on Your Computer

> **Goal:** by the end of this guide you have a working, current Python on your machine and can run a one-line program — no prior experience assumed. This is the only "setup" step in the course; once it's done, every lab and assignment just works.
>
> Pick your operating system, follow the steps, then do the **Verify** check at the bottom. Budget 15–20 minutes.

If you get stuck, that's normal — jump to [Troubleshooting](#troubleshooting). Asking for help early is a skill, not a failure.

---

## What you're installing and why

- **Python** — the language we write in. We install the **current stable version** (Python **3.13 or newer**; 3.14.x is current as of mid-2026). Always take the latest stable release from the official site — *not* an older one. (If you've read older guides that say "pick the oldest version still getting security updates," ignore that here: as a learner you want a current, fully supported version.)
- **An editor** — where you write and run code. We start with **IDLE**, which ships *with* Python (nothing extra to install) and matches our textbook. Alternatives are listed [below](#editors-where-you-write-code).

Only install Python from **[python.org](https://www.python.org/downloads/)**. Other sources exist, but the official installer is the safest, most predictable path for this course.

---

## macOS 🍎

macOS does **not** come with a Python you should use for this course (the system may have an old one or none). Install a fresh copy:

1. Go to **<https://www.python.org/downloads/>**. The page detects your Mac and shows a yellow **"Download Python 3.x.x"** button — click it (this is the current stable release).
2. Open the downloaded `.pkg` file from your **Downloads** folder.
3. Click **Continue** through Introduction → Read Me → License (read them), click **Agree**, then **Install**. Enter your password / Touch ID when asked.
4. When it finishes, click **Close**. (If it offers to move the installer to the Trash, that's fine.)

> Apple Silicon (M1/M2/M3/M4) and Intel Macs both use the same "universal2" installer from that button — you don't have to choose a chip type.

The python.org installer also installs **IDLE** and the `python3` command. Skip to [Verify](#verify-it-works).

> **"Am I installing a second Python?"** Not in a way that bites you. Modern macOS no longer ships a general-use Python — `/usr/bin/python3` is just a stub that prompts to install Apple's developer tools. The python.org installer puts a clean, current Python in its own location and points the `python3` command at it. So after this step, `python3` *is* your course Python, separate from anything Apple-managed. The **Verify** step below confirms you're on the right one (current version, not a system stub). You do **not** need pyenv or virtual environments for this course — see ["Keeping it clean"](#keeping-your-environment-clean-optional).

---

## Windows 🪟

1. Go to **<https://www.python.org/downloads/>** and click the yellow **"Download Python 3.x.x"** button (current stable release).
2. Open the downloaded `.exe` from your **Downloads** folder.
3. **Important — before clicking anything else, check the box at the bottom: "Add python.exe to PATH."** This lets you run Python by name from a terminal. (PATH is just the list of places your computer looks for programs; adding Python means you can type `python` instead of a long folder path.)
4. Click **Install Now**. Approve the User Account Control prompt if it appears and looks legitimate.
5. If you're offered **"Disable path length limit"** at the end, click it (it prevents a class of file-path errors), then **Close**.

> **Do not also install Python from the Microsoft Store.** One Python from python.org is what this course assumes; a second copy from the Store causes confusing "which Python am I running?" problems.

This installs **IDLE** and the `python` command. Skip to [Verify](#verify-it-works).

---

## Linux 🐧 (Ubuntu / Debian shown)

Most Linux distributions already include Python 3, but often not the newest and sometimes without IDLE or `venv`. Install/refresh via your package manager:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv idle3
```

Then check the version (`python3 --version`). If your distro's Python is older than 3.13 and you want the current release, use the [deadsnakes PPA](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa) or [pyenv](https://github.com/pyenv/pyenv) — but for this course, **any Python 3.13+ is fine**, and even 3.11/3.12 will run everything we do. Don't over-engineer it.

> Fedora: `sudo dnf install python3 python3-idle`. Arch: `sudo pacman -S python tk` (Tk gives you IDLE + the graphics we use later).

Skip to [Verify](#verify-it-works).

---

## Verify it works

Open a terminal — **IDLE** is the simplest: launch IDLE and you'll get a `>>>` prompt (the "shell"). Or use your OS terminal (Terminal on macOS/Linux, Command Prompt or PowerShell on Windows).

**Check the version:**

- macOS / Linux: `python3 --version`
- Windows: `python --version`  (or `py --version`)

You should see something like `Python 3.14.6`. Any `3.13.x` or newer is perfect; `3.11`/`3.12` will also work for this course.

**Run your first line of code.** In IDLE's `>>>` shell (or after typing `python3` / `python` in a terminal), type:

```python
print("Hello, CS 1050!")
```

Press **Enter**. If you see `Hello, CS 1050!` printed back, you're done — Python works. 🎉

**One-command environment check.** This repo includes [`check_env.py`](check_env.py). Download it, then run it to confirm you're on the right Python (current version, *not* a macOS system stub):

- macOS / Linux: `python3 check_env.py`
- Windows: `python check_env.py`

It prints PASS/FAIL with your version and interpreter location. Run it any time an assignment "won't run right" — it's the fastest way to catch a wrong-Python problem. You'll use the same command before every assignment.

---

## Editors: where you write code

You'll outgrow the `>>>` shell quickly (it forgets everything when closed). Three good options, easiest first:

| Editor | Best for | Notes |
|---|---|---|
| **IDLE** | starting out, matches our textbook | Ships with Python. Open it, `File → New File`, write code, press **F5** to run. **Use this for the course unless told otherwise.** |
| **Thonny** | absolute beginners who want one simple install | [thonny.org](https://thonny.org) — bundles its *own* Python + a beginner-friendly debugger and variable viewer. A great all-in-one if the steps above felt hard. |
| **VS Code** | when you want a "real" pro editor later | [code.visualstudio.com](https://code.visualstudio.com) + the Python extension. More powerful, more setup — graduate to it when you're comfortable. |

Pick **one** and stick with it for now. More tools ≠ more learning early on.

> **Why IDLE first (on purpose).** IDLE is intentionally bare. No aggressive autocomplete, no AI suggestions, no red-squiggle hand-holding — so you actually learn the syntax and the concepts instead of leaning on an IDE to write code for you. Once the fundamentals are yours, graduate to VS Code and let the power tools earn their keep. Starting in a "dumber" editor is a feature, not a limitation.

---

## Troubleshooting

- **Windows: `'python' is not recognized…`** → PATH wasn't set. Re-run the installer, choose **Modify**, and ensure **"Add python.exe to PATH"** is checked (or reinstall and check the box on the first screen). Then open a *new* terminal.
- **macOS: `python` not found, but `python3` works** → that's expected. On macOS use **`python3`** (and `pip3`). Both refer to your python.org install.
- **macOS: typing `python3` opens the App Store or an old version** → install from python.org (above); the system stub points nowhere useful until you do.
- **IDLE won't open on Linux** → install the Tk/IDLE package: `sudo apt install idle3` (Debian/Ubuntu) or `sudo pacman -S tk` (Arch).
- **"It still doesn't work."** → Note your OS, the exact command you typed, and the exact error text, and bring all three when you ask for help. That trio is what lets anyone diagnose it fast.

> **Using an AI tutor:** tools like ChatGPT/Claude are fine for *explaining* an error message or a concept in plain language — paste the error and ask "what does this mean?" Use them to understand, not to hand in code you can't explain. Course academic-integrity rules still apply.

---

## Keeping your environment clean (optional)

Short version: **for CS 1050 you don't need virtual environments or pyenv.** Here's the honest reasoning so it's a choice, not a mystery.

- **Why people isolate environments:** to stop one project's installed *packages* from clashing with another's. CS 1050 installs **no third-party packages** — we use only Python's standard library plus the textbook's `graphics.py`. The main reason to isolate simply doesn't apply here.
- **What you're already doing right:** installing from python.org (not relying on a system Python) and confirming it with [`check_env.py`](check_env.py). That alone keeps you off any OS-managed interpreter.
- **The cost of venvs in week 1:** you'd have to *activate* the environment every session, and "my code won't run" almost always turns out to be "I forgot to activate." That's more support headaches than isolation is worth when there are no packages to isolate.

**If you still want a clean, isolated setup** (great instinct for later projects), the lightweight way ships *with* Python — no pyenv needed:

```bash
# from your course folder, once:
python3 -m venv .venv            # Windows: python -m venv .venv
# then each session, activate it:
source .venv/bin/activate        # Windows (PowerShell): .venv\Scripts\Activate.ps1
python check_env.py              # confirm you're on the venv's Python
```

> **Instructor / power-user note:** the maintainer runs `pyenv` + `pyenv-virtualenv` on personal and work machines, which is the right tool once you juggle multiple Python *versions* across many projects. That's deliberately **out of scope for students** — it's setup overhead with no CS1 payoff. If a future course in the sequence needs third-party packages, we'll introduce venvs there, where the benefit is real.

---

*Adapted and modernized from two earlier walk-throughs by the author ([2023](https://dakotalearns.wordpress.com/2023/04/03/installation-guide-for-python-macos-windows/), [2024](https://dakotalearns.wordpress.com/2024/04/01/installation-guide-python-3-x-%f0%9f%90%8d/)) — updated for current Python, expanded to Linux, and aligned to this course's IDLE-first, single-install approach.*
