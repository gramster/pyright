# This sample tests type narrowing for conditional expressions (ternary operator)
# where the condition is narrowed such that one branch is known to be unreachable.

from typing import assert_type


class Node:
    pass


class Wrapper:
    def __init__(self, child: Node):
        self.child = child


class SpecialNode(Node):
    pass


def func1(plan: Wrapper | None):
    # After the guard, plan is known to be truthy (not None) and 
    # plan.child is known to be SpecialNode.
    if not (plan and isinstance(plan.child, SpecialNode)):
        return
    
    # This should be fine - direct assignment works.
    ts1: SpecialNode = plan.child
    
    # This should also be fine - the else branch (None) is unreachable
    # because plan is known to be truthy in this context.
    ts2: SpecialNode = plan.child if plan else None
    
    # Also verify the inferred type.
    assert_type(plan.child if plan else None, SpecialNode)


def func2(val: int | None):
    # After this guard, val is known to be not None (truthy).
    if not val:
        return
    
    # The else branch is unreachable since val is known to be truthy.
    ts1: int = val if val else 0
    assert_type(val if val else 0, int)


def func3(val: str | None):
    # After this guard, val is known to be None (falsy).
    if val:
        return
    
    # The if branch is unreachable since val is known to be falsy (None).
    ts1: None = val if val else None
    assert_type(val if val else None, None)


def func4(val: int | None):
    # After this guard, val is known to be not None (but could still be 0, which is falsy).
    if val is None:
        return
    
    # The else branch is still reachable since val could be 0 (falsy).
    # This test verifies that we don't over-narrow. The type should be int | Literal[0].
    ts1: int = val if val else 0
    assert_type(val if val else 0, int)


def func5(val: int | None):
    # After this guard, val is known to be truthy (not None and not 0).
    if not val:
        return
    
    # The else branch is unreachable since val is known to be truthy.
    ts1: int = val if val else 0
    assert_type(val if val else 0, int)


def func6(val: list[int] | None):
    # After this guard, val is known to be not None.
    if val is None:
        return
    
    # However, val could still be an empty list (falsy), so the else branch
    # is still reachable. This should be an error.
    ts1: list[int] = val if val else []  # type: ignore
