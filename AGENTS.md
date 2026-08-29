---
title: computer-science-1 — Repo Rules for Agents
id: agents-computer-science-1
version: 1.0.0
status: active
owner: Dakota Hollmann
maintainer: claude-cowork
created: 2026-08-29
updated: 2026-08-29
scope: repo-local — adds to (and inside this repo, overrides) ~/agents/AGENTS.md
changelog:
  - "1.0.0 (2026-08-29): Initial. Created during the global-rules wiring audit, which found this repo had no CLAUDE.md or AGENTS.md and therefore inherited none of the global rules — not filing, commits, voice, or copyright."
---

# computer-science-1 — Repo Rules for Agents

**PUBLIC** student-facing materials for Computer Science 1 (Python 3), part of the
[`cs-teaching`](https://github.com/dmill166/cs-teaching) initiative. The private sibling
`computer-science-1-solutions` holds everything that would compromise assessment.

Standards live in `cs-teaching` — `COPYRIGHT_POLICY.md`, `MODULE_STANDARD.md`, `STYLE.md`.
Read them there rather than restating them here.

## Hazards

- **Academic-integrity firewall.** Solution keys, exams, rubrics and grading scripts NEVER
  appear in this repo. If a task produces one, it belongs in `computer-science-1-solutions`.
  A leak here is not recoverable by deleting the file — assume anything committed is public forever.
- **Copyright is a hard line.** The course is *aligned to* Zelle's textbook (4th ed, 2024); it does
  not reproduce it. No copied exercises, figures, or passages. Original examples only.
  Standing exception per `~/agents/rules/filing.md`: Zelle's `graphics.py` is kept where it
  accompanies course material.
- **Affiliation disclaimer is load-bearing.** Independent materials, NOT affiliated with or
  endorsed by MSU Denver; CS 1050 objectives referenced for alignment only.
- **Voice and provenance.** Prose carries `author_status` HTML comments marking who wrote what.
  Preserve and update them. Dakota is the author — see `~/agents/rules/voice.md`.
- **Module READMEs** follow the `MODULE_STANDARD.md` shape: what's in it and why, Core,
  Advanced (optional), FAQs / design decisions.
