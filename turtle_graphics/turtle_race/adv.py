from turtle import Turtle, Screen
import random

def setup_turtles(colors):
    x_coordinate = -230
    y_coordinate = -125
    turtles = []
    
    for color in colors:
        turtle = Turtle(shape="turtle")
        turtle.penup()
        turtle.color(color)
        turtle.goto(x=x_coordinate, y=y_coordinate)
        turtles.append(turtle)
        y_coordinate += 50
    
    return turtles

def reset_turtles(turtles):
    x_coordinate = -230
    y_coordinate = -125
    
    for turtle in turtles:
        turtle.goto(x=x_coordinate, y=y_coordinate)
        y_coordinate += 50

def start_race(turtles):
    is_game_on = True
    
    while is_game_on:
        for turtle in turtles:
            if turtle.xcor() > 230:
                is_game_on = False
                return turtle.pencolor()
            
            random_distance = random.randint(1, 10)
            turtle.forward(random_distance)

def display_winner(winning_color, user_bet):
    message = Turtle()
    message.hideturtle()
    message.penup()
    message.goto(0, 0)
    if winning_color == user_bet:
        message.write(f"You won! 😊 The {winning_color} turtle is the winner! 🏆", align="center", font=("Arial", 16, "normal"))
    else:
        message.write(f"You lost! 😒 The winning turtle is the {winning_color} turtle.", align="center", font=("Arial", 16, "normal"))

def clear_message():
    screen.clearscreen()

def main():
    global screen
    screen = Screen()
    screen.setup(width=500, height=400)
    
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    turtles = setup_turtles(colors)
    
    while True:
        user_bet = screen.textinput(title="Make your bet", prompt="Which Turtle will win the race? Choose the color: ")
        
        if user_bet:
            winning_color = start_race(turtles)
            display_winner(winning_color, user_bet)
            
            play_again = screen.textinput(title="Play Again?", prompt="Do you want to play again? (yes/no): ").lower()
            
            if play_again != 'yes':
                break
            else:
                clear_message()
                turtles = setup_turtles(colors)
    
    screen.bye()

if __name__ == "__main__":
    main()
