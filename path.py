
import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Define the relative path to the image
image_path = os.path.join(script_dir, "blank_states_img.gif")
print(image_path)



# Get the current working directory
script_dir = os.getcwd()

# Define the relative path to the image within the images folder
image_path = os.path.join(script_dir,  "blank_states_img.gif")

# Print the full path to the image
print(image_path)
