from   pathlib import Path
import sys
import random
import engine


"""
Exercici 5:

- Fes un programa que mostri mutacions aleatòries d'una seqüència d'ADN a una pàgina html.
- La seqüència està al fitxer dna.fasta.
- Llegiu la seqüència del fitxer i genereu seqüències que tinguin una base (lletra) mutada aleatòriament.
- Les seqüències han de ser úniques, no hi pot haver repetides.
- Per generar la pàgina html, utilitzeu Jinja.
- A la pàgina html la mutació de cada seqüència ha d'estar en vermell,
  i la resta de lletres en color negre.
- El programa només rep un paràmetre: el número de seqüències a generar.
- El programa ha de rebre el número de seqüències des de la línia d'ordres.
- **Poseu el vostre nom i número d'exercici al principi del vostre codi.**

"""



# #############################################################################
# Seq functions
# #############################################################################


# Only works for the first line. We'll see a better version later.
# -----------------------------------------------------------------------------
def read_fasta(fasta_filename: str) -> str:
    """
    Input:  A fasta filename.
    Output: The sequence inside the fasta file.
    ONLY WORKS FOR A SINGLE SEQUENCE.
    """

    # Read text and split in lines
    fasta_text:      str  = Path(fasta_filename).read_text()
    line_list:  list[str] = fasta_text.strip().split('\n')

    # Separate header from body
    header: str       = line_list[0]
    body:   list[str] = line_list[1:]

    # Join body
    seq: str  = ''.join(body)

    return seq


# SNP = Single Nucleotid Polymorphism. A mutation in a single letter.
# -----------------------------------------------------------------------------
def make_mutation(seq: str, mutation_index: int) -> dict[str, str]:
    """
    Input:  A DNA sequence as a string and the index of the mutation.
    Output: Another DNA sequence with a different letter in 'mutation_index'.
    """

    # 1. Preconditions
    assert 0 <= mutation_index < len(seq)

    # 2. Prepare mutation candidates
    old_letter:                 str  = seq[mutation_index]
    candidate_letter_set:   set[str] = {'A', 'T', 'C', 'G'} - {old_letter}
    candidate_letter_list: list[str] = list(candidate_letter_set)

    # 3. Build mutation parts
    before_seq: str = seq[:mutation_index]
    snp:        str = random.choice(candidate_letter_list)
    after_seq:  str = seq[mutation_index+1:]

    # 5. Return mutated sequence parts as a dictionary
    result: dict[str, str] = {  'before_seq': before_seq,
                                'snp':        snp,
                                'after_seq':  after_seq  }

    return result



# #############################################################################
# Main code
# #############################################################################

# -----------------------------------------------------------------------------
def make_html_mutation_list( fasta_filename:     str,
                              num_seqs:          int,
                              template_filename: str,
                              html_filename:     str ):
    '''
    Creates an html file with random mutations on a given DNA sequence.
    - fasta_filename:    A file containing the original sequence.
    - num_seqs:          Number of mutated sequences to generate.
    - template_filename: Name of the template file.
    - html_filename:     Output html file that will be written to disk.
    Example: make_html_mutations_list('dna.fasta', 3, 'template.html', 'index.html')
    '''

    # 1. Read fasta
    seq:    str = read_fasta(fasta_filename)
    length: int = len(seq)

    # 2. Make num_seqs unique mutations
    mutation_index_list: list[int] = random.sample( range(length), k=num_seqs )

    mutation_list: list[dict[str, str]] = [ make_mutation(seq, mutation_index)
                                            for mutation_index
                                            in  mutation_index_list ]

    # 3. Fill template
    template_str:  str  = Path(template_filename).read_text()
    vars_dict:     dict = {'original_seq': seq, 'mutation_list': mutation_list}
    html_seq_list: str  = engine.fill_template_str(template_str, vars_dict)

    # 4. Write html sequence list to disk
    Path(html_filename).write_text(html_seq_list)



# command_line (sys.argv) is a global variable. Never modify it!
# When using deconstruction of lists or tuples, you cannot write types. It's a Python limitation.
# -----------------------------------------------------------------------------
def parse_command_line(command_line: list[str]) -> tuple[str, int, str, str]:
    '''
    Input:  The program command line (sys.argv). Includes the program name.
    Output: Returns the only parameter in the command line: A directory string.
            If there are less or more parameters, the program aborts.
    '''

    # Separate program name from program parameters
    program_name:       str       = command_line[0]
    program_parameters: list[str] = command_line[1:]

    # Make sure we have three parameters
    assert len(program_parameters) == 4

    # List deconstruction
    fasta_filename, num_seqs, template_filename, html_filename = program_parameters

    # Convert types and return parameters
    return fasta_filename, int(num_seqs), template_filename, html_filename


# - The exercise only asked for the number of seqs. The other parameters are not required.
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    # Execution from terminal
    # fasta_filename, num_seqs, template_filename, html_filename = parse_command_line(sys.argv)
    # make_html_mutation_list(fasta_filename, num_seqs, template_filename, html_filename)

    # Execution from VSCode
    make_html_mutation_list('dna.fasta', 3, 'template.html', 'index.html')

# -----------------------------------------------------------------------------
