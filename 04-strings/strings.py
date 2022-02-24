import pprint

# Funciones básicas: type(), id(), dir()

# String creation
#---------------------------------------------------------
s1: str = "Esto es un string. Un string es un texto."
s2: str = 'Esto es un string. Un string es un texto.'

s3: str = "It's a trap!"
s4: str = 'She said: "I love it!"'
s5: str = '''She said: "I'm busy!"'''
s6: str = """She said: "I'm busy!" """
s7: str = 'She said: "I\'m busy!\n"'  # Escape characters

s8: str = """
Comillas simples y comillas dobles son idénticas en Python.
Sirven para poner apóstrofes y comillas dentro.
"""

s9: str = "A" # String de una sola letra. No hay tipo char en Python.

# Strings are immutable
#---------------------------------------------------------

s1: str = "Hello"
# One-letter access
print(s1[5])

# Substrings
s1 = "He Ho"
len(s1)
print(s1)
print(s1[:])
print(s1[0:])
print(s1[0:5])
print(s1[0:len(s1)])

# Error! Strings are immutable!
s1[1] = "o"  
pprint.pp(dir(s1))


s2 = s1.upper()
s2

id(s1)
id(s2)
print(s2.lower())

# Tipos de strings
#---------------------------------------------------------
name: str = "Pablo"
normal_string: str =  "Hello\nWorld!"
raw_string:    str = r"Hello\nWorld!"
format_string: str = f"Hello\n{name}!"

print(normal_string)
print(raw_string)
print(format_string)

# Operaciones con  strings: +, *
#---------------------------------------------------------
# Concatenación
greeting: str = "Hello"
name:     str = "World"
space:    str = " "
bang:     str = "!"
concat:   str = greeting + space + name + bang

print(f"{greeting} {name}!")
print(concat)
print(greeting, name)
print("Hello" "World")

# Repetición
print("Hello " * 3)

# Índices negativos
#---------------------------------------------------------
s2: str = "Python"
print(s2[-1])

#---------------------------------------------------------
