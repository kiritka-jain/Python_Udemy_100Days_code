import random
from turtle import Turtle, Screen

import turtle

timmy = Turtle()
turtle.colormode(255)
timmy.shape("turtle")
timmy.speed("fastest")


def generate_random_pencolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


angle = 0
while angle <= 360:
    timmy.setheading(angle)
    timmy.circle(100)
    timmy.pencolor(generate_random_pencolor())
    angle += 5

screen = Screen()
screen.exitonclick()
