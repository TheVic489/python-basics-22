import table
import engine
from   pathlib import Path

"""
Exercici 5:

- Fes un programa que llegeixi un arxiu .csv i el converteixi en una taula html.
- Utilitza Jinja per fer-ho.
- El resultat final ha de ser un arxiu .html que es pugui obrir en el navegador.

- Solució v2:
- És igual que la versió 1, però ara make_html_table() és una funció pura.
- Per aconseguir-ho vaig canviar el codi de llegir plantilles al mòdul engine.
- Ara la plantilla s'ha de llegir de disc manualment i passar com a un string.
"""


# -----------------------------------------------------------------------------
def make_html_table(data_table: list[list[str]], html_template: str) -> str:
    '''
    Input:
    - A table containing at least one row (the header). Cells are strings.
    - An Jinja html template as a string.
    Output:
    - The table as an html string.
    '''

    # 1. Precondition: There is at least a header in the table
    assert len(data_table) >= 1

    # 2. Get the header and data body
    header: list[str]       = data_table[0]
    body:   list[list[str]] = data_table[1:]

    # 3. Fill template
    vars_dict:  dict = { "header": header, "body": body }
    html_table: str  = engine.fill_template_str(html_template, vars_dict)

    # 4. Return html string
    return html_table


# -----------------------------------------------------------------------------
def convert_table_file( csv_filename:      str,
                        template_filename: str,
                        html_filename:     str ):
    '''
    Input:  A csv filename, a template filename and an html filename.
    Output: Returns None. It reads the csv file and writes it as an html file to disk.
    '''

    # 1. Read table
    data_table: list[list[str]] = table.read_table(csv_filename)

    # 2. Read template
    html_template: str = Path(template_filename).read_text()
    
    # 3. Convert table to html string
    html_table: str = make_html_table(data_table, html_template)

    # 4. Write html to disk
    Path(html_filename).write_text(html_table)


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    convert_table_file( "covid-dades-simple.csv",
                        "template.html",
                        "covid-dades-simple.html")

# -----------------------------------------------------------------------------
