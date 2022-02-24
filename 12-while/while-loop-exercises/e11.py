# PyNative Loop exercises using 'while'
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# Even if the code is only one line, putting the code in a function
# with an easy to understand name adds to readability.
# -----------------------------------------------------------------------------
def is_divisible_by(num: int, divisor: int) -> bool:
    '''Returns True if num is divisible by divisor.'''

    return ((num % divisor) == 0)


# -----------------------------------------------------------------------------
def is_prime(num: int) -> bool:
    '''Returns True if num is a prime number. Returns False otherwise.'''

    # Special case: Numbers equal or less than zero
    if (num < 1):
        return False


    # Normal case: Numbers equal or greater than one
    result: bool = True
    start:  int = 2
    end:    int = num - 1

    iter:     int  = start
    finished: bool = (iter > end)

    while (not finished):
        if is_divisible_by(num, iter):
            result = False

        iter     = iter + 1
        finished = (iter > end)

    return result


# Instead of printing them directly on the terminal, return a list.
# It's more functional.
# -----------------------------------------------------------------------------
def e11(start: int, end: int) -> list[int]:
    '''Exercise 11: Write a program to display all prime numbers within a range.'''

    result:   list[int] = []
    iter:     int       = start
    finished: bool      = (iter > end)

    while (not finished):

        if is_prime(iter):
            result.append(iter)

        iter     = iter + 1
        finished = (iter > end)

    return result


# Main
# -----------------------------------------------------------------------------
print(e11(25, 50))
# -----------------------------------------------------------------------------
