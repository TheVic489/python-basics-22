"""
- v1: A lot of code repetition.
- Canis lupus taxonomy:
  https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Undef&id=9612&lvl=3&keep=1&srchmode=1&unlock
"""

# -----------------------------------------------------------------------------
class Arctos:

    # Constructor
    def __init__(self, name: str, age: int):
        self.species:       str = 'Canis lupus arctos'
        self.greeting:      str = 'I am a cool wolf!'
        self.favorite_food: str = 'Polar bear barbecue'
        self.name:          str = name
        self.age:           int = age

    def __str__(self) -> str:
        introduction: str = f"Hi! My name is {self.name}, I am a {self.species} and I am {self.age} years old."
        closing:      str = f"I love {self.favorite_food} and {self.greeting}."
        return f"{introduction}\n{closing}\n"


# -----------------------------------------------------------------------------
class Baileyi:

    # Constructor
    def __init__(self, name: str, age: int):
        self.species:       str = 'Canis lupus baileyi'
        self.greeting:      str = 'I am a mexican wolf!'
        self.favorite_food: str = 'Burritos'
        self.name:          str = name
        self.age:           int = age

    def __str__(self) -> str:
        introduction: str = f"Hi! My name is {self.name}, I am a {self.species} and I am {self.age} years old."
        closing:      str = f"I love {self.favorite_food} and {self.greeting}."
        return f"{introduction}\n{closing}\n"


# -----------------------------------------------------------------------------
class Signatus:

    # Constructor
    def __init__(self, name: str, age: int):
        self.species:       str = 'Canis lupus signatus'
        self.greeting:      str = 'I am a spanish wolf!'
        self.favorite_food: str = 'Jamón'
        self.name:          str = name
        self.age:           int = age

    def __str__(self) -> str:
        introduction: str = f"Hi! My name is {self.name}, I am a {self.species} and I am {self.age} years old."
        closing:      str = f"I love {self.favorite_food} and {self.greeting}."
        return f"{introduction}\n{closing}\n"


# Functions (Outside the class)
# -----------------------------------------------------------------------------
def show_attributes(something) -> None:

    keys:   list = sorted(something.__dict__.keys())
    values: list = [something.__dict__[key] for key in keys]

    for key, value in zip(keys, values):
        print(f'{key}: {value}')

    print()


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    print('***Create wolves***')
    anya: Arctos   = Arctos('Anya', 4)
    juan: Baileyi  = Baileyi('Juan', 4)
    lola: Signatus = Signatus('Lola', 4)

    print('***Print wolves. print() calls __str__().***')
    print(anya, juan, lola, sep='\n')
    print()

# -----------------------------------------------------------------------------
