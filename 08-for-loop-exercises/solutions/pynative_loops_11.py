"""
Exercise 11: Write a program to display all prime numbers within a range
Note: A Prime Number is a number that cannot be made by multiplying other whole numbers.
A prime number is a natural number greater than 1 that is not a product of
two smaller natural numbers.

Examples:

    6 is not a prime mumber because it can be made by 2×3 = 6
    37 is a prime number because no other whole numbers multiply together to make it.
"""

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
def q11(start: int, end: int) -> list[int]:
    """Returns the list of prime numbers between start and end.
       Both start and end can be included in the list if are prime."""

    prime_list: list[int] = []
    num_list:   list[int] = list(range(start, end+1))

    for num in num_list:
        if is_prime(num):
            prime_list.append(num)

    return prime_list


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    print(q11(25, 50))
# -----------------------------------------------------------------------------
