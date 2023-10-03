from pathlib   import Path
from series_v2 import Series

"""
- Table class v5. Implements all the table.py functionality.
"""

# Class Table
# -----------------------------------------------------------------------------
class Table:

    # Constructor
    # -------------------------------------------------------------------------
    def __init__(self, data: list[list[str]]):

        self.data: list[list[str]] = data


    # Alternative Constructor
    # -------------------------------------------------------------------------
    @classmethod
    def from_csv(cls, csv_file_path: str):

        raw_text:       str             = Path(csv_file_path).read_text()
        stripped_text:  str             = raw_text.strip()
        rows:           list[str]       = stripped_text.split("\n")
        data:           list[list[str]] = [row.split(";") for row in rows]
        table:          Table           = cls(data)

        return table


    # Print
    # -------------------------------------------------------------------------
    def __str__(self) -> str:

        pretty_rows:  list[str] = [', '.join(row) for row in self.data]
        pretty_table: str       =  '\n'.join(pretty_rows)

        return pretty_table


    # -----------------------------------------------------------------------------
    def filter_rows(self, column_name: str, search_str: str):
        ''' Input:  Table, columne and search string to filter by. 
            Output: Returns table with rows whose column_name includes search_str.
                    Includes the header.
        '''

        # Precondition: There is at least a header in the table
        assert len(self.data) >= 1

        # Get the header and data body
        header: list[str]       = self.data[0]
        body:   list[list[str]] = self.data[1:]

        # Precondition: column_name is in the header
        assert column_name in header

        # Find the column index
        column_index: int = header.index(column_name)

        # Filter rows
        filtered_data: list[list[str]] = [row
                                        for row in body
                                        if (search_str in row[column_index]) ]

        # Add header to result
        filtered_data_with_header: list[list[str]] = [header] + filtered_data

        # Return the data as a new object
        result: Table = Table(filtered_data_with_header)

        return result


    # -----------------------------------------------------------------------------
    def get_column(self, column_name: str) -> Series:
        ''' Input:  Column name as a string and Table as a list of lists of strings.
            Output: The column whose name is column_name WITHOUT the header.
        '''

        # Precondition: There is at least a header in the table
        assert len(self.data) >= 1

        # Get the header and data body
        header: list[str]       = self.data[0]
        body:   list[list[str]] = self.data[1:]

        # Precondition: column_name is in the header
        assert column_name in header

        # Find the column index
        column_index: int = header.index(column_name)

        # Return column
        column: list[str] = [row[column_index] for row in body]
        result: Series    = Series(column)

        return result


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    data: list[list[str]] = [
                             ["Area",      "Covid"],
                             ["Barcelona", "23"   ],
                             ["Tarragona", "18"   ],
                            ]

    t1: Table = Table(data)
    t2: Table = Table.from_csv("covid-dades-simple.csv")

    print(t2)

# -----------------------------------------------------------------------------
