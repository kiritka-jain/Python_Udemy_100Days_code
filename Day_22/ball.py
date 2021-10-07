from random import randint
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.x_cor = 10
        self.y_cor = 10

    def move_ball(self):
        new_x_cor = self.xcor() + self.x_cor
        new_y_cor = self.ycor() + self.y_cor
        self.goto(new_x_cor, new_y_cor)

    def bounce(self):
        self.y_cor = self.y_cor * -1

    def bounce_x_direction(self):
        self.x_cor *= -1

    def ball_reset(self):
        self.goto(0, 0)
        self.bounce_x_direction()