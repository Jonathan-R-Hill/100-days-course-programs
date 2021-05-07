from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.shape("circle")
        self.setheading(randint(35, 320))
    
    def move(self):
        self.forward(3)
        
    def hit_wall(self):
        old_head = self.heading()
        self.setheading(-old_head)
    
    def paddle_bounce(self):
        old_head = self.heading()
        self.setheading(old_head + randint(170, 200))
    
    def reset_ball(self):
        self.goto(0, randint(-250, 250))
        self.setheading(randint(35, 320))
            