# Computer Science 1
## Syllabus

<!-- author_status: dakota-authored | section: full page (light voice pass 2026-07-09; Dakota's line-by-line review 2026-07-21 + 2026-08-02 incl. reworded objectives + original course description; promoted 2026-08-02; Accessibility & use section separately marked below) -->

> A portable Computer Science 1 syllabus — its content scope is governed by the [design rationale](design_rationale.md) (MIT-informed, CS2-ready, no-prerequisite). The units map to recognized CS1 outcomes (ABET CAC, ACM/IEEE-CS CS2023) and, for alignment, to MSU Denver's CS 1050 objectives. **Where this stands:** the grading weights and exam structure below are proposed — they lock before any for-credit section runs — and this is not an official section syllabus for any institution.

??? note "How to read this page"
    **Students / self-learners:** this is the course contract — what you'll learn, what you'll build, and how work is weighted. Skim the objectives and assessment mix; the [schedule](schedule.md) shows the rhythm week by week.
    **Instructors:** this syllabus is portable by design — the [design rationale](design_rationale.md) carries the "why" behind every scope decision, and the [outcomes map](outcomes_map_abet_cs2023.md) carries the formal alignment.

---

## Course information

| | |
|---|---|
| **Course** | Computer Science 1 |
| **Credits** | 4 (all lecture; 60 lecture hours + ~120 hours additional student work) |
| **Prerequisite** | **None.** No prior programming and no math beyond basic arithmetic are assumed — the course teaches what it needs from scratch. |
| **Language** | Python |
| **Textbook** | John Zelle, *Python Programming: An Introduction to Computer Science*, 4th ed. (Franklin, Beedle & Associates, 2024) |

## Course description

Your first course in computer science. You'll learn to take a problem apart, design a step-by-step solution, and turn that design into a correct, readable Python program — then test it, debug it, and document it so someone else can follow your thinking. Along the way you'll meet the process real software teams follow — the development life cycle from idea through analysis, design, implementation, testing, and maintenance — practiced here at the scale of a single program. By the end, simple-to-medium problems are yours to solve end to end.

## Learning objectives

By the end of Computer Science 1, you'll be able to:

1. Take a problem you haven't seen before and write a correct, working program that solves it.
2. Write comments and documentation that make your code understandable to another human — including future you.
3. Break a big problem into small, manageable pieces, each with one clear purpose.
4. Create and use classes, methods, and variables — the building blocks your programs are and will be made of.
5. Pass data into functions (parameters) and get results back (return values — the function's output) without surprises.
6. Build expressions and steer a program's flow with decisions and loops.
7. Work confidently with the core data types: integers, floats, booleans, strings (and their characters), and lists.
8. Move data in and out of a program — from the keyboard and screen, and from files.
9. Design top-down: sketch the big steps first, then refine each one until it's runnable code.
10. Reason about scope — which parts of a program can see which names, and why that matters.
11. Test and debug systematically, so "it works" is something you've verified, not something you hope.
12. Describe the process real software teams follow: the development life cycle from idea through maintenance.

> These 12 objectives are written in my own words and numbered 1:1 against recognized CS1 outcomes — ABET CAC student outcomes, ACM/IEEE-CS CS2023 knowledge areas, and (for alignment) MSU Denver's course-of-record objectives. The full crosswalk: [`outcomes_map_abet_cs2023.md`](outcomes_map_abet_cs2023.md).

## Content units

1. **Computers & Programs** — what computer science is; hardware basics; languages; running Python.
2. **Software Engineering & the Development Life Cycle** — the development process; analysis → design → implementation → testing → maintenance.
3. **Testing & Debugging** — exceptions; systematic testing; unit testing.
4. **Data Types & Variables** — numeric types, strings, booleans; expressions; assignment; type conversion.
5. **Input / Output** — interactive input/output (I/O); string formatting; file processing.
6. **Classes & Objects** — using objects; defining classes; encapsulation; modules; an introduction to object-oriented programming (OOP).
7. **Decision Structures** — simple, two-way, and multi-way decisions; exception handling.
8. **Looping** — definite and indefinite loops; common loop patterns; booleans.
9. **Arrays / Lists** — lists and arrays; list operations; **linear search** and **selection sort**.

## Proposed schedule

> **For a real term, use the dated schedule:** [`schedule.md`](schedule.md) maps the units onto MSU Denver's Fall 2026 calendar with actual dates, holidays, drop/withdraw deadlines, and finals. The table below is the generic, date-free version.
> Ordered by the **[design-rationale topic spine](design_rationale.md)** (control-structures-first, MIT-aligned) — *not* the textbook's chapter order. "Unit" = spine unit; chapter columns give **Zelle 4e (primary)** and **3e (budget)**. Front-loaded so weeks 1–5 form a complete "teachable spine."

| Wk | Focus | Unit | Zelle 4e | Zelle 3e |
|---|---|---|---|---|
| 1 | Module 0 setup · what is computation · first program | 0, 1 | 1 | 1 |
| 2 | Values, types, expressions, I/O · decisions/branching | 1, 2 | 2–3, 6 | 2–3, 7 |
| 3 | Iteration / loops | 3 | 7 | 8 |
| 4 | Strings & sequence basics | 4 | 8 | 5 |
| 5 | Functions: decomposition, parameters/return, scope | 5 | 5 | 6 |
| 6 | Lists, tuples, **mutability & aliasing** ★ | 6 | 9 | 11 |
| 7 | Dictionaries & sets · testing & debugging (formalized) | 7, 9 | 9.5, 11.4 | 11, 9 |
| 8 | **Midterm** + review (units 0–7) | — | — | — |
| 9 | Files & exceptions | 8 | 10, 6.4 | 5, 7 |
| 10 | Classes & objects ★ | 10 | 12 | 10 |
| 11 | OO design + intro inheritance ★ | 10 | 13 | 12 |
| 12 | Recursion (numeric + non-numeric) ★ | 11 | 14 | 13 |
| 13 | Algorithms: search, a sort, intro Big-O ★ | 12 | 14 | 13 |
| 14 | Applications / buffer · oral presentations begin | — | — | — |
| 15 | Wrap-up · review · presentations finish | — | — | — |
| Finals | **Final exam** | — | — | — |

★ = critical CS2 bridge (extra time + dedicated assessment). Graphics (Zelle Ch 4) is woven in as motivating enrichment, not a required week (see design rationale).

## Assessment (proposed weights)

The course-of-record assesses across code **and** communication:

| Component | Weight |
|---|---|
| Programming assignments | 30% |
| Labs | 10% |
| Quizzes | 10% |
| Research paper / book report (written communication) | 10% |
| Oral presentation | 5% |
| Midterm exam | 15% |
| Final exam | 20% |

> The writing + presentation components are here on purpose — this course builds written and oral communication alongside programming (it's an accreditation-recognized outcome, ABET SO-3), not as an afterthought.

## Academic integrity

Solution keys, exams, and rubrics are maintained privately and are not published. Collaboration policy, AI-use policy, and the institution's academic-integrity standards will be stated per the official section syllabus.

## Accessibility & use

<!-- author_status: dakota-authored | section: Accessibility & use (shaped from Dakota's Sheet B voice-core dumps 2026-07-11; reframed to "someone close to me" at his call; affirmed + promoted 2026-08-02 — closes syllabus finalization item b) -->
I'll be honest: accessibility hasn't always been front-of-mind for me — not from ill will, just the good fortune of rarely needing it myself. What changed that was someone close to me, who is colorblind. Ever since we confirmed it, I've been noticing how games, websites, and applications handle (or fumble) accessibility — and it became something I want built in from the start, an automatic part of my work rather than an afterthought.

So: I want these materials usable by as many people as possible — that's the whole point of making them free and open. They're built for self-paced learners and for instructors who teach from them, and held to the standards in the initiative's [accessibility guide](https://github.com/dmill166/cs-teaching/blob/main/a11y.md). When a course is taught for credit, the formal accessibility and disability accommodations, the academic-integrity rules, and the other institutional policies come from that institution's official section syllabus — those are theirs to set, and where my guidance differs from your institution's policy, their policy governs your formal coursework. But these materials themselves should never be the thing standing in your way. If you hit an access barrier here — something hard to read, hard to navigate, or hard to use with assistive tech — please [open an issue and tell me](https://github.com/dmill166/computer-science-1/issues). I absolutely want these reports; they're how this gets better. I'd much rather know.
