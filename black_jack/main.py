############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Take list of cards and calculate score"""
    if sum(cards) == 21 and len(cards) ==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(player_score,dealer_score):
    if player_score > 21:
        return "\nYou went over. You lose 😭"
    elif dealer_score > 21:
        return "\nDealer went over. You win 😁"
    elif player_score == dealer_score:
        return "\nDraw 🙃"
    elif player_score == 0:
        return "\nWin with a Blackjack 😎"
    elif dealer_score == 0:
        return "\nLose, opponent has Blackjack 😱"
    elif player_score > dealer_score:
        return "\nYou win 😃"
    else:
        return "\nYou lose 😤"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards} , current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}\n")

        if user_score ==0 or computer_score == 0 or user_score>21:
            is_game_over = True
        else:
            user_should_deal = input("Type Y to get another card otherwise type N to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score !=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    final_result = compare(player_score=user_score,dealer_score=computer_score)
    print(final_result)
    print(f"Your final cards: {user_cards} , final score: {user_score}")
    print(f"Computer's final cards: {computer_cards}, final score: {computer_score}\n")
    
        
while input("\nDo you want to play a game of Blackjack? Type Y or N : ").lower() == 'y':
    play_game()
#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

    
    
    
    
    
    
    
    
