# PyNative Loop exercises
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# -----------------------------------------------------------------------------
def e03(num: int) -> int:
    '''Exercise 3: Calculate the sum of all numbers from 1 to a given number.
       For example, if the user entered 10 the output should be 55
       (1+2+3+4+5+6+7+8+9+10)'''

    return sum(range(1, num+1))


# Main
# -----------------------------------------------------------------------------
print(e03(10))
# -----------------------------------------------------------------------------
