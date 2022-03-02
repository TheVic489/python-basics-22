import table
import pprint

"""
Exercici 4:

- Fes un programa que llegeixi l'arxiu .csv de dades covid
  i retorni un diccionari de la següent forma:
  - Les claus són els noms de les columnes.
  - Els valors són les columnes de la taula, en forma de llistes.

- Solució:
- La forma més fàcil és reutilitzar molt del codi de l'exercici covid que vam fer.
- He copiat l'arxiu "main_v6_comprehensions.py", l'he anomenat "table.py" i l'importo.
"""


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    # 1. Read table    
    covid_table: list[list[str]] = table.read_table("covid-dades-simple.csv")
    
    # 2. Build dict using dict comprehension
    header:     list[str]       = covid_table[0]
    covid_dict: dict[str, list] = {column_name: table.get_column(covid_table, column_name)
                                   for column_name in header}

    # 3. Convert types
    covid_dict['CODI']            = table.convert_type_to_int(covid_dict['CODI'])
    covid_dict['VACUNATS_DOSI_1'] = table.convert_type_to_int(covid_dict['VACUNATS_DOSI_1'])
    covid_dict['VACUNATS_DOSI_2'] = table.convert_type_to_int(covid_dict['VACUNATS_DOSI_2'])

    # 3. Print
    pprint.pp(covid_dict)

    # 4. Usage examples
    print("Total dosi 1:", sum(covid_dict['VACUNATS_DOSI_1']))
    print("Total dosi 2:", sum(covid_dict['VACUNATS_DOSI_2']))

# -----------------------------------------------------------------------------
