# PyNative Loop exercises
# https://pynative.com/python-dictionary-exercise-with-solutions/

import copy

# Do not modify input parameters.
# Delete and insert again manually.
# -----------------------------------------------------------------------------
def e08_v1(data: dict, old_key: str, new_key: str) -> dict:
    '''Exercise 8: Rename key of a dictionary.'''

    # Make copy to avoid modifying input dict
    result: dict = copy.deepcopy(data)

    # Save value to a local variable
    value = result[old_key]

    # Delete old key and its value
    del result[old_key]

    # Insert new key and its value
    result[new_key] = value

    return result


# Do not modify input parameters.
# Use .pop(); .pop() returns the value that has deleted.
# -----------------------------------------------------------------------------
def e08_v2(data: dict, old_key: str, new_key: str) -> dict:
    '''Exercise 8: Rename key of a dictionary.'''

    # Make copy to avoid modifying input dict
    result: dict = copy.deepcopy(data)

    # Delete old key and save value to a local variable
    value = result.pop(old_key)

    # Insert new key and its value
    result[new_key] = value

    return result


# Do not modify input parameters.
# Shorter .pop() version.
# -----------------------------------------------------------------------------
def e08_v3(data: dict, old_key: str, new_key: str) -> dict:
    '''Exercise 8: Rename key of a dictionary.'''

    result:    dict = copy.deepcopy(data)
    result[new_key] = result.pop(old_key)

    return result


# Main
# -----------------------------------------------------------------------------
data: dict = { "name":   "Kelly",
               "age":    25,
               "salary": 8000,
               "city":   "New york" }

old_key: str = 'city'
new_key: str = 'location'

print(e08_v3(data, old_key, new_key))
# -----------------------------------------------------------------------------
