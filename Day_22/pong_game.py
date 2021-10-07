import time
from turtle import Screen

from Day_22.ball import Ball
from Day_22.padles import Paddle
from Day_22.scoreboard import ScoreBoard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

player_a = Paddle(-350)
player_b = Paddle(350)
ball = Ball()
score_a = ScoreBoard('a')
score_b = ScoreBoard('b')




screen.listen()
screen.onkey(player_b.move_paddle_up, "Up")
screen.onkey(player_a.move_paddle_up, "s")
screen.onkey(player_b.move_paddle_down, "Down")
screen.onkey(player_a.move_paddle_down, "x")

game_on = True

while game_on:
    time.sleep(0.01)
    screen.update()
    ball.move_ball()

    # Detecting collision with side walls
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce()

    # Detecting collision with the paddle
    if (ball.distance(player_b) < 50 and ball.xcor() > 320) or (ball.distance(player_a) < 50 and ball.xcor() > -320):
        ball.bounce_x_direction()

    # If paddle_b misses the ball
    if ball.xcor() > 380:
        score_a.update_score('a')
        ball.ball_reset()

    # If paddle_a misses the ball
    elif ball.xcor() < -380:
        score_b.update_score('b')
        ball.ball_reset()

    # Who wins the game
    if score_a.compare_scores():
        score_a.game_over('A')
        game_on = False
    elif score_b.compare_scores():
        score_b.game_over('B')
        game_on = False








screen.exitonclick()
