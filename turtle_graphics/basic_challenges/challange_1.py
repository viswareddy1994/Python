from turtle import Turtle,_Screen,Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)
def dashed_line():
    timmy.pendown()
    timmy.forward(20)
    timmy.penup()
    timmy.forward(20)
for _ in range(10):
    dashed_line()












screen = Screen()
screen.exitonclick()