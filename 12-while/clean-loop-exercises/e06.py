# PyNative Loop exercises
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# -----------------------------------------------------------------------------
def e06(number: int) -> int:
    '''Exercise 6: Count the total number of digits in a number
       Write a program to count the total number of digits in a number using a while loop.
       For example, the number is 75869, so the output should be 5.
    '''

    number_as_string: str = str(number)
    number_of_digits: int = len(number_as_string)

    return number_of_digits


# Main
# -----------------------------------------------------------------------------
input_number: int = 75869
print(e06(input_number))
# -----------------------------------------------------------------------------
