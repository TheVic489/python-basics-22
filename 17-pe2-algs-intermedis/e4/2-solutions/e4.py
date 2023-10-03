import sys
import table
from   pathlib import Path

"""
Exercici 4:

- Fes un programa que llegeixi les dades covid del fitxer adjunt i calculi el següent:
- Ranking d'àrees (NOM) per número de morts (EXITUS).
- Primer mostrar les àrees amb més morts i al final les de menys morts.
- El programa només rep un paràmetre: el nom del fitxer .csv amb les dades covid.
- El programa ha de rebre el nom del fitxer des de la línia d'ordres.
- **Poseu el vostre nom i número d'exercici al principi del vostre codi.**

Pasos recomanats:
1. Filtrar per nom d'àrea i sumar els morts d'una àrea
2. Llistar les àrees úniques
3. Per cada àrea calcular la suma total de morts
4. Ordenar àrees pel total de morts
5. Llegir csv per la línea d'ordres
"""


# #############################################################################
# Deaths and Area functions
# #############################################################################

# -----------------------------------------------------------------------------
def get_deaths(covid_dict: dict[str, list], area_query: str) -> int:
    """
    Input:  Dictionary with covid data and name of the area in Catalunya.
    Output: Number of deaths in that area.
    """

    area_list:   list[str] = covid_dict['NOM']
    deaths_list: list[int] = covid_dict['EXITUS']

    area_deaths_list:  list[int] = [ deaths
                                     for area, deaths
                                     in zip(area_list, deaths_list)
                                     if area == area_query ]

    area_deaths_sum: int = sum(area_deaths_list)

    return area_deaths_sum


# -----------------------------------------------------------------------------
def get_area_list(covid_dict: dict[str, list]) -> list[str]:
    """
    Input:  Dictionary with covid data.
    Output: List of areas (nom) in the data. The list has no repeats.
    """

    area_list:        list[str]  = covid_dict['NOM']
    unique_area_set:  set[str]   = set(area_list)
    unique_area_list: list[str]  = sorted(unique_area_set)

    return unique_area_list



# #############################################################################
# Main code
# #############################################################################

# -----------------------------------------------------------------------------
def print_ranking(csv_filename: str) -> None:
    '''
    Input:   A csv filename as a string.
    Output:  Returns None. It prints a ranking of areas by number of deaths.
    Example: print_tree_size('2022-03-09-covid-dades-example.csv')
    '''

    # 1. Read covid data
    covid_table:  list[list[str]] = table.read_table(csv_filename)
    covid_dict:   dict[str, list] = table.convert_table_to_dict(covid_table)

    # 2. Convert EXITUS column to ints
    covid_dict['EXITUS'] = table.convert_type_to_int(covid_dict['EXITUS'])

    # 3. Get areas and deaths by area
    area_list:   list[str] = get_area_list(covid_dict)
    deaths_list: list[int] = [get_deaths(covid_dict, area) for area in area_list]

    # 4. Make ranking
    zip_list:        list[tuple[str, int]] = list(zip(area_list, deaths_list))
    sorted_zip_list: list[tuple[str, int]] = sorted( zip_list,
                                                     key=lambda tup: tup[1]   ,
                                                     reverse=True)

    # 5. Print ranking
    for area, deaths in sorted_zip_list:
        print(f"{area}: {deaths}")


# command_line (sys.argv) is a global variable. Never modify it!
# -----------------------------------------------------------------------------
def parse_command_line(command_line: list[str]) -> str:
    '''
    Input:  The program command line (sys.argv). Includes the program name.
    Output: Returns the only parameter in the command line: A csv filename string.
            If there are less or more parameters, the program aborts.
    '''

    # Separate program name from program parameters
    program_name:       str       = command_line[0]
    program_parameters: list[str] = command_line[1:]

    # Make sure we have one parameter
    assert len(program_parameters) == 1

    # Get parameter
    csv_filename = program_parameters[0]

    return csv_filename


# - Example: python e4.py 2022-03-09-covid-dades-example.csv
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    # Execution from terminal
    # csv_filename = parse_command_line(sys.argv)
    # print_ranking(csv_filename)

    # Execution from VSCode
    print_ranking('2022-03-09-covid-dades-example.csv')
    # print_ranking('2022-03-09-covid-dades-aga.csv')

# -----------------------------------------------------------------------------
