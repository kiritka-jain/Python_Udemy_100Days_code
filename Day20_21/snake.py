from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snaky = []
        self.create_snake()
        self.head = self.snaky[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.__add_segment(position)

    def move_snake(self):
        for seg_num in range(len(self.snaky) - 1, 0, -1):
            new_x_cor = self.snaky[seg_num - 1].xcor()
            new_y_cor = self.snaky[seg_num - 1].ycor()
            self.snaky[seg_num].goto(new_x_cor, new_y_cor)
        self.head.forward(MOVING_DISTANCE)

    def move_snake_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_snake_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_snake_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def __add_segment(self,position):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape('square')
        new_segment.color('white')
        new_segment.goto(position)
        self.snaky.append(new_segment)

    def reset_snake(self):
        for segment in self.snaky:
            segment.goto(1000,1000)
        self.snaky.clear()
        self.create_snake()
        self.head = self.snaky[0]

    def extend_segment(self):
        self.__add_segment(self.snaky[-1].position())