import random

print("welcome to heads or tail's! ")

one = 'heads'
two = 'tails'

valid = ['heads', 'tails']

while True:
    user = input('Enter heads or tails \n').lower()
    try:
        if user in valid:
            break
    except ValueError:
        print('Enter Heads or tails')

rand = random.randint(1, 2)

if rand == 1:
    if user == one:
        print(f'The coin flipped {one}. You won!')
    else:
        print(f"The coin flipped {one}. You lost.")
        
elif rand == 2:
    if user == two:
        print(f'The coin flipped {two}. You won!')
    else:
        print(f"The coin flipped {two}. You lost.")