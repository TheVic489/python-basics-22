"""
Exercise 17: Find the sum of the series up to n terms
Write a program to calculate the sum of series up to n term.
For example, if n = 5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

Given:
# number of terms
n = 5

Expected output:
24690
"""

# -----------------------------------------------------------------------------
def q17(num: int) -> list[int]:
    """Returns the sum of a series of terms of length up to num."""

    two_str:     str       = "2"
    num_list:    list[int] = []
    length_list: list[int] = list(range(1, num+1))

    # Generate all terms
    for length in length_list:
        num_as_string: str = two_str * length
        num_as_int:    int = int(num_as_string)
        num_list.append(num_as_int)

    return num_list


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    number: int = 5
    print(q17(number))
    print(sum(q17(number)))
# -----------------------------------------------------------------------------
