# This sample tests type checking for match statements (as
# described in PEP 634) that contain sequence patterns.

# pyright: reportMissingModuleSource=false

from typing import reveal_type
from typing_extensions import Unpack

def test_unbounded_tuple1(
    subj: tuple[int] | tuple[str, str] | tuple[int, Unpack[tuple[str, ...]], complex],
):
    match subj:
        case (x,):
            reveal_type(subj, expected_text="tuple[int]")
            reveal_type(x, expected_text="int")

        case (x, y):
            reveal_type(subj, expected_text="tuple[str, str] | tuple[int, complex]")
            reveal_type(x, expected_text="str | int")
            reveal_type(y, expected_text="str | complex")

        case (x, y, z):
            reveal_type(subj, expected_text="tuple[int, str, complex]")
            reveal_type(x, expected_text="int")
            reveal_type(y, expected_text="str")
            reveal_type(z, expected_text="complex")
