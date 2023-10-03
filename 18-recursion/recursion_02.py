from pathlib import Path

#######################################################################
# List files in a tree recursively without .rglob()
#######################################################################

#----------------------------------------------------------------------
def list_tree_v1(base: Path):

    # Recursive branch
    if (base.is_dir()):

        path_list: list[Path] = sorted(base.glob('*'))

        for path in path_list:
            list_tree_v1(path)

    # Termination branch
    if (base.is_file()):
        print(str(base))


#----------------------------------------------------------------------
def list_tree_v2(base: Path) -> list[str]:

    result: list[str] = []

    # Recursive branch
    if (base.is_dir()):

        path_list: list[Path] = sorted(base.glob('*'))

        for path in path_list:
            result.extend( list_tree_v2(path) )

    # Termination branch
    if (base.is_file()):
        result.append(str(base))

    return result


#----------------------------------------------------------------------
def list_tree_v3(base: Path) -> list[str]:

    result: list[str] = []

    # Recursive branch
    if (base.is_dir()):

        path_list: list[Path] = sorted(base.glob('*'))

        for path in path_list:
            result.extend(list_tree_v3(path))

    # Termination branch
    if (base.is_file()):
        result.append(str(base))

    return result


# Main
#----------------------------------------------------------------------
dir: Path = Path('data')

list_tree_v1(dir)

for filename in list_tree_v2(dir):
    print(filename)

# for filename in list_tree_v3(dir):
#     print(filename)

#----------------------------------------------------------------------
