from turtle import *

# --------------------------------------------
# Use penup() to move the turtle freely.
# Use pendown() to start drawing.
# penup()
# pendown()
# --------------------------------------------

# Window and Canvas setup
def configure_canvas():
    canvas_height = 300
    canvas_width  = 300

    window_origin_x = 0
    window_origin_y = 0

    setup(canvas_width,
          canvas_height,
          window_origin_x,
          window_origin_y)


# Draw triangle
def draw_triangle(origin_x, origin_y):

    penup()
    
    goto(origin_x,
         origin_y)
    
    pendown()

    goto(origin_x + 100,
         origin_y + 100)

    goto(origin_x - 100,
         origin_y + 100)

    goto(origin_x,
         origin_y)


# Main
# --------------------------------------------
configure_canvas()

draw_triangle(  0, 0)
draw_triangle(-100, -100)
draw_triangle(-200, -200)

