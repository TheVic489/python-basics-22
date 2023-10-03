import sys
from   pathlib import Path

"""
Exercici 1:

- Fes un programa que calculi quant ocupa un arbre a disc.
- El programa només rep un paràmetre: un directori 'dir'.
- El programa ha de llistar dir i tots els seus subdirectoris recursivament.
- Per cada directori, ha de mostrar el seu tamany.
- El tamany d'un directori és la suma de tots els arxius que conté recursivament.
- Mostra el resultat en bytes.
- Els directoris han d'estar llistat per tamany, de menor a major.
- El programa ha de rebre el directori 'dir' des de la línia d'ordres.
- **Poseu el vostre nom i número d'exercici al principi del vostre codi.**

Solution:
1. Write function to get size of directory
2. Get list of directories
3. Get sizes for each directory
4. Sort directories by size
5. Pretty-print the list of directories, with their sizes
6. Use sys.argv for commandline options
"""



# #############################################################################
# Path listing functions
# #############################################################################

# -----------------------------------------------------------------------------
def get_recursive_filepath_list(dirpath: Path) -> list[Path]:
    '''
    Input:  A directory route as a string.
    Output: Returns a list of files in dir. Includes files in subdirs.
    '''

    path_list:     list[Path] = list(dirpath.rglob('*'))
    filepath_list: list[Path] = [path for path in path_list if path.is_file()]

    return filepath_list


# -----------------------------------------------------------------------------
def get_recursive_dirpath_list(dirpath: Path) -> list[Path]:
    '''
    Input:  A directory route as a string.
    Output: Returns a list including dirpath and all its subdirectories.
    '''

    path_list:    list[Path] = list(dirpath.rglob('*'))
    dirpath_list: list[Path] = [path for path in path_list if path.is_dir()]
    dirpath_list.append(dirpath)

    return dirpath_list



# #############################################################################
# Path size functions
# #############################################################################

# -----------------------------------------------------------------------------
def get_filepath_size(filepath: Path) -> int:
    '''
    Input:  A file Path.
    Output: Returns its size.
    '''

    size: int = filepath.stat().st_size

    return size


# -----------------------------------------------------------------------------
def get_filepath_list_size(filepath_list: list[Path]) -> int:
    '''
    Input:  A list of files.
    Output: Returns the sum of their sizes.
    '''

    size_list:  list[int] = [get_filepath_size(filepath) for filepath in filepath_list]
    total_size: int       = sum(size_list)

    return total_size


# -----------------------------------------------------------------------------
def get_dirpath_size(dirpath: Path) -> int:
    '''
    Input:  A directory route as a string.
    Output: Returns the sum of the sizes of all the files in it.
            Includes files in subdirectories.
    '''

    filepath_list: list[Path] = get_recursive_filepath_list(dirpath)
    size:          int        = get_filepath_list_size(filepath_list)

    return size



# #############################################################################
# Sorting functions
# #############################################################################

# -----------------------------------------------------------------------------
def sort_dirpath_list_by_size(dirpath_list: list[Path]) -> list[Path]:
    '''
    Input:  A list of directory paths.
    Output: Returns the list sorted by the size of the directories.
    '''

    result: list[Path] = sorted(dirpath_list,
                                key=lambda dirpath: get_dirpath_size(dirpath) )

    return result



# #############################################################################
# Printing functions
# #############################################################################

# -----------------------------------------------------------------------------
def get_pretty_dirpath_str(dirpath: Path) -> str:
    '''
    Input:  A directory Path object.
    Output: Returns a string with the dirname and the size.
    '''

    dirname: str = str(dirpath)
    size:    int = get_dirpath_size(dirpath)

    result:   str = f"{dirname}: {size}"

    return result



# #############################################################################
# Main code
# #############################################################################

# -----------------------------------------------------------------------------
def print_tree_size(dir: str) -> None:
    '''
    Input:   A directory route as a string.
    Output:  Returns None. It prints a list containing dir, its subdirs and their sizes.
             The list is sorted by their sizes.
    Example: print_tree_size('my data')
    '''

    dirpath:             Path       = Path(dir)
    dirpath_list:        list[Path] = get_recursive_dirpath_list(dirpath)
    sorted_dirpath_list: list[Path] = sort_dirpath_list_by_size(dirpath_list)

    for dirpath in sorted_dirpath_list:
        print(get_pretty_dirpath_str(dirpath))


# command_line (sys.argv) is a global variable. Never modify it!
# When using deconstruction of lists or tuples, you cannot write types. It's a Python limitation.
# -----------------------------------------------------------------------------
def parse_command_line(command_line: list[str]) -> str:
    '''
    Input:  The program command line (sys.argv). Includes the program name.
    Output: Returns the only parameter in the command line: A directory string.
            If there are less or more parameters, the program aborts.
    '''

    # Separate program name from program parameters
    program_name:       str       = command_line[0]
    program_parameters: list[str] = command_line[1:]

    # Make sure we have one parameter
    assert len(program_parameters) == 1

    # Get parameter
    dir = program_parameters[0]

    return dir



# - WARNING: When executing from terminal, you must quote the parameters.
# - Correct example: python e3.py 'my data'
# - Wrong example:   python e3.py my data
#   => Bash will split 'my data' into 'my' and 'data' before calling Python.
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    # Execution from terminal
    dir = parse_command_line(sys.argv)
    print_tree_size(dir)

    # Execution from VSCode
    # print_tree_size('my data')
    # print_tree_size('.')
    # print_tree_size('../../..')
    # print_tree_size('/')

# -----------------------------------------------------------------------------
