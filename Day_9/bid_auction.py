import art

auction_dict = {}
another_bidder = False
print(art.logo)
while not another_bidder:
    print("Welcome to secret auction program!")
    name = input("Enter your name:")
    bid_amt = int(input("What's your bid?:"))
    auction_dict[name] = bid_amt
    another_bid = input("Do we have any other bidder? 'yes' or 'no'")
    if another_bid == 'no':
        another_bidder = True
highest_bid = 0
highest_bidder = ''
for bidder in auction_dict:
    if auction_dict[bidder] > highest_bid:
        highest_bid = auction_dict[bidder]
        highest_bidder = bidder
print(f"The highest bid is won by :{highest_bidder} and the highest bid is:{highest_bid}")
