"""
Exercise 14: Reverse a given integer number

Given:
76542

Expected output:
24567
"""

# - reversed() always returns an iterator.
# - For now, it's better to convert the iterator to a list. It's easier to debug.
# - a_str.join() works on lists of strings. It joins all strings using a_str.
# -----------------------------------------------------------------------------
def q14_v1(number: int) -> int:
    """Version 1. Returns the reversed number."""

    number_as_string:          str       = str(number)
    reversed_list_of_digits:   list[str] = list(reversed(number_as_string))
    reversed_number_as_string: str       = "".join(reversed_list_of_digits)
    reversed_number:           int       = int(reversed_number_as_string)

    return reversed_number


# Slices = [start:end:step]
# - End is always excluded.
# - If you omit start, the slice starts from the beginning.
# - If you omit end, the slice goes until the end.
# - If step is negative, the slice goes backwards.
# -----------------------------------------------------------------------------
def q14_v2(number: int) -> int:
    """Version 2. Returns the reversed number."""

    number_as_string:          str = str(number)
    reversed_number_as_string: str = number_as_string[::-1]
    reversed_number:           int = int(reversed_number_as_string)

    return reversed_number


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    print(q14_v1(12345))
# -----------------------------------------------------------------------------
