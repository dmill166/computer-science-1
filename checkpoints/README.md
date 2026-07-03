# Checkpoints

Low-stakes graded check-ins — one per unit, numbered by the unit they assess (Checkpoint 1 covers Unit 1). A checkpoint lands **before** that unit's larger graded work, so students get an honest, early signal with almost nothing at stake. (MIT's courses call these "finger exercises"; we call them checkpoints.)

## Convention

- One folder per checkpoint: `NN_topic/` (unit number + topic, matching the lecture folder it follows).
- Each folder contains:
  - `index.md` — the student-facing prompt page (renders on the site at the folder's clean URL, e.g. `/checkpoints/01_topic/`; files named `README.md` are repo-internal and excluded from the sync).
  - `starter/` — the file(s) students download and edit, plus `check_my_work.py`, a self-check students run themselves before submitting (plain Python — no extra installs; the same checks are pytest-compatible for grading).
- Solutions and rubrics live in the **private** `computer-science-1-solutions` repo, never here.

## Design rules

- A checkpoint exercises the unit's real semantics — never busy-work, never hello-world.
- `check_my_work.py` must **fail on the untouched starter** (a self-check that passes with no work done is an answer key in disguise).
- Low-stakes means low-stakes: completion-weight grading, generous retries, and the point is the feedback signal — for the student *and* the schedule's informed-drop front-load.
