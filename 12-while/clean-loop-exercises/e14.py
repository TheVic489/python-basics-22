# PyNative Loop exercises
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# This exercise is like exercise 6.
# We do not even need to take into account the special zero case.
# We still need the absolute value abs() because -7 // 10 returns -1, not 0.
# -----------------------------------------------------------------------------
def e14(num: int) -> int:
    '''Exercise 14: Reverse a given integer number.
       Given: 76542
       Expected output: 24567
    '''

    num_as_string:          str = str(num)
    reversed_num_as_string: str = num_as_string[::-1]
    reversed_num:           int = int(reversed_num_as_string)

    return reversed_num


# Main
# -----------------------------------------------------------------------------
input_num: int = 76542
print(e14(input_num))
# -----------------------------------------------------------------------------
