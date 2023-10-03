from pathlib import Path

"""
- Table v4. Table class with two constructors.
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
