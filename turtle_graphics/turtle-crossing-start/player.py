from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self, shape: str = "turtle"):
        super().__init__(shape)
        self.color("black")
        self.penup()
        self.setheading(90)
        self.reset_position()
        self.draw_divided_road()
    
    def move(self):
        self.forward(MOVE_DISTANCE)
        
    def reset_position(self):
        self.goto(STARTING_POSITION)
        
    def draw_divided_road(self):
        line = Turtle()
        line.color("yellow")
        line.penup()
        line.goto(300, 0)
        line.setheading(180)
        for _ in range(30):
            line.pendown()
            line.forward(20)
            line.penup()
            line.forward(20)
        line.hideturtle()
