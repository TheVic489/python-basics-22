# PyNative Loop exercises using 'while'
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# This exercise is like exercise 6.
# We do not even need to take into account the special zero case.
# We still need the absolute value abs() because -7 // 10 returns -1, not 0.
# -----------------------------------------------------------------------------
def e14(input_number: int) -> int:
    '''Exercise 14: Reverse a given integer number.
       Given: 76542
       Expected output: 24567
    '''

    # Normal case
    reversed_num: int  = 0
    tmp_num:      int  = abs(input_number)
    finished:     bool = (tmp_num == 0)

    while (not finished):

        # Update the number of digits
        remainder: int = tmp_num % 10
        reversed_num   = (reversed_num * 10) + remainder

        # Prepare next iteration
        tmp_num  = tmp_num // 10
        finished = (tmp_num == 0)

    return reversed_num


# Main
# -----------------------------------------------------------------------------
input_number: int = 76542
print(e14(input_number))
# -----------------------------------------------------------------------------
