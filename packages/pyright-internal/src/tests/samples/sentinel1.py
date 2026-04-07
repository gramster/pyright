# This sample tests the handling of Sentinel as described in PEP 661.

from typing import Literal, TypeAlias
from typing_extensions import Sentinel, TypeForm  # pyright: ignore[reportMissingModuleSource]

# This should generate an error because the names don't match.
BAD_NAME1 = Sentinel("OTHER")

# This should generate an error because the arg count is wrong.
BAD_CALL1 = Sentinel()

# This should generate an error because the arg count is wrong.
BAD_CALL2 = Sentinel("BAD_CALL2", 1)

# This should generate an error because the arg type is wrong.
BAD_CALL3 = Sentinel(1)


MISSING = Sentinel("MISSING")

type TA1 = int | MISSING

TA2: TypeAlias = int | MISSING

TA3 = int | MISSING

# This should generate an error because Literal isn't appropriate here.
x: Literal[MISSING]


def func1(value: int | MISSING) -> None:
    if value is MISSING:
        reveal_type(value, expected_text="MISSING")
    else:
        reveal_type(value, expected_text="int")


def func2(value=MISSING) -> None:
    pass


reveal_type(func2, expected_text="(value: Unknown | MISSING = MISSING) -> None")


def test_typeform[T](v: TypeForm[T]) -> TypeForm[T]: ...


reveal_type(test_typeform(MISSING), expected_text="TypeForm[MISSING]")


def func3(x: Literal[0, 3, "hi"] | MISSING) -> None:
    if x:
        reveal_type(x, expected_text="MISSING | Literal[3, 'hi']")
    else:
        reveal_type(x, expected_text="Literal[0]")


t1 = type(MISSING)
reveal_type(t1, expected_text="type[MISSING]")


# Test narrowing with dataclass fields
from dataclasses import dataclass


@dataclass
class Foo:
    name: str | MISSING = MISSING


foo = Foo()

reveal_type(foo.name, expected_text="str | MISSING")

if foo.name is MISSING:
    reveal_type(foo.name, expected_text="MISSING")
else:
    reveal_type(foo.name, expected_text="str")

if foo.name is not MISSING:
    reveal_type(foo.name, expected_text="str")
else:
    reveal_type(foo.name, expected_text="MISSING")


# Test with multiple sentinels
UNSET = Sentinel("UNSET")


@dataclass
class Bar:
    value: int | MISSING | UNSET = MISSING


bar = Bar()

if bar.value is MISSING:
    reveal_type(bar.value, expected_text="MISSING")
elif bar.value is UNSET:
    reveal_type(bar.value, expected_text="UNSET")
else:
    reveal_type(bar.value, expected_text="int")


# Test with complex union including None
@dataclass
class Baz:
    data: int | str | None | MISSING = MISSING


baz = Baz()

if baz.data is MISSING:
    reveal_type(baz.data, expected_text="MISSING")
elif baz.data is None:
    reveal_type(baz.data, expected_text="None")
else:
    reveal_type(baz.data, expected_text="int | str")


# Test with generic dataclass
@dataclass
class GenericContainer[T]:
    value: T | MISSING = MISSING


g_int = GenericContainer[int]()
reveal_type(g_int.value, expected_text="int | MISSING")

if g_int.value is not MISSING:
    reveal_type(g_int.value, expected_text="int")

g_str = GenericContainer[str]()
if g_str.value is MISSING:
    reveal_type(g_str.value, expected_text="MISSING")
else:
    reveal_type(g_str.value, expected_text="str")


# Test that the fix is scoped to dataclasses only - regular classes should not be affected
class RegularClass:
    name: str | MISSING = MISSING


regular = RegularClass()
# Regular class should still show the type contamination (not fixed by this patch)
# This confirms the fix is intentionally scoped to dataclasses only
# NOTE: This asserts current broken behavior (str | Unknown). When the root cause
# (TODO at line 5649 in typeEvaluator.ts) is fixed, this should change to "str | MISSING"
reveal_type(regular.name, expected_text="str | Unknown")
