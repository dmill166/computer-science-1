# Computer Science 1 — Outcomes Mapping
## Course objectives → ABET CAC student outcomes → ACM/IEEE-CS CS2023 knowledge areas

> **Purpose:** demonstrate that CS 1050 materials are deliberately aligned to (1) the **ABET Computing Accreditation Commission** student outcomes under which MSU Denver's CS B.S. is accredited, and (2) the **ACM/IEEE-CS CS2023** curricular knowledge areas. Doubles as a build-in-public content asset and a tested-experience artifact.
>
> **Draft status (2026-06-14):** mappings are the author's reasoned alignment, not an official department or ABET determination.

## Reference: ABET CAC student outcomes (computing programs)

1. **(SO-1)** Analyze a complex computing problem and apply principles of computing and other relevant disciplines to identify solutions.
2. **(SO-2)** Design, implement, and evaluate a computing-based solution to meet a given set of computing requirements.
3. **(SO-3)** Communicate effectively in a variety of professional contexts.
4. **(SO-4)** Recognize professional responsibilities and make informed judgments in computing practice based on legal and ethical principles.
5. **(SO-5)** Function effectively as a member or leader of a team.
6. **(SO-6)** Apply computer science theory and software development fundamentals to produce computing-based solutions. *(CS-specific)*

## Reference: CS2023 knowledge areas used here

- **SDF** — Software Development Fundamentals
- **FPL** — Foundations of Programming Languages
- **SE** — Software Engineering
- **AL** — Algorithmic Foundations
- **SEP** — Society, Ethics, and Professionalism

## Mapping table

| # | CS 1050 objective | ABET SO | CS2023 KA | Course-of-record unit(s) |
|---|---|---|---|---|
| 1 | Solve simple-to-medium problems by writing correct programs | SO-1, SO-2, SO-6 | SDF, AL | 1, 2, all |
| 2 | Document code clearly and appropriately | SO-3, SO-6 | SE, SDF | 2, 6 |
| 3 | Decompose a problem into modular components | SO-2, SO-6 | SDF, SE | 2, 3 (functions), 9-design |
| 4 | Declare and use classes, methods, and variables | SO-2, SO-6 | FPL, SDF | 4, 6 |
| 5 | Use parameters and return values correctly | SO-2, SO-6 | FPL, SDF | 6 (functions) |
| 6 | Write expressions; use decision and loop control structures | SO-2, SO-6 | SDF, FPL | 4, 7, 8 |
| 7 | Use core data types (int, real, char, bool, array/list, string) | SO-6 | FPL, SDF | 4, 9 |
| 8 | Perform interactive and file I/O | SO-2, SO-6 | SDF | 5 |
| 9 | Apply top-down design and stepwise refinement | SO-1, SO-2 | SE, SDF | 2, 9-design |
| 10 | Reason about scope and visibility of identifiers | SO-6 | FPL | 6 |
| 11 | Test and debug programs systematically | SO-2, SO-6 | SE, SDF | 3 |
| 12 | State the steps of the software development life cycle | SO-1, SO-6 | SE | 2 |
| — | Written report / oral presentation (course-of-record) | SO-3, SO-4 | SEP, SE | labs/assignments writing thread |

> **Reading the last column — and how to tag a lecture.** The **Course-of-record unit(s)** column uses the **9 catalog (course-of-record) units** from [`lectures/README`](../lectures/README.md) (e.g. CoR unit 4 = *Data Types & Variables*). These are **NOT** the 13-unit teaching-spine numbers used for lecture folders (`lectures/NN_topic/`), where 4 = *Strings*. The two schemes deliberately reuse the same integers, so **never tag a lecture by matching unit numbers.** The stable join key is the **objective # (1–12)**: a lecture declares the objective(s) it covers (see the [crosswalk below](#lecture-to-objective-crosswalk-tagging-key)), then this table maps each objective → ABET SO + CS2023 KA.

## Coverage summary (ABET SO → where assessed)

| ABET SO | Covered by objectives | Primary assessment |
|---|---|---|
| SO-1 (analyze) | 1, 9, 12 | assignments, exams |
| SO-2 (design/implement/evaluate) | 1, 3, 4, 5, 6, 8, 9, 11 | assignments, labs, exams |
| SO-3 (communicate) | 2, + writing/presentation | research paper, oral presentation, code documentation |
| SO-4 (professional/ethical) | writing/presentation thread | research paper / book report (ethics topic option) |
| SO-5 (teamwork) | *not a primary CS1 outcome* | optional paired lab(s); revisit at course level |
| SO-6 (CS theory + dev fundamentals) | 1–12 | assignments, labs, exams |

> **Gap note:** SO-5 (teamwork) is only lightly touched by a single-author CS1. That's expected — it's carried more heavily by later courses. If the department wants CS1 to contribute to SO-5, add at least one paired/collaborative lab and assess it explicitly.

## Lecture-to-objective crosswalk (tagging key)

> Added 2026-06-20. **The authoritative source for tagging a lecture's outcomes — join on the `objective #`, never on a unit integer.** Spine unit + week are exact (spine→obj mirrors [`design_rationale`](design_rationale.md); weeks from [`schedule_fall2026`](schedule_fall2026.md)). The **CoR unit** column is a best-effort accreditation cross-reference only — the 9-unit catalog scheme doesn't map 1:1 to the spine.

| Spine unit (folder `NN_`) | Topic | Week(s) | Objective(s) | CoR unit(s) |
|---|---|---|---|---|
| 0 | What is computation / how programs run | 1 | 12 | 1 (+2) |
| 1 | Values, types, variables, expressions, I/O | 1–2 | 6, 7, 8 | 4, 5 |
| 2 | Decisions / branching | 2 | 6 | 7 |
| 3 | Iteration / loops | 3 | 6 | 8 |
| 4 | Strings & sequence basics | 4 | 6, 7 | 4 |
| 5 | Functions: decomposition, parameters, scope | 5 | 3, 4, 5, 10 | 2 (decomposition) |
| 6 | Lists, tuples, mutability & aliasing | 6 | 7 | 9 |
| 7 | Dictionaries & sets | 7 | 7 | 9 |
| 8 | Files & exceptions | 9 | 8 | 5 |
| 9 | Testing & debugging | 7 | 11 | 3 |
| 10 | Classes & OOP (+ intro inheritance) | 10–11 | 4, 10 | 6 |
| 11 | Recursion | 12 | 1, 9 | — (problem-solving; no clean CoR unit) |
| 12 | Algorithms: search, sort, intro Big-O | 13 | 1, 9 | 9 |

*(Module 0 — Python setup — is an enabler with no objective mapping.)*

**To fill a lecture's "Objectives (ABET-mapped)" section:** spine unit → its **Objective(s)** here → each objective's **ABET SO + CS2023 KA** from the [mapping table](#mapping-table). Example: `00_what_is_computation` (spine 0) → objective 12 → **SO-1, SO-6 / CS2023 SE**.
