# PyNative Loop exercises
# https://pynative.com/python-dictionary-exercise-with-solutions/

from collections.abc import KeysView
from collections.abc import ValuesView


# Different from PyNative. Checks for a key.
# 'in' works with keys by default.
# -----------------------------------------------------------------------------
def e07_key_v1(data:  dict[str, int], key: str) -> bool:
    '''Exercise 7: Check if a key exists in a dictionary.'''

    result: bool = ( key in data )

    return result


# Different from PyNative. Checks for a key. Uses keys().
# -----------------------------------------------------------------------------
def e07_key_v2(data:  dict[str, int], key: str) -> bool:
    '''Exercise 7: Check if a key exists in a dictionary.'''

    data_keys: KeysView = data.keys()
    result:    bool     = ( key in data_keys )

    return result


# PyNative exercises. Checks for a value. Uses values().
# -----------------------------------------------------------------------------
def e07(data:  dict[str, int], value: int) -> bool:
    '''Exercise 7: Check if a value exists in a dictionary.'''

    data_values: ValuesView = data.values()
    result:      bool       = ( value in data_values )

    return result


# Main
# -----------------------------------------------------------------------------
data:  dict[str, int] = {'a': 100, 'b': 200, 'c': 300}
key:   str            = 'b'
value: int            = 200

print(e07_key_v2(data, key))
print(e07(data, value))
# -----------------------------------------------------------------------------
