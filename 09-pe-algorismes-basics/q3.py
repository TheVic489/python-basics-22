from pathlib import Path

# -----------------------------------------------------------------------------
# Student name: WRITE YOUR NAME HERE
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Q3: get_indexes()
# - Input:
#   - target: str. A string of nucleotides we want to search.
#   - fasta:  str. The contents of a fasta file.
# - Output:
#   - indexes: list[int] with all indexes where we found the target.
# 
# - Notes:
#   - Fasta files are very common in Bioinformatics.
#     The first line is always a comment and the other lines form a sequence.
#   - Indexes start at 0, the usual in Python.
#   - get_indexes() returns an empty list if the target cannot be found.
#   - get_indexes() returns all indexes it finds.
#   - get_indexes() also finds overlapping targets.
# 
# - Recommended algorithm:
#   - Use the string method .startswith()
#   - Have a look at its second parameter.
# 
# - Remember:
#   - Write your solution inside the given function.
#   - Functions must be pure. Remember to delete your print() calls when done.
#   - You can write additional functions to simplify your algorithm.
# -----------------------------------------------------------------------------


# - Input:  The contents of the fasta file as a string.
# - Output: The dna string without the comment line and no newlines.
# -----------------------------------------------------------------------------
def get_dna(fasta: str) -> str:

    # Split in lines
    fasta_lines: list[str] = fasta.split("\n")

    # Remove comment line (first line)
    del fasta_lines[0]

    # Join all lines
    dna: str = "".join(fasta_lines)

    return dna


# -----------------------------------------------------------------------------
def search(target: str, dna: str) -> list[int]:

    length:        int       = len(dna)
    all_indexes:   list[int] = list(range(length))
    found_indexes: list[int] = []

    for index in all_indexes:

        found: bool = dna.startswith(target, index)

        if found:
            found_indexes.append(index)


    return found_indexes


# - Write your solution here.
# - This function must be pure. Remember to delete your print() calls when done.
# -----------------------------------------------------------------------------
def get_indexes(target: str, fasta: str) -> list[int]:

    dna:     str       = get_dna(fasta)
    indexes: list[int] = search(target, dna)

    return indexes


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    # Write your solution inside the function.
    # Code here is not evaluated.
    # This is just for your convenience.
    coronavirus_fasta: str = Path("q3_coronavirus.fasta").read_text()
    print(get_indexes("AAA", coronavirus_fasta))

# -----------------------------------------------------------------------------
