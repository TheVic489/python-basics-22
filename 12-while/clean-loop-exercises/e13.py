# PyNative Loop exercises
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/

import math


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
    return math.prod(range(1, num+1))


# Main
# -----------------------------------------------------------------------------
print(e13(5))
# -----------------------------------------------------------------------------
