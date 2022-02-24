#----------------------------------------------------------------------
class Square:

    # Class variables. Will be shadowed! Remove later.
    x:      float
    y:      float
    length: float

    def __init__(self, x: float, y: float, length: float):
        "Constructor"

        self.x = x
        self.y = y
        self.length = length

    def get_upper_left(self) -> float:
        "Esta función devuelve la x un vértice del cuadrado"

        midlength: float = self.length / 2

        upper_left_x = self.x - midlength
        upper_left_y = self.y + midlength

        return upper_left_x, upper_left_y


    def get_upper_right(self) -> float:
        "Esta función devuelve la x un vértice del cuadrado"

        midlength: float = self.length / 2

        upper_right_x = self.x + midlength
        upper_right_y = self.y + midlength

        return upper_right_x, upper_right_y

    


s: Square = Square(0, 0, 10)

print("Atributos del cuadrado s:")
print(s.x)
print(s.y)
print(s.length)

print("Vértice superior izquierdo del cuadrado s:")
print(s.get_upper_left())

print("Vértice superior derecho del cuadrado s:")
print(s.get_upper_right())






















# #----------------------------------------------------------------------
# def get_upper_left_x(x:      float,
#                      y:      float,
#                      length: float) -> float:
#     "Esta función devuelve la x un vértice del cuadrado"

#     midlength: float = length / 2

#     upper_left_x = x - midlength
#     upper_left_y = y + midlength

#     result = upper_left_x
#     return result

# #----------------------------------------------------------------------
# def get_upper_left_y(x:      float,
#                      y:      float,
#                      length: float) -> float:
#     "Esta función devuelve la y un vértice del cuadrado"

#     midlength: float = length / 2

#     upper_left_x = x - midlength
#     upper_left_y = y + midlength

#     result = upper_left_y
#     return result

# #----------------------------------------------------------------------
# def get_upper_right_x(x:      float,
#                       y:      float,
#                       length: float) -> float:
#     "Esta función devuelve la x un vértice del cuadrado"

#     midlength: float = length / 2

#     upper_right_x = x + midlength
#     upper_right_y = y + midlength

#     result = upper_right_x
#     return result

# #----------------------------------------------------------------------
# def get_upper_right_y(x:      float,
#                       y:      float,
#                       length: float) -> float:
#     "Esta función devuelve la x un vértice del cuadrado"

#     midlength: float = length / 2

#     upper_right_x = x + midlength
#     upper_right_y = y + midlength

#     result = upper_right_y
#     return result


# # Main
# #----------------------------------------------------------------------

# x = 0
# y = 0
# length = 10

# print("El vértice superior izquierdo es:")
# print(get_upper_left_x(x, y, length))
# print(get_upper_left_y(x, y, length))

# print("El vértice superior derecho es:")
# print(get_upper_right_x(x, y, length))
# print(get_upper_right_y(x, y, length))


# #----------------------------------------------------------------------
