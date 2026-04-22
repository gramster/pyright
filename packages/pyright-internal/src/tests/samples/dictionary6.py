# This sample tests that the maxSubtypeCount cap works correctly in strict mode.

# pyright: strictDictionaryInference=true
# pyright: reportMissingModuleSource=false

# Test that <64 distinct types retain precision with strictDictionaryInference
def test_strict_below_cap():
    # Dictionary with 10 distinct value types - should retain precise union
    d1 = {
        "str": str,
        "int": int,
        "float": float,
        "bool": bool,
        "list": list,
        "dict": dict,
        "set": set,
        "tuple": tuple,
        "bytes": bytes,
        "range": range,
    }
    # With strictDictionaryInference, should retain precise union (not Any or Unknown)
    reveal_type(d1, expected_text="dict[str, type[str] | type[int] | type[float] | type[bool] | type[list[Unknown]] | type[dict[Unknown, Unknown]] | type[set[Unknown]] | type[tuple[Unknown, ...]] | type[bytes] | type[range]]")


# Test that >64 distinct types degrade gracefully with strictDictionaryInference
def test_strict_above_cap():
    # Dictionary with 67 distinct value types - should hit the cap and degrade to Any
    d2 = {
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
        "isinstance": isinstance,
        "issubclass": issubclass,
        "callable": callable,
        "hash": hash,
        "id": id,
        "repr": repr,
        "ascii": ascii,
        "bin": bin,
        "hex": hex,
        "oct": oct,
        "ord": ord,
        "chr": chr,
        "dir": dir,
        "vars": vars,
        "getattr": getattr,
        "setattr": setattr,
        "delattr": delattr,
        "hasattr": hasattr,
        "globals": globals,
        "locals": locals,
        "open": open,
        "input": input,
        "print": print,
        "format": format,
        "iter": iter,
        "next": next,
        "property": property,
        "staticmethod": staticmethod,
        "classmethod": classmethod,
        "super": super,
        "object": object,
        "complex": complex,
        "memoryview": memoryview,
        "compile": compile,
        "eval": eval,
        "exec": exec,
        "help": help,
    }
    # Should degrade to Any due to >64 distinct types
    reveal_type(d2, expected_text="dict[str, Any]")
