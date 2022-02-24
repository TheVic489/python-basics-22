# PyNative Loop exercises
# https://pynative.com/python-dictionary-exercise-with-solutions/


# Helper function. Easier to understand than PyNative's solution.
# -----------------------------------------------------------------------------
def get_value(item: tuple[str, int]) -> int:
    '''Input:  Dictionary item. A tuple with a key and a value.
       Output: The value in the tuple (the 2nd element).'''

    # key, value = item
    key:   str = item[0]
    value: int = item[1]

    return value


# Take the minimum using the helper function.
# -----------------------------------------------------------------------------
def e09_v1(data: dict[str, int]) -> tuple[str, int]:
    '''Exercise 9: Get the key of a minimum value from the following dictionary.'''

    item_list: list[tuple[str, int]] = list(data.items())
    min_item:       tuple[str, int]  = min(item_list, key=get_value)

    return min_item


# Take the minimum using a lambda function.
# -----------------------------------------------------------------------------
def e09_v2(data: dict[str, int]) -> tuple[str, int]:
    '''Exercise 9: Get the key of a minimum value from the following dictionary.'''

    item_list: list[tuple[str, int]] = list(data.items())
    min_item:       tuple[str, int]  = min(item_list, key=lambda item: item[1])

    return min_item


# Sort and take the first item using the helper function.
# -----------------------------------------------------------------------------
def e09_v3(data: dict[str, int]) -> tuple[str, int]:
    '''Exercise 9: Get the key of a minimum value from the following dictionary.'''

    item_list:        list[tuple[str, int]] = list(data.items())
    sorted_item_list: list[tuple[str, int]] = sorted(item_list, key=get_value)
    min_item:              tuple[str, int]  = sorted_item_list[0]

    return min_item


# Sort and take the first item using a lambda function.
# -----------------------------------------------------------------------------
def e09_v4(data: dict[str, int]) -> tuple[str, int]:
    '''Exercise 9: Get the key of a minimum value from the following dictionary.'''

    item_list:        list[tuple[str, int]] = list(data.items())
    sorted_item_list: list[tuple[str, int]] = sorted(item_list, key=lambda item: item[1])
    min_item:              tuple[str, int]  = sorted_item_list[0]

    return min_item


# Main
# -----------------------------------------------------------------------------
data: dict[str, int] = { 'Physics': 82,
                         'Math':    65,
                         'history': 75 }

print(e09_v4(data))
# -----------------------------------------------------------------------------
