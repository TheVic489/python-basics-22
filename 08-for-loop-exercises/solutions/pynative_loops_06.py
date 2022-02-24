"""
Exercise 6: Count the total number of digits in a number
Write a program to count the total number of digits in a number using a while loop.

For example, the number is 75869, so the output should be 5.
"""

# -----------------------------------------------------------------------------
def q06(number: int) -> int:
    """Returns the number of digits (letters) in a number."""

    number_as_string: str = str(number)
    number_of_digits: int = len(number_as_string)

    return number_of_digits


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    print(q06(75869))
# -----------------------------------------------------------------------------
