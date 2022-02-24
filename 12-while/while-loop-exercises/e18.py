# PyNative Loop exercises using 'while'
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# -----------------------------------------------------------------------------
def print_row(length: int):

    start: int = 1
    end:   int = length

    iter:     int  = start
    finished: bool = (iter > end)

    while (not finished):

        print('*', end=' ')

        iter     = iter + 1
        finished = (iter > end)

    print()


# -----------------------------------------------------------------------------
def make_heights_list(max_height: int) -> list[int]:
    """Returns a list with the heights of each row in the pyramid."""

    result: list[int] = []

    # Ascending part
    start: int = 1
    end:   int = max_height

    iter:     int  = start
    finished: bool = (iter > end)

    while (not finished):

        result.append(iter)

        iter     = iter + 1
        finished = (iter > end)


    # Descending part
    start = max_height - 1
    end   = 1

    iter     = start
    finished = (iter < end)

    while (not finished):

        result.append(iter)

        iter     = iter - 1
        finished = (iter < end)

    return result


# -----------------------------------------------------------------------------
def e18(max_height: int):
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

    heights_list: list[int] = make_heights_list(max_height)

    start: int = 0
    end:   int = len(heights_list) - 1

    index:    int  = start
    finished: bool = (index > end)

    while (not finished):

        length: int = heights_list[index]
        print_row(length)

        index    = index + 1
        finished = (index > end)


# Main
# -----------------------------------------------------------------------------
e18(5)
# -----------------------------------------------------------------------------
