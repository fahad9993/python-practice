from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Right paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if R paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect if L paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    scoreboard.show_winner()
    if scoreboard.show_winner():
        is_game_on = False
        if scoreboard.restart().lower() == "y":
            # ball.reset_position()
            scoreboard.update_scoreboard()
            is_game_on = True

screen.exitonclick()
