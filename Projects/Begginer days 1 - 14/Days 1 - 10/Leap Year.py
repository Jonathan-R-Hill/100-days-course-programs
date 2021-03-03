year = input('Enter a year: \n')

num = int(year)

if num % 4 == 0:
    if num % 100 != 0:
        print("It's a leap year!")
    elif num % 400 == 0:
        print("It's a leap year!")
    else:
        print("It's not a leap year.")
else:
    print("It's not a leap year.")