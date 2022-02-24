# PyNative Loop exercises using 'while'
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# Simplest solution: int("2"*length)
# We use a loop just for practice.
# -----------------------------------------------------------------------------
def make_term(length: int) -> int:

    result: int = 0

    start: int = 1
    end:   int = length

    iter:     int  = start
    finished: bool = (iter > end)

    while (not finished):

        result   = result * 10 + 2

        iter     = iter + 1
        finished = (iter > end)

    return result


# Return a list to make it more functional.
# -----------------------------------------------------------------------------
def e17(num_terms: int) -> int:
    '''Exercise 17: Find the sum of the series upto n terms.'''

    result: int = 0

    start: int = 1
    end:   int = num_terms

    iter:     int  = start
    finished: bool = (iter > end)

    while (not finished):

        term: int = make_term(iter)
        result = result + term

        iter     = iter + 1
        finished = (iter > end)

    return result


# Main
# -----------------------------------------------------------------------------
print(e17(5))
# -----------------------------------------------------------------------------
