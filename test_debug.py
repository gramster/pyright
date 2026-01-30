from typing import TypeAlias

Func6Input: TypeAlias = tuple[int] | tuple[str, str] | tuple[int, *tuple[str, ...], int]

def func6(val: Func6Input):
    match val:
        case (x,):
            reveal_type(val)  # Should be tuple[int]

        case (x, y):
            reveal_type(val)  # Should be tuple[str, str] | tuple[int, int]

        case (x, y, z):
            reveal_type(val)  # Should be tuple[int, str, int], NOT unreachable!
