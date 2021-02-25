import random

# Stored Variables
words = ["ardvark", "baboon", "camel", "dog"]
len_words = len(words)

valid = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
         'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
         's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

lives = 10
user_guesses = []

# Picks a random world from the list
chosen_word = random.choice(words)
len_chosen_word = len(chosen_word)

# Creating the display of empty spaces
display = []

for letter in chosen_word:
    display += '_'

print(display)


while lives > 0 and '_' in display:
    
    # Checks input is valid and hasn't already been guessed
    while True:
        guess = input('Guess a letter:  ').lower()
        
        try:
            if guess in valid and not user_guesses:
                break
        except TypeError:
            print("please enter a letter that you haven't guessed already")

    # checks to see if the input is in the word and enters it if it is. if not it takes 1 life away
    for i in range(0, len_chosen_word):
        if chosen_word[i] == guess:
            display[i] = guess
            
        elif lives >= 1 and guess not in chosen_word:
            print(f"You're guess: ({guess}) was wrong. you lost a life")
            lives -= 1
            break
        elif lives == 0:
            print("You're out of lives")
            break
    print(f'{lives} lives remaining') 
    
    print(display)
    
    # win/loss conditions 
    if '_' not in display and lives > 0:
        print("You've won!")
        break
           
    if lives == 0:
        print("You're out of lives")
        print(f"you lost. The word was: {chosen_word}")
        break
