from turtle import Screen, Turtle

# Constants for paddle dimensions and positions
COLOR = "white"
HEIGHT = 90
WIDTH = 20
LEFT_PADDLE_POSITION = (-350, 0)
RIGHT_PADDLE_POSITION = (350, 0)
DEFAULT_PADDLE_POSITION = (0, 0)
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, position="middle"):
        super().__init__()
        self.shape("square")  # Set the shape of the turtle to a square
        self.color(COLOR)
        self.shapesize(stretch_wid=5, stretch_len=1)  # Stretch the square shape to form a paddle
        self.coordinates = self.set_paddle_position(position)  # Set initial paddle position
        self.penup()
        self.goto(self.coordinates)  # Move the turtle to the initial position
        self.hideturtle()

    def set_paddle_position(self, position):
        if position == "left":
            return LEFT_PADDLE_POSITION
        elif position == "right":
            return RIGHT_PADDLE_POSITION
        else:
            return DEFAULT_PADDLE_POSITION

    def move_paddle(self):
        self.forward(MOVE_DISTANCE)

# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create paddles
left_paddle = Paddle(position="left")
right_paddle = Paddle(position="right")

# Bind key events (example for moving left paddle up)
def move_left_paddle():
    left_paddle.move_paddle()

screen.listen()
screen.onkey(move_left_paddle, "Up")  # Example for moving left paddle up on "Up" key press

# Update screen
screen.update()

# Close the window on click
screen.exitonclick()
