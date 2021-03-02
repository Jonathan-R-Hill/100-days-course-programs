bids = {}
valid = ['yes', 'no']

winner_name = ""
winner_bid = 0.0

print("Welcome to the secret auction!")

def add():
    name = input("Enter your name: ")
    bid = float(input("Enter your bid: "))
    
    bids[name] = bid


def others():
    while True:
        people = input("Is there anyon else bidding? yes or no \n").lower()

        try:
            if people in valid:
                break
            
        except ValueError:
            print("Please enter: yes or no")
    return people

while True:
    add()

    while others() == "yes":
        add()
            
    else:
        break

for key in bids:
    print(key, bids[key])
    if bids[key] > winner_bid:
        winner_name = key
        winner_bid = bids[key]
    
print(f"The winner is: {winner_name} with a bid of {winner_bid}")
