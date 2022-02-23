import turtle as t

# Draw a Dashed Line
the_turtle = t.Turtle()

for _ in range(15):
    the_turtle.forward(10)
    the_turtle.penup()
    the_turtle.forward(10)
    the_turtle.pendown()
    