# Computer Science 1
## Syllabus (v1 draft)

> **Draft status (2026-06-14):** Built from the MSU Denver course-of-record (Regular Course Syllabus, CS 1050, Fall 2016) + the 2026 Curriculog revision + the locked Python/Zelle decision. The **content scope is governed by [`design_rationale.md`](design_rationale.md)** (a portable, MIT-informed, CS2-ready design); the 9 units below are the MSU course-of-record framing the design maps onto. Schedule and grading weights are *proposed*. Not yet an official section syllabus.

---

## Course information

| | |
|---|---|
| **Course** | Computer Science 1 |
| **Credits** | 4 (all lecture; 60 lecture hours + ~120 hours additional student work) |
| **Prerequisite** | **None** (per the 2026 Curriculog revision, which removes the MTH 1110 math-readiness gate to broaden access; no prior Python assumed). *Historical course-of-record listed: CS 1030 with "C" or better, or readiness for MTH 1110.* |
| **Language** | Python 3 |
| **Textbook** | John Zelle, *Python Programming: An Introduction to Computer Science*, 4th ed. (Franklin, Beedle & Associates, 2024) |

## Catalog description (course-of-record)

First course in the computer science core sequence. Emphasis on algorithm development, correctness, and programming style; an introduction to software engineering and the software development life cycle. Students learn to design, implement, document, test, and debug programs that solve simple-to-medium problems.

## Learning objectives

By the end of CS 1050, a student can:

1. Solve simple-to-medium problems by writing correct programs.
2. Document code clearly and appropriately.
3. Decompose a problem into modular components.
4. Declare and use classes, methods, and variables.
5. Use parameters and return values correctly.
6. Write expressions and use decision and loop control structures.
7. Use the core data types: integer, real, character, boolean, array/list, and string.
8. Perform interactive (keyboard/screen) and file input/output.
9. Apply top-down design and stepwise refinement.
10. Reason about the scope and visibility of identifiers.
11. Test and debug programs systematically.
12. State the steps of the software development life cycle.

> These 12 objectives map to ABET CAC student outcomes and ACM/IEEE-CS CS2023 knowledge areas — see [`outcomes_map_abet_cs2023.md`](outcomes_map_abet_cs2023.md).

## Content units (9)

1. **Computers & Programs** — what computer science is; hardware basics; languages; running Python.
2. **Software Engineering & the Development Life Cycle** — the development process; analysis → design → implementation → testing → maintenance.
3. **Testing & Debugging** — exceptions; systematic testing; unit testing.
4. **Data Types & Variables** — numeric types, strings, booleans; expressions; assignment; type conversion.
5. **Input / Output** — interactive I/O; string formatting; file processing.
6. **Classes & Objects** — using objects; defining classes; encapsulation; modules; intro to OOP.
7. **Decision Structures** — simple, two-way, and multi-way decisions; exception handling.
8. **Looping** — definite and indefinite loops; common loop patterns; booleans.
9. **Arrays / Lists** — lists and arrays; list operations; **linear search** and **selection sort**.

## Proposed schedule (15 weeks)

> **For a real term, use the dated schedule:** [`schedule_fall2026.md`](schedule_fall2026.md) maps the units onto MSU's Fall 2026 calendar with actual dates, holidays, drop/withdraw deadlines, and finals. The table below is the generic, date-free version.
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

> The writing + presentation components are part of the course-of-record and are intentionally preserved — CS 1050 builds written and oral communication alongside programming, not as an afterthought.

## Academic integrity

Solution keys, exams, and rubrics are maintained privately and are not published. Collaboration policy, AI-use policy, and the institution's academic-integrity standards will be stated per the official section syllabus.

## Accessibility & use

These are **independent, open materials** for self-paced learners and instructors. When taught for credit, accessibility/disability accommodations, academic-integrity, and other institutional policies are governed by the official section syllabus at the offering institution. Spotted an access barrier in these materials? Please [open an issue](https://github.com/dmill166/computer-science-1/issues).
