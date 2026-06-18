# Computer Science 1 — Course Design Rationale

> **Purpose:** define the *content scope* of this CS1 from first principles — portable enough to teach anywhere, but compatible with MSU Denver's program and the courses that follow it. This doc explains **what** we teach and **why**; the syllabus says **when**.
>
> **Design date:** 2026-06-14.

## Design goals

1. **Portable, not parochial.** Build a CS1 that satisfies MSU Denver's CS 1050 objectives but isn't custom-fit to only their catalog. It should be recognizable as a strong CS1 at any institution.
2. **Accessibility-first, no prerequisites.** MSU's current Curriculog revision **removes the math-readiness (MTH 1110) prerequisite** and assumes **no prior Python**. We design accordingly: every concept is introduced from scratch; no assumed programming background; math is taught inline where a topic needs it, never assumed.
3. **Serves many destinations.** At MSU, CS 1050 feeds CS, Data Science & Machine Learning, Cybersecurity, Computer Engineering, and several science majors. The course must build *general* computational competence, not CS-major-only trivia.
4. **Explicitly bridges to CS2.** The single most important job of CS1 is to make CS2 (data structures) learnable. We name the bridge concepts and make sure they're solid.

## Three sources we triangulated

| Source | What we took from it |
|---|---|
| **MIT 6.100L** *Introduction to CS and Programming using Python* (the current single-semester combined CS1; OCW Fall 2022, Dr. Ana Bell) | The gold-standard topic spine and ordering for a no-prerequisite Python CS1 — including the parts a weaker CS1 skips: recursion, aliasing/mutability, intro complexity (Big-O), classes + inheritance, hashing. |
| **MSU Denver CS 1050 objectives** (course-of-record + 2026 Curriculog revision) | The 12 required objectives and 9 content units; the accessibility/no-prereq mandate; the writing + oral-presentation requirement (atypical for CS1, and worth keeping). |
| **MSU Denver CS 2050 description** (the very next course) | What CS1 must prepare students *for*: "introduces the abstract data type (ADT)… linked-lists, trees, stacks, queues, classes, recursion, data representation… sorting and searching." Prereq for CS2 is CS 1050 **and** MTH 1110. |

## The CS2-readiness bridge (most important section)

CS 2050 assumes students arrive able to do these. CS1 must deliver them, not just mention them:

| CS2 needs… | …so CS1 must solidly teach |
|---|---|
| Building ADTs (stacks, queues, lists) as classes | **Classes & objects** — attributes, methods, `__init__`, `__str__`, encapsulation; at least intro **inheritance** |
| Linked structures (nodes pointing to nodes) | **References, mutability, and aliasing** — the mental model of "a variable is a name bound to an object." This is the #1 thing weak CS1 courses underteach and the #1 reason linked lists confuse students. |
| Recursive structures (trees) and algorithms | **Recursion** — base case / recursive case, on numbers *and* non-numeric data (strings, lists) |
| Reasoning about which structure/algorithm to use | **Intro algorithmic complexity** — counting operations, Big-O intuition (not proofs), why linear vs. binary search differ |
| Sorting & searching | **Linear search, binary search, at least one O(n²) sort** built and traced by hand |

If a student leaves CS1 shaky on **aliasing**, **classes**, or **recursion**, they will struggle in CS2. These get extra time and dedicated assessment.

## Topic spine (13 units)

Ordered for a no-prerequisite learner; each unit lists the MSU objective(s) it satisfies and whether it's a CS2 bridge. Math-light throughout.

| # | Unit | Covers MSU obj. | CS2 bridge | Zelle 4e | Zelle 3e | MIT 6.100L |
|---|---|---|---|---|---|---|
| 00 | **Module 0 — Set up Python** (per-OS install, editor, verify) | — (enabler) | — | — | — | — |
| 0 | What is computation; how programs run | 12 (SDLC intro) | — | 1 | 1 | L1 |
| 1 | Values, types, variables, expressions, interactive I/O | 6, 7, 8 | — | 2–3 | 2–3 | L2 |
| 2 | Decisions / branching | 6 | — | 6 | 7 | L2 |
| 3 | Iteration / loops | 6 | — | 7 | 8 | L3–4 |
| 4 | Strings & sequence basics | 6, 7 | — | 8 | 5 | L2, L4 |
| 5 | Functions: decomposition, abstraction, parameters/return, scope | 3, 4, 5, 10 | indirect | 5 | 6 | L7–8 |
| 6 | Lists, tuples, **mutability & aliasing** | 7 | ★★★ | 9 | 11 | L9–11 |
| 7 | Dictionaries & sets | 7 | ★ | 9 (9.5; sets orig.) | 11 | L14 |
| 8 | Files & exceptions (interactive + file I/O) | 8 | — | 10, 6.4 | 5, 7 | L13 |
| 9 | Testing & debugging *(woven through, formalized here)* | 11 | ★ | 11.4, 6.4 | 9 | L12 |
| 10 | **Classes & OOP** (attributes, methods, encapsulation, intro inheritance) | 4, 10 | ★★★ | 12, 13 | 10, 12 | L17–20 |
| 11 | **Recursion** (numeric + non-numeric) | 1, 9 | ★★★ | 14 | 13 | L15–16 |
| 12 | Algorithms: linear/binary **search**, a **sort**, **intro Big-O** | 1, 9 | ★★★ | 14 | 13 | L21–24 |
| — | **SE & SDLC thread** (style, documentation, top-down design) | 2, 3, 9, 12 | — | 2, 11 | 2, 9 | woven |
| — | **Communication thread** (research paper/report + oral presentation) | (MSU-specific) | — | — | — | — |

