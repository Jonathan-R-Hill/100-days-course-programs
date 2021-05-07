from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid = 4, stretch_len = 1)
        self.goto(pos_x, pos_y)
    
    def Up(self):
        new_y = self.ycor() + 25
        self.goto(self.xcor(), new_y)
        
    def Down(self):
        new_y = self.ycor() - 25
        self.goto(self.xcor() , new_y)
        
