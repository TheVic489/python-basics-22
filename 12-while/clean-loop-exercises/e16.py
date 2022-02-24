# PyNative Loop exercises
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# List comprehension = How to transform one list into a new one in just one line.
# -----------------------------------------------------------------------------
def e16(num: int) -> list[int]:
    '''Exercise 16: Calculate the cube of all numbers from 1 to a given number.'''

    num_list:  list[int] = list(range(1, num+1))
    cube_list: list[int] = [num**3 for num in num_list]

    return cube_list


# Main
# -----------------------------------------------------------------------------
print(e16(6))
# -----------------------------------------------------------------------------
