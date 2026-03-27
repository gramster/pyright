from typing import TypeAlias

# Test cases to explore potential issues with the fix

# Case 1: Variadic tuple that should be exhausted by shorter patterns
Input1: TypeAlias = tuple[int, *tuple[str, ...], int]

def test1(val: Input1):
    match val:
        case (x, y):  # Matches when variadic part is empty: tuple[int, int]
            reveal_type(val)  # Should be tuple[int, int]
        case _:
            # Should be reachable - variadic part with 1+ elements
            reveal_type(val)  # Should be tuple[int, *tuple[str, ...], int] with len >= 3


# Case 2: Union with variadic tuple - original test case
Input2: TypeAlias = tuple[int] | tuple[str, str] | tuple[int, *tuple[str, ...], int]

def test2(val: Input2):
    match val:
        case (x,):
            reveal_type(val)  # Should be tuple[int]
        case (x, y):
            reveal_type(val)  # Should be tuple[str, str] | tuple[int, int]
        case (x, y, z):
            # MUST be reachable - tuple[int, str, int]
            reveal_type(val)  # Should be tuple[int, str, int]
        case (x, y, z, w):
            # MUST be reachable - tuple[int, str, str, int]
            reveal_type(val)  # Should be tuple[int, str, str, int]


# Case 3: Multiple variadic tuples
Input3: TypeAlias = tuple[int, *tuple[str, ...]] | tuple[*tuple[float, ...], bool]

def test3(val: Input3):
    match val:
        case (x, y):
            # Could be tuple[int, str] or tuple[float, bool]
            reveal_type(val)
        case _:
            reveal_type(val)


# Case 4: Variadic with specific length should not match longer patterns
Input4: TypeAlias = tuple[int, str, int]  # Fixed length 3

def test4(val: Input4):
    match val:
        case (a, b, c):
            reveal_type(val)  # Should be tuple[int, str, int]
        case (a, b, c, d):
            # Should be UNREACHABLE - fixed tuple can't have 4 elements
            reveal_type(val)


# Case 5: Empty variadic part
Input5: TypeAlias = tuple[int, *tuple[()], str]  # Effectively tuple[int, str]

def test5(val: Input5):
    match val:
        case (x, y):
            reveal_type(val)  # Should match
        case (x, y, z):
            # Should this be reachable? tuple[int, *tuple[()], str] is effectively tuple[int, str]
            reveal_type(val)
