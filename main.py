# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo

print(logo)
over = False
bids = {}
while over == False:
    name = str(input("What is your name: "))
    price = int(input("What is your bid: £"))
    bids[name] = price
    more = input("Is there another bidder. Type 'y' or 'n'.").lower()
    if more == "y":
        print("\n" * 20)
        over = False
    elif more == "n":
        over = True
        print("Thank you for bidding!")
        highest = max(bids, key = bids.get)
        print(f"{highest} won with a bid of £{bids[highest]}")
