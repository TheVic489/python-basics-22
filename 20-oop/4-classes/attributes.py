"""
- Attributes. Classes vs Instances.
- Canis lupus taxonomy:
  https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Undef&id=9612&lvl=3&keep=1&srchmode=1&unlock
"""

# -----------------------------------------------------------------------------
class Dog:

    # Class Attribute (está fuera del constructor y no es self.xxx)
    species: str = 'Canis lupus familiaris'

    # Constructor
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age:  int = age

    def __str__(self) -> str:
        return f"{self.name} is a {Dog.species} is {self.age} years old."


# Functions (Outside of Dog class)
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

    print('***Create dogs***')
    sarah: Dog = Dog('Sarah', 4)
    james: Dog = Dog('James', 3)

    print('***Print dogs. print() calls __str__().***')
    print(sarah, james, sep='\n')
    print()

    print('***Print Instance Attributes***')
    show_attributes(sarah)
    show_attributes(james)

    print('***Print Class Attributes***')
    show_attributes(Dog)

    print('***We can access attributes from outside***')
    print(Dog.species)  # Class attribute
    print(sarah.name)   # Instance attribute
    print()

    print('***We can change Instance Attributes***')
    sarah.name = "Sarah Connor"
    print(sarah.name)   
    print()

    print('***We can change Class Attributes***')
    Dog.species = 'Canis lupus lupus'
    print(Dog.species)
    print(sarah, james, sep='\n')
    print()

    show_attributes(sarah)
    show_attributes(james)
    show_attributes(Dog)

    print('***You CANNOT change Class Attributes through instances***')
    # - Instances can read class attributes.
    # - If an attribute is not found in an instance, Python automatically searches it in the Class.
    # - But Instances cannot write class attributes.
    # - Instead, a new instance attribute is created. It shadows the Class Attribute (cannot read it anymore).
    sarah.species = 'Canis lupus signatus'
    show_attributes(sarah)
    show_attributes(james)
    show_attributes(Dog)

# -----------------------------------------------------------------------------
