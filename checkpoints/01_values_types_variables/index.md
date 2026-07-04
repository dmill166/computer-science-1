---
title: "Checkpoint 1 — Values, Types, and Variables"
date_published: 2026-07-03
---

<!--
STATUS: assistant-drafted spec (author map: independent practice = shared). PENDING Dakota's
"honest preview" sign-off (P9 ethical gate) before this counts as final.
Assesses: spine Unit 1 → MSU Denver obj 6, 7, 8 → ABET SO-2, SO-6 / CS2023 SDF, FPL.
Grading bucket: TBD pending syllabus finalization (flagged in the private rubric).
-->

# Checkpoint 1 — Values, Types, and Variables

??? note "For instructors — outcome alignment"
    Assesses **MSU Denver CS 1050 objectives 6–8** (core data types, variables, output) at a formative level; aligns with **ABET** student outcomes **SO-2** and **SO-6**, under the **ACM/IEEE-CS CS2023** *SDF + FPL* knowledge areas. *(Alignment only — not an accreditation claim. Full mapping in the [outcomes map](../../syllabus/outcomes_map_abet_cs2023.md).)*
<!-- author_status: assistant-shared | section: Checkpoint prompt (Dakota reviews the framing) -->
This is your first graded check-in — and it's deliberately a small one. A **checkpoint** is a low-stakes exercise that tells *you* (and me) whether the week's core idea stuck, while the stakes are still tiny. It's also an honest preview of what working in this course feels like, **before** the drop deadline — so you can judge the fit with real information. (In Fall 2026, that means it's due **before Monday, Aug 24** — see the [schedule](../../syllabus/schedule.md).)

Everything you need comes straight from [the Unit 1 lesson](../../lectures/01_values_types_variables/index.md). If you did the "Your turn" practice there, this will feel very familiar — that was the warm-up for exactly this.

## The task

Create a file named **`checkpoint_1.py`** (start from the one in `starter/`) that builds a tiny "movie card" out of variables — one of each of the four core types, using **exactly** these names:

| Variable name | Type it must hold | What to put in it |
|---|---|---|
| `favorite_movie` | `str` (text) | a movie you love, in quotes |
| `movies_watched_this_year` | `int` (whole number) | your honest-ish count |
| `movie_rating` | `float` (has a decimal part) | your rating of that movie, like `9.5` |
| `saw_it_in_theaters` | `bool` (`True`/`False`) | did you see it on the big screen? |

Then:

1. `print(...)` each of the four variables (four print lines).
2. Add one more line that prints the **type** of `movie_rating` — the lesson's "Want to see a value's type?" note shows you how.

That's the whole thing. No math, no user input, no tricks — those come later, on purpose.

## Check your own work first

The starter folder includes **`check_my_work.py`**. Keep it in the same folder as your `checkpoint_1.py` and run it:

```text
macOS / Linux:  python3 check_my_work.py
Windows:        python check_my_work.py
```

It checks each variable exists and holds the right *type* of value, and tells you in plain language what to fix. **Every line should say PASS before you submit.** Running it costs you nothing and is never a penalty — checking your own work before turning it in is exactly the habit this course is trying to build.

## Getting the files & turning it in

- Grab the `starter/` folder from the course repository — the [Using GitHub guide](https://dakotalearns.com/guides/using-github/) shows how to download it as a ZIP (no GitHub account needed).
- **Enrolled in a course section that uses this material?** Submit through your section's learning platform (Canvas or similar) — the where-and-how comes from your instructor, not this page.
- **Self-learning?** There's nothing to turn in. When every line in `check_my_work.py` says **PASS**, you've completed Checkpoint 1 — that's the whole bar, and it's the same one enrolled students are held to.

## FAQ

??? faq "What if a check still says FAIL and I can't figure out why?"
    Read the message under the FAIL line — each one says what it expected in plain language (the classic: `9` is an `int`, but `9.5` is a `float` — the decimal part is the whole point of that variable). Still stuck? In a formal section, bring it to class or office hours *before* the due date — a checkpoint is exactly the right place to get unstuck cheaply. Self-learning? Step away, re-read [the lesson's variables section](../../lectures/01_values_types_variables/index.md), and run the check again — the FAIL messages name exactly what to fix.

??? faq "How heavily is this graded?"
    It's a small number of points, and every one of them is earnable before the deadline: the self-check tells you exactly what's wrong, and you can fix and resubmit until everything passes. Full credit comes from *meeting the spec* — not from getting close — but you have every tool to get there. What it's really for: showing you, concretely and early, what this course asks of you each week.

<!-- /author_status -->
