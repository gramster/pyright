from typing import TypeAlias

# Test case for the regression mentioned in the review
Func6Input: TypeAlias = tuple[int, *tuple[str, ...], int]

def test_longer_patterns(val: Func6Input):
    match val:
        case (x, y, z):
            # Natural length 3 - should match when variadic part has 1 element
            reveal_type(val)  # Should be tuple[int, str, int]

        case (x, y, z, w):
            # Length 4 - should match when variadic part has 2 elements
            # This should NOT be unreachable!
            reveal_type(val)  # Should be tuple[int, str, str, int]
