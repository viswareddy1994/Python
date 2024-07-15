from turtle import Turtle

COLOR = "white"
LENGTH = 1
WIDTH = 5
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color(COLOR)
        self.speed("fastest")
        self.shapesize(stretch_wid=WIDTH,stretch_len=LENGTH)
        self.penup()
        self.goto(position)        
              
    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(),new_y)
    
    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(),new_y)
        
        



