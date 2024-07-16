# main.py

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FINISH_LINE_Y

def main():
    # Setup the screen
    screen = Screen()
    screen.bgcolor("gray")
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
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
        car_manager.clear_off_screen_cars()

        # Check for collision with cars
        for car in car_manager.cars_list:
            if player.distance(car) < 20:  # Adjusted distance for better collision detection
                scoreboard.game_over()
                game_is_on = False

        # Check if the player reached the finish line
        if player.ycor() >= FINISH_LINE_Y:
            player.reset_position()
            car_manager.level_up()
            scoreboard.update_level()

    screen.exitonclick()

if __name__ == "__main__":
    main()
