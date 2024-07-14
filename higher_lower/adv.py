import random
from game_data import data

def get_random_index():
    """Return a random index from the data list."""
    return random.randint(0, len(data) - 1)

def get_person_info(index):
    """Return formatted string with person's information."""
    person = data[index]
    return f"{person['name']}, {person['description']}, from {person['country']}"

def get_follower_count(index):
    """Return the follower count of the person at the given index."""
    return data[index]['follower_count']

def compare_follower_counts(count_a, count_b):
    """Return 'a' if count_a is higher, else 'b'."""
    return 'a' if count_a > count_b else 'b'

def prompt_user_guess():
    """Prompt the user to guess which person has more followers."""
    while True:
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if guess in ['a', 'b']:
            return guess
        else:
            print("Invalid input. Please type 'A' or 'B'.")

def play_round():
    """Play a single round of the game."""
    score = 0
    continue_game = True

    while continue_game:
        index_a = get_random_index()
        index_b = get_random_index()
        
        while index_a == index_b:
            index_b = get_random_index()

        print(f"Compare A: {get_person_info(index_a)}\n")
        print(f"Against B: {get_person_info(index_b)}\n")
        
        count_a = get_follower_count(index_a)
        count_b = get_follower_count(index_b)
        correct_answer = compare_follower_counts(count_a, count_b)
        user_guess = prompt_user_guess()
        
        if user_guess == correct_answer:
            score += 1
            print(f"You're right! Current score: {score}\n")
        else:
            print(f"Sorry! That's wrong. Final score: {score}\n")
            continue_game = False

def main():
    """Main function to handle game replay logic."""
    while True:
        play_round()
        replay = input("Do you want to play another game? Type 'yes' or 'no': ").lower()
        if replay != 'yes':
            print("Thank you for playing!")
            break
        print()

main()
