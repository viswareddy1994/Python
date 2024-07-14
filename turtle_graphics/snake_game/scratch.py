from turtle import Turtle,Screen
screen = Screen()
tim =Turtle()

screen.tracer(0)
dist = 2
for i in range(200):
    tim.fd(dist)
    tim.rt(90)
    dist += 2
screen.update()
screen.exitonclick()