# PyNative Loop exercises using 'while'
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# Put meaningful names to variables to make your code easy to understand.
# -----------------------------------------------------------------------------
def e12(length: int) -> list[int]:
    '''Exercise 12: Display Fibonacci series.'''

    result:   list[int] = [0, 1]
    finished: bool      = (len(result) >= length)

    while (not finished):

        last_num: int = result[-1]
        prev_num: int = result[-2]
        next_num: int = last_num + prev_num

        result.append(next_num)

        finished = (len(result) >= length)

    return result


# Main
# -----------------------------------------------------------------------------
print(e12(10))
# -----------------------------------------------------------------------------
