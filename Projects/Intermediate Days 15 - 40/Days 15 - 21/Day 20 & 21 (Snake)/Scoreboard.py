from turtle import Turtle

alignment = "center"
FONT = ("Courier", 15, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.setposition(0, 280)
        self.write(arg = f"Score: {self.score}", move = False, align = alignment, font = FONT)
    
    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg = f"Score: {self.score}", move = False, align = alignment, font = FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write(arg = f"Game Over", move = False, align = alignment, font = FONT)
