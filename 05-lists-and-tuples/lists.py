import copy
import pprint
import random

# Official tutorial
# Use Python 3.9 to use native types subtyping

# Lists (Tutorial: 3.1.3 Lists)
#---------------------------------------------------------

# List literals
l1: list      = [] # Empty list
l2: list[str] = ["John", "Mary", "Lucy"]

# Length of a list
l2_len: int   = len(l2)

# Element access
print(l2[0])         # John
print(l2[2])         # Lucy
print(l2[-1])        # Lucy
print(l2[len(l2)-1]) # Lucy

print(l2[2][0])      # "Lucy"[0] -> "L"

# Sublists (Slices)
l3: list[str] = ["a", "b", "c", "d", "e", "f"]
print(l3[0:4]) # a,b,c,d
print(l3[4:6]) # e,f
print(l3[4:])  # e,f  <- Preferred way.

# List operations +, *
print(["John", "Mary", "Lucy"] + ["Peter", "Isaac"])
print([1, 2, 3]  * 3) # Repeats elements of a list

# Multiple types in a list. NOT recommended!
l4: list[object] = print([1, "John", True, 0.9])
l5: list[list[int]] = [[1, 2], [3, 4]]

first_row:  list[int] = l5[0]
second_row: list[int] = l5[1]
print(f"{first_row}\n{second_row}")

# Search elements
l6: list[str] = ["a", "b", "c", "d", "e", "f"]
print(l6.index("a"))

# Count
l6: list[str] = ["a", "b", "b", "c", "c", "c"]
print(l6.count("b"))

# Sorted
# sorted() returns a new sorted list.
# There is .sort() but it is impure!
l6:        list[int] = [4, 2, 1, 3, 0]
l6_sorted: list[int] = sorted(l6, reverse=True)
print(l6_sorted)

# Reversed
# Returns a new reversed list.
# There is .reverse() but it is impure!
l6:          list[int] = [4, 3, 2, 1, 0]
l6_reversed: list[int] = list(reversed(l6))
print(l6_reversed)



# Pure functions vs Impure functions
#---------------------------------------------------------

# In Python, all functions return something.
# If there is no "return" keyword, they return None.

# A function is pure if...
# 1. Only reads from its input parameters.
# 2. Only writes its output parameters.
# 3. Given the same input parameters
#    it always outputs the same output parameters.

# Examples: Failure of condition 1
a = 1
def do_something_v1():
    print(a)

do_something_v1()

def do_something_v2():
    b = input()
    print(b)

do_something_v2()


# Examples: Failure of condition 2
l6: list[int] = [1, 2, 3]
l6.append(4)  # Returns None. I want a new list!


# Examples: Failure of condition 3
def do_something_v3():
    return random.randint(1,10)

do_something_v3()


# List mutations (Tutorial: 5.1 More on Lists)
#---------------------------------------------------------
# ALL THESE METHODS MUTATE THE ORIGINAL LIST.
# ALL THESE METHODS ARE IMPURE!

# Assignments. Lists are mutable!
l3[0] = "z"
l3[0] = "a"
print(l3)

# Slice assignments
l3[3:] = [1, 2, 3]  # d,e,f -> 1,2,3
l3[3:] = ["d"]      # New assignment can be of different length
l3[3:] = []         # Deletes from index 3
l3[:]  = []
print(l3)

# List methods
l3_methods: list[str] = dir(l3)
pprint.pp(l3_methods)

# Append
l3: list[int] = [0, 1, 2, 3, 4, 5]
l3.append(6)
print(l3)

# Extend
l6: list[int] = [1,2,3]
l7: list[int] = [4,5,6]

l8: list[int] = l6 + l7  # Pure operation!
print(l8)

l6.extend(l7)  # l6 is extended with l7 elements
print(l6)      # Prefer always '+' rather than .extend()

# Insert. Does NOT overwrite. Other elements are moved.
l6:list[int] = ["a", "b", "c"]
l6.insert(0, "x")  # Insert x at position 0.
l6.insert(len(l6), "x")  # Insert x at the end!

print(l6)

# Remove.
# Uses the element to be removed, NOT the index!
# Removes only the first element found.
# It's an error if the element is not in the list!
l6.remove("b") # Removes the element.
print(l6)

# Pop
# Removes by index
# Returns an error if index is out of bounds
l6.pop(1)
print(l6)

# Clear
# Removes all elements, but keeps the list.
l6.clear()


# "del" keyword
#---------------------------------------------------------
# "del" is a keyword, not a function!
# After "del", there are no brackets!
# "del" means "delete"
# "del" CAN DELETE ANYTHING!

l6: list[str] = ["a", "b", "c", "d"]
del l6[1]  # Delete an element
print(l6)

del l6[:]  # Delete all elements. Keep the list.
print(l6)

del l6    # Delete the whole list!
print(l6)

# Copy
#---------------------------------------------------------
# Use always the copy module
# There are two functions: .copy() and .deepcopy()

l6: list[int] = [1,2,3] 
l7: list[int] = copy.copy(l6)
print(id(l6))
print(id(l7))

l7.clear()
print(l6)
print(l7)

#---------------------------------------------------------
