---
title: "Values, Types, and Variables (and Your First Program)"
date_published: 2026-07-03
---

# Values, Types, and Variables (and Your First Program)

<!-- purpose: Unit 1 lesson: values, the four core types, variables, comments and your first program. -->

<!-- author_status: assistant-mechanical | section: For instructors note (alignment from the outcomes map) -->
??? note "For instructors: outcome alignment"
    Aligns with **MSU Denver CS 1050 objectives 6–8** (expressions, core data types, I/O); more broadly, with **ABET** student outcomes **SO-2** and **SO-6**, under the **ACM/IEEE-CS CS2023** *SDF + FPL* knowledge areas. *(Alignment only; not an accreditation claim. Full mapping in the [outcomes map](https://dakotalearns.com/courses/computer-science-1/syllabus/outcomes_map_abet_cs2023/); see also the [disclaimers](https://dakotalearns.com/disclaimers/).)*
<!-- /author_status -->

<!-- author_status: dakota-authored | section: Frame -->
Welcome back! Last time we figured out what computation *is*: inputs, exact in-order steps, a predictable output. Today we meet the building blocks that every program is made of: **values, types, and variables.**

I want to be straight with you about why we're starting here. These three terms are critical to *every* future lesson; get a good grasp on them now and the rest of this course gets dramatically easier.

If we try to brute-force past them, it'd be like trying to speak a language without using any parts of speech. If you're lucky, you end up with caveman speak: *"Me hungry! We eat?"*, and that's the **best** case.

So let's dive right in.
<!-- /author_status -->

---

## What you'll be able to do

<!-- author_status: assistant-mechanical | section: Objectives -->
By the end of this lesson, you'll be able to:

1. **Explain what a value is** and why a value is meaningful only when it's tied to *some thing*.
2. **Name the four core types** we'll use constantly (whole numbers, decimal numbers, text, and true/false) and tell them apart.
3. **Explain what a variable is** (a name you attach to a value) and write a good, descriptive variable name.
4. **Write and run your first real Python program**, assigning values to variables and printing them.


!!! note "Before you start"
    This lesson assumes you've installed Python and can open **IDLE**; the [install guide](https://dakotalearns.com/guides/install-python/) walks you through it. If not, do that first; it's the one gate everything else depends on.
<!-- /author_status -->

---

## Values: what something is worth

<!-- author_status: dakota-authored | section: Core explanation (values) -->
A **value** is just what something is actually worth.

Imagine you open your bank app and see you have **$650**; that's your value for that account. Take an antique doll to get appraised and it might be worth **$75**. Or say you're trying out for an NFL team and have to run a 40-meter dash; if you're *really* fast, the stopwatch might read **4.3 seconds**. Those are all values: worths, measurements.

Here's the key thing I want you to take away: **a value is always associated with *some* thing.** We recognize `650` and `75` and `4.3` as numbers, sure, but without a *thing* they're attached to, they're just numbers floating in space, relatively meaningless. $650 of *what*? 4.3 seconds of *what*? The "what" is the whole point.
<!-- /author_status -->

---

## Types: not all values are the same kind of thing

<!-- author_status: dakota-authored | section: Core explanation (types) -->
Look again at those values and you'll notice they're not all the same *kind* of thing. That "kind" is what we call a **type**.

In just that one example we already had two different kinds of numbers:

- **Whole numbers** like `650` and `75`: no decimal part. In Python these are called **integers** (`int` for short).
- **Numbers with a decimal part** like `4.3` (the `.3` is the giveaway). Python calls these **floats** (`float`).

Computers actually store those two differently under the hood. The good news: you almost certainly won't be building computers or operating systems in your first course, so we don't have to care about the *how*; just know they're treated as different types.

There are other types, too. The words on this page are text; many languages, Python included, call text a **string** (`str`). And it isn't all words and numbers; some values are just plain true-or-false facts. Picture a **statement** you could stamp as true or false:

- *"It rained today."*
- *"We're getting takeout tonight."*
- *"My flight is cancelled."*

Each one is either **True** or **False**, nothing in between: a type all its own, called a **boolean** (`bool`). (Notice these are *statements*, not questions; a boolean is the truth of a statement, and that becomes the very thing you'll test with `if` down the road.)

I hope those examples show you that types tie right into everyday life, and that values aren't always words or numbers.

!!! tip "The four core types, at a glance"
    | Type | Means | Example value |
    |---|---|---|
    | `int` | whole number | `650` |
    | `float` | number with a decimal part | `4.3` |
    | `str` | text ("string") | `"21 Jump Street"` |
    | `bool` | a true/false fact | `False` |

These four are the building blocks we'll lean on constantly, but they aren't the *only* types. Python has plenty more (you can see them all in [the official Python type docs](https://docs.python.org/3/library/stdtypes.html)), and you'll meet the big ones (**lists** and **dictionaries**) in their own lessons later.

Heads up: that link is the *official* documentation; it's thorough and a little dense, which is completely normal. You're not meant to read it all today; just getting comfortable knowing the official docs exist (and that you *can* look things up there) is a real skill we'll build the whole way through.
<!-- /author_status -->

---

## Variables: names for your values

<!-- author_status: dakota-authored | section: Core explanation (variables) -->
I know the word **variable** scares a lot of people; it drags up memories of algebra class and solving for *x*. Take a breath: this is gentler than that.

A **variable** is simply a human-readable name you attach to a value. Honestly, you've already met a bunch of them today. That bank balance worth $650? If you were writing a program, you might keep it in a variable named `bank_balance`. The doll appraisal worth $75? You might call it `doll_appraisal_dollar_amount`. That's it: **variables are just a readable way to refer to things, and you usually assign some value to them.**

Notice those names actually *say what they hold*. `bank_balance` tells you exactly what's inside; a name like `x` wouldn't. **Good, descriptive names** are a habit worth building from day one.

!!! warning "★ Hold onto this; it comes back"
    A variable is a **name that refers to a value**; it is *not* the value itself. That distinction feels small right now, but it's the seed of one of the most important (and most under-taught) ideas in this whole course. We'll come back to it hard in **Week 5/6** when we look at how Python *really* stores your data.
<!-- /author_status -->

### The rules for naming things

<!-- author_status: assistant-shared | section: Variable naming rules (Dakota to confirm framing) -->
Before you go wild naming things, Python has a few **hard rules**; break one and your program won't run:

| ✅ Valid | ❌ Won't run | The rule |
|---|---|---|
| `bank_balance`, `player1` | `bank-balance`, `my variable` | letters, digits, and `_` only (that `-` is a minus sign; spaces aren't allowed) |
| `score1` | `1score` | can't start with a digit |
| `total`, `class_size` | `class`, `if`, `for` | can't be one of Python's **keywords** (its reserved words; [the full list](https://docs.python.org/3/reference/lexical_analysis.html#keywords) is short) |

One more gotcha (not an error, just surprising): **case matters**; `score`, `Score`, and `SCORE` are three *different* names.

And two **habits**, not rules, but they'll save you (and anyone who reads your code):

- **Say what it holds:** `total_price` beats `tp` beats `x`.
- **Use `snake_case`:** lowercase words joined by underscores (`first_name`, `is_logged_in`). It's the standard Python style, so your code looks like everyone else's.
<!-- /author_status -->

---

## Your first program

<!-- author_status: assistant-shared | section: Worked example (uses the shell; IDLE mechanics live in the install guide) -->
Enough words; let's make the machine do something with what we just learned. Open **IDLE's interactive shell** (new to it? [the IDLE primer in the setup guide](https://dakotalearns.com/guides/install-python/#meet-idle) has you covered) and type these one at a time:

```pycon
>>> 650
650
>>> bank_balance = 650
>>> bank_balance
650
>>> "21 Jump Street"
'21 Jump Street'
>>> type(4.3)
<class 'float'>
```

See it? Typing a value echoes it back; assigning `bank_balance = 650` stores it under a name; typing the name hands back what's inside; and `type(...)` tells you what *kind* of value you've got. Play with your own values here; it's the fastest way to build a feel for types.

### Now save it as a real program

The shell forgets everything when you close it, so when you want to **keep** your steps, put them in a file (`first_program.py`) and run it; [the IDLE primer in the setup guide](https://dakotalearns.com/guides/install-python/#meet-idle) shows you how:

```python
# Attach values to descriptive names (variables)
bank_balance = 650               # whole number  -> int
doll_appraisal = 75              # whole number  -> int
dash_time = 4.3                  # has a decimal  -> float
favorite_movie = "21 Jump Street"   # text         -> str
it_rained_today = False          # a yes/no fact  -> bool

# A file doesn't echo like the shell does, so we print() what we want to see
print(bank_balance)
print(favorite_movie)
print(it_rained_today)
```

Run it and you'll see:

```text
650
21 Jump Street
False
```

And there it is, a real program: you gave it **inputs** (the values), it followed your **steps** *exactly and in order* (assign, then print), and it produced a **predictable output**, the same shape from Lesson 1.

!!! note "Want to see a value's type?"
    Python will tell you a value's type if you ask. In a file, try `print(type(dash_time))` and you'll see `<class 'float'>` (in the shell, just `type(dash_time)` is enough). Handy when you're not sure what kind of thing you're holding.
<!-- /author_status -->

---

## Comments: notes to future you

<!-- author_status: dakota-authored | section: Comments | source: WK1, 2026-07-03 | approved + promoted 2026-07-03 -->
Did you catch those lines starting with `#` in the program above? Those weren't for Python; they were for *you*. Let's give them a proper introduction, because you'll be writing them for the rest of this course (and, honestly, the rest of your programming life).

A **comment** is a special kind of code: a human-readable note that lives right beside the code it describes. Python skips comments entirely when it runs your program (zero effect on the output), and that's exactly what makes them so valuable. They're a space for *humans* in a file otherwise written for a machine.

Here's one of the biggest lessons I can hand you on day one: **you will not remember why you wrote what you wrote.** Not 12 months from now; sometimes not even 12 days from now. A comment is a note to *future you* (and, as you grow, to future *others* who read your code) explaining what past-you was thinking. Future you will be grateful.

Writing one is simple: type a hashtag (or "pound sign," for those of us who had Yahoo Messenger accounts and played outside), then a space, then your note:

```python
# Attach values to descriptive names (variables)
bank_balance = 650  # checking account, not savings
```

A comment can take a whole line, or ride at the end of one. Need more room? Go to a new line and start it with another `#`. (How long is too long for one line? The official Python style guide, [PEP 8](https://peps.python.org/pep-0008/), wraps code at 79 characters and comments at 72, and plenty of workplaces stretch that to ~100. Don't memorize the numbers; just don't write novels sideways.)

And if you're wondering *how many* comments to write: if I had to pick, I'd rather you leave too many than too few. You'll find the right balance over time; every programmer does. Watch for it through this course, too: I'll use comments constantly in the sample files (assignment instructions, spacing out sections, little explanations right where you need them).

*(Python also has a way to write longer, multi-line documentation; we'll meet it in Week 5 when we start defining our own functions. One new idea at a time.)*
<!-- /author_status -->

---

## Check yourself

<!-- author_status: assistant-mechanical | section: Retrieval checks (quiz/parsons data - rendered by the site) -->
No grade; just retrieval. These score themselves, so be honest with your first answer.

```quiz
{
  "questions": [
    {
      "prompt": "What type is the value `4.3`?",
      "hint": "Whole numbers never carry a decimal point - `4.3` does.",
      "options": ["`int`", "`float`", "`str`", "`bool`"],
      "answer": "`float`",
      "explain": "The decimal part is the giveaway - `650` and `75`, with no decimal part, are `int` values."
    },
    {
      "prompt": "Is `\"21 Jump Street\"` a number or text?",
      "hint": "Don't look at the characters inside - look at what's wrapped *around* them.",
      "options": [
        "A number - it starts with `21`.",
        "Text - the quotes are the giveaway.",
        "Both - Python splits it into a number and words."
      ],
      "answer": "Text - the quotes are the giveaway.",
      "explain": "It's a **string** (`str`). That `21` is part of a name - a place - not a quantity."
    },
    {
      "prompt": "In `bank_balance = 650`, which part is the variable?",
      "hint": "One side of the `=` is a name somebody invented; the other side is the value that name points to.",
      "options": ["`bank_balance`", "`650`", "The `=` sign"],
      "answer": "`bank_balance`",
      "explain": "`bank_balance` is the **name**; `650` is the **value** it refers to. The name isn't the value itself - hold onto that for Week 5/6."
    },
    {
      "prompt": "Which type fits a statement that's either true or false, like \"My flight is cancelled\"?",
      "hint": "Count the possible answers to a true-or-false question. One of the four types holds exactly that many values.",
      "options": ["`int`", "`float`", "`str`", "`bool`"],
      "answer": "`bool`",
      "explain": "A **boolean** (`bool`) - its only two values are `True` and `False`."
    },
    {
      "prompt": "What does Python do when it runs a line like `# update this next week`?",
      "hint": "Ask yourself who a `#` line is written *for* - the computer, or the humans reading the code later?",
      "options": [
        "Prints the note to the screen.",
        "Stops with an error - that isn't valid code.",
        "Skips it entirely - comments are notes for humans, not instructions."
      ],
      "answer": "Skips it entirely - comments are notes for humans, not instructions.",
      "explain": "Comments have zero effect on your program - they exist for future you (and anyone else reading your code)."
    }
  ]
}
```

```parsons
{
  "title": "Build the program",
  "prompt": "Put the lines in order so the program stores a dash time, prints its value, and then prints its type - in that order.",
  "code": true,
  "lines": [
    "dash_time = 4.3",
    "print(dash_time)",
    "print(type(dash_time))"
  ]
}
```
<!-- /author_status -->

---

## Your turn (practice)

<!-- author_status: assistant-shared | section: Independent practice -->
Make a new file and create one variable of **each** of the four types, with a descriptive name:

1. an `int` (a whole-number value from your life: steps walked today, dollars in your pocket),
2. a `float` (something with a decimal: your height, a race time),
3. a `str` (a favorite movie, your city),
4. a `bool` (the answer to a yes/no question about your day).

`print()` each one and run it. Then add `print(type(your_variable))` for one of them and see what Python says.

*(This is the warm-up for [**Checkpoint 1**](checkpoint/index.md), your first low-stakes graded check, due this week.)*
<!-- /author_status -->

---

## Things people get wrong (FAQ)

<!-- author_status: dakota-authored | section: Misconceptions & FAQ (Dakota seeded both) -->
??? faq "Isn't the variable the same as its value?"
    This is the big one, so let's nail it. People think the variable *is* the value; but the bank balance is **independent** of the number attached to it. Your balance might be $650 today and something else next week; the *value* changes, but you keep signing into the **same account** with the same credentials to check it. The variable (`bank_balance`) is the account; the value ($650) is just what's in it right now. **The variable doesn't change; the value assigned to it does.** Hold that thought; it's exactly what makes Week 5/6 click.

??? faq "How do I know if something is a number or text?"
    Look at how it's written. The number `5` with no quotes means the *value* five. But sometimes you want a number that isn't a *quantity*, like talking about how much I love the movie **21 Jump Street**. That `21` isn't "twenty-one streets they jump across"; it's part of a name: a place. So it's text, a **string**, even though it looks like a number. Quotes are the tell.

??? faq "Why aren't we doing math or asking the user for input yet?"
    On purpose. We're locking in values, types, and variables first. Doing math with them (**expressions**) and asking the user to type things in (**input**) are next week; one new idea at a time.
<!-- /author_status -->

---

## Say it in your own words (communicate)

<!-- author_status: dakota-authored | section: Communicate -->
Here's your day-one communication rep: in **2–3 sentences**, explain to a friend the difference between a **variable** and its **value**, using an everyday example that *isn't* the bank account. (Think lockers, name tags, parking spots: anything where a name points to a thing that can change.)

If your friend gets it, you've understood the single most important idea in this lesson.
<!-- /author_status -->

---

## Key terms

<!-- author_status: assistant-mechanical | section: Key terms (vocab convention P12) -->
| Term | Plain-language meaning |
|---|---|
| **Value** | What something is worth; always tied to some thing. |
| **Type** | The *kind* of value. |
| **Integer (`int`)** | A whole number, no decimal part. |
| **Float (`float`)** | A number with a decimal part. |
| **String (`str`)** | Text. |
| **Boolean (`bool`)** | A true/false fact. |
| **Variable** | A readable name that refers to a value. |
| **Comment** | A `#`-prefixed note for humans, right beside the code; Python skips it entirely. |

*(Durable terms also live in the site-wide [Glossary](https://dakotalearns.com/glossary/).)*
<!-- /author_status -->

---

## Summary & what's next

<!-- author_status: assistant-mechanical | section: Summary + spaced hooks -->
- A **value** is what something is worth, and it only means something when it's tied to a thing.
- A **type** is the *kind* of value. Your four workhorses: **`int`** (whole number), **`float`** (decimal), **`str`** (text), **`bool`** (true/false).
- A **variable** is a readable **name** that refers to a value; *not* the value itself. ★ That last part returns in a big way in Week 5/6.
- You wrote and ran a real program: assign values to variables, then `print` them. Inputs → exact, in-order steps → predictable output.
- **Comments** (`# like this`) are notes for humans; Python skips them, and future you will thank present you for writing them.

**Next lesson (Week 2):** we put these building blocks to work: doing math with them (**expressions**) and letting your program **ask the user for input** so it can respond to whatever they type.

!!! info "Coming this week"
    [**Checkpoint 1**](checkpoint/index.md), your first low-stakes graded check, lands right after this lesson, built straight from today's "Your turn" practice. It's due before the add/drop deadline, so you get an honest, early taste of the course's rhythm.
<!-- /author_status -->

<!-- author_status: dakota-authored | section: Sign-off (Dakota's standard skeleton - confirm/customize the day) -->
Thanks for taking the time to read along. Until the next time we learn something together, have a wonderful day! 👋
<!-- /author_status -->
