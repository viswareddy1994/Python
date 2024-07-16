# car_manager.py

from turtle import Turtle
import random
from constants import COLORS, STARTING_MOVE_DISTANCE, MOVE_INCREMENT, CAR_CREATION_CHANCE

class CarManager:
    def __init__(self):
        self.cars_list = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_cars(self):
        random_chance = random.randint(1, CAR_CREATION_CHANCE)
        if random_chance == 3:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(280, random.randint(-250, 250))
            self.cars_list.append(new_car)

    def move_left(self):
        for car in self.cars_list:
            car.backward(self.car_speed)

    def clear_off_screen_cars(self):
        self.cars_list = [car for car in self.cars_list if car.xcor() > -300]
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
