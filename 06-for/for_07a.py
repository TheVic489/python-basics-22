# 7. Recorrer una lista de nombres mostrando
#    su índice dentro de la lista

# Solution No 1. Write indexes MANUALLY.
name_list: list[str]  = ["John", "Mary", "Lucy"]
index_list: list[int] = [0, 1, 2]

for index in index_list:
    print(f"Index: {index}")
    print(f"Name:  {name_list[index]}")
    print()
