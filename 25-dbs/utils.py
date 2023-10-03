import json
from   pathlib  import Path
from   sqlite3  import Connection, Row, connect
from   tabulate import tabulate

'''
Utils for DB Access from Python (SQLite).

- Syntax highlighting:
    - Install 'python-string-sql' extension from VSCode Marketplace.
    - Start all statement strings with '--sql'.
    - The extension needs this, not SQLite3.

- Printing tables on the terminal:
    - Tabulate: https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data
    - Pandas:   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql_query.html
    - Recommended:
        - Pandas is the best, but requires the SQL query string itself.
        - For now better use Tabulate: conda install -n your_environment -c conda-forge tabulate
        - Remember to do also:
            - cd this_project_dir
            - conda activate your_environment
            - mypy --install-types
            - Restart VSCode
'''


# #############################################################################
# Path functions
# #############################################################################

# Get the base directory of this python script using __file__.
# We'll store the databases and other files in the base dir.
# No matter where we call the script from, we'll be able to locate the files.
# When using Path, always call .resolve() before accessing .parent (see docs).
# -----------------------------------------------------------------------------
def get_base_dir() -> Path:

    this_file_path: Path = Path(__file__)
    base_dir:       Path = this_file_path.resolve().parent

    return base_dir



# #############################################################################
# JSON functions
# #############################################################################

# -----------------------------------------------------------------------------
def read_json_file(json_filename: str) -> list[dict]:

    base_dir:  Path       = get_base_dir()
    json_path: Path       = base_dir/json_filename
    json_text: str        = json_path.read_text()
    data:      list[dict] = json.loads(json_text)

    return data



# #############################################################################
# SQLite3 functions
# #############################################################################

# Connect to a DB
# - If db_name is ':memory:', all statements will be done in RAM and will be lost.
# - It's good for tests.
# -----------------------------------------------------------------------------
def get_connection(db_name: str) -> Connection:

    if db_name == ':memory:':
        mem_connection: Connection = connect(db_name)
        return mem_connection

    else:
        base_dir:      Path       = get_base_dir()
        db_path:       Path       = base_dir/db_name
        db_connection: Connection = connect(db_path)
        return db_connection


# Returns the header of a list of Rows. If empty, it returns an empty list.
# Row.keys() returns all keys (header) of that row.
# -----------------------------------------------------------------------------
def get_header(row_list: list[Row]) -> list[str]:

    is_empty: bool = not row_list

    if is_empty:
        return []

    else:
        first_row:  Row       = row_list[0]
        header:     list[str] = first_row.keys()
        return header


# Easy way to print a single row: print(list(row)), print(tuple(row)) or print(dict(row))
# -----------------------------------------------------------------------------
def print_rows(row_list: list[Row]):

    header:       list[str] = get_header(row_list)
    pretty_table: str       = tabulate(row_list, header)

    print(pretty_table)


# -----------------------------------------------------------------------------
