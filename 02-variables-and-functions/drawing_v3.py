from turtle import *

# --------------------------------------------
# Documentation:
# - https://docs.python.org/3/library/turtle.html
# --------------------------------------------

# Window and Canvas setup
# --------------------------------------------
def configure_canvas(
    canvas_height: int,
    canvas_width:  int):

    # Coordinates of the window in the desktop
    window_top_left_x: int = 0
    window_top_left_y: int = 0

    # Create Window with Canvas inside
    setup(canvas_width,
          canvas_height,
          window_top_left_x,
          window_top_left_y)


# Draw line. goto() coordinates are absolute.
# --------------------------------------------
def draw_line(vertex1_x, vertex1_y,
              vertex2_x, vertex2_y):

    # Move to vertex1
    penup()
    goto(vertex1_x, vertex1_y) 

    # Draw vertex1 -> vertex2
    pendown()
    goto(vertex2_x, vertex2_y)


# Draw triangle
# --------------------------------------------
def draw_triangle(top_x, top_y):

    vertex1_x = top_x
    vertex1_y = top_y

    vertex2_x = top_x + 100
    vertex2_y = top_y - 100

    vertex3_x = top_x - 100
    vertex3_y = top_y - 100


    draw_line(vertex1_x, vertex1_y,
              vertex2_x, vertex2_y)

    draw_line(vertex2_x, vertex2_y,
              vertex3_x, vertex3_y)

    draw_line(vertex3_x, vertex3_y,
              vertex1_x, vertex1_y)


# Draw rectangle
# --------------------------------------------
def draw_rectangle(top_left_x,     top_left_y,
                   bottom_right_x, bottom_right_y):

    width  = bottom_right_x - top_left_x

    vertex1_x = top_left_x
    vertex1_y = top_left_y

    vertex2_x = top_left_x + width
    vertex2_y = top_left_y

    vertex3_x = bottom_right_x
    vertex3_y = bottom_right_y

    vertex4_x = bottom_right_x - width
    vertex4_y = bottom_right_y


    draw_line(vertex1_x, vertex1_y,
              vertex2_x, vertex2_y)

    draw_line(vertex2_x, vertex2_y,
              vertex3_x, vertex3_y)

    draw_line(vertex3_x, vertex3_y,
              vertex4_x, vertex4_y)

    draw_line(vertex4_x, vertex4_y,
              vertex1_x, vertex1_y)


# Draw tree. Main drawing.
# --------------------------------------------
def draw_tree():

    # Tree leafs
    draw_triangle(0, 100)
    draw_triangle(0, 150)
    draw_triangle(0, 200)

    # Tree trunk
    draw_rectangle(-20, 0, 20, -100)




# Main
# --------------------------------------------
configure_canvas(500, 500)
draw_tree()
done()
