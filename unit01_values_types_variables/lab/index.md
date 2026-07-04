---
title: "Lab 1 — Meet the Shell and Run Your First Program"
date_published: 2026-07-03
---

<!--
STATUS: assistant-drafted spec (author map: independent practice = shared). Dakota reviews framing/tone.
Re-scoped 2026-07-03 (unit-first restructure): this is UNIT 1's lab — the old week-shaped Part A
(setup proof) became the precondition note; Module 0 verification lives with the install guide.
Covers: spine Unit 1 → MSU Denver obj 6, 7, 8 → ABET SO-2, SO-6 / CS2023 SDF, FPL.
PRIMM: Part B is an explicit predict→run→investigate→modify sequence (Make = Checkpoint 1).
-->

# Lab 1 — Meet the Shell and Run Your First Program

??? note "For instructors — outcome alignment"
    Unit 1's practice session. Covers **MSU Denver CS 1050 objectives 6–8** at a formative level; aligns with **ABET** student outcomes **SO-2** and **SO-6**, under the **ACM/IEEE-CS CS2023** *SDF + FPL* knowledge areas. Part B is a deliberate PRIMM sequence (Predict–Run–Investigate–Modify; the final M, **Make**, is Checkpoint 1 — students build their own from scratch there); Part C carries the course-of-record written-communication thread. *(Alignment only — not an accreditation claim. Full mapping in the [outcomes map](../../syllabus/outcomes_map_abet_cs2023.md).)*

<!-- author_status: assistant-shared | section: Lab prompt (Dakota reviews the framing) -->
Labs are where a unit's ideas get into your fingers. This one has exactly one goal: **by the end, you've explored Python's shell and written and run a real program of your own.** Work through the parts in order — each one leans on the last (steps, followed exactly and in order… sound familiar?).

Nothing here is graded on correctness — labs are practice. Get stuck? That's normal on your first lab, and it's what the room (and office hours) are for.

!!! note "Before you start"
    This lab assumes Python is installed and working — run [`check_env.py`](https://github.com/dmill166/computer-science-1/blob/main/resources/setup/check_env.py) and make sure the last line says **PASS** (the [install guide](https://dakotalearns.com/guides/install-python/) gets you there, and the [Using GitHub guide](https://dakotalearns.com/guides/using-github/) shows how to download course files). Everything else in the course depends on that PASS.

## Part A — Ten minutes in the interactive shell

Open **IDLE's shell** ([primer here](https://dakotalearns.com/guides/install-python/#meet-idle) if it's new to you) and try each of these with **your own values** — don't copy mine:

1. Type a number and press Enter. Then a decimal number. Then some text in quotes.
2. Create two variables about yourself with good descriptive names (the [Unit 1 lesson](../index.md) is your reference), then type each name to see what comes back.
3. Ask Python for the type of each: `type(your_variable_here)`.
4. Now break something on purpose: try text **without** quotes, or a variable name with a space in it. Read the error — you'll be seeing messages like this all semester, and they're friendlier than they look.

## Part B — Predict, then run

Grab the starter file [`my_lab1.py`](https://github.com/dmill166/computer-science-1/tree/main/unit01_values_types_variables/lab/starter) and open it in IDLE's **editor** (not the shell — the primer covers the difference).

1. **Predict:** the file's comments contain a tiny finished program. Before you run anything, write down — on paper or in a comment — exactly what you think it will print, line by line.
2. **Run it** and compare against your prediction. Exactly right? Great — you just traced a program like the machine does. Different? Even better: figure out *which line* surprised you and why.
3. **Make it yours:** replace the example variables with four of your own (one `int`, one `float`, one `str`, one `bool` — descriptive names, please) and print each one.

## Part C — Say it in your own words

At the bottom of `my_lab1.py`, in a comment (start the line with `#`), write **2–3 sentences** for a friend who's never coded: what's the difference between a *variable* and its *value*? Use your own everyday example. (Yes, this is the same rep as the lesson's communicate prompt — explaining things clearly is a skill this course grades on later, so we start practicing now.)

## Done looks like

- [ ] `check_env.py` says **PASS** (the precondition)
- [ ] You tried values, variables, and `type(...)` in the shell — including breaking it on purpose
- [ ] Your `my_lab1.py` runs and prints your four variables
- [ ] Your variable-vs-value explanation is in a comment at the bottom
- [ ] Enrolled in a section? Turned in per your section's instructions. Self-learning? All the boxes above checked *is* done.

<!-- /author_status -->
