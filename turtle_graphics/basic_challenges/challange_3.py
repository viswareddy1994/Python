from turtle import Turtle,_Screen,Screen
import turtle as t
import random

t.colormode(255)
def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    return (r,b,g)

timmy = Turtle()
timmy.shape("turtle")
timmy.speed("fastest")  
timmy.pensize(10)
directions = [0,90,180,270]


for i in range(100):
    timmy.color(random_color())
    timmy.forward(50)
    timmy.setheading(random.choice(directions))
    
screen = Screen()
screen.exitonclick()