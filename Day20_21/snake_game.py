import time
from turtle import Screen

from Day20_21.food import Food
from Day20_21.scoreboard import ScoreBoard
from Day20_21.snake import Snake

screen = Screen()
screen.title("The snake Game.")
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.move_snake_up, "Up")
screen.onkey(snake.move_snake_down, "Down")
screen.onkey(snake.move_snake_left, "Left")
screen.onkey(snake.move_snake_right, "Right")

if __name__ == '__main__':
    game_on = True
    snake.create_snake()

    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move_snake()
        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.food_refresh()
            snake.extend_segment()
            score.increase_score()

        # Detect collision with walls
        if (snake.head.xcor() > 290) or (snake.head.xcor() < -290) or (snake.head.ycor() > 290) or (
                snake.head.ycor() < -290):
            score.reset_score_board()
            snake.reset_snake()

        # Detect collision with tail
        for segment in snake.snaky[1:]:
            if snake.head.distance(segment) < 10:
                score.reset_score_board()
                snake.reset_snake()

screen.exitonclick()
