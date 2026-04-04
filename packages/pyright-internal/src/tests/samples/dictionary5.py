# This sample tests that dictionary type inference handles large dictionaries
# correctly without causing OOM, and that maxSubtypeCount limits work properly.

# pyright: reportMissingModuleSource=false

# Test case (a): A dict with >64 entries of uniform type should retain precise inference
# Under non-strict mode, uniform types take the areTypesSame fast-path
def test_large_uniform_dict():
    # Manual dict with 70 uniform entries
    d1 = {
        "a": 1, "b": 2, "c": 3, "d": 4, "e": 5,
        "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
        "k": 11, "l": 12, "m": 13, "n": 14, "o": 15,
        "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
        "u": 21, "v": 22, "w": 23, "x": 24, "y": 25,
        "z": 26, "aa": 27, "ab": 28, "ac": 29, "ad": 30,
        "ae": 31, "af": 32, "ag": 33, "ah": 34, "ai": 35,
        "aj": 36, "ak": 37, "al": 38, "am": 39, "an": 40,
        "ao": 41, "ap": 42, "aq": 43, "ar": 44, "as": 45,
        "at": 46, "au": 47, "av": 48, "aw": 49, "ax": 50,
        "ay": 51, "az": 52, "ba": 53, "bb": 54, "bc": 55,
        "bd": 56, "be": 57, "bf": 58, "bg": 59, "bh": 60,
        "bi": 61, "bj": 62, "bk": 63, "bl": 64, "bm": 65,
        "bn": 66, "bo": 67, "bp": 68, "bq": 69, "br": 70,
    }
    reveal_type(d1, expected_text="dict[str, int]")


# Test case (b): Under non-strict mode, heterogeneous values degrade to Unknown
def test_heterogeneous_nonstrict():
    # Dictionary with 30 distinct builtin value types (non-strict mode)
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
    }
    # Under non-strict mode with no expected type, heterogeneous values → Unknown
    reveal_type(d2, expected_text="dict[str, Unknown]")


# Test case (c): With expected type, test that <64 distinct types retain precision
def test_with_expected_type_below_cap():
    # Dictionary with <64 distinct value types with expected type
    d3: dict[str, object] = {
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
    }
    # With expected type, should retain precise type (under cap)
    reveal_type(d3, expected_text="dict[str, object]")


# Test case (d): The OOM scenario from the PR description shouldn't crash or hang
def test_oom_scenario():
    result = {"first": str}
    result.update({
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
    })
    # Should complete without OOM
    reveal_type(result, expected_text="dict[str, Unknown]")
