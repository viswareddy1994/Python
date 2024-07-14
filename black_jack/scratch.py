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


# start = input("Do you want to Play a game of Blackjack? Type 'Y' or 'N': ").lower()

# if start == 'n':
#     None
# else:
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []


def black_jack():
    should_continue = True
    def deal():
            for card in cards:
                if len(player_cards)<2 and len(computer_cards)<2:
                    card = random.choice(cards)
                    player_cards.append(card)
                    card = random.choice(cards)
                    computer_cards.append(card)
            print(f"player1 cards: {player_cards}, Your current score is {sum(player_cards)}. ")
            print(f"Dealer first card: {computer_cards[0]} ")
    deal()
    def hit():
            pick= input("Type 'Y' to get another card, Type 'N' to Stand: ").lower()
            if pick =='y':
                player_cards.append(random.choice(cards))
                return 'Yes'
            else:
                return 'No' 
             

    while should_continue:
        if sum(player_cards)==21:
            print(f"Congratulations,  Its BLACK JACK YOU WON!!!")
            should_continue = False
            result = 'No'
        elif sum(player_cards)<21:    
            result = hit()
            if result =='Yes':
                if sum(player_cards)>21:
                    print(f"Its BURST!, You Lost. Your score is {sum(player_cards)}")
                else:
                    print(f"player1 cards: {player_cards}, Your current score is {sum(player_cards)}. ")
                    hit()

            if result == 'No':
                should_continue = False
                print(f"Your Final cards: {player_cards}, and Your Final Score is {sum(player_cards)}")
        else:
            print(f"You Lost! Your final Score is {sum(player_cards)}")
            should_continue = False
        if sum(player_cards) == 22 or sum(player_cards)>21 or result =='No':
            next_game = input("Do you want to play another game type 'Y', or 'N': ").lower()
            if next_game == 'y':
                player_cards.clear()
                computer_cards.clear()
                should_continue = False
                black_jack()
            else:
                should_continue = False
                print("Good Bye!")
    
black_jack()

    
        
        