"""
- v3: Use of decorator to create class method for 'from_lullaby()'.
- Canis lupus taxonomy:
  https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Undef&id=9612&lvl=3&keep=1&srchmode=1&unlock
"""

# Example of default values in the superclass.
# -----------------------------------------------------------------------------
class CanisLupus:

    # Constructor
    def __init__(self, name: str, age: int):
        self.species:       str = 'Canis lupus'
        self.greeting:      str = 'I am a normal wolf'
        self.favorite_food: str = 'Meat'

        self.name:          str = name
        self.age:           int = age

    def __str__(self) -> str:
        introduction: str = f"Hi! My name is {self.name}, I am a {self.species} and I am {self.age} years old."
        closing:      str = f"I love {self.favorite_food} and {self.greeting}."
        return f"{introduction}\n{closing}\n"


# -----------------------------------------------------------------------------
class Arctos(CanisLupus):

    # Constructor
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.species:       str = 'Canis lupus Arctos'
        self.greeting:      str = 'I am a cool wolf!'
        self.favorite_food: str = 'Polar bear barbecue'


# -----------------------------------------------------------------------------
class Baileyi(CanisLupus):

    # Constructor
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.species:       str = 'Canis lupus Baileyi'
        self.greeting:      str = 'I am a mexican wolf!'
        self.favorite_food: str = 'Burritos'


# ALWAYS WRITE A CONSTRUCTOR IN YOUR CLASSES.
# And the first thing is to call super().__init__()
# -----------------------------------------------------------------------------
class Signatus(CanisLupus):

    # Constructor
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.species:       str = 'Canis lupus Signatus'
        self.greeting:      str = 'I am a spanish wolf!'
        self.favorite_food: str = 'Jamón'

    def __str__(self) -> str:
        canis_lupus_phrase: str = super().__str__()
        lola_phrase:        str = f"A cup of Café con leche in Plaza Mayor!"
        return canis_lupus_phrase + '\n' + lola_phrase + '\n'


# Invented species :)
# -----------------------------------------------------------------------------
class SignatusSiestus(Signatus):

    # Constructor
    def __init__(self, name: str, age: int, snore: str):
        super().__init__(name, age)
        self.snore = snore


    # Alternative Constructor
    @classmethod
    def from_lullaby(cls, name: str, age: int, lullaby: str):

        result: SignatusSiestus

        if lullaby == 'Duérmete niño':
            result = cls(name, age, 'Zzzz')

        elif lullaby == 'Megadeth':
            result = cls(name, age, 'Woooo!!')

        return result


    def __str__(self) -> str:
        return f"Soy {self.name}, tengo {self.age} años y hago {self.snore}"


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
    cani: CanisLupus      = CanisLupus('Cani', 4)
    anya: Arctos          = Arctos('Anya', 4)
    juan: Baileyi         = Baileyi('Juan', 4)
    lola: Signatus        = Signatus('Lola', 4)
    toni: SignatusSiestus = SignatusSiestus('Toni', 4, 'Zzzzz')

    print('***Print wolves. print() calls __str__().***')
    print(cani, anya, juan, lola, toni, sep='\n')
    print()

    print('***Show instance attributes.***')
    show_attributes(cani)
    show_attributes(anya)
    show_attributes(juan)
    show_attributes(lola)
    show_attributes(toni)

    print('***Show inheritance relationships.***')
    print(f'Toni es de tipo {type(toni)}.')
    print(f'Toni es un Signatus? {isinstance(toni, Signatus)}.')
    print(f'Toni es un CanisLupus? {isinstance(toni, CanisLupus)}.')
    print(f'Toni es un Arctos? {isinstance(toni, Arctos)}.')

    print('***Alternative constructor.***')
    mari_nice:  SignatusSiestus = SignatusSiestus.from_lullaby('Mari', 4, 'Duérmete niño')
    mari_heavy: SignatusSiestus = SignatusSiestus.from_lullaby('Mari', 4, 'Megadeth')

    show_attributes(mari_nice)
    show_attributes(mari_heavy)


# -----------------------------------------------------------------------------
