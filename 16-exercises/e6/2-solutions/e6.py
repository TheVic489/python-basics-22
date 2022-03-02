import sys
import copy
import random

"""
Exercici 6:

- Fes un programa que rebi múltiples paràmetres per la línia d'ordres i esculli un a l'atzar.
- Exemple:
    e6 platja muntanya
    => platja
"""


# command_line (sys.argv, ARGument Values) is a global variable. Never modify it!
# We need at least one parameter. That's why we use assert.
# Before returning the program parameters, we call them 'word_list', but it's not necessary.
# -----------------------------------------------------------------------------
def parse_command_line(command_line: list[str]) -> list[str]:
    '''
    Input:  The program command line (sys.argv). Includes the program name.
    Output: Returns the list of parameters in the command line: A list of words.
            If there are zero parameters, the program aborts.
    '''

    # Separate program name from program parameters
    program_name:       str       = command_line[0]
    program_parameters: list[str] = command_line[1:]

    # Make sure we have two parameters
    assert len(program_parameters) >= 1

    # Rename parameters just to make code easier to read
    word_list: list[str] = program_parameters

    return word_list


# IMPORTANT:
# - Comment/uncomment the 'word_list' variable to choose between terminal and VSCode execution.
# Execution form terminal:
# - Example: python e6.py vanilla chocolate strawberry
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    # Execution from terminal
    word_list: list[str] = parse_command_line(sys.argv)

    # Execution from VSCode
    # word_list: list[str] = ['vanilla', 'chocolate', 'strawberry']

    # Choose and print
    chosen_word: str = random.choice(word_list)
    print(chosen_word)

# -----------------------------------------------------------------------------
