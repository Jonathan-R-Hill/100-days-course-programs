logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
     """

valid = ['encode', 'decode']
valid1 = ['yes', 'no']

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(message, shift):
    encrypted_message = ''
    
    for letter in message:       
        if letter not in letters:
            encrypted_message += letter 
              
        elif letter in letters:
            x = letters.index(letter)
            letter = letters[(x + shift) % 26]
            encrypted_message += letter
        
            
    print(f"here is your encoded message\n{encrypted_message}")
                

def decode(message, shift):
    decrypted_message = ''
    
    for letter in message:           
        if letter not in letters:
            decrypted_message += letter
            
        elif letter in letters:
            x = letters.index(letter)
            letter = letters[(x - shift) % 26]
            decrypted_message += letter
            
    print(f"here is your decoded message\n{decrypted_message}")

# Loops through the game untill carry_on is False
carry_on = True
print(logo)
while carry_on == True:
# Checks for valid input (encode / decode) if not valid it will ask again
    while True:
        play = input("Type 'encode' to encrypt or type 'decode' to decrypt \n").lower()
        try:
            if play in valid:
                break
        except TypeError:
            print("Please enter either: 'encode' or 'decode'")

    message = input("Enter your message here\n").lower()
    shift = int(input("Enter the shift number: "))

    if play == 'encode':
        encode(message, shift)
        
    elif play == 'decode':
        decode(message, shift)
    
    # Checks whether input is valid. Sets condition of while loop depending on the answer given
    while True:
        play_again = input("Would you like to play again? yes or no\n").lower()
        try:
            if play_again in valid1:
                break
        except TypeError:
            print("Please enter: yes or no")
            
    if play_again == 'yes':
        carry_on = True
        
    elif play_again == 'no':
        carry_on = False