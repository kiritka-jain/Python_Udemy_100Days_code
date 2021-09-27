import random
from turtle import Turtle, Screen


def create_turtles():
    for i in range(7):
        timmy = Turtle(shape='turtle')
        timmy.penup()
        timmy.color(turtle_colors[i])
        timmy.goto(-240, y_positions[i])
        turtle_list.append(timmy)
    return turtle_list


def who_wins(user_bet, winning_color):
    if winning_color == user_bet:
        return "You Win!"
    return f"You lose.the winning color is {winning_color}"


def run_game():
    is_race_on = False
    create_turtles()

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle_chosen in turtle_list:
            if turtle_chosen.xcor() > 230:
                is_race_on = False
                winning_color = turtle_chosen.pencolor()
                print(who_wins(user_bet, winning_color))

            distance_to_travel = random.randint(1, 10)
            turtle_chosen.forward(distance_to_travel)


if __name__ == '__main__':
    turtle_colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
    y_positions = [-180, -120, -60, 0, 60, 120, 180]
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title='Make your bet.', prompt="Which turtle will win the race?Enter the color:")
    turtle_list = []
    run_game()
    screen.exitonclick()