import random
from turtle import Turtle

COLORS = ['purple', 'indigo', 'red', 'orange', 'yellow', 'green', 'blue', 'magenta', 'purple',
          'navy', 'cyan', 'turquoise', 'gold']


class CarManager:
    def __init__(self):
        self.all_car = []
        self.car_speed = -10

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_color = random.choice(COLORS)
            new_car.color(random_color)
            y_cor_position = random.randint(-250, 250)
            x_car_position = random.randint(300, 340)
            new_car.penup()
            new_car.goto(x_car_position, y_cor_position)
            self.all_car.append(new_car)

    def move_car(self):
        for car in self.all_car:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed -= 5
        self.move_car()
