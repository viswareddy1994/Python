import random

# ASCII art for rock, paper, and scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Create a list of options for the user and computer choices
list_options = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors!")

# Generate a random index for the computer's choice
computer_index = random.randint(0, len(list_options) - 1)
computer_choice = list_options[computer_index]

# Get the user's choice
user_index = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

# Validate user input
if user_index < 0 or user_index > 2:
    print("Invalid number. You lose!")
else:
    user_choice = list_options[user_index]
    print(f"You chose:\n{user_choice}")
    print(f"Computer chose:\n{computer_choice}")

    # Determine the winner based on the choices made
    if user_index == computer_index:
        print("It's a draw!")
    elif (user_index == 0 and computer_index == 2) or (user_index == 1 and computer_index == 0) or (user_index == 2 and computer_index == 1):
        print("You win!")
    else:
        print("You lose!")
