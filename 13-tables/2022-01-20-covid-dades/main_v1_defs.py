
''' Exercise: Count the total for dosi_1 and dosi_2 in the simple dataset.
    v1: Just the function definitions.'''


# 1. Read csv file
def read_csv(csv_file_path: str) -> str:
    '''Reads csv_file_path and returns
       its contents as a string.'''
    pass

# 2. Separate by rows
def separate_by_rows(contents: str) -> list[str]:
    '''Receives file contents and returns
       a list of strings, where each string
       is a row of the csv file.'''
    pass


# 3. Separate by columns
def separate_by_columns(rows: list[str]) -> list[list[str]]:
    '''Splits each row into its columns.
       Each column is separated by semicolons.'''
    pass

# 4. Get Covid Shots
def get_covid_shots(table: list[list[str]]) -> list[list[int]]:
    '''Filters the covid table
       and returns only two columns: "dosi_1" and "dosi_2"'''
    pass

# 5. Sum Shots
def sum_shots(shots: list[list[int]]) -> tuple[int, int, int]:
    '''Receives two columns (dosi_1 and dosi_2)
       and returns the sum of dosi_1, dosi_2
       and the total.'''
    pass

