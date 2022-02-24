# 5. Pedir 3 números, recorrerlos y sumarlos.
#---------------------------------------------------------

# Create empty name list
num_list: list[int] = []

# Input three names on list
num1: int = int(input("Escribe un número: "))
num_list.append(num1)

num2: int = int(input("Escribe un número: "))
num_list.append(num2)

num3: int = int(input("Escribe un nombre: "))
num_list.append(num3)

total:    int       = 0
# num_list: list[int] = [1, 2, 3]

# Print all numbers
for num in num_list:
    total = total + num

print(total)

#---------------------------------------------------------
