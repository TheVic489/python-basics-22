'''
- Exceptions
    - Cuando detectamos un error: raise <excepcion>
    - El código despues del raise NO se ejecuta !!
    
    try:
    |       <- Codigo que puede fallar
    |
    except:
    |       <- El tratamiento del error
    |
'''
ex: Exception = Exception(' Error! :( ')
 
age: int = 18
 
if age > 0:
    print(age)
else:
    raise ex    

num1: float = 1
num2: float = 1

print(num1 + num2)