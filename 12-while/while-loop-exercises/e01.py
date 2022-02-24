# PyNative Loop exercises using 'while'
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# -----------------------------------------------------------------------------
def e01():
    '''Exercise 1: Print First 10 natural numbers using while loop'''

    start: int = 1
    end:   int = 10

    iter:     int  = start
    finished: bool = (iter > end)

    while (not finished):
        print(iter)

        iter     = iter + 1
        finished = (iter > end)


# Main
# -----------------------------------------------------------------------------
e01()
# -----------------------------------------------------------------------------
