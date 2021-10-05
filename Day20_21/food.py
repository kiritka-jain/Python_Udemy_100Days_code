from random import randint
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.food_refresh()

    def food_refresh(self):
        random_location_x = randint(-280, 280)
        random_location_y = randint(-280, 280)
        self.goto(random_location_x, random_location_y)