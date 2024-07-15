from turtle import Screen
from poddle import Paddle
from ball import Ball
from score import Score
import time


LEFT_PADDLE_POSITION = (-350, 0)
RIGHT_PADDLE_POSITION = (350, 0)
# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

# Create paddles
left_paddle = Paddle(LEFT_PADDLE_POSITION)

screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down,"s")

right_paddle = Paddle(RIGHT_PADDLE_POSITION)
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down,"Down")

ball = Ball()
score = Score()
# r_score = Score((20,260))
# r_score.center_line()
# l_score = Score((-20,260))


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()  
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 330) or  (ball.distance(left_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()
    if ball.xcor() > 350:
        ball.reset_position()
        score.l_point()
    if ball.xcor() < -350:
        ball.reset_position()
        score.r_point()
        
        
    # Close the window on click
screen.exitonclick()
