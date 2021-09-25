import random
from turtle import Turtle

import colorgram
import turtle

timmy = Turtle()
turtle.colormode(255)
timmy.shape("turtle")
timmy.speed("fastest")


def generate_colors():
    number_of_colors = colorgram.extract('hirst.png', 15)
    color = random.choice(number_of_colors)
    first_color = color.rgb.r
    second_color = color.rgb.g
    third_color = color.rgb.b
    color_formed = (first_color, second_color, third_color)
    return color_formed



timmy.setheading(225)
timmy.penup()
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.pendown()
    timmy.dot(20, (generate_colors()))
    timmy.penup()
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


