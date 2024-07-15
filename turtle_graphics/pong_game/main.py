from turtle import Screen
from paddle import Paddle
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

# Create paddles, ball, and score
left_paddle = Paddle(LEFT_PADDLE_POSITION)
right_paddle = Paddle(RIGHT_PADDLE_POSITION)
ball = Ball()
score = Score()

# Variables to control game state
game_is_paused = False
game_is_on = True

def toggle_pause():
    global game_is_paused
    game_is_paused = not game_is_paused

def exit_game():
    global game_is_on
    game_is_on = False

# Bind keys
screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(toggle_pause, "space")
screen.onkey(exit_game, "Escape")

# Main game loop
while game_is_on:
    if not game_is_paused:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()
        
        # Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        
        # Detect collision with paddles
        if (ball.distance(right_paddle) < 50 and ball.xcor() > 330) or (ball.distance(left_paddle) < 50 and ball.xcor() < -330):
            ball.bounce_x()
        
        # Detect when right paddle misses
        if ball.xcor() > 350:
            ball.reset_position()
            score.l_point()
        
        # Detect when left paddle misses
        if ball.xcor() < -350:
            ball.reset_position()
            score.r_point()

    # Update the screen even if the game is paused to reflect the current state
    screen.update()

# Close the window
screen.bye()
