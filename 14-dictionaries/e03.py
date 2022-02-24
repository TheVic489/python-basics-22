# PyNative Loop exercises
# https://pynative.com/python-dictionary-exercise-with-solutions/


# Don't write parameter types if they are too complex or unknown.
# https://mypy.readthedocs.io/en/stable/dynamic_typing.html
# -----------------------------------------------------------------------------
def e03_v1(all_data: dict) -> int:
    '''Exercise 3: Print the value of key 'history' from the dict below.'''

    class_data:   dict = all_data['class']
    student_data: dict = class_data['student']
    marks_data:   dict = student_data['marks']
    history_data: int  = marks_data['history']

    return history_data


# -----------------------------------------------------------------------------
def e03_v2(data: dict) -> int:
    '''Exercise 3: Print the value of key 'history' from the dict below.'''

    history_data: int = data['class']['student']['marks']['history']

    return history_data


# Main
# -----------------------------------------------------------------------------
data: dict = { 'class': { 'student': { 'name': 'Mike',
                                       'marks': { 'physics': 70,
                                                  'history': 80, }}}}

print(e03_v2(data))
# -----------------------------------------------------------------------------
