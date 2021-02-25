print('Welcome to the love calculator!')

true = ['t', 'r', 'u', 'e']
love = ['l', 'o', 'v', 'e']

true_score = 0
love_score = 0
# Getting names as input
name1 = input('What is your name?\n').lower()
name2 = input('What is their name?\n').lower()

# Putting the names in the same string
names = name1 + name2

# Loops through the names and adds to the score if a valid letter occurs
for i in range(len(names)):
    if names[i] in true:
        true_score += 1
        
    if names[i] in love:
        love_score += 1
    
score = int(str(true_score) + str(love_score))

# Checks your score and tells you the message based off score
if score > 90 or score < 10:
    print(f'Your score is {score}, you go togeather like mentos and coke.')

elif 50 < score < 90:
    print(f"Your score is {score}, you're alright togeather.")

elif score < 50:
    print(f"Your score is {score}, I wouldn't suggest it!")

