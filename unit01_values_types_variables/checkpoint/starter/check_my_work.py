"""Checkpoint 1 self-check.

Keep this file in the SAME folder as your checkpoint_1.py, then run:

    macOS / Linux:  python3 check_my_work.py
    Windows:        python check_my_work.py

Every check should say PASS before you submit. Running this is never a
penalty -- it's the habit the whole course is built on: check your own
work.

(Course staff note: the checks below are plain test_ functions, so this
same file runs under pytest unchanged.)
"""

_IMPORT_ERROR = None
try:
    import checkpoint_1
except Exception as e:  # missing file, syntax error, crash while running
    checkpoint_1 = None
    _IMPORT_ERROR = e


# A note on the f"{...!r}" pattern in the messages below: !r formats a
# value the way Python sees it — text keeps its quotes ('12' vs 12) —
# so an error message reveals a TYPE mistake, not just a wrong value.
def _value(name, hint):
    """Fetch variable `name` from checkpoint_1, with friendly failures."""
    assert checkpoint_1 is not None, (
        "I couldn't load checkpoint_1.py at all: "
        f"{_IMPORT_ERROR!r}. Make sure checkpoint_1.py is in this same "
        "folder and runs without errors on its own first."
    )
    assert hasattr(checkpoint_1, name), (
        f"I couldn't find a variable named {name}. Check the spelling -- "
        f"it must be exactly {name}. Hint: {hint}"
    )
    return getattr(checkpoint_1, name)


def test_favorite_movie_is_text():
    """favorite_movie must hold text (a str)."""
    v = _value("favorite_movie", "a movie title, in quotes")
    assert isinstance(v, str), (
        f"favorite_movie holds {v!r}, which isn't text (a str). "
        "Wrap the movie title in quotes."
    )


def test_movies_watched_is_a_whole_number():
    """movies_watched_this_year must hold an int (bools don't count)."""
    v = _value("movies_watched_this_year", "a whole number, no quotes")
    assert isinstance(v, int) and not isinstance(v, bool), (
        f"movies_watched_this_year holds {v!r}, which isn't a whole "
        "number (an int). No quotes, no decimal point -- just the count."
    )


def test_movie_rating_is_a_float():
    """movie_rating must hold a float -- the decimal part is the point."""
    v = _value("movie_rating", "a rating with a decimal part, like 9.5")
    assert isinstance(v, float), (
        f"movie_rating holds {v!r}, which isn't a float. The decimal "
        "part is the whole point here -- 9 is an int, but 9.5 (or 9.0) "
        "is a float."
    )


def test_saw_it_in_theaters_is_a_bool():
    """saw_it_in_theaters must hold a bool (True or False, no quotes)."""
    v = _value("saw_it_in_theaters", "True or False, no quotes")
    assert isinstance(v, bool), (
        f"saw_it_in_theaters holds {v!r}, which isn't a bool. It should "
        'be True or False -- capitalized, and NOT in quotes ("True" is '
        "text)."
    )


def _main():
    """Run every check with friendly PASS/FAIL output; return exit code."""
    checks = [
        test_favorite_movie_is_text,
        test_movies_watched_is_a_whole_number,
        test_movie_rating_is_a_float,
        test_saw_it_in_theaters_is_a_bool,
    ]
    passed = 0
    print("-" * 60)
    for check in checks:
        name = check.__name__.replace("test_", "").replace("_", " ")
        try:
            check()
        except AssertionError as e:
            print(f"FAIL  {name}\n      -> {e}")
        else:
            print(f"PASS  {name}")
            passed += 1
    print("-" * 60)
    if passed == len(checks):
        print(f"All {passed} checks pass. You're ready to submit!")
        return 0
    print(
        f"{passed} of {len(checks)} checks pass. Read the FAIL messages "
        "above, fix, and run me again. (Reminder: your four print lines "
        "are still required -- these checks can't see printing, but "
        "your grader can.)"
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(_main())
