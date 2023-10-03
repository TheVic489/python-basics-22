from   pathlib import Path
import sys
import random
import engine

"""
Exercici 2:

- Fes un programa que mostri seqüències aleatòries d'ADN a una pàgina html.
- Les seqüències han de tenir només les lletres A, T, C o G
  i tenir longitud d'entre 100 i 120 bases.
- Per generar la pàgina html, utilitzeu Jinja.
- A la pàgina html les seqüències han d'estar en línies de màxim 60 lletres.
- El programa només rep un paràmetre: el número de seqüències a generar.
- El programa ha de rebre el número de seqüències des de la línia d'ordres.
- **Poseu el vostre nom i número d'exercici al principi del vostre codi.**
"""


# #############################################################################
# Sequence functions
# #############################################################################

# random.randint(a,b) includes b.
# random.choices() returns a list of elements.
# We join the list to get a single string.
# -----------------------------------------------------------------------------
def make_random_seq(min_len: int, max_len: int) -> str:
    '''
    Input:  The length of the sequence to be generated.
    Output: String containing random A,T,C,G.
    '''

    seq_len:  int       = random.randint(min_len, max_len)
    seq_list: list[str] = random.choices("ATCG", k=seq_len)
    seq_str:  str       = ''.join(seq_list)

    return seq_str


# -----------------------------------------------------------------------------
def make_random_seq_list(num_seqs: int, min_len: int, max_len: int) -> list[str]:
    '''
    Input:
    - num_seqs: Number of sequences to make
    - min_len:  Minimum length of the sequences
    - max_len:  Maximum length of the sequences
    Output:
    - A list of random DNA sequences
    '''

    seq_list: list[str] = [make_random_seq(min_len, max_len) for _ in range(num_seqs)]

    return seq_list


# Many ways to achieve this:
# https://stackoverflow.com/questions/9475241/split-string-every-nth-character
# The easiest is: from textwrap import wrap
# -----------------------------------------------------------------------------
def split_seq(seq: str, chunk_length: int) -> list[str]:
    '''
    Input:
    - seq:          The sequence to be split.
    - chunk_length: The length of the chunks.
    Output:
    - A list with all the chunks. The last chunk can have less than length letters.
    '''

    # Vars to make code easier to read
    seq_length: int = len(seq)

    # Start and end of chunks
    start_list: list[int] = list(range(0, seq_length, chunk_length))
    end_list:   list[int] = [start + chunk_length for start in start_list]
    zip_list:   list[tuple[int,int]] = list(zip(start_list, end_list))

    # Split in chunks (end is excluded)
    chunk_list: list[str] = [ seq[start:end] for start, end in zip_list ]

    return chunk_list



# #############################################################################
# Main code
# #############################################################################

# -----------------------------------------------------------------------------
def make_html_seq_list( num_seqs:          int,
                        template_filename: str,
                        html_filename:     str ):
    '''
    Creates an html file with random DNA sequences.
    - template_filename: A directory route to the template file.
    - html_filename:     Output html file that will be written to disk.
    Example: make_html_seq_list('template.html', 'index.html')
    '''

    # Program constants
    min_len:   int = 100
    max_len:   int = 120
    chunk_len: int =  60

    # Get list of sequences
    seq_list: list[str] = make_random_seq_list(num_seqs, min_len, max_len)

    # Split sequences
    split_seq_list: list[list[str]] = [split_seq(seq, chunk_len) for seq in seq_list]

    # Fill template
    template_str:  str  = Path(template_filename).read_text()
    vars_dict:     dict = {'split_seq_list': split_seq_list}
    html_seq_list: str  = engine.fill_template_str(template_str, vars_dict)

    # Write html sequence list to disk
    Path(html_filename).write_text(html_seq_list)


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
    num_seqs, template_filename, html_filename = program_parameters

    # Return parameters
    return num_seqs, template_filename, html_filename


# - The exercise only asked for the number of seqs. The other parameters are not required.
# - WARNING: When executing from terminal, you must quote the parameters.
# - Correct example: python e3.py 'my data'
# - Wrong example:   python e3.py my data
#   => Bash will split 'my data' into 'my' and 'data' before calling Python.
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    # Execution from terminal
    # num_seqs, template_filename, html_filename = parse_command_line(sys.argv)
    # make_html_seq_list(num_seqs, template_filename, html_filename)

    # Execution from VSCode
    make_html_seq_list(3, 'template.html', 'index.html')

# -----------------------------------------------------------------------------
