# Computer Science 1 (Python)

<!-- purpose: Front page of the course repo: what Computer Science 1 is, who it's for, how the repo is organized, and its licenses. -->

<!-- author_status: dakota-authored | section: full page (light voice pass 2026-07-09; Dakota's reviews 2026-07-21 through 2026-08-02 - naming sweep, evergreen status line, audience framing, solutions-transparency call; promoted 2026-08-02) -->

Open, beginner-first course materials for **Computer Science 1**, taught in **Python 3** using Zelle's *Python Programming: An Introduction to Computer Science* (4th ed, 2024). Designed to be portable (a strong CS1 you'd recognize anywhere) and aligned to recognized CS1 outcomes (ABET CAC, ACM/IEEE-CS CS2023) and, for alignment only, MSU Denver's CS 1050 objectives.

I'm building this in the open, one unit at a time (on top of a full-time job, with nothing fancier than a laptop and an internet connection), and if you've never written a line of code before, you're exactly who it's for. (Already in a CS program and the material just isn't clicking the way it's presented? You're welcome here too; sometimes a different phrasing is all it takes.) Part of the [`cs-teaching`](https://github.com/dmill166/cs-teaching) initiative.

> **Affiliation:** Independent materials by Dakota Hollmann. **Not affiliated with, endorsed by, or sponsored by Metropolitan State University of Denver.** MSU Denver course codes and objectives are referenced for curriculum alignment only.

> **Status:** building in public. The [course hub](https://dakotalearns.com/courses/computer-science-1/) always shows what's live; each new unit announces on the [blog](https://dakotalearns.com/blog/).

> **Where to read this:** This public repo is the **single source of truth** for the course; prose *and* code, authored once here. The readable lessons render on **[dakotalearns.com](https://dakotalearns.com)**, pulled from this repo at build time; the **runnable code** is grabbed here as a ZIP. The site is a read surface, never a second copy.

## What's here

| Folder | Contents |
|---|---|
| [`syllabus/`](syllabus/) | Course syllabus, schedule, and the ABET CAC / ACM-IEEE CS2023 outcomes-mapping table |
| `unitNN_topic/` | The content tree: one folder per teaching-spine unit at the repo root, each containing its lecture (`index.md`), `lab/`, `checkpoint/`, and (where one lands) `assignment/`. Convention below; cross-course [structure standard](https://github.com/dmill166/cs-teaching/blob/main/COURSE_STRUCTURE.md) |
| [`resources/`](resources/) | Textbook reference, toolchain setup, and supplementary material |

## Unit folder convention

- One folder per unit at the repo root: `unitNN_topic/`, numbered by the design-rationale teaching spine (not by week; pacing lives in [`syllabus/schedule.md`](syllabus/schedule.md), the swappable per-term overlay). Zero-padded numbers keep them in teaching order everywhere.
- Inside each unit, in learner order: `index.md` (the **lecture**: renders on the site at the folder's clean URL), `lab/` (that unit's guided practice, only where the unit warrants one), `checkpoint/` (the unit's low-stakes graded check; its `starter/` self-check **fails on the untouched starter**), `assignment/` (the larger deliverable, living in the **last** unit it covers), and `.nav.yml` (the unit's on-site title).
- Labs and checkpoints are numbered by **unit** (Checkpoint 1 = Unit 1's).
- Solutions, rubrics, hidden tests, and exams live in the **private** `computer-science-1-solutions` repo, mirroring these paths, never here.
- Course-spanning artifacts (the research paper + oral presentation thread) get a course-level home when built; they belong to no unit.


## What's *not* here

Solution keys, exams, rubrics, and grading scripts live in a **private** sibling repository (`computer-science-1-solutions`) to preserve academic integrity. **Instructors:** solutions are available on request.

## Course at a glance

- **Credits:** 4 (all lecture)
- **Prerequisite:** none; no prior programming or math assumed (accessibility-first; see design rationale)
- **Language:** Python 3
- **Textbook:** John Zelle, *Python Programming: An Introduction to Computer Science*, 4th ed. (Franklin, Beedle & Associates, 2024)
- **Focus:** algorithm development, correctness, programming style, intro to software engineering and the development life cycle

See [`syllabus/design_rationale.md`](syllabus/design_rationale.md) for the course-design philosophy (portable, MIT-informed, CS2-ready, no-prerequisite), [`syllabus/index.md`](syllabus/index.md) for the full syllabus, and [`syllabus/outcomes_map_abet_cs2023.md`](syllabus/outcomes_map_abet_cs2023.md) for how the 12 course objectives map to ABET CAC student outcomes and the ACM/IEEE-CS CS2023 knowledge areas.

## Licensing

- **Course content** (text, slides, assignment prompts): [CC BY-NC-ND 4.0](LICENSE-CONTENT.md), free to read and share for noncommercial use with attribution; no derivatives.
- **Code** (starter code, examples, scripts): [PolyForm Noncommercial 1.0.0](LICENSE), free for noncommercial use.

Read it, learn from it, share it (with credit), for free. **For commercial use or to create and share an adaptation, email me at hello@dakotalearns.com for permission;** it may well be welcome.

## Attribution & copyright

This repository contains only original work. It teaches *from* the course textbook but does **not** reproduce it; concepts are explained in original words and examples, and the book is referenced by chapter, not copied. The license above covers this repo's original content only and grants no rights to any third-party material. See the initiative's [copyright policy](https://github.com/dmill166/cs-teaching/blob/main/COPYRIGHT_POLICY.md).

## Contributing / corrections

Spotted an error or have a suggestion? Open an issue. (Note the NoDerivatives terms: suggestions are welcome via issues; please don't publish modified copies.)
