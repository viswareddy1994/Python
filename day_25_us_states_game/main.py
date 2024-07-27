from turtle import Turtle, Screen
import os
import pandas as pd
from states import States

# Set up the screen
screen = Screen()
screen.title("U.S. States Game")

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Define the relative path to the image
image_path = os.path.join(script_dir, "blank_states_img.gif")
csv_path = os.path.join(script_dir,"states_to_learn.csv")

# Check if the file exists
if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image file not found: {image_path}")

# Register the image as a new shape
screen.addshape(image_path)

# Set the turtle shape to the image
turtle = Turtle()
turtle.shape(image_path)

state = States()

keep_guessing = True

while keep_guessing:
    answer_state = screen.textinput(
        title=f"{state.get_score()}/50 States Correct",
        prompt="What's another State Name?"
    )
    
    # Check if user cancels the input dialog
    if answer_state is None or  answer_state.lower() == "exit":
        new_data = pd.DataFrame(state.remaining_states(),columns=["State"])
        new_data.to_csv(csv_path, index=False)
        break
    
    answer_state = answer_state.title()
    # print(answer_state)
    
    state.check_user_guess(user_input=answer_state)
    state.get_coordinates()
    state.update_state()

# screen.mainloop()
