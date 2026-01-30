from typing import TypeAlias, assert_type

Func6Input: TypeAlias = tuple[int] | tuple[str, str] | tuple[int, *tuple[str, ...], int]


def func6(val: Func6Input):
    match val:
        case (x,):
            # Type may be narrowed to tuple[int].
            assert_type(val, tuple[int])  # E[func6_1]
            assert_type(val, Func6Input)  # E[func6_1]

        case (x, y):
            # Type may be narrowed to tuple[str, str] | tuple[int, int].
            assert_type(val, tuple[str, str] | tuple[int, int]) # E[func6_2]
            assert_type(val, Func6Input)  # E[func6_2]

        case (x, y, z):
            # Type may be narrowed to tuple[int, str, int].
            assert_type(val, tuple[int, str, int]) # E[func6_3]
            assert_type(val, Func6Input)  # E[func6_3]
