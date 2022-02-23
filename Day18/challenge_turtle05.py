import turtle as t
import random


# Generate a random walk
the_turtle = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]
the_turtle.pensize(15)

for _ in range(300):
    the_turtle.color(random_color())
    the_turtle.forward(30)
    the_turtle.setheading(random.choice(directions))