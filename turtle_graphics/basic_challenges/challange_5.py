from turtle import Turtle,Screen

turtle =Turtle()
screen = Screen()

def forward():
    turtle.forward(20)
    
def backword():
    turtle.backward(20)
    
def clockwise():
    turtle.right(10)
    # new_heading = turtle.heading() +10
    # turtle.setheading(new_heading)

def counter_clockwise():
    turtle.left(10)
    # new_heading = turtle.heading() - 10
    # turtle.setheading(new_heading)
    
def clear():
    turtle.clear()
    turtle.reset()

screen.listen() 
screen.onkey(fun=forward,key="w")
screen.onkey(fun=backword,key="s")
screen.onkey(fun=clockwise,key="d")
screen.onkey(fun=counter_clockwise,key="a")
screen.onkey(fun=clear,key="c")

screen.exitonclick()