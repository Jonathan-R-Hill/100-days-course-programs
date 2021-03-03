import random

player_cards = []
ai_cards = []

valid = ["yes", "no"]
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
hit_hold = ["hit", "hold"]


def play():
    
    play = input("Would you like to play a game of Blackjack? ").lower()
    
    while True:
        try:
            if play in valid:
                break
        except TypeError:
            print("Please pice from: yes / no")
    
    return play


def deal():
    for i in range(2):
        player_cards.append( random.choice(cards) )
    
    for i in range(2):
        ai_cards.append( random.choice(cards) )
    


def another_card():
    while True:
        another = input("Would you like to hit or hold?\n").lower()
        
        if another in hit_hold:
            break
        elif another not in hit_hold:
            print("Please enter: hit or hold")
            
            
    if another == "hit":
        return True
        
    else:
        return False


def clear_hand():
    for i in range(len(player_cards)):
        player_cards.pop()
    
    for i in range(len(ai_cards)):
        ai_cards.pop()   


def ai_turn():
    tot = 0
    for i in ai_cards:
        tot += i
    while tot < 15:
        if tot > 15:
            break
        else:
            card = ( random.choice(cards) )
            ai_cards.append(card)
            tot += card

def winner():
    player_total = 0
    for i in player_cards:
        player_total += i
    print(f"Your total is: {player_total}")
    
    ai_total = 0
    for i in ai_cards:
        ai_total += i
    print(f"The AI's total is: {ai_total}")
    
    if player_total > 21:
        print("You Lost")
        
    elif player_total > ai_total or ai_total > 21:
        print("You Won!")
        
    elif player_total < ai_total:
        print("You Lost!")

while True:
    deal()
    print(player_cards, ai_cards)

    while True:
        if another_card() == True:
            player_cards.append( random.choice(cards) )
            print(player_cards)
            
        else:
            break

    ai_turn()
    winner()
    clear_hand()
    
    if play() == "yes":
        print("Let's play again!")
    else:
        break
    