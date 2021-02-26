import random
# Winning variables
won = 'You won!'
lost = 'You lost!'
draw = 'Draw'

# check that input was valid variables 
valid = ['rock', 'paper', 'scissors']

# AI picking from valid at random
ai = random.randint(0, 2)
ai_pick = valid[ai]

# Getting user input for rock,paper, scissors and making sure its a valid choice
while True:
    choice = input('What do you want to choose? rock, paper or scissors  ').lower()
    try:
        if choice in valid:
            break
    except TypeError:
        print('Please enter: rock, paper or scissors')

print(f"You chose: {choice}\n")
print(f"AI chose: {ai_pick}\n")

# Win/Lost/Draw conditions
if choice == 'rock':
    if ai_pick == 'rock':
        print(draw)
        
    elif ai_pick == 'paper':
        print(lost)
        
    elif ai_pick == 'scissors':
        print(won)
        
elif choice == 'paper':
    if ai_pick == 'rock':
        print(won)
        
    elif ai_pick == 'paper':
        print(draw)
        
    elif ai_pick == 'scissors':
        print(lost)

elif choice == 'scissors':
    if ai_pick == 'rock':
        print(lost)
        
    elif ai_pick == 'paper':
        print(won)
        
    elif ai_pick == 'scissors':
        print(draw)