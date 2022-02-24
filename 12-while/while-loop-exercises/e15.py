# PyNative Loop exercises using 'while'
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# Small function to make code more readable
# -----------------------------------------------------------------------------
def is_odd(num: int) -> bool:
    return ((num % 2) == 1)


# Return a list to make it more functional.
# -----------------------------------------------------------------------------
def e15(num_list: list[int]) -> list[int]:
    '''Exercise 15: Use a loop to display elements from a given list present at odd index positions.'''

    result: list[int] = []

    start: int = 0
    end:   int = len(num_list) - 1

    index:    int  = start
    finished: bool = (index > end)

    while (not finished):

        if is_odd(index):
            result.append(num_list[index])

        index     = index + 1
        finished = (index > end)

    return result


# Main
# -----------------------------------------------------------------------------
input_list: list[int] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(e15(input_list))
# -----------------------------------------------------------------------------
