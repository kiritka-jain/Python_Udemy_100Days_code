from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position,0)

    def move_paddle_up(self):
        self.forward(20)

    def move_paddle_down(self):
        self.backward(20)
