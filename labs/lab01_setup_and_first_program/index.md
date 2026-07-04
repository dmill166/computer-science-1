---
title: "Lab 1 — Set Up, Meet the Shell, and Run Your First Program"
date_published: 2026-07-03
---

<!--
STATUS: assistant-drafted spec (author map: independent practice = shared). Dakota reviews framing/tone.
Covers: Module 0 (setup) + spine Units 0–1 → MSU Denver obj 6, 7, 8, 12 → ABET SO-1, SO-2, SO-6 / CS2023 SDF, FPL, SE.
PRIMM: Part C is an explicit predict→run→investigate sequence.
-->

# Lab 1 — Set Up, Meet the Shell, and Run Your First Program

??? note "For instructors — outcome alignment"
    Covers **Module 0** (environment) plus **MSU Denver CS 1050 objectives 6–8 and 12** at a formative level; aligns with **ABET** student outcomes **SO-1, SO-2, SO-6**, under the **ACM/IEEE-CS CS2023** *SDF, FPL, SE* knowledge areas. Part C is a deliberate PRIMM sequence (Predict–Run–Investigate–Modify; the final M, **Make**, is Checkpoint 1 — students build their own from scratch there); Part D carries the course-of-record written-communication thread. *(Alignment only — not an accreditation claim. Full mapping in the [outcomes map](../../syllabus/outcomes_map_abet_cs2023.md).)*
<!-- author_status: assistant-shared | section: Lab prompt (Dakota reviews the framing) -->
Labs are where the week's ideas get into your fingers. This first one has exactly one goal: **by the end, your machine runs Python, and you've written and run a real program on it.** Work through the parts in order — each one leans on the last (steps, followed exactly and in order… sound familiar?).

Nothing here is graded on correctness — labs are completion-credit. Get stuck? That's normal on week one, and it's what the room (and office hours) are for.

## Part A — Prove your setup works

1. If you haven't installed Python yet, stop here and do the [install guide](https://dakotalearns.com/guides/install-python/) first — it walks every operating system through it.
2. Download [`check_env.py`](https://github.com/dmill166/computer-science-1/blob/main/resources/setup/check_env.py) from the course repository (the [Using GitHub guide](https://dakotalearns.com/guides/using-github/) shows how) and run it:

    ```text
    macOS / Linux:  python3 check_env.py
    Windows:        python check_env.py
    ```

3. The last line should say **PASS**. If it doesn't, it tells you what's wrong — fix that first; everything else this semester depends on it.

## Part B — Ten minutes in the interactive shell

Open **IDLE's shell** ([primer here](https://dakotalearns.com/guides/install-python/#meet-idle) if it's new to you) and try each of these with **your own values** — don't copy mine:

1. Type a number and press Enter. Then a decimal number. Then some text in quotes.
2. Create two variables about yourself with good descriptive names (the [Unit 1 lesson](../../lectures/01_values_types_variables/index.md) is your reference), then type each name to see what comes back.
3. Ask Python for the type of each: `type(your_variable_here)`.
4. Now break something on purpose: try text **without** quotes, or a variable name with a space in it. Read the error — you'll be seeing messages like this all semester, and they're friendlier than they look.

## Part C — Predict, then run

Grab the starter file [`my_lab1.py`](https://github.com/dmill166/computer-science-1/tree/main/labs/lab01_setup_and_first_program/starter) and open it in IDLE's **editor** (not the shell — the primer covers the difference).

1. **Predict:** the file's comments contain a tiny finished program. Before you run anything, write down — on paper or in a comment — exactly what you think it will print, line by line.
2. **Run it** and compare against your prediction. Exactly right? Great — you just traced a program like the machine does. Different? Even better: figure out *which line* surprised you and why.
3. **Make it yours:** replace the example variables with four of your own (one `int`, one `float`, one `str`, one `bool` — descriptive names, please) and print each one.

## Part D — Say it in your own words

At the bottom of `my_lab1.py`, in a comment (start the line with `#`), write **2–3 sentences** for a friend who's never coded: what's the difference between a *variable* and its *value*? Use your own everyday example. (Yes, this is the same rep as the lesson's communicate prompt — explaining things clearly is a skill this course grades on later, so we start practicing now.)

## Done looks like

- [ ] `check_env.py` says **PASS**
- [ ] You tried values, variables, and `type(...)` in the shell — including breaking it on purpose
- [ ] Your `my_lab1.py` runs and prints your four variables
- [ ] Your variable-vs-value explanation is in a comment at the bottom
- [ ] Turned in per your section's instructions *(section-specific details are provided in class)*

<!-- /author_status -->
