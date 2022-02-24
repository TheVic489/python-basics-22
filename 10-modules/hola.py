# ---------------------------------------------------------
def say_hola():
    print("¡Hola!")

# ---------------------------------------------------------
def is_main_module() -> bool:
    this_module_name: str = __name__
    main_module_name: str = "__main__"

    return this_module_name == main_module_name


# Main
# ---------------------------------------------------------
if is_main_module():
    say_hola()
else:
    pass
# ---------------------------------------------------------
