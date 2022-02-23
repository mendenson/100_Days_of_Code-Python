import turtle as t
import random


# Draw a Spirograph
the_turtle = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        the_turtle.color(random_color())
        the_turtle.circle(100)
        the_turtle.setheading(the_turtle.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick