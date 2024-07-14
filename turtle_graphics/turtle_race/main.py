from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which Turtle will win the race? Choose the color: ")
colors = ["red","orange","yellow","green","blue","purple"]
x_cordinate = -230
y_coordinate = -125
turtle_list = []

for i in colors:
    turtle =Turtle(shape="turtle")
    turtle.penup()
    turtle.color(i)
    turtle.goto(x=x_cordinate,y=y_coordinate)
    turtle_list.append(turtle)
    y_coordinate +=50
    
if user_bet:
    is_game_on = True
    
while is_game_on:
    
    for turtle in turtle_list:
        if turtle.xcor() >230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won!😊 The {winning_color} turtle is the winner!🏆")
            else:
                print(f"You Lost!😒 The winning turtle is {winning_color} turtle")
        
        random_dist = random.randint(1,10)
        turtle.forward(random_dist)
       
screen.exitonclick()