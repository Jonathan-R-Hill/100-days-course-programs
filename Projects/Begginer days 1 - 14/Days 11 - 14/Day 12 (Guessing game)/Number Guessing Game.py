import random

valid = ["hard", "easy"]
valid1 = ["yes", "no"]

lives = 5

nums = []
for i in range(1, 101):
    nums.append(int(i))


def play():
    global lives
    print(f"You have {lives} lives")
    while True:
        while True:
            guess = int(input("Guess a number: "))
            
            if guess in nums:
                break
            elif guess not in nums:
                print("Enter a number between 1 and 100.")



        if guess != random_num and lives > 0:
            print(f"Your guess of {guess} was incorrect. You have {lives} Lives Remaining")

            if guess > random_num:
                print("You guessed too high!")
            else:
                print("Your guess was too low")
            lives -= 1
            
        elif lives == 0:
            print(f"You lost! The number was {random_num}")
            break
        
        elif guess == random_num:
            print("You have Won!")
            break
            

def play_again():
    while True:
        yes_no = input("Would you like to play? yes or no\n")
        
        if yes_no in valid1:
            
            if yes_no == "yes":
                return True
            else:
                return False
            
        else:
            print("Please Enter yes or no.")

while play_again():
    print("I'm thinking of a number between 1 and 100")
    random_num = random.choice(nums)
    play()
    lives = 5
    