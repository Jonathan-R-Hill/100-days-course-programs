from turtle import Turtle

alignment = "center"
FONT = ("Courier", 20, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.setposition(0, 270)
        self.write(arg = f"{self.p1_score}   |   {self.p2_score}", move = False, align = alignment, font = FONT)
    
    def update_one(self):
        self.p1_score += 1
        self.clear()
        self.write(arg = f"{self.p1_score}   |   {self.p2_score}", move = False, align = alignment, font = FONT)
    
    def update_two(self):
        self.p2_score += 1
        self.clear()
        self.write(arg = f"{self.p1_score}   |   {self.p2_score}", move = False, align = alignment, font = FONT)
    