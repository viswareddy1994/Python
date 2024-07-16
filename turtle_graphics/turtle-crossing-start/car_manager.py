from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars_list = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    
    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance ==3:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_x = 280
            new_y = random.randint(-250,250)
            new_car.color(random.choice(COLORS))
            new_car.goto(new_x,new_y)
            self.cars_list.append(new_car)

    def move_left(self):
        for car in self.cars_list:
            car.setheading(180)
            car.forward(self.car_speed)
    def level_up(self):
        self.car_speed += MOVE_INCREMENT