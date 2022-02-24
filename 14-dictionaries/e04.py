# PyNative Loop exercises
# https://pynative.com/python-dictionary-exercise-with-solutions/


# Alternative:
#   import pprint
#   pprint.pp(data)
# Beware:
# - for key in data:
# - for key, value in data.items():
# -----------------------------------------------------------------------------
def print_dict(data: dict):
    '''Pretty-print a dictionary'''

    for key, value in data.items():
        print(f"{key}: {value}")


# Note 1:
# - 'dict' is a class.
# - Classes can have callable ('static') methods.
# - Example: dict.fromkeys()
# Note 2:
# - PyNative's solution to exercise 4 IS DANGEROUS.
# - NEVER USE MUTABLE DATA AS A DEFAULT VALUE.
# - The value will be shared by all keys.
# - Use only immutable data like numbers or strings.
# -----------------------------------------------------------------------------
def show_no_problem_with_immutable_default_values():

    keys:          list[str] = ['Anna', 'Lucy']
    default_value: int       = 12000
    result:        dict      = dict.fromkeys(keys, default_value)

    # Before changing data
    print_dict(result)

    # Change data
    result['Anna'] = 0

    # After changing data
    print_dict(result)


# -----------------------------------------------------------------------------
def show_problem_with_mutable_default_values():

    keys:          list[str] = ['Anna', 'Lucy']
    default_value: dict      = {'salary': 8000, 'bonus': 12000}
    result:        dict      = dict.fromkeys(keys, default_value)
    
    # Before changing data
    print_dict(result)

    # Change data
    result['Anna']['bonus'] = 0

    # After changing data. ERROR: Lucy's bonus has changed!
    print_dict(result)


# -----------------------------------------------------------------------------
def show_solution_for_mutable_default_values():

    keys:          list[str] = ['Anna', 'Lucy']
    default_value: dict      = None
    result:        dict      = dict.fromkeys(keys, default_value)

    # Create a new mutable value for each key in a loop
    for key in result:
        result[key] = {'salary': 8000, 'bonus': 12000}

    # Before changing data
    print_dict(result)

    # Change data
    result['Anna']['bonus'] = 0

    # After changing data. All ok. Lucy's bonus has not changed.
    print_dict(result)


# Main
# -----------------------------------------------------------------------------
show_problem_with_mutable_default_values()
show_no_problem_with_immutable_default_values()
show_solution_for_mutable_default_values()
# -----------------------------------------------------------------------------
