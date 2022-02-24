# PyNative Loop exercises
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# -----------------------------------------------------------------------------
def is_stop(num: int) -> bool:
    '''Returns True if num satisfies the following conditions:
       - If the number is greater than 500, then it is a stop number.'''
    
    return (num > 500)


# -----------------------------------------------------------------------------
def is_printable(num: int) -> bool:
    '''Returns True if num satisfies the following conditions:
       - The number must be divisible by five.
       - If the number is greater than 150, then skip it and move to the next number.
    '''

    divisible_by_5:   bool = ((num % 5) == 0)
    greater_than_150: bool = (num > 150)
    printable:        bool = (divisible_by_5 and not greater_than_150)

    return printable

# Strategy:
# 1. Check if we are out of range
# 2. If we are not, take the number, print it if printable
# 3. Then, if it's greater than 500 set the boolean to stop in the next iteration.
# Notes:
# - 'gt_500' means 'Greater Than 500'
# - THIS IS A BAD EXAMPLE. IT USES FOR + BREAK TO MAKE CODE SHORTER ONLY. AVOID.
# -----------------------------------------------------------------------------
def e05(num_list: list[int]):
    '''Exercise 5: Display numbers from a list using loop.
        Write a program to display only those numbers from a list that satisfy the following conditions:
        - The number must be divisible by five.
        - If the number is greater than 150, then skip it and move to the next number.
        - If the number is greater than 500, then stop the loop.
    '''

    for num in num_list:

        if is_printable(num):
            print(num)

        if is_stop(num):
            break


# Main
# -----------------------------------------------------------------------------
input_numbers: list[int] = [12, 75, 150, 180, 145, 525, 50]
e05(input_numbers)
# -----------------------------------------------------------------------------
