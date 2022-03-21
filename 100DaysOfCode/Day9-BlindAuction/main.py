from art import logo
import os

print(logo)
auction_dict = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?")
    bid = int(input("How much are you willing to bid? $"))
    auction_dict[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(auction_dict)
    elif should_continue == "yes":
        os.system('clear')
