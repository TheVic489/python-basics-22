"""
Exercise 18: Print the following pattern.
Write a program to print the following start pattern using the for loop.

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""


# one_asterisk is a string in a list.
# one_asterisk * num_asterisks is not a multiplication. It is repetition.
# -----------------------------------------------------------------------------
def make_row(num_asterisks: int) -> str:
    """Returns a row of asterisks as a string"""

    one_asterisk:   list[str] = ["*"]
    asterisks_list: list[str] = one_asterisk * num_asterisks
    row:            str       = " ".join(asterisks_list)

    return row


# ascent + descent is a concatenation of lists, not a sum.
# -----------------------------------------------------------------------------
def make_heights_list(max_height: int) -> list[int]:
    """Returns a list with the heights of each row in the pyramid."""

    ascent:  list[int] = list(range(1, max_height+1))
    descent: list[int] = list(range(max_height-1, 0, -1))
    heights: list[int] = ascent + descent

    return heights


# Use the debugger and click on the lists to see all their elements.
# .join() works only on lists of strings.
# -----------------------------------------------------------------------------
def q18(max_height: int) -> str:
    """Returns a pyramid of numbers"""

    height_list: list[int] = make_heights_list(max_height)
    row_list:    list[str] = []

    for height in height_list:
        row: str = make_row(height)
        row_list.append(row)

    pyramid: str = "\n".join(row_list)

    return pyramid


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    print(q18(5))
# -----------------------------------------------------------------------------
