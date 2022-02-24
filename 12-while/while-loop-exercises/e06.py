# PyNative Loop exercises using 'while'
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# About:
# - Input must be an int. It can be positive or negative.
# - We perform integer division (// 10) until it becomes 0.
# - Input number 0 must be treated apart.
# Abs():
# - We need the absolute value abs() because -7 // 10 returns -1, not 0.
# Notes:
# - Always keep the inputs, do not modify input_number.
# - It's good for debugging.
# - All modifications will be done to tmp_num.
# Alternative:
# - The exercise forces us to use a while loop, but the easiest is:
#   len(str(input_number))
# -----------------------------------------------------------------------------
def e06(input_number: int) -> int:
    '''Exercise 6: Count the total number of digits in a number
       Write a program to count the total number of digits in a number using a while loop.
       For example, the number is 75869, so the output should be 5.
    '''

    # Special case
    if (input_number == 0):
        return 1


    # Normal case
    num_digits: int  = 0
    tmp_num:    int  = abs(input_number)
    finished:   bool = (tmp_num == 0)

    while (not finished):

        # Update the number of digits
        num_digits = num_digits + 1

        # Prepare next iteration
        tmp_num  = tmp_num // 10
        finished = (tmp_num == 0)

    return num_digits


# Main
# -----------------------------------------------------------------------------
input_number: int = 75869
print(e06(input_number))
# -----------------------------------------------------------------------------
