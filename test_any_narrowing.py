from typing import Any, reveal_type

def f(x: Any, y: object, xs: list[Any]):
    if x is None:
        reveal_type(x)  # Any  (expected: None)
    if y is None:
        reveal_type(y)  # None
    filtered = [x for x in xs if isinstance(x, str) or x is None]
    reveal_type(filtered)  # list[str | Any]  (expected: list[str | None])
