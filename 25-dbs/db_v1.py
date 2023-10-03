import utils
from   sqlite3  import Connection, Row

'''
DB Access from Python (SQLite).
Example 1: Creation and insertion.

- About this example:
    - This is an improved version of the offcial Python example
    - https://docs.python.org/3/library/sqlite3.html

- Impure functions:
    - Beware that many functions are impure (they modify the database).

- Syntax highlighting:
    - Install 'python-string-sql' extension from VSCode Marketplace.
    - Start all statement strings with '--sql'.
    - The extension needs this, not SQLite3.
'''


# #############################################################################
# SQL Statements
# #############################################################################

# Create table
# -----------------------------------------------------------------------------
def create_table(connection: Connection):

    statement: str = '''--sql
                        CREATE TABLE stocks ( date   TEXT
                                            , trans  TEXT
                                            , symbol TEXT
                                            , qty    REAL
                                            , price  REAL
                                            );
                     '''

    connection.execute(statement)


# Insert data in table using named variables to prevent SQL Injection
# -----------------------------------------------------------------------------
def insert_data(connection: Connection, stock_list: list[dict]):

    statement: str = '''--sql
                        INSERT INTO stocks
                        VALUES ( :date
                               , :trans
                               , :symbol
                               , :qty
                               , :price
                               );
                     '''

    connection.executemany(statement, stock_list)


# Select data in table.
# - An SQLite Row is a mix of a tuple and a dictionary.
# - You can access values by position or by key.
# -----------------------------------------------------------------------------
def query_stocks(connection: Connection) -> list[Row]:

    statement: str = '''--sql
                        SELECT   *
                        FROM     stocks
                        ORDER BY price
                        ;
                     '''

    result: list[Row] = connection.execute(statement).fetchall()

    return result



# #############################################################################
# Main
# #############################################################################

# - Use :memory: for tests. No db is written to disk.
# - 'connection.row_factory = Row' is needed if you want to use Rows instead of tuples.
# - 'with' uses the connection to do .commit() or .rollback() automatically at the end of the block.
#   1. .commit()   if no exception was raised.
#   2. .rollback() if an exception was raised.
# - In any case you must call connection.close() manually afterwards.
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    
    # Read data from json file
    stock_list: list[dict] = utils.read_json_file('stock_data.json')

    # Create Connection
    db_name:    str        = ':memory:'  # 'stocks.db'
    connection: Connection = utils.get_connection(db_name)
    connection.row_factory = Row

    # Insert data
    with connection:
        create_table(connection)
        insert_data(connection, stock_list)
    
    # Query DB
    rows: list[Row] = query_stocks(connection)
    utils.print_rows(rows)

    # Close DB
    connection.close()

# -----------------------------------------------------------------------------
