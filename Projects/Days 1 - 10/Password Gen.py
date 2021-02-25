import random

# Stored Variables 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# Getting input from user
num_letters = int(input("How many letters would you like in your password?\n")) 
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))

# creating list and getting random letters/numbers/symbols from variables above
pw_list = []
for _ in range(num_letters):
    pw_list.append(letters[random.randint(0, len(letters)-1)])

for _ in range(num_numbers):
    pw_list.append(numbers[random.randint(0, len(numbers)-1)])
    
for _ in range(num_symbols):
    pw_list.append(symbols[random.randint(0, len(symbols)-1)])

# Shuffles lsit into a random order
random.shuffle(pw_list)

# Making the list into a string
password = ''.join(pw_list)

print(password)