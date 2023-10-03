
"""
- Series class v2.
- Addd convert_type_to_int() method.
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


    # Convert
    # -------------------------------------------------------------------------
    def convert_type_to_int(self):
        ''' Input:  A list of a certain type.
            Output: The list with all elements converted to new_type.
        '''

        int_data:   list[int] = [int(elem) for elem in self.data]
        int_series: Series    = Series(int_data)

        return int_series



# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    data: list[str] = ['1', '2', '3', '4', '5']
    s1:    Series    = Series(data)
    s2:    Series    = s1.convert_type_to_int()
    print(s2)

# -----------------------------------------------------------------------------
