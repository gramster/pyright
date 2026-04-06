# This sample tests a performance issue where multiple functions using
# yield from with a type alias union causes exponential processing time.

from collections.abc import Iterator
from typing import Generator, reveal_type


class A[T]:
    def __iter__(self) -> Iterator[T]: ...


class B[T]:
    def __iter__(self) -> Iterator[T]: ...


type C[T] = A[T] | B[T]


def g() -> C[int | str]: ...


def g_optional() -> C[int | str] | None: ...


def f_0():
    yield from g()


def f_1():
    yield from g()


def f_2():
    yield from g()


def f_3():
    yield from g()


def f_4():
    yield from g()


def f_5():
    yield from g()


def f_6():
    yield from g()


def f_7():
    yield from g()


def f_8():
    yield from g()


def f_9():
    yield from g()


# Test optional union case
def f_optional():
    # This should generate an error for optional iterable
    yield from g_optional()


# Validate inferred types
# Note: Send type (2nd parameter) is Unknown, not None, because the generator
# uses yield result (isYieldResultUsed=true) which defaults to Unknown
reveal_type(f_0, expected_text="() -> Generator[int | str, Unknown, None]")
reveal_type(f_optional, expected_text="() -> Generator[int | str, Unknown, None]")
