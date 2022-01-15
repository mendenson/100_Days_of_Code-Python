from art import logo, gavel, win

auction = {}

def play():
    
    auction_continue = True
    while auction_continue:
        # SHow logo from art.py
        print("\n")
        print(logo)
        print(gavel)
        # Ask for Name Input
        name = input("\nWhat's is your name?: ")
        # Ask for Bid Price
        bid = int(input("\nWhat's your bid?: $"))
        # Add Name and Bid into a disctionary as the key and value
        auction[name] = bid
        
        should_continue = input("\nAre there any other bidders? Type 'yes' or 'no'\n").lower()
        if should_continue == "no":
            auction_continue = False
            hiddest_bidder(auction)
        else:
            print("\033c", end='')


# Looking for a auction winner
def hiddest_bidder(bidding_record):
    hightest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > hightest_bid:
            hightest_bid = bid_amount
            winner = bidder
    print(win)
    print(f"The winner is {winner} with a bid of ${hightest_bid}.\n")

    

if __name__ == "__main__":
    play()