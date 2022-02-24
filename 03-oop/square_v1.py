#----------------------------------------------------------------------
def get_upper_left_x(x:      float,
                     y:      float,
                     length: float) -> float:
    "Esta función devuelve la x un vértice del cuadrado"

    midlength: float = length / 2

    upper_left_x = x - midlength
    upper_left_y = y + midlength

    result = upper_left_x
    return result

#----------------------------------------------------------------------
def get_upper_left_y(x:      float,
                     y:      float,
                     length: float) -> float:
    "Esta función devuelve la y un vértice del cuadrado"

    midlength: float = length / 2

    upper_left_x = x - midlength
    upper_left_y = y + midlength

    result = upper_left_y
    return result

#----------------------------------------------------------------------
def get_upper_right_x(x:      float,
                      y:      float,
                      length: float) -> float:
    "Esta función devuelve la x un vértice del cuadrado"

    midlength: float = length / 2

    upper_right_x = x + midlength
    upper_right_y = y + midlength

    result = upper_right_x
    return result

#----------------------------------------------------------------------
def get_upper_right_y(x:      float,
                      y:      float,
                      length: float) -> float:
    "Esta función devuelve la x un vértice del cuadrado"

    midlength: float = length / 2

    upper_right_x = x + midlength
    upper_right_y = y + midlength

    result = upper_right_y
    return result


# Main
#----------------------------------------------------------------------

x = 0
y = 0
length = 10

print("El vértice superior izquierdo es:")
print(get_upper_left_x(x, y, length))
print(get_upper_left_y(x, y, length))

print("El vértice superior derecho es:")
print(get_upper_right_x(x, y, length))
print(get_upper_right_y(x, y, length))


#----------------------------------------------------------------------
