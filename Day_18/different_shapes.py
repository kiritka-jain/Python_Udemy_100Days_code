import random
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")


# timmy draws different shapes of different color.

def generate_random_pencolor():
    color_list = ['red', 'yellow', 'blue', 'cyan', 'green', 'brown', 'orange', 'maroon', 'cyan', 'indigo',
                  'crimson', 'coral', 'teal']
    color = random.choice(color_list)
    return color


def draw_shape(sides, each_angle, color):
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(each_angle)
        timmy.pencolor(color)


sides_count = [3, 4, 5, 6, 7, 8]
for side in sides_count:
    angle = 360 / side
    color = generate_random_pencolor()
    draw_shape(side, angle, color)

screen = Screen()
screen.exitonclick()
