# PyNative Loop exercises using 'while'
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# Almost the same as exercise 2.
# The code could be unified for both exercises, but becomes harder to understand.
# Not worth it.
# -----------------------------------------------------------------------------
def print_decreasing_line(start: int, end: int):
    '''Print line of decreasing numbers, from start to end, both included.'''

    iter:     int  = start
    finished: bool = (iter < end)

    while (not finished):
        print(iter, end=' ')

        iter     = iter - 1
        finished = (iter < end)

    print()


# Almost the same as exercise 2.
# The code could be unified for both exercises, but becomes harder to understand.
# Not worth it.
# -----------------------------------------------------------------------------
def e07(num_lines: int):
    '''Exercise 7: Print the following pattern:
        5 4 3 2 1 
        4 3 2 1 
        3 2 1 
        2 1 
        1
    '''

    start: int = num_lines
    end:   int = 1

    iter:     int  = start
    finished: bool = (iter < end)

    while (not finished):
        print_decreasing_line(iter, 1)

        iter     = iter - 1
        finished = (iter < end)


# Main
# -----------------------------------------------------------------------------
e07(5)
# -----------------------------------------------------------------------------
