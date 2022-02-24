# PyNative Loop exercises
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# -----------------------------------------------------------------------------
def is_divisible(num: int, div: int) -> bool:
    """Returns True if num is divisible by div. Otherwise it returns False."""

    remainder: int  = num % div
    divisible: bool = (remainder == 0)

    return divisible


# -----------------------------------------------------------------------------
def is_prime(num: int) -> bool:
    """Returns True if num is a prime number. Otherwise it returns False."""

    prime:    bool      = True
    div_list: list[int] = list(range(2, num))

    for div in div_list:
        if is_divisible(num, div):
            prime = False

    return prime


# -----------------------------------------------------------------------------
def e11(start: int, end: int) -> list[int]:
    '''Exercise 11: Write a program to display all prime numbers within a range.'''

    prime_list: list[int] = []
    num_list:   list[int] = list(range(start, end+1))

    for num in num_list:
        if is_prime(num):
            prime_list.append(num)

    return prime_list


# Main
# -----------------------------------------------------------------------------
print(e11(25, 50))
# -----------------------------------------------------------------------------
