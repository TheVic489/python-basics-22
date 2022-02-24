# PyNative Loop exercises using 'while'
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# IMPORTANT: Never enclose the check and the message in parentheses! Example:
#   assert (num >= 0, "Error message")
# If you do so, it will be a tuple. Non-empty tuples always evaluate to True.
# The assert will never fail. It will be a useless assert.
# -----------------------------------------------------------------------------
def e13(num: int) -> int:
    '''Exercise 13: Find the factorial of the given number.
       The factorial of negative numbers is undefined'''

    # Input number must be zero or postive. If negative stop the program.
    assert (num >= 0), "Error: Factorial of a negative number is undefined!"


    # Input number is zero or positive.
    factorial: int = 1

    start:     int = 1
    end:       int = num

    iter:     int  = start
    finished: bool = (iter > end)

    while (not finished):
        factorial = factorial * iter

        iter     = iter + 1
        finished = (iter > end)

    return factorial


# Main
# -----------------------------------------------------------------------------
print(e13(5))
# -----------------------------------------------------------------------------
