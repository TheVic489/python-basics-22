# PyNative Loop exercises
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# -----------------------------------------------------------------------------
def e08(num_list: list[int]):
    '''Exercise 8: Print list in reverse order using a loop.'''

    for num in reversed(num_list):
        print(num)


# Main
# -----------------------------------------------------------------------------
input_list: list[int] = [10, 20, 30, 40, 50]
e08(input_list)
# -----------------------------------------------------------------------------
