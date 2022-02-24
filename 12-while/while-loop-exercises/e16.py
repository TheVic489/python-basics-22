# PyNative Loop exercises using 'while'
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# Small function to make code more readable
# Double asterisk means "power of" some number (num^3).
# Same as num * num * num.
# -----------------------------------------------------------------------------
def get_power_of_three(num: int) -> int:
    return num**3


# Return a list to make it more functional.
# -----------------------------------------------------------------------------
def e16(num: int) -> list[int]:
    '''Exercise 16: Calculate the cube of all numbers from 1 to a given number.'''

    result: list[int] = []

    start: int = 1
    end:   int = num

    iter:     int  = start
    finished: bool = (iter > end)

    while (not finished):

        cube: int = get_power_of_three(iter)
        result.append(cube)

        iter     = iter + 1
        finished = (iter > end)

    return result


# Main
# -----------------------------------------------------------------------------
print(e16(6))
# -----------------------------------------------------------------------------
