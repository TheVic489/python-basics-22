# PyNative Loop exercises using 'while'
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# Note: AVOID THE USE OF 'ELSE' AFTER A LOOP.
# Only Python has it. It is almost never used. Forget about it.
# The code is almost the same as exercise 9.
# -----------------------------------------------------------------------------
def e10(start: int, end: int):
    '''Exercise 10: Use else block to display a message “Done” after successful execution of loop.'''

    iter:     int  = start
    finished: bool = (iter > end)

    while (not finished):
        print(iter)

        iter     = iter + 1
        finished = (iter > end)
    else:
        print("Done!")


# Main
# -----------------------------------------------------------------------------
e10(1, 3)
# -----------------------------------------------------------------------------
