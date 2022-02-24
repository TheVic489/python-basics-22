# PyNative Loop exercises
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# Almost the same as exercise 2.
# The code could be unified for both exercises, but becomes harder to understand.
# Remember that the range end is always excluded.
# -----------------------------------------------------------------------------
def print_decreasing_line(line_start: int, line_end: int):
    '''Print line of decreasing numbers, from start to end, both included.'''

    range_start: int = line_start
    range_end:   int = line_end - 1
    step:        int = -1

    for num in range(range_start, range_end, step):
        print(num, end=' ')

    print()


# Almost the same as exercise 2.
# The code could be unified for both exercises, but becomes harder to understand.
# Remember that the range end is always excluded.
# -----------------------------------------------------------------------------
def e07(num_lines: int):
    '''Exercise 7: Print the following pattern:
        5 4 3 2 1 
        4 3 2 1 
        3 2 1 
        2 1 
        1
    '''

    range_start: int = num_lines
    range_end:   int = 1 - 1
    step:        int = -1

    for num in range(range_start, range_end, step):
        print_decreasing_line(num, 1)


# Main
# -----------------------------------------------------------------------------
e07(5)
# -----------------------------------------------------------------------------
