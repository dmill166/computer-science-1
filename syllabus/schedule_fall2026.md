# Computer Science 1 — Fall 2026 Schedule (MSU Denver instance)

> **What this is:** a *dated instance* of the portable course design ([`design_rationale.md`](design_rationale.md)) mapped onto MSU Denver's **Fall 2026** academic calendar. The portable design stays general; this file is the term-specific overlay — schedule, deadlines, and how assessment is timed around the institution's drop/withdraw dates.
>
> **Term:** classes Mon **Aug 17** → Sun **Dec 6, 2026**; finals **Dec 7–13**; grades posted **Dec 18**.

## Key calendar constraints (Fall 2026)

| Date | Event | Why it matters for course design |
|---|---|---|
| Mon **Aug 17** | Classes begin | Week 1 starts. |
| Mon **Aug 24** | Last day to drop, **100% refund** | End of Week 1 — students need a real taste + a graded signal *before* this. |
| Wed **Sep 2** | Last day to drop, **50% refund** | Week 3 — second decision point. |
| Mon **Sep 7** | Labor Day (campus closed) | No class Mon of Week 4. |
| Fri **Nov 20** | Last day to **withdraw** | Week 14 — students should know their standing by here. |
| Mon–Wed **Nov 23–25** | Fall Break (no classes) | Week of Nov 23 is effectively dead (see below). |
| Thu–Fri **Nov 26–27** | Thanksgiving (campus closed) | — |
| Sun **Dec 6** | Classes end | Last instructional day. |
| **Dec 7–13** | Final Exam Week | Final assessment window. |
| ~**Dec 16** | Grades due (posted **Dec 18**) | All grading — incl. the final — must clear in ~3 days. Demands autograding + ready rubrics. |

## Design consequence: the "informed-drop" front-load

Because the **100% drop deadline is the end of Week 1** and the **50% deadline is Week 3**, the course deliberately gives an honest preview of its real rhythm early, so students self-select with accurate information rather than discovering the workload after the refund window closes:

- **Week 1** ships Module 0 (setup) **and** a genuine first taste of programming, with a **low-stakes graded finger exercise due before Aug 24**.
- **By Sep 2 (50% deadline)** students have completed assignment **a01** and an early quiz — enough signal to judge fit.
- By the drop deadlines you'll have completed the setup exercise, your first assignment (a01), and Quiz 1 — enough to gauge whether the course fits your time and goals. Honesty over enrollment-protection.

## Week-by-week (15 instructional weeks)

> Unit numbers reference the design-rationale topic spine. Front-loaded so Weeks 1–5 form the complete "teachable spine" that gets built first. Zelle chapter↔unit mapping (**4e** primary, **3e** budget) lives in the [design rationale](design_rationale.md) and the syllabus schedule table.

| Wk | Week of | Units / focus | Calendar notes | Assessment milestones |
|---|---|---|---|---|
| 1 | Aug 17 | **Module 0** setup · **Unit 0** what is computation · **Unit 1** values, types, variables, first program | Classes begin Aug 17 | **Finger exercise 0 due before Aug 24** (pre-100%-drop taste) |
| 2 | Aug 24 | **Unit 1** expressions, I/O · **Unit 2** decisions | **Aug 24: 100% drop deadline** | **a01** assigned |
| 3 | Aug 31 | **Unit 3** iteration / loops | **Sep 2: 50% drop deadline** | **a01 due**; Quiz 1 |
| 4 | Sep 7 | **Unit 4** strings & sequences | **Mon Sep 7 Labor Day — no class** | a02 assigned |
| 5 | Sep 14 | **Unit 5** functions, decomposition, scope | — | a02 due |
| 6 | Sep 21 | **Unit 6** lists, tuples, **mutability & aliasing** ★CS2 bridge — extra time | — | a03 assigned; Quiz 2 |
| 7 | Sep 28 | **Unit 7** dictionaries & sets · **Unit 9** testing & debugging (formalized) | — | a03 due |
| 8 | Oct 5 | **Review + Midterm** (Units 0–7) | — | **Midterm exam** |
| 9 | Oct 12 | **Unit 8** files & exceptions | — | a04 assigned |
| 10 | Oct 19 | **Unit 10** classes & objects ★CS2 bridge | — | a04 due |
| 11 | Oct 26 | **Unit 10** inheritance + OOP example | — | a05 assigned; Quiz 3 |
| 12 | Nov 2 | **Unit 11** recursion ★CS2 bridge | — | a05 due |
| 13 | Nov 9 | **Unit 12** searching, sorting, intro Big-O ★CS2 bridge | — | **Research paper due** (written-comm) |
| 14 | Nov 16 | Applications / buffer · **oral presentations** begin | **Fri Nov 20: withdraw deadline** | Presentations (part 1) |
| — | Nov 23 | **Fall Break + Thanksgiving — NO CLASS** | Nov 23–27 campus closed/no classes | — |
| 15 | Nov 30 | Wrap-up · review · **oral presentations** finish | Classes end **Dec 6** | Presentations (part 2) |
| Finals | Dec 7–13 | **Final exam** | Grades due ~Dec 16 | **Final exam** |

> **Lost week flag:** the week of **Nov 23** is gone to Fall Break + Thanksgiving. No new material or high-stakes deadline lands the week before or immediately after it — Week 13 closes the last CS2-bridge unit, Week 14 starts presentations, and Week 15 is wrap + finish. Don't schedule a deadline on Dec 1–2 expecting momentum across the break.

## Assessment timing rationale

- **Early + low-stakes before the drop deadlines** (finger exercise W1, a01 + quiz by W3) so students judge fit honestly.
- **Midterm at W8** — natural midpoint, covers the procedural half (Units 0–7) before the OOP/recursion/algorithms half.
- **CS2-bridge units (6, 10, 11, 12)** carry extra time and dedicated assessment — these are what make or break CS 2050.
- **Communication thread** (ABET SO-3): research paper due W13, oral presentations W14–W15 — deliberately *not* crammed into finals.
- **Grading-due constraint (~Dec 16):** the final and late deliverables must be gradeable fast → autograding for code + rubrics finalized before finals week.

## Portability note

Everything above except the **dates, holidays, and drop/withdraw deadlines** comes straight from the portable design. To run this course at another institution or term, swap this single file for that calendar — the units, assessments, and outcomes mapping don't change. That separation (portable core + dated overlay) is intentional.
