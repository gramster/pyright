# This sample tests that for loops over non-empty literal list or tuple
# expressions are treated as executing at least once for definite assignment
# analysis.

# pyright: reportPossiblyUnbound=true


def test_non_empty_list_literal():
    """Variable assigned in for loop over non-empty list literal should not be reported as possibly unbound."""
    for x in [1]:
        y = 123
    # This should not generate an error because the loop executes at least once
    del y


def test_non_empty_tuple_literal():
    """Variable assigned in for loop over non-empty tuple literal should not be reported as possibly unbound."""
    for x in (1,):
        z = 456
    # This should not generate an error because the loop executes at least once
    del z


def test_non_empty_list_multiple_elements():
    """Variable assigned in for loop over non-empty list with multiple elements."""
    for x in [1, 2, 3]:
        a = "hello"
    # This should not generate an error
    del a


def test_non_empty_tuple_multiple_elements():
    """Variable assigned in for loop over non-empty tuple with multiple elements."""
    for x in (1, 2, 3):
        b = "world"
    # This should not generate an error
    del b


def test_empty_list_literal():
    """Variable assigned in for loop over empty list literal should be reported as possibly unbound."""
    for x in []:
        # This should generate an error because c is possibly unbound
        c = 789
    del c


def test_empty_tuple_literal():
    """Variable assigned in for loop over empty tuple literal should be reported as possibly unbound."""
    for x in ():
        # This should generate an error because d is possibly unbound
        d = 999
    del d


def test_non_literal_iterable():
    """Variable assigned in for loop over non-literal iterable should still be reported as possibly unbound."""
    items = [1, 2, 3]
    for x in items:
        e = "test"
    # This should generate an error because e is possibly unbound
    del e


def test_string_literal():
    """Variable assigned in for loop over string literal should still be reported as possibly unbound (not implemented)."""
    for x in "abc":
        f = "string"
    # This should generate an error because string literals are not supported in this PR
    del f
