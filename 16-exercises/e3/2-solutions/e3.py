import sys
from   pathlib import Path
from   os      import stat_result

"""
Exercici 3:

- Fes un programa que calculi quant ocupa un arbre a disc.
- Mostra el resultat en bytes.
- Permet filtrar per un glob.
- Permet passar el glob per la línia d'ordres utilitzant sys.argv.

Solution:
1. Get list of files
2. Get total size
3. Pretty-print the list of files and total size
4. Use sys.argv for commandline options
"""


# Rglob:
# - rglob() is a Recursive Glob. Scans all subdirectories.
# - rglob() returns a Generator. It's simpler to convert it to a list.
# is_file():
# - rglob() will return both files and directories that match the pattern.
# - We only want files, so we filter by is_file().
# -----------------------------------------------------------------------------
def get_filepath_list(dir: str, pattern: str) -> list[Path]:
    '''
    Input:  A directory route and glob pattern, both as strings.
    Output: Returns a list of files in dir. Includes files in subdirs.
            Only includes files whose name matches the pattern.
    '''

    dirpath:       Path       = Path(dir)
    path_list:     list[Path] = list(dirpath.rglob(pattern))
    filepath_list: list[Path] = [path for path in path_list if path.is_file()]

    return filepath_list


# stat():
# - Path objects have a .stat() method that returns their status as a os.stat_result object. (See import)
# - Stat objects have different variables. Example: Path('.').stat()
# - The variable .st_size is the size of the file. Example: Path('e3.py').stat().st_size
# -----------------------------------------------------------------------------
def get_total_size(filepath_list: list[Path]) -> int:
    '''
    Input:  A list of files.
    Output: Returns the sum of their sizes.
    '''

    stat_list:  list[stat_result] = [filepath.stat() for filepath in filepath_list]
    size_list:  list[int]         = [stat.st_size for stat in stat_list]
    total_size: int               = sum(size_list)

    return total_size


# -----------------------------------------------------------------------------
def sort_by_size(filepath_list: list[Path]) -> list[Path]:
    '''
    Input:  A list of files.
    Output: Returns the list sorted by the size of the files.
    '''

    result: list[Path] = sorted(filepath_list,
                                key=lambda filepath: filepath.stat().st_size )

    return result


# -----------------------------------------------------------------------------
def get_pretty_str(filepath: Path) -> str:
    '''
    Input:  A file path object.
    Output: Returns a string with the filename and the size.
    '''

    filename: str = str(filepath)
    size:     int = filepath.stat().st_size

    result:   str = f"{filename}: {size}"

    return result


# -----------------------------------------------------------------------------
def print_tree_size(dir: str, pattern: str) -> None:
    '''
    Input:   A directory route and glob pattern, both as strings.
    Output:  Returns None. It prints the list of files, their sizes and the total size.
    Example: print_tree_size('my data', '*.txt')
    '''

    filepath_list:         list[Path] = get_filepath_list(dir, pattern)
    sorted_file_path_list: list[Path] = sort_by_size(filepath_list)
    total_size:            int        = get_total_size(filepath_list)

    for filepath in sorted_file_path_list:
        print(get_pretty_str(filepath))

    print(f"Total size: {total_size} bytes")


# command_line (sys.argv) is a global variable. Never modify it!
# When using deconstruction of lists or tuples, you cannot write types. It's a Python limitation.
# -----------------------------------------------------------------------------
def parse_command_line(command_line: list[str]) -> tuple[str, str]:
    '''
    Input:  The program command line (sys.argv). Includes the program name.
    Output: Returns the two parameters in the command line: A dir and a glob pattern.
            If there are less or more parameters, the program aborts.
    '''

    # Separate program name from program parameters
    program_name:       str       = command_line[0]
    program_parameters: list[str] = command_line[1:]

    # Make sure we have two parameters
    assert len(program_parameters) == 2

    # List deconstruction
    dir, pattern = program_parameters

    return dir, pattern


# Main
# - WARNING: When executing from terminal, you must quote the parameters.
# - Correct example: python e3.py 'my data' '*.txt'
# - Wrong example:   python e3.py my data *.txt     
#   => Bash will split 'my data' into 'my' and 'data' before calling Python.
#   => Bash will capture the *.txt glob and convert it to a list of files before calling Python.
#      If *.txt matches no file in current dir, the pattern arrives unchanged to Python, but do not rely on this behavior.
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    # Execution from terminal
    dir, pattern = parse_command_line(sys.argv)
    print_tree_size(dir, pattern)

    # Execution from VSCode
    # print_tree_size('my data', '*.txt')
    # print_tree_size('my data', '*.md')
    # print_tree_size('my data', '*.*')
    # print_tree_size('../../..', '*.py')

# -----------------------------------------------------------------------------
