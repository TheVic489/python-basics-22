# PyNative Loop exercises using 'while'
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# Very simple. Straightforward loop.
# -----------------------------------------------------------------------------
def e09(start: int, end: int):
    '''Exercise 9: Display numbers from -10 to -1 using for loop.'''

    iter:     int  = start
    finished: bool = (iter > end)

    while (not finished):
        print(iter)

        iter     = iter + 1
        finished = (iter > end)


# Main
# -----------------------------------------------------------------------------
e09(-10, -1)
# -----------------------------------------------------------------------------
