# PyNative Loop exercises
# https://pynative.com/python-dictionary-exercise-with-solutions/

import copy
import pprint


# Do not modify input parameters!
# -----------------------------------------------------------------------------
def e10(data: dict[str, dict], new_salary: int) -> dict[str, dict]:
    '''Exercise 10: Change value of a key in a nested dictionary.
       Change Brad's salary to new_salary.'''

    result: dict = copy.deepcopy(data)
    result['emp3']['salary'] = new_salary

    return result


# Main
# -----------------------------------------------------------------------------
data: dict[str, dict] = {
    'emp1':  {'name': 'Jhon',  'salary': 7500},
    'emp2':  {'name': 'Emma',  'salary': 8000},
    'emp3':  {'name': 'Brad',  'salary':  500},
}

new_salary: int = 8500

# Pretty Printing
pprint.pp(e10(data, new_salary))
# -----------------------------------------------------------------------------
