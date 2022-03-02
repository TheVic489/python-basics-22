import table
import engine
from   pathlib import Path

"""
Exercici 5:

- Fes un programa que llegeixi un arxiu .csv i el converteixi en una taula html.
- Utilitza Jinja per fer-ho.
- El resultat final ha de ser un arxiu .html que es pugui obrir en el navegador.

- Solució v1:
- La forma més fàcil és reutilitzar el codi de l'exercici covid i SSG.
- La clau és començar per la plantilla (template.html).
- Primer repassem com es fan les taules html i escrivim una plantilla per fer-ho.
- Exemples: https://www.w3schools.com/html/html_tables.asp
"""


# -----------------------------------------------------------------------------
def make_html_table(data_table: list[list[str]], template_dir: str, template_filename: str) -> str:
    '''
    Input:
    - A table containing at least one row (the header). Cells are strings.
    - The directory containing the template.
    - The name of a Jinja template file.
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
    html_table: str  = engine.fill_template_file(template_dir, template_filename, vars_dict)

    # 4. Return html string
    return html_table


# -----------------------------------------------------------------------------
def convert_table_file( csv_filename:      str,
                        template_dir:      str,
                        template_filename: str,
                        html_filename:     str ):
    '''
    Input:  A csv filename, a template dir, a template filename and an html filename.
    Output: Returns None. It reads the csv file and writes it as html to html_filename.
    '''

    # 1. Read table
    data_table: list[list[str]] = table.read_table(csv_filename)

    # 2. Convert table to html string
    html_table: str = make_html_table(data_table, template_dir, template_filename)

    # 3. Write html to disk
    Path(html_filename).write_text(html_table)


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    convert_table_file( "covid-dades-simple.csv",
                        ".",
                        "template.html",
                        "covid-dades-simple.html")

# -----------------------------------------------------------------------------
