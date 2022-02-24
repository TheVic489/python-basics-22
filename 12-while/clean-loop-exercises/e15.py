# PyNative Loop exercises
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# Return a list to make it more functional.
# -----------------------------------------------------------------------------
def e15(num_list: list[int]) -> list[int]:
    '''Exercise 15: Display elements from a given list present at odd index positions.'''

    return num_list[1::2]


# Main
# -----------------------------------------------------------------------------
input_list: list[int] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(e15(input_list))
# -----------------------------------------------------------------------------
