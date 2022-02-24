
#---------------------------------------------------------
# Tuples
#---------------------------------------------------------

#---------------------------------------------------------
# About:
#   - Tuples are just immutable lists.
#   - Values are separated by commas
#   - Surrounding brackets are optional if the context in unambigous!
#---------------------------------------------------------

def example1() -> None:

    tuple1 = (1, 2, 3)
    print(tuple1)

    tuple2 = 4, 5, 6
    print(tuple2)



#---------------------------------------------------------
# Tuples typing:
#   - Example: birthday_date: tuple[int, int, int] = (2000, 4, 30)
#   - Unlike lists, it is usual for tuples to have multiple types
#---------------------------------------------------------

def example2() -> None:

    score: tuple[int, int] = (2, 2)
    print("Soccer match: Barça vs Madrid!", score)

    person: tuple[str, int, bool, float] = ("Pepe", 22, True, 1.78)
    print(person)



#---------------------------------------------------------
# Methods:
#   - They have all the methods of lists for reading data (.count, .index)
#   - They have none of the methods for modifying data (.append, etc.)
#---------------------------------------------------------

def example3() -> None:

    score: tuple[int, int] = (2, 2)
    print("Soccer match: Barça vs Madrid!")
    print("Barça: ", score[0])
    print("Madrid:", score[1])

    person: tuple[str, int, bool, float] = ("Pepe", 22, True, 1.78)
    print("Number of fields:", len(person))


#---------------------------------------------------------
# Tuples usage:
#   - Return multiple parameters from a function
#   - Group related variables
#   - Split multiple values into separate variables
#   - Variable swapping
#---------------------------------------------------------

def example4() -> tuple[float, float]:

    height: float = 1.75
    weight: float = 70.2

    return height, weight


def example5() -> None:

    scores: tuple[int, int] = (1, 0)
    user_score, cpu_score = scores

    print(f"User score: {user_score}")
    print(f"CPU  score: {cpu_score}")


def example6() -> None:

    user_score, cpu_score = (1, 0)

    print(f"User score: {user_score}")
    print(f"CPU  score: {cpu_score}")


def example7() -> None:

    a, b = 1, 2
    a, b = b, a

    print(f"a: {a}")
    print(f"b: {b}")

#---------------------------------------------------------
example1()
example2()
example3()
example4()
example5()
example6()
example7()
