from Cdata import MENU, resources

user_choice = ""
cost = 0

def choice():
    while True:
        global user_choice
        user_choice = input("What would you like? (Espresso/latte/cappuccino)\n").lower()
        
        if user_choice in MENU:
            break
        
        else:
            print("Please choose from: espresso/latte/cappuccini")
    return user_choice


def resource_check():
    global cost
    enough_resources = True
    
    w_res = resources.get("water")
    m_res = resources.get("milk")
    c_res = resources.get("coffee")

    cost = MENU[user_choice].get("cost")

    
    Rwater = MENU[user_choice].get("ingredients")["water"]
    Rmilk = MENU[user_choice].get("ingredients")["milk"]
    Rcoffee = MENU[user_choice].get("ingredients")["coffee"]

    
    if Rwater <= w_res and Rmilk <= m_res and Rcoffee <= c_res: 
        enough_resources = True 
    else: 
        enough_resources = False

      
    if enough_resources == False:
        print("Insufficient Resources available")
        return False   
    else:
        return True

def pay():
    pounds = float(input("How many pound coins do you insert?: £"))
    pence = float(input("How many pennies do you insert: "))
    total_payed = round(pounds + (pence / 100), 2)
    
    if total_payed >= cost:
        print(f"{user_choice} dispensed. Enjoy your drink!")
        print(f"Your change is: {round(total_payed - cost, 2)}")
    
    elif total_payed < cost:
        print("Youd didn't insert enough momey. You have been refunded")
    
   
while True:
    choice()

    if resource_check() == True:
        print(f"The cost is £{cost}")
        pay()
        
    else:
        print("Insufficient Resources available. No charge")
        break

      