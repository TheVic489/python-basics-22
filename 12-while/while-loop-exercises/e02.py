# PyNative Loop exercises using 'while'
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# I could use range(), but I am using a while loop for practice.
# -----------------------------------------------------------------------------
def print_line(start: int, end: int):
    '''Draw line of numbers, from start to end, both included'''

    iter:     int  = start
    finished: bool = (iter > end)

    while (not finished):
        print(iter, end=' ')

        iter     = iter + 1
        finished = (iter > end)

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

    start: int = 1
    end:   int = num_lines

    iter:     int  = start
    finished: bool = (iter > end)

    while (not finished):
        print_line(1, iter)

        iter     = iter + 1
        finished = (iter > end)


# Main
# -----------------------------------------------------------------------------
e02(5)
# -----------------------------------------------------------------------------
