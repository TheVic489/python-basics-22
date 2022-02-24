from pathlib import Path

# 1. Read csv file
# -----------------------------------------------------------------------------
def read_csv(csv_file_path: str) -> str:
    '''Input:  The path to a .csv file.
      Output: The contents of the .csv file as a single string.'''

    raw_text:      str = Path(csv_file_path).read_text()
    stripped_text: str = raw_text.strip()

    return stripped_text


# 2. Separate by rows
# -----------------------------------------------------------------------------
def separate_by_rows(contents: str) -> list[str]:
    '''Input:  The file contents as a single string.
        Output: A list of strings where each string is a row of the csv file.'''
    
    rows: list[str] = contents.split("\n")

    return rows


# 3. Separate by columns
# -----------------------------------------------------------------------------
def separate_by_columns(rows: list[str]) -> list[list[str]]:
    '''Input:  A list of strings. Each string is a row of a csv file. Row fields are separated by ";".
        Output: A table where each row has been splitted into a list of fields.'''

    table: list[list[str]] = []
    row:   str

    for row in rows:
        splitted_row: list[str] = row.split(";")
        table.append(splitted_row)

    return table


# -----------------------------------------------------------------------------
def read_table(csv_file_path: str) -> list[list[str]]:
    '''Input:  Path of a .csv file.
       Output: Table as a list of lists of strings with the csv contents.'''

    csv_str: str             = read_csv(csv_file_path)
    rows:    list[str]       = separate_by_rows(csv_str)
    table:   list[list[str]] = separate_by_columns(rows)

    return table


# -----------------------------------------------------------------------------
def filter_rows(table: list[list[str]], column_name: str, search_str: str) -> list[list[str]]:
    '''Input:  Table, columne and search string to filter by. 
       Output: Returns table with rows whose column_name includes search_str. Includes the header.'''

    # Precondition: There is at least a header in the table
    assert len(table) >= 1

    # Get the header and data body
    header: list[str]       = table[0]
    data:   list[list[str]] = table[1:]

    # Precondition: column_name is in the header
    assert column_name in header

    # Find the column index
    column_index: int = header.index(column_name)

    # Filter rows
    filtered_data: list[list[str]] = []
    for row in data:
        search_field: str = row[column_index]
        if (search_str in search_field):
            filtered_data.append(row)

    # Add header to result
    result: list[list[str]] = [header] + filtered_data

    return result


# -----------------------------------------------------------------------------
def get_column(table: list[list[str]], column_name: str) -> list[str]:
    '''Input:  Column name as a string and Table as a list of lists of strings.
       Output: The column whose name is column_name WITHOUT the header.'''

    # Precondition: There is at least a header in the table
    assert len(table) >= 1

    # Get the header and data body
    header: list[str]       = table[0]
    data:   list[list[str]] = table[1:]

    # Precondition: column_name is in the header
    assert column_name in header

    # Find the column index
    column_index: int = header.index(column_name)

    # Return column
    result: list[str] = []
    row:    list[str]
    for row in data:
        result.append(row[column_index])

    return result


# -----------------------------------------------------------------------------
def convert_type_to_int(input_list: list) -> list[int]:
    '''Input:  A list of a certain type.
       Output: The list with all elements converted to new_type.'''

    result: list[int] = []

    for elem in input_list:
        result.append(int(elem))

    return result
    

# Main
# -----------------------------------------------------------------------------
table:     list[list[str]]       = read_table("2022-01-20-covid-dades-aga.csv")
bcn_table: list[list[str]]       = filter_rows(table, 'NOM', 'BARCELONA')

dosi1_str_list: list[str]        = get_column(bcn_table, 'VACUNATS_DOSI_1')
dosi1_int_list: list[int]        = convert_type_to_int(dosi1_str_list)
dosi2_str_list: list[str]        = get_column(bcn_table, 'VACUNATS_DOSI_2')
dosi2_int_list: list[int]        = convert_type_to_int(dosi2_str_list)

dosi1_total: int = sum(dosi1_int_list)
dosi2_total: int = sum(dosi2_int_list)

print(set(get_column(bcn_table, 'NOM')))

print(f"Total de dosi 1: {dosi1_total}")
print(f"Total de dosi 2: {dosi2_total}")

# -----------------------------------------------------------------------------
