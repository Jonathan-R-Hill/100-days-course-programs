height = input('Enter your height in cm: ')

ticket_adult = 10
ticket_adult_pic = 13

ticket_child = 5
ticket_child_pic = 8

if int(height) >= 120:
    age = input('How old are you? \n')
    if int(age) >= 18:
        choice = input('Would you like a picture included with your ticket? yes or no \n')
        if choice.lower() == 'yes':
            print(f"The cost of your ticket is: £{ticket_adult_pic}")
        else:
            print(f"The cost of your ticket is: £{ticket_adult}")
    else:
        choice = input('Would you like a picture included with your ticket? \n')
        if choice.lower() == 'yes':
            print(f"The cost of your ticket is: £{ticket_child_pic}")
        else:
            print(f"The cost of your ticket is: £{ticket_child}")
else:
    print("You're not tall enough to ride the roller coaster. Sorry.")
