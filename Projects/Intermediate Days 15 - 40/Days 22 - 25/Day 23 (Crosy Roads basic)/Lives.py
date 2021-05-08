from turtle import Turtle

font = ["Arial", 16, "italic"]
align = "center"

class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.Lives = 3
        self.color("green")
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.write(arg = f"Lives: {self.Lives}", font = font, align = align)
        
    def die(self):
        self.Lives -= 1
        self.clear()
        self.write(arg = f"Lives: {self.Lives}", font = font, align = align)
    
    def gain(self):
        self.Lives += 1
        self.clear()
        self.write(arg = f"Lives: {self.Lives}", font = font, align = align)