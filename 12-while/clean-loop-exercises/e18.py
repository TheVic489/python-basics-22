# PyNative Loop exercises
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# -----------------------------------------------------------------------------
def print_row(length: int):

    for _ in range(length):
        print('*', end=' ')

    print()


# -----------------------------------------------------------------------------
def make_length_list(max_length: int) -> list[int]:
    """Returns a list with the length of each row in the pyramid."""

    ascent:  list[int] = list(range(1, max_length+1))
    descent: list[int] = list(range(max_length-1, 0, -1))
    heights: list[int] = ascent + descent

    return heights


# -----------------------------------------------------------------------------
def e18(max_length: int):
    '''Exercise 18: Print the following pattern:
    * 
    * * 
    * * * 
    * * * * 
    * * * * * 
    * * * * 
    * * * 
    * * 
    *
    '''

    length_list: list[int] = make_length_list(max_length)

    for length in length_list:
        print_row(length)


# Main
# -----------------------------------------------------------------------------
e18(5)
# -----------------------------------------------------------------------------
