# Resources

<!-- author_status: dakota-authored | section: full page (light voice pass 2026-07-09; Dakota reviewed 2026-07-21 - CS2 recommendation pulled, affiliate link + disclosure added; promoted 2026-07-21) -->

Everything course-adjacent lives here: the textbook reference, toolchain setup, and supplementary material for Computer Science 1.

## Textbook

**John Zelle, [*Python Programming: An Introduction to Computer Science*, 4th edition](https://amzn.to/3Qpgrt1)[^aff]** (Franklin, Beedle & Associates, 2024). ISBN-13: 978-1590282977 (print); eText 978-1590282984.

I've recommended this book since my own first Python coursework back in 2012; Zelle's writing style and teaching approach earn it. It covers all 12 of the course's learning objectives. Note: this book is intentionally scoped to *introductory* CS: it ends at recursion and basic searching/sorting and does **not** cover abstract data types, linked lists, stacks, queues, or trees. Those belong to Computer Science 2, which will use a dedicated data-structures text.

**Funds a bit tight?** If you know you learn better with a book in hand but the 4th edition doesn't fit the budget right now, the [**3rd edition**](https://amzn.to/4vJmxTT)[^aff] (Franklin, Beedle & Associates, 2016; ISBN-13: 978-1590282755 print, 978-1590282779 eText) is a solid lower-cost pick (used copies go cheap) or take either edition's ISBN to your local library and rent it. You'll still get a quality experience out of the course either way; the chapter numbering differs a little between editions, and the course materials flag those differences wherever they matter.

**And one book that isn't about Python at all:** the course's writing-and-presentation thread is anchored by **Barbara Oakley, [*A Mind for Numbers: How to Excel at Math and Science (Even If You Flunked Algebra)*](https://amzn.to/4xI5piu)[^aff]** (TarcherPerigee, 2014; ISBN-13: 978-0399165245). It's the learning-how-to-learn book (written for students who don't yet believe they're "math people") and it teaches the same study techniques this course's own design is built on. Which chapters, and exactly how they feed the written report and oral presentation, arrive with that thread later in the course; it's listed now so you can plan ahead or put in a library reservation (physical, eBook, and audiobook variants all exist).

## Toolchain

- **Python 3**: the current stable release (3.13 or newer) from python.org; 3.11/3.12 also run everything in this course.
- A code editor: **IDLE first** (ships with Python; the course default), Thonny for an all-in-one beginner option, or VS Code once the fundamentals are yours.
- Zelle's `graphics.py` module for the graphics-based examples (4e Ch 4 & 12), bundled with the textbook materials.

## Setup: Module 0

Step-by-step environment setup (install current Python on macOS/Windows/Linux, choose an editor, verify it works, troubleshoot the common failures) lives in **[`setup/`](setup/)**. This is the course's day-one gate; no prior experience assumed.

[^aff]: Affiliate link: if you buy through it, Dakota Learns may earn a small commission at no extra cost to you, which helps keep this work free. [Here's why](https://dakotalearns.com/disclaimers/#affiliate-links); you're always welcome to find the book elsewhere; same book, your choice.

## Accessibility note

I'm building this course in public partly to make CS more accessible. Where a free, high-quality resource exists, I prefer it or pair it (the open [Python documentation](https://docs.python.org/3/) is the flagship example) and starter code stays runnable on a stock Python install wherever possible, so nothing here needs a paid tool to learn from.
