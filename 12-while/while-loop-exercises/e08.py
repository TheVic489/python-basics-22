# PyNative Loop exercises using 'while'
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# -----------------------------------------------------------------------------
def e08(num_list: list[int]):
    '''Exercise 8: Print list in reverse order using a loop.'''

    start: int = len(num_list) - 1
    end:   int = 0

    index:    int  = start
    finished: bool = (index < end)

    while (not finished):
        print(num_list[index])

        index    = index - 1
        finished = (index < end)


# Main
# -----------------------------------------------------------------------------
input_list: list[int] = [10, 20, 30, 40, 50]
e08(input_list)
# -----------------------------------------------------------------------------
