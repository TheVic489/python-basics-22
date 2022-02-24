# 1. Recibe tres nombres por teclado (input)
# 2. Guardarlos en una lista (usa un método)
# 3. Recorrer la lista imprimiéndolos. (for)
# 4. Recorrer la lista invertida. (usa un método)
#---------------------------------------------------------

# Create empty name list
# name_list: list[str] = []

# Input three names on list
# name1: str = input("Escribe un nombre: ")
# name_list.append(name1)

# name2: str = input("Escribe un nombre: ")
# name_list.append(name2)

# name3: str = input("Escribe un nombre: ")
# name_list.append(name3)

name_list: list[str] = ["John", "Mary", "Lucy"]

# Print all names
for name in name_list:
    print(f"Hello {name}")


# reversed_names: list[str] = list(reversed(name_list))

# Print all names
for name in reversed(name_list):
    print(f"Hello {name}")



#---------------------------------------------------------
