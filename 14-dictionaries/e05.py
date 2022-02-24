# PyNative Loop exercises
# https://pynative.com/python-dictionary-exercise-with-solutions/


# -----------------------------------------------------------------------------
def e05_v1(data: dict, keys: list[str]) -> dict:
    '''Exercise 5: Create a dictionary by extracting the keys from a given dictionary.'''

    result: dict = {}

    for key in keys:
        value       = data[key]
        result[key] = value

    return result


# -----------------------------------------------------------------------------
def e05_v2(data: dict, keys: list[str]) -> dict:
    '''Exercise 5: Create a dictionary by extracting the keys from a given dictionary.'''

    result: dict = {key: data[key] for key in keys}

    return result


# Main
# -----------------------------------------------------------------------------
data: dict = {  "name":   "Kelly",
                "age":    25,
                "salary": 8000,
                "city":   "New york" }

keys = ["name", "salary"]

print(e05_v2(data, keys))
# -----------------------------------------------------------------------------
