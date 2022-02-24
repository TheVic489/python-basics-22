#----------------------------------------------------------------------
class Square:

    # Class attributes go here.

    def __init__(self, x: float, y: float, length: float):
        "Constructor"

        # Instance attributes. Created on-the-fly.
        self.x = x
        self.y = y
        self.length = length


    def get_upper_left(self) -> tuple[float]:
        "Esta función devuelve el vértice superior izquierda del cuadrado"

        midlength: float = self.length / 2

        upper_left_x = self.x - midlength
        upper_left_y = self.y + midlength

        return upper_left_x, upper_left_y


    def get_upper_right(self) -> tuple[float]:
        "Esta función devuelve el vértice superior derecha del cuadrado"

        midlength: float = self.length / 2

        upper_right_x = self.x + midlength
        upper_right_y = self.y + midlength

        return upper_right_x, upper_right_y

    
# Main
#----------------------------------------------------------------------
s: Square = Square(0, 0, 10)

print("Atributos del cuadrado s:")
print(s.x)
print(s.y)
print(s.length)

print("Vértice superior izquierdo del cuadrado s:")
print(s.get_upper_left())

print("Vértice superior derecho del cuadrado s:")
print(s.get_upper_right())

#----------------------------------------------------------------------

