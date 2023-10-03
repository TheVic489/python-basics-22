'''
Object-Oriented Programming (OOP) in Python.
'''

# Classes follow CamelCase notation
class BadExample:
    pass

# Classes usually have a constructor method (__init__)
# Constructor:
# - On definition, we write __init__()
# - On calling, we write Dog()
# Methods:
# - All methods have a special paremeter: self.
# - When calling the methods, we don't write it.
# Attributes:
# - Attributes are variables stored inside the object.
# - They are created by the Constructor.
# - Methods in the object can access attributes directly.
# - To access them write: self.<attribute>
# ---------------------------------------------------------
class Dog:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age  = age

    def greet(self):
        print(f"Hello! I'm {self.name}")

# ---------------------------------------------------------

firulais: Dog = Dog("Firulais", 3)
firulais.greet()

dama: Dog = Dog("Dama", 5)
dama.greet()

# ---------------------------------------------------------
