# This sample tests the type analyzer's type narrowing logic for
# Any type with "is None" checks.

# pyright: strict

from typing import Any, reveal_type


def test_any_narrowing(x: Any):
    if x is None:
        reveal_type(x, expected_text="None")
    else:
        reveal_type(x, expected_text="Any")


def test_any_list_comprehension(xs: list[Any]):
    filtered = [x for x in xs if isinstance(x, str) or x is None]
    reveal_type(filtered, expected_text="list[str | None]")
