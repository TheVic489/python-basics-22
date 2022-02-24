# 6. Crear una lista con nombres y otra vacía.
#    Copiar todos los nombres en la lista vacía.
#---------------------------------------------------------

name_list: list[str] = ["John", "Mary", "Lucy"]

new_list_1: list[str] = []

for name in name_list:
    new_list_1.append(name)

print(new_list_1)


# Comentario de Gabriel
new_list_2:  list[str] = []

for name in name_list:
    new_list_2 = new_list_2 + [name]

print(new_list_2)

print(new_list_1 == new_list_2)

#---------------------------------------------------------
