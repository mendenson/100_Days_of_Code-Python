import turtle as turtle_module
import random

turtle_module.colormode(255)
the_turtle = turtle_module.Turtle()
the_turtle.speed("fastest")
the_turtle.penup()
the_turtle.hideturtle()
color_list = [(245, 243, 237), (248, 241, 244), (238, 240, 246), (201, 164, 112), (239, 246, 241), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44), (138, 31, 20), (135, 163, 183), (196, 94, 75), (49, 121, 88), (143, 177, 149), (95, 75, 77), (76, 39, 32), (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48), (32, 61, 76), (22, 83, 89), (182, 204, 176), (141, 22, 25), (86, 147, 127), (45, 66, 85), (8, 68, 53), (177, 94, 97), (222, 177, 182), (109, 128, 151)]
the_turtle.setheading(315)
the_turtle.forward(300)
the_turtle.setheading(0)
number_of_dots = 100

for dot_count in range(10, number_of_dots + 1):
    the_turtle.dot(20, random.choice(color_list))
    the_turtle.forward(50)

    if dot_count % 10 == 0:
        the_turtle.setheading(90)
        the_turtle.forward(50)
        the_turtle.setheading(180)
        the_turtle.forward(500)
        the_turtle.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
