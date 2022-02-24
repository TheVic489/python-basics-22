# PyNative Loop exercises
# https://pynative.com/python-dictionary-exercise-with-solutions/



# Looping with indexes and using result[key] = value.
# Could use the range directly, the list of indexes is not necessary.
# index_list is not necessary. I could use index_range directly.
# But ranges are hard to debug and lists are easy.
# Remember: ranges always exclude the last index: 0..length-1
# -----------------------------------------------------------------------------
def e01_v1(keys: list[str], values: list[int]) -> dict[str, int]:
    '''Exercise 1: Convert two lists into a dictionary.'''

    # Create empty dictionary
    result: dict[str, int] = {}

    # Create list of indexes
    keys_length:   int = len(keys)
    values_length: int = len(values)

    assert keys_length == values_length
    length:        int = keys_length

    index_range: range     = range(0, length)
    index_list:  list[int] = list(index_range)

    # Traverse keys and values in pairs, insert in dict
    for index in index_list:

        key:   str = keys[index]
        value: int = values[index]

        result[key] = value

    return result


# Looping with tuples.
# Lengths:
# - keys and values must have the same length.
# - If length is different, zip() will take the shortest length
# -----------------------------------------------------------------------------
def e01_v2(keys: list[str], values: list[int]) -> dict[str, int]:
    '''Exercise 1: Convert two lists into a dictionary.'''

    tuple_zip:   zip[tuple[str, int]] = zip(keys, values)
    tuple_list: list[tuple[str, int]] = list(tuple_zip)
    result:           dict[str, int]  = {}

    for tup in tuple_list:

        key:   str  = tup[0]
        value: int  = tup[1]

        result[key] = value

    return result


# Looping with tuple deconstruction.
# -----------------------------------------------------------------------------
def e01_v3(keys: list[str], values: list[int]) -> dict[str, int]:
    '''Exercise 1: Convert two lists into a dictionary.'''

    tuple_zip:   zip[tuple[str, int]] = zip(keys, values)
    tuple_list: list[tuple[str, int]] = list(tuple_zip)
    result:           dict[str, int]  = {}

    for key, value in tuple_list:
        result[key] = value

    return result


# Dictionary comprehension
# -----------------------------------------------------------------------------
def e01_v4(keys: list[str], values: list[int]) -> dict[str, int]:
    '''Exercise 1: Convert two lists into a dictionary.'''

    tuple_zip:   zip[tuple[str, int]] = zip(keys, values)
    tuple_list: list[tuple[str, int]] = list(tuple_zip)
    result:           dict[str, int]  = {key: value for key, value in tuple_list}

    return result


# Version without loops nor dictionary comprehensions.
# -----------------------------------------------------------------------------
def e01_v5(keys: list[str], values: list[int]) -> dict[str, int]:
    '''Exercise 1: Convert two lists into a dictionary.'''

    tuple_zip:   zip[tuple[str, int]] = zip(keys, values)
    tuple_list: list[tuple[str, int]] = list(tuple_zip)
    result:           dict[str, int]  = {}

    result.update(tuple_list)

    return result


# Constructor:
# - The dict constructor admits any iterable that returns tuples of two elements.
# - tuple_list is not necessary, but it is useful when debugging.
# -----------------------------------------------------------------------------
def e01_v6(keys: list[str], values: list[int]) -> dict[str, int]:
    '''Exercise 1: Convert two lists into a dictionary.'''

    tuple_zip:   zip[tuple[str, int]] = zip(keys, values)
    tuple_list: list[tuple[str, int]] = list(tuple_zip)
    result:           dict[str, int]  = dict(tuple_list)

    return result


# Best version. One-liner of previous code.
# tuple_list was not necessary. The dict constructor accepts zips and any iterator.
# -----------------------------------------------------------------------------
def e01_v7(keys: list[str], values: list[int]) -> dict[str, int]:
    '''Exercise 1: Convert two lists into a dictionary.'''

    result: dict[str, int] = dict(zip(keys, values))

    return result


# Main
# -----------------------------------------------------------------------------
keys   = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

print(e01_v7(keys, values))
# -----------------------------------------------------------------------------
