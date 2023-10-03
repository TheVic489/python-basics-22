import utils
from   sqlite3  import Connection, Row

'''
DB Access from Python (SQLite).
Example 2: Creation, insertion, updating, deletion, Row access

- About this example:
    - This example uses scientific papers.
    - Compared to the official example, this example adds UPDATE and DELETE.

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
                        CREATE TABLE papers ( title           TEXT
                                            , authors         TEXT
                                            , keywords        TEXT
                                            , submission_date TEXT
                                            , DOI             TEXT
                                            );
                     '''

    connection.execute(statement)


# Insert data in table using named variables to prevent SQL Injection.
# Insert multiple data using a list of dicts and callling .executemany().
# Do NOT write a for loop. Let SQLite handle it internally.
# -----------------------------------------------------------------------------
def insert_papers(connection: Connection, paper_list: list[dict]):

    statement: str = '''--sql
                        INSERT INTO papers
                        VALUES ( :title
                               , :authors
                               , :keywords
                               , :submission_date
                               , :DOI
                               );
                     '''

    connection.executemany(statement, paper_list)


# Update data in table using named variables to prevent SQL Injection.
# Use a single dictionary when using .execute() instead of executemany().
# -----------------------------------------------------------------------------
def update_papers(connection: Connection, update_filter: dict):

    statement: str = '''--sql
                        UPDATE   papers
                        SET      title   = 'Discarded paper'
                        WHERE    authors = :researcher
                        ;
                     '''

    connection.execute(statement, update_filter)


# Delete data in table using named variables to prevent SQL Injection.
# Use a single dictionary when using .execute() instead of executemany().
# -----------------------------------------------------------------------------
def delete_papers(connection: Connection, delete_filter: dict):

    statement: str = '''--sql
                        DELETE FROM papers
                        WHERE       title = :title
                        ;
                     '''

    connection.execute(statement, delete_filter)


# Select data in table.
# - An SQLite Row is a mix of a tuple and a dictionary.
# - You can access values by position or by key.
# -----------------------------------------------------------------------------
def query_all_papers(connection: Connection) -> list[Row]:

    statement: str = '''--sql
                        SELECT   *
                        FROM     papers
                        ORDER BY submission_date
                        ;
                     '''

    result: list[Row] = connection.execute(statement).fetchall()

    return result


# - Even if it's a single row, it's better to use .fetchall().
# - .fetchone() returns None if the query is empty, and that is far more dangerous.
# -----------------------------------------------------------------------------
def query_latest_paper(connection: Connection) -> list[Row]:

    statement: str = '''--sql
                        SELECT   *
                        FROM     papers
                        ORDER BY submission_date DESC
                        LIMIT    1
                        ;
                     '''

    result: list[Row] = connection.execute(statement).fetchall()

    return result



# #############################################################################
# Print functions
# #############################################################################

# - An SQLite Row is a mix of a tuple and a dictionary.
# - Easy way to print a single row: print(list(row)), print(tuple(row)) or print(dict(row))
# - 'not row_list' is equivalent to 'len(row_list) == 0'
# -----------------------------------------------------------------------------
def print_latest_paper(row_list: list[Row]):

    is_empty: bool = not row_list

    if is_empty:
        print('Error: Could not find the latest paper in the DB.')

    else:
        latest_paper:    Row = row_list[0]
        title:           str = latest_paper['title']
        authors:         str = latest_paper['authors']
        submission_date: str = latest_paper['submission_date']

        print(f'The latest paper is "{title}", from {authors}, published on {submission_date}.')



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
    papers_list: list[dict] = utils.read_json_file('papers_data.json')

    # Create Connection
    db_name:    str        = ':memory:'  # 'papers.db'
    connection: Connection = utils.get_connection(db_name)
    connection.row_factory = Row

    # Insert data
    with connection:
        create_table(connection)
        insert_papers(connection, papers_list)
        update_papers(connection, {'researcher': 'Researcher X'})
        delete_papers(connection, {'title':      'Discarded paper'})

    # Query DB: Multiple rows
    all_papers: list[Row] = query_all_papers(connection)
    utils.print_rows(all_papers)

    # Query DB: Single row
    latest_paper: list[Row] = query_latest_paper(connection)
    print_latest_paper(latest_paper)

    # Close DB
    connection.close()

# -----------------------------------------------------------------------------
