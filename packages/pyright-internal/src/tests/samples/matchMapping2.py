# This sample tests type narrowing for mapping patterns with unions
# containing non-mapping types like None and tuples.

from typing import Any, Mapping, TypedDict


class Movie(TypedDict):
    title: str
    year: int


def test_union_with_none(x: dict[str, str] | None) -> None:
    match x:
        case {}:
            reveal_type(x, expected_text="dict[str, str]")
        case _:
            reveal_type(x, expected_text="None")


def test_union_with_tuple(x: dict[str, str] | tuple[str, str]) -> None:
    match x:
        case {}:
            reveal_type(x, expected_text="dict[str, str]")
        case _:
            reveal_type(x, expected_text="tuple[str, str]")


def test_union_with_tuples_and_none(
    x: tuple[str, str] | tuple[str, str, str] | dict[str, str] | None
) -> None:
    match x:
        case {}:
            reveal_type(x, expected_text="dict[str, str]")
        case _:
            reveal_type(x, expected_text="tuple[str, str] | tuple[str, str, str] | None")


def test_union_with_str(x: dict[str, str] | str) -> None:
    match x:
        case {}:
            reveal_type(x, expected_text="dict[str, str]")
        case _:
            reveal_type(x, expected_text="str")


def test_union_with_any(x: dict[str, str] | Any) -> None:
    match x:
        case {}:
            reveal_type(x, expected_text="dict[str, str] | Any")
        case _:
            reveal_type(x, expected_text="Any")


def test_typeddict_with_none(x: Movie | None) -> None:
    match x:
        case {}:
            reveal_type(x, expected_text="Movie")
        case _:
            reveal_type(x, expected_text="None")


def test_multiple_dicts(x: dict[str, str] | dict[int, int] | None) -> None:
    match x:
        case {}:
            reveal_type(x, expected_text="dict[str, str] | dict[int, int]")
        case _:
            reveal_type(x, expected_text="None")


def test_mapping_with_int(x: Mapping[str, str] | int) -> None:
    match x:
        case {}:
            reveal_type(x, expected_text="Mapping[str, str]")
        case _:
            reveal_type(x, expected_text="int")
