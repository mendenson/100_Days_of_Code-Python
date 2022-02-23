from random import random
import turtle as t
import random


# Drawing Differents Shapes #2
the_turtle = t.Turtle()

colours = ["black", "red", "yellow", "blue", "green", "orange", "purple"]

def draw_shape(n_sides):
    angle = 360 / n_sides
    for _ in range(n_sides):
        the_turtle.forward(100)
        the_turtle.right(angle)

for shape_side_n in range(3, 11):
    the_turtle.color(random.choice(colours))
    draw_shape(shape_side_n)
    