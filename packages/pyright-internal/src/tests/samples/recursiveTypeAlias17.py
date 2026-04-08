# This sample tests that a recursive type alias defined in terms of itself
# via a forward reference resolves correctly without producing Unknown types.
# This is a regression test for https://github.com/microsoft/pyright/issues/10850.

from typing import TypeVar

J = TypeVar("J", bound="JSON")
JSONObjectOf = dict[str, J]
JSON = str | JSONObjectOf["JSON"]
JSONObject = JSONObjectOf[JSON]


def identity(json: JSONObjectOf[JSON]) -> JSONObjectOf[JSON]:
    return json


def identity2(json: JSONObject) -> JSONObject:
    return json
