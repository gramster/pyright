# This test case validates that deeply nested callable expressions
# do not cause an OOM or infinite loop during type analysis.
# See: https://github.com/microsoft/pyright/issues/xxxxx

from asyncio import AbstractEventLoop


def io_bound_method() -> None:
    pass


async def do_something_with_loop(loop: AbstractEventLoop) -> None:
    delay = 5
    # This line previously caused an OOM/infinite loop due to deeply nested
    # callable type constraint solving without proper recursion depth tracking.
    _ = loop.call_soon_threadsafe(
        loop.call_later, delay, loop.run_in_executor, None, io_bound_method
    )
