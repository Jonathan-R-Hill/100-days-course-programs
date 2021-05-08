from turtle import Turtle


start = (0, -280)

class player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(0.5, 0.5)    # 10 x 10
        self.setheading(90)
        self.penup()
        self.goto(start)
    
    def reset(self):
        self.goto(start)
    
    def up(self):
       self.forward(10)
    
    def down(self):
        self.backward(10)
    
