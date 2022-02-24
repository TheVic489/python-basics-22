"""
Exercise 2: Print the following pattern
Write a program to print the following number pattern using a loop.

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""


# .join() only works on lists of strings
# -----------------------------------------------------------------------------
def make_row(max_num: int) -> str:
    """Returns a row of numbers as a string"""

    # Create a list of numbers
    num_list: list[int] = list(range(1, max_num+1))

    # Convert each number to a string
    str_list: list[str] = []
    for num in num_list:
        str_list.append(str(num))

    # Join the list of string numbers using spaces
    row: str = " ".join(str_list)

    # Return the row
    return row


# -----------------------------------------------------------------------------
def q02(num_rows: int) -> None:
    """Prints a triangle of numbers"""

    num_list: list[int] = list(range(1, num_rows+1))

    for num in num_list:
        print(make_row(num))

# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q02(5)
# -----------------------------------------------------------------------------
