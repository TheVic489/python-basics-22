# PyNative Loop exercises
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# -----------------------------------------------------------------------------
def print_line(start: int, end: int):
    '''Draw line of numbers, from start to end, both included'''

    for num in range(start, end+1):
        print(num, end=' ')

    print()


# -----------------------------------------------------------------------------
def e02(num_lines: int):
    '''Exercise 2: Print the following pattern:
    1 
    1 2 
    1 2 3 
    1 2 3 4 
    1 2 3 4 5
    '''

    for num in range(1, num_lines+1):
        print_line(1, num)


# Main
# -----------------------------------------------------------------------------
e02(5)
# -----------------------------------------------------------------------------
