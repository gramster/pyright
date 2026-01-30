# This sample tests a performance issue where multiple functions using
# yield from with a type alias union causes exponential processing time.

from collections.abc import Iterator


class A[T]:
    def __iter__(self) -> Iterator[T]: ...


class B[T]:
    def __iter__(self) -> Iterator[T]: ...


type C[T] = A[T] | B[T]


def g() -> C[int | str]: ...


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
