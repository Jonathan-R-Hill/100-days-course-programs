import random

score = 0

higher_lower = ["higher", "lower"]
valid = ["yes", "no"]

numbers = []
for i in range(30):
    numbers.append(int(i))

def play():
    global score
    global numbers
    
    number = random.choice(numbers)
    
    while True:
        
        print(f"The number is {number}")
        new_num = random.choice(numbers)
        
        while True:
            guess = input("Higher or Lower?\n")
            
            if guess in higher_lower:
                break
            elif guess not in higher_lower:
                print("please enter: higher or lower")
        
        if guess == "higher" and new_num > number or guess == "lower" and new_num < number:
            score += 1
            number = new_num
            print("That was correct.")
            
        else:
            print(f"That was wrong. Your final score was: {score}")
            return False
        

def play_again():
    while True:
        yes_no = input("Would you like to play? yes or no\n")
        
        if yes_no in valid:
            
            if yes_no == "yes":
                return True
            else:
                return False
            
        else:
            print("Please Enter yes or no.")

while play_again():
    score = 0
    play()
    