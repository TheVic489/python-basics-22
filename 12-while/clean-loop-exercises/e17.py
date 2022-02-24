# PyNative Loop exercises
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# -----------------------------------------------------------------------------
def make_term(length: int) -> int:
    '''Makes a term made of twos with the given length.
       Example for length=3: 222'''

    return int("2"*length)


# Return a list to make it more functional.
# -----------------------------------------------------------------------------
def e17(num: int) -> list[int]:
    '''Exercise 17: Find the sum of the series up to n terms.'''

    length_list: list[int] = list(range(1, num+1))
    term_list:   list[int] = [make_term(length) for length in length_list]

    return term_list


# Main
# -----------------------------------------------------------------------------
num: int = 5
print(e17(num))
print(sum(e17(num)))
# -----------------------------------------------------------------------------