★ = touches a CS2 prerequisite; ★★★ = critical CS2 bridge.

> **Editions:** **Zelle 4e is the structural reference** (the locked textbook); the **3e** column is a budget-friendly fallback (cheap used copies — accessibility goal). The 4e reorg split 3e's combined "Sequences" chapter (3e Ch 5) into **Strings (8)**, **Data Collections (9)**, and **Persistent Data (10)**. Divergences to flag for 3e learners: 4e teaches **f-strings** (8.6) where 3e uses `.format()`; 4e's **pathlib** (10.2.2) is absent in 3e; 4e ends at **Ch 14**, 3e at **Ch 13**. Dictionaries are *Optional* in Zelle (4e 9.5.2) and **sets** are essentially uncovered — both are original content here, by design.

## Deliberate scope decisions

- **In, beyond a minimal CS1 (because MIT includes them and CS2 needs them):** aliasing/mutability as a first-class topic, recursion on non-numeric data, intro Big-O, intro inheritance.
- **Light touch / optional:** Zelle's graphics chapters (Ch. 4, 10) are great for engagement but not load-bearing for CS2 — use as motivating examples, not required mastery. MIT's numerical methods (float approximation, bisection on functions) become *one* lesson on binary/bisection search rather than a numerical-methods unit, to stay math-light.
- **Out (belongs to CS2 / later):** ADT *implementation* (linked lists, stacks, queues, trees), formal complexity proofs, advanced sorting (merge/quurt analysis beyond a demo). CS1 builds the intuition; CS2 builds the structures.
- **Kept because MSU requires it and it's genuinely valuable:** the **written report + oral presentation**. Communication is an ABET outcome (SO-3) and rarely assessed this early — it's a differentiator, not overhead.

## Module 0 — environment setup (the true day-one step)

A no-prerequisite course cannot assume a working interpreter, so **Module 0 is environment setup**, distinct from the conceptual Unit 0. It's a per-OS install guide (macOS / Windows / Linux), an IDLE-first editor recommendation aligned to Zelle (with Thonny and VS Code as alternatives), a copy-paste **verify** step, and a troubleshooting section for the predictable failures (Windows PATH, macOS `python` vs `python3`). It lives in `resources/setup/` so it doubles as a permanent reference, and it's the gate every later week depends on. Modernized from the author's two earlier install posts (current Python, Linux added, single-install discipline). This is also strong standalone build-in-public content — "how to install Python without prior experience" is one of the most-searched beginner questions.

## Accessibility / no-prereq design principles

- No concept assumes a prior concept the course hasn't taught, including math. Where a topic needs math (e.g., Big-O), build the intuition from counting, not algebra.
- Lead with concrete, runnable examples; introduce vocabulary after the experience, not before.
- Every unit ships a low-stakes "finger exercise" (à la MIT) before the graded assignment, so students self-check before they're evaluated.
- Starter code runs on a stock Python install; no heavyweight setup gates participation.
- **Informed-drop front-loading (calendar-aware instances):** when the course is mapped to a real term, Week 1–3 give an honest taste of the workload plus an early low-stakes graded signal *before* the institution's refund/drop deadlines, so students self-select on accurate information rather than after the refund window closes. The portable design stays date-free; a per-term overlay (e.g., [`schedule_fall2026.md`](schedule_fall2026.md)) carries the dates, holidays, and deadlines. Swap that one file to retarget another term or school.

## How this maps back to MSU

Every one of MSU's 12 objectives and 9 course-of-record units is covered (see the table above and [`outcomes_map_abet_cs2023.md`](outcomes_map_abet_cs2023.md)). We **add** depth where MIT and the CS2 prerequisites justify it (aliasing, recursion, Big-O, inheritance) and **preserve** MSU's distinctive writing/presentation requirement. The result satisfies MSU without being shaped *only* for MSU.

## Sources

- MIT 6.100L, *Introduction to CS and Programming using Python*, OCW (Fall 2022): https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/ — see "Materials by Lecture" for the 26-lecture spine.
- MIT 6.100A / 6.100B course descriptions, MIT EECS catalog / OCW.
- MSU Denver CS 2050 — Computer Science 2, catalog: https://catalog.msudenver.edu/preview_course_nopop.php?catoid=32&coid=90030
- MSU Denver CS 1050 — course-of-record (Fall 2016) + 2026 Curriculog revision (prerequisite removal; accessibility framing).
