from   pathlib import Path
import sys
import engine

"""
Exercici 3:

- Fes un programa per visualitzar imatges d'un directori local.
- El programa només rep un paràmetre: un directori 'dir'.
- El programa ha de buscar totes les imatges a 'dir' i generar una pàgina html que les mostri.
- El programa ha de rebre el directori 'dir' des de la línia d'ordres.
- **Poseu el vostre nom i número d'exercici al principi del vostre codi.**


Solution:
- 1. Create template
- 2. List image files in disk
- 3. Fill template
"""


# #############################################################################
# Path listing functions
# #############################################################################


# -----------------------------------------------------------------------------
def is_image(path: Path) -> bool:
    '''
    Input:  A Path.
    Output: Returns True if filepath is an image file. False otherwise.
            Image file formats are only those widely supported by browsers:
            https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types
    '''

    image_suffix_list: list[str] = ['.apng', '.avif', '.gif',
                                    '.jpg',  '.jpeg', '.jfif', '.pjpeg', '.pjp',
                                    '.png',  '.svg',  '.webp']

    is_file:             bool = path.is_file()
    has_image_extension: bool = (path.suffix in image_suffix_list)
    result:              bool = (is_file and has_image_extension)

    return result


# -----------------------------------------------------------------------------
def get_image_filepath_list(dir: str) -> list[Path]:
    '''
    Input:  A directory route as a string.
    Output: Returns a list of filepaths in dir. Includes files in subdirs.
            Only includes files with an image suffix (suffix).
            The returned list is sorted alphabetically.
    '''

    dirpath:       Path       = Path(dir)
    path_list:     list[Path] = sorted(dirpath.rglob('*'))
    filepath_list: list[Path] = [path for path in path_list if is_image(path)]

    return filepath_list



# #############################################################################
# Main code
# #############################################################################

# -----------------------------------------------------------------------------
def make_html_gallery( imgs_dirname:      str,
                       template_filename: str,
                       html_filename:     str ):
    '''
    Creates an html file linking to image files for easy viewing in the browser.
    - imgs_dirname:      A directory route that contains image files.
    - template_filename: A directory route to the template file.
    - html_filename:     Output html file that will be written to disk.
    Example: make_html_gallery('imgs', 'index.html')
    '''

    # Get list of images
    image_list: list[Path] = get_image_filepath_list(imgs_dirname)

    # Fill template
    template_str: str  = Path(template_filename).read_text()
    vars_dict:    dict = {'image_list': image_list}
    html_gallery: str  = engine.fill_template_str(template_str, vars_dict)

    # Write html gallery to disk
    Path(html_filename).write_text(html_gallery)


# command_line (sys.argv) is a global variable. Never modify it!
# When using deconstruction of lists or tuples, you cannot write types. It's a Python limitation.
# -----------------------------------------------------------------------------
def parse_command_line(command_line: list[str]) -> tuple[str, str, str]:
    '''
    Input:  The program command line (sys.argv). Includes the program name.
    Output: Returns the only parameter in the command line: A directory string.
            If there are less or more parameters, the program aborts.
    '''

    # Separate program name from program parameters
    program_name:       str       = command_line[0]
    program_parameters: list[str] = command_line[1:]

    # Make sure we have three parameters
    assert len(program_parameters) == 3

    # List deconstruction
    imgs_dirname, template_filename, html_filename = program_parameters

    return imgs_dirname, template_filename, html_filename



# - The exercise only asked for the image dirname. The other parameters are not required.
# - WARNING: When executing from terminal, you must quote the parameters.
# - Correct example: python e3.py 'my data'
# - Wrong example:   python e3.py my data
#   => Bash will split 'my data' into 'my' and 'data' before calling Python.
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    # Execution from terminal
    # imgs_dirname, template_filename, html_filename = parse_command_line(sys.argv)
    # make_html_gallery(imgs_dirname, template_filename, html_filename)

    # Execution from VSCode
    make_html_gallery('imgs', 'template.html', 'index.html')

# -----------------------------------------------------------------------------
