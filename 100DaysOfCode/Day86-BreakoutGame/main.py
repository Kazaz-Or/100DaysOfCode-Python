from turtle import Screen, tracer, update
import time

from brick import Brick
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

INITIAL_PADDLE_POSITION = (0, -320)
INITIAL_BALL_POSITION = (0, -305)
VERTICAL_LIMIT = 380
HORIZONTAL_LIMIT = 720

screen = Screen()
screen.title("Break Out")
screen.bgcolor("black")
screen.setup(width=1400, height=750)
tracer(0, 0)

scoreboard = ScoreBoard()

brick_x_axis = -HORIZONTAL_LIMIT
brick_y_axis = 330
bricks = []
for i in range(7):
    for j in range(23):
        brick = Brick((brick_x_axis, brick_y_axis))
        bricks.append(brick)
        brick_x_axis += 65
    brick_x_axis = -HORIZONTAL_LIMIT
    brick_y_axis -= 20
ball = Ball(INITIAL_BALL_POSITION)

paddle = Paddle(INITIAL_PADDLE_POSITION)

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkeypress(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")
screen.onkeypress(paddle.move_right, "Right")

is_game_on = True
while is_game_on:
    time.sleep(ball.get_speed())
    screen.update()
    ball.move()

    if ball.ycor() > VERTICAL_LIMIT:
        ball.bounce_y()

    if ball.xcor() > HORIZONTAL_LIMIT+20 or ball.xcor() < -HORIZONTAL_LIMIT-20:
        ball.bounce_x()

    if ball.distance(paddle) < 45 and ball.ycor() < 290:
        ball.bounce_y()

    for brick in bricks:
        if ball.distance(brick) < 30:
            ball.bounce_x()
            brick.hideturtle()
            x_axis_difference = ball.distance(brick)
            y_axis_difference = ball.distance(brick)
            if x_axis_difference > y_axis_difference:
                ball.bounce_x()
            else:
                ball.bounce_x()
                ball.bounce_y()
            bricks.remove(brick)
            scoreboard.increase_score()
            if scoreboard.get_score() % 8 == 0:
                ball.increase_speed()
            break

    if ball.ycor() < -VERTICAL_LIMIT:
        is_game_on = False

    if not bricks:
        is_game_on = False

update()
screen.exitonclick()
