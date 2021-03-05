from Cdata import MENU, resources

user_choice = ""
cost = 0
w_res = resources.get("water")
m_res = resources.get("milk")
c_res = resources.get("coffee")
Rwater = 0
Rmilk = 0
Rcoffee = 0

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
    global w_res
    global m_res
    global c_res
    global Rwater 
    global Rmilk
    global Rcoffee
    
    cost = MENU[user_choice].get("cost")

    Rwater = MENU[user_choice].get("ingredients")["water"]
    Rmilk = MENU[user_choice].get("ingredients")["milk"]
    Rcoffee = MENU[user_choice].get("ingredients")["coffee"]
    
    if Rwater <= w_res and Rmilk <= m_res and Rcoffee <= c_res: 
        return True
    else:
        return False  
    

def pay():
    global cost
    global w_res
    global m_res
    global c_res

    
    pounds = float(input("How many pound coins do you insert?: £"))
    pence = float(input("How many pennies do you insert: "))
    total_payed = round(pounds + (pence / 100), 2)
    
    if total_payed >= cost:
        print(f"{user_choice} dispensed. Enjoy your drink!")
        print(f"Your change is: {round(total_payed - cost, 2)}")
        w_res -= Rwater 
        m_res -= Rmilk
        c_res -= Rcoffee

    elif total_payed < cost:
        print("Youd didn't insert enough momey. You have been refunded")
    
   
while True:
    choice()

    if resource_check() == True:
        print(f"The cost is £{cost}")
        pay()
        
    else:
        print("Insufficient Resources available. No charge")
        

      