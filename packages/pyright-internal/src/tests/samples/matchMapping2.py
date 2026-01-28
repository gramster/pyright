# This sample tests type narrowing for mapping patterns with unions
# containing non-mapping types like None and tuples.


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
