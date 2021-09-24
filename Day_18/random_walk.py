import random
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
turtle.colormode(255)
timmy.shape("turtle")
timmy.width(7)
timmy.speed("fastest")


def generate_random_pencolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for _ in range(150):
    angles = [0, 90, 180, 270]
    angle = random.choice(angles)
    timmy.pencolor(generate_random_pencolor())
    timmy.setheading(angle)
    timmy.forward(20)

screen = Screen()
screen.exitonclick()
