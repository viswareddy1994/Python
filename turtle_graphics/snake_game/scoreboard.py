from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 16, 'bold')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("White")
        self.goto(0,270)
        self.hideturtle()
        self.score = 0
        self.calculate_score()
    
    def update_scoreboard(self):
        self.write(arg= f"Your Score: {self.score}", move=False ,align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT,font=FONT)
    
    def calculate_score(self):
        self.clear()
        self.update_scoreboard()
        self.score +=1

        

        
            