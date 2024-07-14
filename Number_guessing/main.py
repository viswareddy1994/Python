import random
from art import logo
def guess_random_num():
    return random.choice(range(1, 101))
    #random.randint(1,100) -- this one also works

def guessing_num(attempts, correct_number):
    for _ in range(attempts):
        print(f"You have {attempts} attempts remaining to guess the number")
        user_guess = int(input("Make a guess: "))
        if user_guess > correct_number:
            print("Too High")
        elif user_guess < correct_number:
            print("Too Low")
        else:
            print(f"You got it! The answer was {correct_number}")
            return
        attempts -= 1
        if attempts == 0:
            print("You have run out of guesses. You lose.")
            return
        else:
            print("Guess again.")
should_continue = True
while should_continue:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 to 100")
    correct_answer = guess_random_num()
    print(f"Pssst, the correct answer is: {correct_answer}")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        guesses = 10
    else:
        guesses = 5
    guessing_num(attempts=guesses, correct_number=correct_answer)
    play_again = input("Want to Play New game again, Type Y or N: ").lower()
    if play_again == 'n':
        should_continue = False
        
print("Thank you for playing! Goodbye!")