# Creating Bill variable to change based off choice
bill = 0

# Costs of Pizza items/Sizes
small = 10
medium = 15
large = 20

pep_cost = 2
cheese_cost = 1

# Variables for checking for valid input
yes_no = ['YES', 'NO']
valid_size = ['SMALL', 'MEDIUM', 'LARGE']

# Welcome Messages
print('Welcome to the Pizza shop!')
print(f"A Small Pizza costs: £{small}, a Medium Pizza costs: £{medium} and a Large Pizza costs: £{large}.")

# Getting choice of Size and checking for valid input
while True:
    size = input('What size Pizza do you want? Please enter: SMALL  MEDIUM  LARGE \n').upper()
    try:
        if size in valid_size:
            break
    except ValueError:
        print('Please pick from the following:  SMALL  MEDIUM  LARGE')
     
# Setting price of the Pizza based off the size chosen
if size == 'SMALL':
    bill = small
    
elif size == 'MEDIUM':
    bill = medium
    
elif size == 'LARGE':
    bill = large

print(f"You've picked a {size.lower()} Pizza and will cost £{bill}.")

# Asking if they want pepperoni on the Pizza and checking for valid input
while True:
    pepperoni = input('Would you like pepperoni on your Pizza for an extra £2? yes or no\n').upper()
    try:
        if pepperoni in yes_no:
            break
        
    except ValueError:
        print('Please enter: yes or no')
        
# If they chose yes this adds pepperoni to the cost
if pepperoni == 'YES':
    bill += pep_cost

# Asking if they want cheese on the Pizza and checking for valid input
while True:
    cheese = input('Would you like cheese on your Pizza for an extra £1? yes or no\n').upper()
    try:
        if cheese in yes_no:
            break
        
    except ValueError:
        print('Please enter: yes or no')
        
# If they chose yes this adds cheese to the cost
if cheese == 'YES':
    bill += cheese_cost

print(f"The cost of your Pizza is: £{bill}.\nThank you for shopping with us!")