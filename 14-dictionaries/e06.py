# PyNative Loop exercises
# https://pynative.com/python-dictionary-exercise-with-solutions/

import copy


# - Do not modify input parameters!
# - Never traverse a collection and delete elements from it.
#   Use other collections for traversal.
# -----------------------------------------------------------------------------
def e06_v1(data: dict, del_keys: list[str]) -> dict:
    '''Exercise 6: Delete a list of keys from a dictionary.'''

    result: dict = copy.deepcopy(data)

    for key in del_keys:
        del result[key]

    return result


# - Do not modify input parameters!
# - Never traverse a collection and delete elements from it.
#   Use other collections for traversal.
# -----------------------------------------------------------------------------
def e06_v2(data: dict, del_keys: list[str]) -> dict:
    '''Exercise 6: Delete a list of keys from a dictionary.'''

    result: dict = copy.deepcopy(data)

    for key in del_keys:
        result.pop(key)

    return result


# Construct list of allowed keys
# -----------------------------------------------------------------------------
def e06_v3(data: dict, del_keys: list[str]) -> dict:
    '''Exercise 6: Delete a list of keys from a dictionary.'''

    all_keys:     list[str] = list(data.keys())
    denied_keys:  list[str] = del_keys
    allowed_keys: list[str] = []
    result:       dict      = {}

    # Create list of valid keys
    for key in all_keys:
        if key not in denied_keys:
            allowed_keys.append(key)

    # Fill result dictionary
    for key in allowed_keys:
        value       = data[key]
        result[key] = value

    return result


# List comprehension using a conditional. Recommended version.
# -----------------------------------------------------------------------------
def e06_v4(data: dict, del_keys: list[str]) -> dict:
    '''Exercise 6: Delete a list of keys from a dictionary.'''

    denied_keys: list[str]  = del_keys
    result:      dict       = { key: value
                                for key, value in data.items()
                                if key not in denied_keys }

    return result


# Set substraction.
# -----------------------------------------------------------------------------
def e06_v5(data: dict, del_keys: list[str]) -> dict:
    '''Exercise 6: Delete a list of keys from a dictionary.'''

    all_keys:     set[str] = set(data.keys())
    denied_keys:  set[str] = set(del_keys)
    allowed_keys: set[str] = all_keys - denied_keys
    result:       dict     = { key: value
                               for key, value in data.items()
                               if key in allowed_keys }

    return result


# Shorter set substraction. Sets do NOT guarantee order. ORDER CAN CHANGE!!
# -----------------------------------------------------------------------------
def e06_v6(data: dict, del_keys: list[str]) -> dict:
    '''Exercise 6: Delete a list of keys from a dictionary.'''

    all_keys:     set[str] = set(data.keys())
    denied_keys:  set[str] = set(del_keys)
    allowed_keys: set[str] = all_keys - denied_keys
    result:       dict     = { key: data[key]
                               for key in allowed_keys }

    return result


# Main
# -----------------------------------------------------------------------------
data: dict = {  "name":   "Kelly",
                "age":    25,
                "salary": 8000,
                "city":   "New york" }

keys = ["name", "salary"]

print(e06_v6(data, keys))
# -----------------------------------------------------------------------------
