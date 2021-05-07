from turtle import Turtle, Screen, bgcolor
from random import choice
John = Turtle()

John.shape("turtle")
screen = Screen()
screen.bgcolor("black")

colours = ["red", "blue", "yellow", "orange", 
           "grey", "pink", "purple", 
           "green", "cyan", "AliceBlue", 
           "chocolate", "brown", "cornsilk", "DarkOrange"]

# Square
"""
for _ range(4):
    john.forward(100)
    john.right(90)
    i += 1
"""

# Sqaure Dashed Lines and solid lines
"""
i = 0
while i < 4:
    for _ in range(10):
        John.forward(10)
        John.pendown()
        John.forward(10)
        John.penup()
    
    for _ in range(10):
        John.pendown()
        John.forward(10)
            
    John.right(90)
    i += 1
"""
def draw_shape(num_sides):
    angle = 360 / num_sides
    John.color(choice(colours))
    
    # Multiple shapes
    for _ in range(num_sides):
        John.forward(100)
        John.right(angle)
    

for i in range(3, 11):
    draw_shape(i)
    

screen.exitonclick()