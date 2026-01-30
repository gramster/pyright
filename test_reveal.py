from typing import TypeAlias, reveal_type
from typing_extensions import Unpack

Func6Input: TypeAlias = tuple[int] | tuple[str, str] | tuple[int, Unpack[tuple[str, ...]], complex]


def func6(val: Func6Input):
    match val:
        case (x,):
            reveal_type(val)

        case (x, y):
            reveal_type(val)

        case (x, y, z):
            reveal_type(val)
