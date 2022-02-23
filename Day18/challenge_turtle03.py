import turtle as t

from numpy import angle

# Drawing Differents Shapes
the_turtle = t.Turtle()

n_sides = 10

for _ in range(n_sides):
    angle = 360 / n_sides
    the_turtle.forward(100)
    the_turtle.right(angle)
    