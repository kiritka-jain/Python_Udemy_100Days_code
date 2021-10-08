import time
from random import randint
from turtle import Screen

from Day_23.car import CarManager
from Day_23.level_board import Level
from Day_23.player import Player

screen = Screen()
screen.setup(height=600, width=800)
screen.title("The turtle crossing game")
screen.tracer(0)


# Generate turtle
timmy = Player()

# Generate cars
car_manager = CarManager()

# Game level
level = Level()
level.write_level()

screen.listen()
screen.onkey(timmy.move_forward, 'Up')

game_on = True
car_no = 0
while game_on:

    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Detecting collision with timmy
    for car in car_manager.all_car:
        if timmy.distance(car) < 20:
            game_on = False
            level.game_over()

    # Has timmy crossed the road
    if timmy.is_at_finish_line():
        level.update_level()
        timmy.reset_position()
        car_manager.increase_speed()






screen.exitonclick()
