valid = ['encode', 'decode']
valid1 = ['yes', 'no']

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']*10

def encode(message, shift):
    encrypted_message = ''
    
    for letter in message:       
        if letter not in letters:
            encrypted_message += letter 
              
        elif letter in letters:
            x = letters.index(letter)
            letter = letters[x + shift]
            encrypted_message += letter
        
            
    print(f"here is your encoded message\n{encrypted_message}")
                

def decode(message, shift):
    decrypted_message = ''
    
    for letter in message:           
        if letter not in letters:
            decrypted_message += letter
            
        elif letter in letters:
            x = letters.index(letter)
            letter = letters[x - shift + 26]
            decrypted_message += letter
            
    print(f"here is your decoded message\n{decrypted_message}")

# Loops through the game untill carry_on is False
carry_on = True
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