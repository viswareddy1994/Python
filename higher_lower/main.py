from game_data import data
from art import logo,vs
import random

def choice():
    index = index = random.randint(0,len(data)-1)
    return index

def player_info(ind):
    name = data[ind]['name']
    profession = data[ind]['description']
    place = data[ind]['country']
    return f"{name}, {profession}, from {place}"

def followers_count(index):
    count = data[index]['follower_count']
    return count

def highest_follower(cnt_a,cnt_b):
    if cnt_a >cnt_b:
        return cnt_a
    else:
        return cnt_b
def user_guess(cnt_a,cnt_b):
    users_choice = input("Who has more follower's Type A or B: ").lower()
    if users_choice == 'a':
        return cnt_a
    else:
        return cnt_b
def validate(correct_ans,player_ans):
    if correct_ans == player_ans:
        return True   
    else:
        return False


def play_game():
    print(logo)
    cnt =0
    should_continue = True
    ind_b= choice()
    while should_continue:
        ind_a = ind_b
        ind_b =choice()
        while ind_a == ind_b:
            ind_b = choice()
        choice_a = player_info(ind_a)
        choice_b = player_info(ind_b)
        print(f"\nCompare A: {choice_a}")
        print(vs)
        print(f"Against B: {choice_b}\n")
        choice_a_cnt = followers_count(ind_a)
        choice_b_cnt = followers_count(ind_b)
        answer = highest_follower(choice_a_cnt,choice_b_cnt)
        player_guess = user_guess(choice_a_cnt,choice_b_cnt)
        valid = validate(answer,player_guess)
        if valid:
            cnt+=1
            print(f"\nYou're Right! Current score; {cnt}\n")
        else:
            print(f"\nSorry! that's wrong. Final score: {cnt}\n")
            should_continue = False

def main():
    while True:
        play_game()
        replay = input("Do you want to play another game? Type 'yes' or 'no': ").lower()
        if replay!= 'yes':
            print("Thank you for Playing!! Bye\n")
            break
main()