from art import logo
print(logo)
print("Welcome to Secret Auction Programm")
bidders_info_dict = {}

def add_bidders (name,amount):
    bidders_info_dict[name] = amount
def auction_winner(dict):
    highest_bid = 0
    for name, amt in dict.items():
        if amt > highest_bid:
            highest_bid = amt
            winner = name
    return f"Winner is {winner} with bid amount $ {highest_bid} "
            
additional_bidders = True

while additional_bidders:
    bidder_name = input("Enter the name of Bidder: \n")
    bid_amount = int(input("What's your bid $ ? : \n"))
    add_bidders(name=bidder_name,amount=bid_amount)
    other_bidders = input("Are there additional buidders ? Type 'Yes' or 'No'. ").lower()
    if other_bidders == 'no':
        additional_bidders = False
result = auction_winner(dict=bidders_info_dict)
print(result)