from pathlib import Path

# IMPORTANT: Read the pathlib docs.
# https://docs.python.org/3/library/pathlib.html


"""
Exercici 2:

- Fes un programa que renombri una llista d'arxius.
- Heu de vigilar que no es produeixin errors.

- Inputs:
    - La llista d'arxius.
    - Un string a cercar.
    - Un string de substitució.

- Exemple:
    - Llista d'arxius: ['a1.txt', 'a2.txt', 'a3.txt']
    - String de cerca: 'a'
    - String de substitució: 'b'
    - Resultat: ['b1.txt', 'b2.txt', 'b3.txt']

- Exemple d'error:
    - Llista d'arxius: ['a1.txt', 'a2.txt', 'b1.txt']
    - String de cerca: 'a'
    - String de substitució: 'b'
    - Resultat: El programa ha d'abortar avisant que b1.txt es sobreescriuria.

- Notes:
    - Utilitzeu el directori 2-test-files per fer proves.

"""

"""
1. Dividir el problema en subproblemes fàcils de resoldre.

a. Crear llista d'arxius renombrats
b. Comprovar que no hi ha repetits ni solapaments.
c. Renombrar fitxers

2. Escriure una funció que resoldrà cada subproblema.
    Escriure els paràmetres d'entrada i de sortida.

3. Escriure les precondicions i postcondicions
    de cada paràmetre per a cada funció.
"""


# -----------------------------------------------------------------------------
def rename_filename_list(old_filename_list: list[str], old_str: str, new_str: str):

    new_filename_list: list[str] = [filename.replace(old_str, new_str) for filename in old_filename_list]
    return new_filename_list


# Checks:
# 1. No repeats:  renamed_filename_list has no repeated filenames.
# 2. No overlaps: No original filenames in renamed_filename_list  =>  Could lead to file overwriting
# -----------------------------------------------------------------------------
def is_renaming_ok(old_filename_list: list[str], new_filename_list: list[str]) -> bool:

    # 1. No repeats:  renamed_filename_list has no repeated filenames.
    no_repeats: bool = len(new_filename_list) == len(set(new_filename_list))

    # 2. No overlaps: No original filenames in renamed_filename_list
    no_overlaps: bool = all([filename not in new_filename_list
                             for filename
                             in old_filename_list])

    # Result
    all_ok: bool = no_repeats and no_overlaps

    return all_ok


# -----------------------------------------------------------------------------
def rename_files_on_disk(old_filename_list: list[str], new_filename_list: list[str]):

    renaming_list: list[tuple[str, str]] = list(zip(old_filename_list, new_filename_list))

    for old_filename, new_filename in renaming_list:
        filepath: Path = Path(old_filename)
        filepath.rename(new_filename)


# -----------------------------------------------------------------------------
def rename_files(pattern: str, old_str: str, new_str: str):

    current_dir:       Path       = Path('.')
    old_filepath_list: list[Path] = list(current_dir.glob(pattern))

    old_filename_list: list[str] = [str(filepath) for filepath in old_filepath_list]
    new_filename_list: list[str] = rename_filename_list(old_filename_list, old_str, new_str)

    assert is_renaming_ok(old_filename_list, new_filename_list)
    rename_files_on_disk(old_filename_list, new_filename_list)


# v1: Assumes files are in the same directory as the code
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    rename_files('*.txt', 'a', 'b')

# -----------------------------------------------------------------------------
