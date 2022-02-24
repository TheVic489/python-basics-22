from pathlib import Path

''' Exercise: Count the total for dosi_1 and dosi_2 in the simple dataset.
    v3: get_covid_shots() returns a tuple instead of a list.'''


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


# 4. Get Covid Shots
# -----------------------------------------------------------------------------
def get_covid_shots(table: list[list[str]]) -> tuple[list[int], list[int]]:
   '''Input:  A table with Covid Data. Each datum is a string.
      Output: The data of two columns as ints: "dosi_1" and "dosi_2"'''
   
   header:     list[str]       = table[0]
   covid_data: list[list[str]] = table[1:]
   row:        list[str]

   dosi1_field_index: int = header.index("VACUNATS_DOSI_1")
   dosi2_field_index: int = header.index("VACUNATS_DOSI_2")

   dosi1_list: list[int] = []
   dosi2_list: list[int] = []

   for row in covid_data:
      dosi1_str: str = row[dosi1_field_index]
      dosi1_int: int = int(dosi1_str)
      dosi1_list.append(dosi1_int)

      dosi2_str: str = row[dosi2_field_index]
      dosi2_int: int = int(dosi2_str)
      dosi2_list.append(dosi2_int)

   return dosi1_list, dosi2_list


# 4. Get Covid Shots (v2)
# -----------------------------------------------------------------------------
def get_covid_shots_v2(table: list[list[str]]) -> tuple[list[int], list[int]]:
   '''Input:  A table with Covid Data. Each datum is a string.
      Output: The data of two columns as ints: "dosi_1" and "dosi_2"'''

   # Vars
   dosi1_list: list[int] = []
   dosi2_list: list[int] = []

   # 1. Sacar la columna dosi1
   # 1.1 Separar la fila header del resto de datos
   header:     list[str]       = table[0]
   covid_data: list[list[str]] = table[1:]

   # Precondition: There is at least one row
   assert len(table) >= 1

   # Precondition: There are at least 2 columns: "VACUNATS_DOSI_1" & 2.
   assert len(header) >= 2
   assert "VACUNATS_DOSI_1" in header
   assert "VACUNATS_DOSI_2" in header


   # 1.2 Buscar el índice (dosi1_index) de "VACUNATS_DOSI_1"
   dosi1_index: int = header.index("VACUNATS_DOSI_1")
   dosi2_index: int = header.index("VACUNATS_DOSI_2")

   # 1.3 Para cada fila, guardar el string del campo dosi1_index
   #     y convertir a int
   row: list[str]
   for row in covid_data:
      dosi1_str: str = row[dosi1_index]
      dosi1_int: int = int(dosi1_str)
      dosi1_list.append(dosi1_int)

      dosi2_str: str = row[dosi2_index]
      dosi2_int: int = int(dosi2_str)
      dosi2_list.append(dosi2_int)

   # Postcondition: Check that all numbers are positive
   for num in dosi1_list:
      assert num >= 0

   for num in dosi2_list:
      assert num >= 0



   return dosi1_list, dosi2_list



# 5. Sum Shots
# -----------------------------------------------------------------------------
def sum_shots(dosi1_list: list[int], dosi2_list: list[int]) -> tuple[int, int, int]:
   '''Input: A list of two columns: dosi_1 and dosi_2.
      Output: The sum of dosi_1, the sum of dosi_2 and the sum of both.'''

   dosi1_sum: int = sum(dosi1_list)
   dosi2_sum: int = sum(dosi2_list)
   total_sum: int = dosi1_sum + dosi2_sum

   return dosi1_sum, dosi2_sum, total_sum


# Main
# -----------------------------------------------------------------------------
contents: str                   = read_csv("2022-01-20-covid-dades-simple.csv")
rows:     list[str]             = separate_by_rows(contents)
table:    list[list[str]]       = separate_by_columns(rows)
dosi1_list, dosi2_list          = get_covid_shots(table)
dosi1_sum, dosi2_sum, total_sum = sum_shots(dosi1_list, dosi2_list)

print(f"Total de dosi 1: {dosi1_sum}")
print(f"Total de dosi 2: {dosi2_sum}")
print(f"Total de dosis:  {total_sum}")

# -----------------------------------------------------------------------------
