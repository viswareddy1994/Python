# scoreboard.py

from turtle import Turtle
from constants import FONT

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.create_scoreboard()
               
    def create_scoreboard(self):
        self.clear()
        self.goto(-230, 270)
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)
    
    def update_level(self):
        self.level += 1
        self.create_scoreboard()
    
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg="GAME OVER 😭", align="center", font=FONT)
