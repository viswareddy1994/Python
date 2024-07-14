import random
from art import logo
# Constants
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def guess_random_num():
    """Generates a random number between 1 and 100."""
    return random.randint(1, 100)

def get_user_guess():
    """Prompts the user to make a guess and ensures valid input."""
    while True:
        try:
            guess = int(input("Make a guess: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")

def guessing_num(attempts, correct_number):
    """Handles the guessing logic and user interaction."""
    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining to guess the number.")
        user_guess = get_user_guess()
        
        if user_guess > correct_number:
            print("Too high.")
        elif user_guess < correct_number:
            print("Too low.")
        else:
            print(f"Congratulations! You got it! The answer was {correct_number}.")
            return True  # User guessed correctly
        
        attempts -= 1
        if attempts == 0:
            print(f"\nYou have run out of guesses. The correct number was {correct_number}. You lose.")
            return False  # User ran out of attempts

def choose_difficulty():
    """Prompts the user to choose a difficulty level and returns the corresponding number of attempts."""
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if level == 'easy':
            return EASY_ATTEMPTS
        elif level == 'hard':
            return HARD_ATTEMPTS
        else:
            print("Invalid input. Please type 'easy' or 'hard'.")

def play_game():
    """Sets up and runs a single game session."""
    print(logo)
    print("\nWelcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    correct_answer = guess_random_num()
    
    attempts = choose_difficulty()
    guessing_num(attempts, correct_answer)

def main():
    """Main game loop allowing the user to play multiple games."""
    while True:
        play_game()
        
        play_again = input("\nDo you want to play again? Type 'yes' or 'no': ").lower()
        if play_again != 'yes':
            break
    
    print("Thank you for playing! Goodbye!")

if __name__ == "__main__":
    main()
