# While loops

# while ejecuta el body
# mientras la condición sea True.

# 1. Mira la condición
# 2. Si es True ejecuta el body
# 3.   Después de ejecutar el body
#      salta otra vez a la condición
# 4. Si la condición es False, acaba.
# La actualización de "finished"
# tiene que ser siempre al final!

count:    int  = 0
finished: bool = (count > 3)

while not finished:

    # Body
    print(count)

    # Update finishing condition
    count = count + 1
    finished = (count > 3)
