# This sample tests that dictionary type inference doesn't cause OOM
# when combining many different types.

# This used to cause pyright to crash with OOM before the fix
# because it was creating unbounded unions in dictionary type inference.
def trigger_oom() -> dict:
    import numpy as np

    result = {"np": np}
    result.update(
        {
            "str": str,
            "int": int,
            "float": float,
            "bool": bool,
            "list": list,
            "dict": dict,
            "set": set,
            "tuple": tuple,
            "frozenset": frozenset,
            "bytes": bytes,
            "bytearray": bytearray,
            "abs": abs,
            "round": round,
            "min": min,
            "max": max,
            "sum": sum,
            "pow": pow,
            "divmod": divmod,
            "len": len,
            "range": range,
            "enumerate": enumerate,
            "zip": zip,
            "sorted": sorted,
            "reversed": reversed,
            "slice": slice,
            "map": map,
            "filter": filter,
            "any": any,
            "all": all,
            "type": type,
        }
    )
    return result


# This should infer the type without crashing
result1 = trigger_oom()
reveal_type(result1, expected_text="dict[str, Any]")


# Similar test with a large dict literal
def large_dict_literal() -> dict:
    return {
        "str": str,
        "int": int,
        "float": float,
        "bool": bool,
        "list": list,
        "dict": dict,
        "set": set,
        "tuple": tuple,
        "frozenset": frozenset,
        "bytes": bytes,
        "bytearray": bytearray,
        "abs": abs,
        "round": round,
        "min": min,
        "max": max,
        "sum": sum,
        "pow": pow,
        "divmod": divmod,
        "len": len,
        "range": range,
        "enumerate": enumerate,
        "zip": zip,
        "sorted": sorted,
        "reversed": reversed,
        "slice": slice,
        "map": map,
        "filter": filter,
        "any": any,
        "all": all,
        "type": type,
    }


result2 = large_dict_literal()
reveal_type(result2, expected_text="dict[str, Any]")
