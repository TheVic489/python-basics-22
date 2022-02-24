# PyNative Loop exercises
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# Use '_' for variables you won't use.
# -----------------------------------------------------------------------------
def e12(length: int) -> list[int]:
    '''Exercise 12: Display Fibonacci series.'''

    result: list[int] = [0, 1]

    for _ in range(length):

        last_num: int = result[-1]
        prev_num: int = result[-2]
        next_num: int = last_num + prev_num

        result.append(next_num)

    return result


# Main
# -----------------------------------------------------------------------------
print(e12(10))
# -----------------------------------------------------------------------------
