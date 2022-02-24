# PyNative Loop exercises using 'while'
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


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
# -----------------------------------------------------------------------------
def e05(num_list: list[int]):
    '''Exercise 5: Display numbers from a list using loop.
        Write a program to display only those numbers from a list that satisfy the following conditions:
        - The number must be divisible by five.
        - If the number is greater than 150, then skip it and move to the next number.
        - If the number is greater than 500, then stop the loop.
    '''

    start: int = 0
    end:   int = len(num_list) - 1

    index:        int  = start
    out_of_range: bool = (index > end)

    found_gt_500: bool = False

    finished:     bool = (out_of_range or found_gt_500)


    while (not finished):

        num: int = num_list[index]

        if is_printable(num):
            print(num)

        found_gt_500 = (num > 500)

        index        = index + 1
        out_of_range = (index > end)

        finished     = (out_of_range or found_gt_500)


# Main
# -----------------------------------------------------------------------------
input_numbers: list[int] = [12, 75, 150, 180, 145, 525, 50]
e05(input_numbers)
# -----------------------------------------------------------------------------
