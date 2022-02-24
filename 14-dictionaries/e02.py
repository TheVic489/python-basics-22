# PyNative Loop exercises
# https://pynative.com/python-dictionary-exercise-with-solutions/


# Do not modify input parameters!
# Avoid PyNative's solution using the double splat. It's not readable.
# -----------------------------------------------------------------------------
def e02(dict1: dict[str, int], dict2: dict[str, int]) -> dict[str, int]:
    '''Exercise 2: Merge two Python dictionaries into one.'''

    result: dict[str, int] = {}

    result.update(dict1)
    result.update(dict2)

    return result


# Main
# -----------------------------------------------------------------------------
dict1: dict[str, int] = {'Ten':    10, 'Twenty': 20, 'Thirty': 30}
dict2: dict[str, int] = {'Thirty': 30, 'Fourty': 40, 'Fifty':  50}

print(e02(dict1, dict2))
# -----------------------------------------------------------------------------
