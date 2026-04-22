from dataclasses import dataclass
from typing import NamedTuple, Protocol, TypedDict, disjoint_base


@disjoint_base
def bad_func() -> None:
    # This should generate an error.
    pass


@disjoint_base
class BadProto(Protocol):
    # This should generate an error.
    def method(self) -> None: ...


@disjoint_base
class BadTypedDict(TypedDict):
    # This should generate an error.
    field: int


@disjoint_base
class Base1:
    pass


@disjoint_base
class Base2:
    pass


class InvalidDisjointBase(Base1, Base2):
    # This should generate an error.
    pass


# This should generate an error because conflicting inherited disjoint bases
# are still invalid even if this class is intrinsically disjoint via __slots__.
class SneakyChild(Base1, Base2):
    __slots__ = ('x',)


@disjoint_base
class NamedTupleOk(NamedTuple):
    field: int


@dataclass(slots=True)
class DataClassDisjointBase:
    field: int


class DataClassDisjointBaseChild(DataClassDisjointBase):
    pass


class DerivedDisjointBase(Base1):
    __slots__ = ('field',)


class DerivedDisjointBaseChild(DerivedDisjointBase, Base1):
    pass


@disjoint_base
class DiamondBase:
    pass


class DiamondLeft(DiamondBase):
    pass


class DiamondRight(DiamondBase):
    pass


class DiamondChild(DiamondLeft, DiamondRight):
    pass


class EmptySlotsBase:
    __slots__ = ()


class EmptySlotsNoConflict(EmptySlotsBase, Base1):
    pass


@dataclass
class DataClassNoSlots:
    field: int


class DataClassNoSlotsNoConflict(DataClassNoSlots, Base1):
    pass
