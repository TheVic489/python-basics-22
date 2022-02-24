# 7. Recorrer una lista de nombres mostrando
#    su índice dentro de la lista

# - range() always returns an iterator.
#   You must convert it to a list manually.
# - range() function can be called with
#   up to three parameters.

# 1. One parameter
print(list(range(5))) # Excludes last number

# 2. Two parameters
print(list(range(3, 6))) # Excludes last number

# 3. Three parameters
# Third paramer means "step".
print(list(range(1, 11, 2))) # Excludes last number




# Solution No 2. Write indexes AUTOMATICALLY.
name_list: list[str]  = ["John", "Mary", "Lucy"]
index_list: list[int] = list(range(len(name_list)))

for index in index_list:
    print(f"Index: {index}")
    print(f"Name:  {name_list[index]}")
    print()

