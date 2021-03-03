# Variables fo checks and bill
bill = 0
valid = ['yes', 'no']

# Checking to make sure their height is enough to go on the ride with valid input (number)
while True:
        try:
            height = int(input('Enter your height in cm: \n'))
        except ValueError:
            print("Sorry please enter a number")
            continue
        else:
            break

# Basic check to see if they're tall enough to go on the ride
if height >= 120:
    # Checking their age to determain how much their ticket (bill) will cost and that the age entered is a number assuming they are over 120cm
    while True:
        try:
            age = int(input('How old are you? \n'))
        except ValueError:
            print("Sorry please enter a number")
            continue
        else:
            break
        
    # Setting the bill based off their age
    if age >= 18:
        bill = 10
        print(f'Adult tickets cost £{bill}')
    elif age >= 12:
        bill = 7
        print(f'Youth tickets cost £{bill}')
    elif age < 12:
        bill = 5
        print(f'Child tickets cost £{bill}')
    
    # Checking to see if they want a picture and the input is either yes or no
    while True:    
        want_pic = input('Do you want a picture taken? they cost £3 extra yes or no \n')
        if want_pic in valid: # Valid is in stored variables for checking the input was valid
            break
        else:
            print('Please enter: yes or no')
            
    # If they want a picture adding 3 to the bill based off their age and changing input to lower case
    if want_pic.lower() == 'yes':
        bill += 3
    
    # This prints the final cost of the ticket either with the ticket if they said yes or just the base price based off their age if they said no
    print(f"Your ticket price is: £{bill}") 

# This runs if they're not at or above 120cm in height  
else:
    print("Sorry, you're not tall enough to go on the ride")