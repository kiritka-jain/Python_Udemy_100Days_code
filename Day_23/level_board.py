from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.goto(-340, 260)
        self.hideturtle()
        self.write_level()

    def write_level(self):
        self.write(f"Level{self.level}", font=("Verdana", 20, "normal"), align="left")

    def update_level(self):
        self.__increase_level()
        self.clear()
        self.write_level()

    def __increase_level(self):
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!!!", font=("Verdana", 30, "normal"), align="center")
