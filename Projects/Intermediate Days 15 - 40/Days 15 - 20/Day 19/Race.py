from turtle import Turtle, Screen
from random import randint

# Storage for Variables and Turtles 
winner = False
race_on = False

colours = ["red", "orange", "yellow", "green", "blue", "purple", "green", "black", "grey"]
turtles = []

# Screen setup
screen = Screen()
screen.setup(width = 500, height = 500) 

# Setting position and index for getting a colour from the list
x = -230
y = -200
col = 0

for i in colours:
    i = Turtle(shape = "turtle")
    i.color(colours[col])   # assigning a new turle as name from colours
    col += 1    # Changing idex for colours
    i.penup()
    i.goto(x, y)    # sets position 
    y += 50     # sets each turle on a different y axis by increasing it each time its looped
    turtles.append(i)   # adds the new turle to the list of turtles 


user_bet = screen.textinput(title = "Place your bet", prompt = "Which turtle will win the race? Enter a colour: ")
print(f"You bet on {user_bet} to win.")

if user_bet:
    race_on = True

while race_on:

    for turtle in turtles:
        
        if turtle.xcor() > 230:
            winner = True
            break
        
        turtle.forward(randint(2, 16))
        
    if winner:
        print(f"\n{turtle.pencolor()} won the race!\n")
        break

