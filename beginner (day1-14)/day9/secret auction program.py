import os
from art import logo
print(logo)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

bids = {}
bidding_finished = False

print("Welcome to the Secret Auction Program.")

def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name? : ")
    bid = int(input("What's your bid?: $"))

    bids[name] = bid

    other = input("Are there any other bidders? Type 'yes' or 'no': ")

    if other == "no":
        bidding_finished = True
        find_highest_bid(bids)

    elif other == "yes":
        clear()