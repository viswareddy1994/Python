from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width= 600,height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score_board = Scoreboard()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Calculate Score
    if snake.head.distance(food) < 15:
        food.reshape()
        snake.extend()
        score_board.calculate_score()
        
    #Detect Collesion with walls
    if snake.head.xcor() >298 or snake.head.xcor() < -298 or snake.head.ycor() > 298 or snake.head.ycor() < -298:
        game_is_on = False
        score_board.game_over()
        
    #Detect Tail collesion
    for segment in snake.segments[1:]:
        if snake.head.distance(segment):
            game_is_on = False
            score_board.game_over()
        # if segment == snake.head:
        #     pass
        # elif snake.head.distance(segment) < 10:
        #     game_is_on = False
        #     score_board.game_over()

























screen.exitonclick()












