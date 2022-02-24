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
def make_new_filename_list(filename_list: list[str], old_str: str, new_str: str):
    '''Replaces old_str for new_str in old_filename_list.'''

    result: list[str] = [filename.replace(old_str, new_str) for filename in filename_list]
    return result


# Checks:
# 1. No repeats:  renamed_filename_list has no repeated filenames.
# 2. No overlaps: No original filenames in renamed_filename_list  =>  Could lead to file overwriting
# -----------------------------------------------------------------------------
def is_renaming_ok(original_filename_list: list[str], renamed_filename_list: list[str]) -> bool:

    # 1. No repeats:  renamed_filename_list has no repeated filenames.
    no_repeats: bool = len(renamed_filename_list) == len(set(renamed_filename_list))

    # 2. No overlaps: No original filenames in renamed_filename_list
    no_overlaps: bool = all([filename not in renamed_filename_list for filename in original_filename_list])

    # Result
    all_ok: bool = no_repeats and no_overlaps

    return all_ok


# -----------------------------------------------------------------------------
def rename_files_on_disk(dir: Path, old_filename_list: list[str], new_filename_list: list[str]):

    old_filepath_list: list[Path] = [dir/filename for filename in old_filename_list]
    new_filepath_list: list[Path] = [dir/filename for filename in new_filename_list]

    renaming_list: list[tuple[Path, Path]] = list(zip(old_filepath_list, new_filepath_list))

    for old_filepath, new_filepath in renaming_list:
        old_filepath.rename(new_filepath)


# -----------------------------------------------------------------------------
def main(glob: str, old_str: str, new_str: str):
    '''Renames files in glob, replacing old_str for new_str in filenames.'''

    glob_path:         Path       = Path(glob)
    dir:               Path       = glob_path.parent
    pattern:           str        = glob_path.name

    old_filename_list: list[str] = [filepath.name for filepath in dir.glob(pattern)]
    new_filename_list: list[str] = make_new_filename_list(old_filename_list, old_str, new_str)

    assert is_renaming_ok(old_filename_list, new_filename_list)
    rename_files_on_disk(dir, old_filename_list, new_filename_list)


# v2: Works on subdirectories
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    main('2-test-files/*.txt', 'a', 'b')

# -----------------------------------------------------------------------------
