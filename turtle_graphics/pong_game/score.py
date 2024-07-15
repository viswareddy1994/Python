from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 50, 'bold')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.update_scoreboard()
    
    def center_line(self):
        y = self.ycor()
        while y !=300:
            self.goto(0,-300)
            self.pendown()
            self.color("white")
            self.forward(20)
            self.penup()
            self.forward(20)
        
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(arg= self.l_score ,align=ALIGNMENT,font=FONT)
        self.goto(100,200)
        self.write(arg= self.r_score ,align=ALIGNMENT,font=FONT)
    
    def l_point(self):
        self.l_score +=1
        self.update_scoreboard()
    
    def r_point(self):
        self.r_score +=1
        self.update_scoreboard()
        

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT,font=FONT)
    
