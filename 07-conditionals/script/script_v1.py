# This module that can be imported.
# This module can also be executed as a script from the terminal.

# ---------------------------------------------------------------------
def print_message() -> None:
    print("Hello!")

# ---------------------------------------------------------------------
def is_main_module() -> bool:
    
    this_module_name: str = __name__
    main_module_name: str = "__main__"

    return (this_module_name == main_module_name)

# ---------------------------------------------------------------------
if is_main_module():
    print_message()

# ---------------------------------------------------------------------
