import math

first = float(input("Enter your first number: "))
operation = input("* / - + Pick an operation: ")
second = float(input("Enter your second number: "))
valid = ["yes", "no"]

def answer(first, operation ,second):
    if operation == "*":
        return first * second
    
    elif operation == '/':
        return first / second
    
    elif operation == '+':
        return first + second
    
    elif operation == '-':
        return first - second

def carry_on():
    while True:
        play_on = input(f"Would you like to carry on with the number {new_answer}? yes or no\n").lower()
        
        try:
            if play_on in valid:
                break
            
        except ValueError:
            print("Please pick yes or no. ")
    return play_on

playing = True
while playing:
    new_answer = answer(first, operation, second)
    print(new_answer)
    
    while carry_on() == "yes":
        first = new_answer
        operation = input("*\n/\n-\n+\nPick an operation: ")
        second = float(input("Enter a number: "))
        new_answer = answer(first, operation, second)
        print(new_answer)

    playing = False