# Module 0 — Set Up Python on Your Computer

<!-- author_status: dakota-authored | section: full page (adapted from Dakota's 2023/2024 install posts — see footer; deep-dive reviewed by Dakota 2026-07-15/2026-07-21, two passes, 17 revisions executed; promoted 2026-07-21) -->

> **Goal:** by the end of this guide you have a working, current Python on your machine and can run a one-line program — no prior experience assumed. This is the only "setup" step in the course; once it's done, every lab and assignment just works.
>
> Pick your operating system, follow the steps, then do the **Verify** check at the bottom. This could take you somewhere around 15–20 minutes.

If you get stuck, that's normal — jump to [Troubleshooting](#troubleshooting). Asking for help early is a skill, not a failure.

---

## What's in this module (and what's not)

- **Goal:** a working, current Python you can run a program with — no prior experience assumed.
- **Covered:** installing Python on macOS / Windows / Linux, picking an editor (IDLE), verifying it works, and fixing the common setup failures.
- **Not covered (and where it lives):** writing actual programs — that's Unit 1 onward. Virtual environments and version managers are **optional** and sit in [Advanced Instructions](#advanced-instructions-optional), not the required path.
- **Prerequisites:** none.

---

## What you're installing and why

- **Python** — the language we write in. It has a longer history than most people expect — created by Guido van Rossum, first released in 1991, and openly developed ever since (the [official history and license notes](https://docs.python.org/3/license.html) and [Wikipedia's History of Python](https://en.wikipedia.org/wiki/History_of_Python) are both worth a skim if you're curious where your new language came from). We install the **current stable version** (Python **3.13 or newer**; 3.14 is current as of mid-2026). Always take the latest stable release from the official site — *not* an older one; the [FAQ below](#faqs--design-decisions) explains why.
- **An editor** — where you can write and run code. For the same reason you'd go to Microsoft Word to write a letter, you'll go to **IDLE** to write Python (or later, VS Code, PyCharm, or other editors). We start with IDLE (Python's built-in editor and interactive shell — it rides along free with every python.org install, nothing extra to get) and it matches our textbook. You'll meet it for real in the [Verify](#verify-it-works) step; alternatives are listed [below](#editors-where-you-write-code).

Only install Python from **[python.org](https://www.python.org/downloads/)**. Other sources exist, but the official installer is the safest, most predictable path for this course.

---

## macOS 🍎

macOS does **not** come with a Python you should use for this course (the system may have an old one or none). Install a fresh copy:

1. Go to **<https://www.python.org/downloads/>**. The page detects your Mac and shows a yellow **"Download Python 3.x.x"** button — click it (this is the current stable release).
2. Open the downloaded `.pkg` file from your **Downloads** folder.
3. Click **Continue** through Introduction → Read Me → License (read them), click **Agree**, then **Install**. Enter your password / Touch ID when asked.
4. When it finishes, click **Close**. (If it offers to move the installer to the Trash, that's fine.)

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

Most Linux distributions already include Python 3, but often not the newest and sometimes without IDLE or `venv`. Install/refresh via your package manager (`sudo` runs a command with admin rights; `apt` is Debian/Ubuntu's package manager — though if you're on Linux, odds are you knew that already):

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv idle3
```

Then check the version (`python3 --version`). If your distro's Python is older than 3.13 and you want the current release, use the [deadsnakes PPA](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa) or [pyenv](https://github.com/pyenv/pyenv) — but for this course, **any Python 3.13 or newer is fine**, and even 3.11/3.12 will run everything we do. Don't over-engineer it.

> - Fedora: `sudo dnf install python3 python3-idle`
> - Arch: `sudo pacman -S python tk` (Tk gives you IDLE + the graphics we use later)

Skip to [Verify](#verify-it-works).

---

## Verify it works

Two ways to check the version — pick whichever tool you already have open:

- **In IDLE:** launch it (Windows: press Start and type "IDLE"; macOS: press `Cmd+Space` and type "IDLE"; Linux: run `idle3`) and look at the **top of the shell window** — the very first line announces the version (something like `Python 3.14.6 (...)`). No command needed.
- **In your operating system's terminal** (Terminal on macOS/Linux; Command Prompt or PowerShell on Windows — *not* IDLE's `>>>` shell, which speaks Python, not terminal commands): type `python3 --version` on macOS/Linux, or `python --version` (or `py --version`) on Windows. Never used a terminal before? The short [Terminal Basics guide](https://dakotalearns.com/guides/terminal-basics/) covers everything this course needs.

Either way, you should see something like `Python 3.14.6`. Any `3.13` or newer is perfect; `3.11`/`3.12` will also work for this course.

**Run your first line of code.** In IDLE's `>>>` shell (or after typing `python3` / `python` in a terminal), type:

```python
print("Hello, Computer Science 1!")
```

Press **Enter**. If you see `Hello, Computer Science 1!` printed back, you're done — Python works. 🎉

**One-command environment check.** This repo includes [`check_env.py`](check_env.py). Download it, then run it to confirm you're on the right Python (current version, *not* a macOS system stub). One catch that trips people up: your terminal has to be **in the same folder as the file** (or you give the full path) — you can't run it "from anywhere." (If "in the same folder" is a new idea, [Terminal Basics](https://dakotalearns.com/guides/terminal-basics/) explains it in about ten minutes.) In my case, the file lands in Downloads, so:

- macOS / Linux: `cd ~/Downloads`, then `python3 check_env.py`
- Windows: `cd Downloads`, then `python check_env.py`

It prints PASS/FAIL with your version and interpreter location. Run it any time an assignment "won't run right" — it's the fastest way to catch a wrong-Python problem. You'll use the same command before every assignment.

---

## Editors: where you write code

You'll outgrow the `>>>` shell quickly (it forgets everything when closed). Three good options, easiest first:

| Editor | Best for | Notes |
|---|---|---|
| **IDLE** | starting out, matches our textbook | Ships with Python. Open it, `File → New File`, write code, press **F5** to run. **Use this for the course unless told otherwise.** |
| **Thonny** | absolute beginners who want one simple install | [thonny.org](https://thonny.org) — bundles its *own* Python + a beginner-friendly debugger and variable viewer. A great all-in-one if the steps above felt hard. |
| **VS Code** (Visual Studio Code) | when you want a "real" pro editor later | [code.visualstudio.com](https://code.visualstudio.com) + the Python extension. More powerful, more setup — graduate to it when you're comfortable. |

Pick **one** and stick with it for now. More tools ≠ more learning early on.

> **Why IDLE first (on purpose).** IDLE is intentionally bare. No aggressive autocomplete, no AI suggestions, no red-squiggle hand-holding — so you actually learn the syntax and the concepts instead of leaning on an IDE to write code for you. Once the fundamentals are yours, graduate to VS Code and let the power tools earn their keep. Starting in a "dumber" editor is a feature, not a limitation.

---

## Troubleshooting

- **Windows: `'python' is not recognized…`** → PATH wasn't set. Re-run the installer, choose **Modify**, and ensure **"Add python.exe to PATH"** is checked (or reinstall and check the box on the first screen). Then open a *new* terminal.
- **macOS: `python` not found, but `python3` works** → that's expected. On macOS use **`python3`** (and `pip3`). Both refer to your python.org install.
- **macOS: typing `python3` opens the App Store or an old version** → install from python.org (above); the system stub points nowhere useful until you do.
- **IDLE won't open on Linux** → install the Tk/IDLE package: `sudo apt install idle3` (Debian/Ubuntu) or `sudo pacman -S tk` (Arch).
- **"It still doesn't work."** → Note your OS, the exact command you typed, and the exact error text — that trio is what lets anyone diagnose it fast. Then bring all three to me by [opening an issue on the course repo](https://github.com/dmill166/computer-science-1/issues) (or use the feedback link at the bottom of any course page on the site). No carrier pigeons required.

> **Using an AI tutor:** tools like ChatGPT/Claude are fine for *explaining* an error message or a concept in plain language — paste the error and ask "what does this mean?" Use them to understand, not to produce work you can't explain. If you're taking this for credit somewhere, your institution's academic-integrity rules govern what you submit; if you're self-learning, the only person you can shortcut is yourself.

---

## Advanced Instructions (optional)

> **You do not need any of this to do the course.** Computer Science 1 installs no third-party packages, so a plain python.org interpreter + IDLE is the whole requirement. This section is for students who *want* a cleaner setup or already have programming experience. Skipping it costs you nothing.

### Option A — an isolated environment with `venv` (recommended if you want isolation)

A virtual environment is a project-local sandbox so one project's packages can't clash with another's — think of it like an **artist's palette**: each artist squeezes out exactly the colors and types of paint *they* prefer, and at any time they can rinse it all clean and start over, without touching anyone else's palette. It ships *with* Python — no pyenv required. (Want the deeper dive? I wrote a whole post on these back in 2022: [Virtual Environments: What, Why, How?](https://dakotalearns.com/blog/virtual-environments-what-why-how/)) We include a helper script that creates one and verifies it. Same pathing catch as `check_env.py`: these commands assume your terminal is **inside the course folder** (the unzipped repo) — `cd` there first ([Terminal Basics](https://dakotalearns.com/guides/terminal-basics/) shows how, and why no `chmod` is needed here):

```bash
# macOS / Linux, from the course folder root:
bash resources/setup/setup_env.sh

# Windows (PowerShell), from the course folder root:
powershell -ExecutionPolicy Bypass -File resources\setup\setup_env.ps1
```

Or do it by hand (again, from inside your project folder):

```bash
python3 -m venv .venv             # Windows: python -m venv .venv
source .venv/bin/activate         # Windows (PowerShell): .venv\Scripts\Activate.ps1
python check_env.py               # confirm you're on the venv's Python
```

The one catch: you must **activate** the environment in each new terminal session (`source .venv/bin/activate`), and `deactivate` to leave. Forgetting to activate is the #1 "why won't my code run?" cause — which is exactly why it's optional, not required.

### Option B — multiple Python versions with `pyenv` (power users)

If you juggle several Python *versions* across many projects, [`pyenv`](https://github.com/pyenv/pyenv) (+ `pyenv-virtualenv`) is the right tool — it's what I uses on personal/work machines. It's **overkill for this course** and adds real setup overhead, so it's listed here only for those who already want it. We introduce environment isolation properly in a later course in the sequence, where third-party dependencies make it worthwhile.

---

## FAQs & design decisions

**Why IDLE instead of VS Code / PyCharm?**
IDLE ships with Python (zero extra install) and is intentionally bare — no aggressive autocomplete or AI suggestions — so you learn the syntax and concepts yourself instead of leaning on the editor. Graduate to VS Code once the fundamentals are yours. (See [Editors](#editors-where-you-write-code).)

**Why don't we use virtual environments or `pyenv` by default?**
The reason to isolate environments is third-party *package* conflicts, and this course installs no third-party packages — everything runs on the standard library. (If you follow the optional textbook's graphics chapters, its companion `graphics.py` is a single file you download alongside your code, not a package install.) Requiring virtual environments in week 1 mostly produces "I forgot to activate" problems. We enforce the thing that actually matters — a correct interpreter — with [`check_env.py`](check_env.py) instead. Want isolation anyway? See [Advanced Instructions](#advanced-instructions-optional).

**Why install from python.org instead of Homebrew / Anaconda / the Microsoft Store?**
One predictable, official source keeps everyone's setup the same and easy to support. Homebrew/Anaconda/Store installs each have their own quirks and PATH behaviors that generate avoidable confusion in a beginner course.

**Why the "latest stable" version and not the one in "security" status?**
Older guides (including my own earlier posts) suggested the oldest still-supported version. For a *learner* that's backwards — you want a current, fully supported release. Any 3.13 or newer is ideal; 3.11/3.12 still work.

**On macOS, am I installing a second Python that conflicts with the system one?**
No — modern macOS has no general-use system Python (just a stub). Your python.org install becomes the `python3` you use. `check_env.py` confirms you're on it.

**Can I use ChatGPT / Claude to help?**
Yes, to *explain* errors or concepts in plain language — not to produce work you can't explain. If you're enrolled somewhere for credit, your institution's academic-integrity rules govern your submissions; self-learners — you're only cheating yourself with AI shortcuts and copy-pastes.

---

*Follows the [Module Standard](https://github.com/dmill166/cs-teaching/blob/main/MODULE_STANDARD.md). Adapted and modernized from two install walk-throughs I wrote in [2023](https://dakotalearns.com/blog/installation-guide-for-python-macos-windows/) and [2024](https://dakotalearns.com/blog/installation-guide-python-3-x/).*
