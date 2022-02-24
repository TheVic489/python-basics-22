# PyNative Loop exercises using 'while'
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# -----------------------------------------------------------------------------
def e04(input_num: int):
    '''Exercise 4: Write a program to print multiplication table of a given number.'''

    start: int = 1
    end:   int = 10

    iter:        int  = start
    finished:    bool = (iter > end)

    while (not finished):
        multiplication: int = input_num * iter
        print(multiplication)

        iter     = iter + 1
        finished = (iter > end)


# Main
# -----------------------------------------------------------------------------
# input_num: int = int(input("Enter number: "))
# e04(input_num)
e04(2)
# -----------------------------------------------------------------------------
