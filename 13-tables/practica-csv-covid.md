# Pràctica CSV Covid19
-------------------------------------------------------------------------------

# Get Covid19 data for Catalunya
- https://dadescovid.cat/descarregues
  - Població Residències/General
  - Divisió Territorial AGA
  - Agregació 7 dies
  - CSV

# Charset conversion
- iconv -f ISO-8859-1 -t UTF-8 aga_setmanal_total_pob.csv > covid_dades.csv

# Practice exercise
1. Read the CSV file.
2. Analyse the data.
  - Print how many people are vaccinated with only the 1st shot in Barcelona.
  - Print how many people are vaccinated with two shots in Barcelona.
  - Print the difference (absolute and percentage).

It is advised that you create two separate modules for tasks 1 and 2.

-------------------------------------------------------------------------------

