import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Setup the screen
screen = Screen()
screen.bgcolor("gray")
screen.setup(width=600, height=600)
screen.tracer(0)

# Initialize player and draw the divided road
player = Player()


# Initialize car manager and scoreboard
car_manager = CarManager()
scoreboard = Scoreboard()

# Listen for key presses
screen.listen()
screen.onkey(player.move, "Up")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_left()

    # Check for collision with cars
    for car in car_manager.cars_list:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Check if the player reached the finish line
    if player.ycor() >= 280:
        player.reset_position()
        car_manager.level_up()
        scoreboard.update_level()

screen.exitonclick()
