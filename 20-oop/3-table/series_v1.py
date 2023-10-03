
"""
- Series class v1.
- Represents a column in a table.
- All elements in the series have the same type.
"""

# Class Series
# -----------------------------------------------------------------------------
class Series:

    # Constructor
    # -------------------------------------------------------------------------
    def __init__(self, data: list):

        self.data: list = data


    # Print
    # -------------------------------------------------------------------------
    def __str__(self) -> str:

        str_data:      list[str] = [str(elem) for elem in self.data]
        pretty_column: str       = ', '.join(str_data)

        return pretty_column


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    data: list[int] = [1, 2, 3, 4, 5]
    s:    Series    = Series(data)
    print(s)

# -----------------------------------------------------------------------------
