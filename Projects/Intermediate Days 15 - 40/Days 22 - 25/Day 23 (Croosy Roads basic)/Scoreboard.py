from turtle import Turtle

font = ["Arial", 18, "italic"]
align = "center"

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.goto(-250, 270)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write(arg = f"Level {self.level}", font = font, align = align)

    def update(self):
        self.level += 1
        self.clear()
        self.write(arg = f"Level {self.level}", font = font, align = align)
    
    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(arg = f"You ran out of lives on Level {self.level} \n             Game Over.", font = font, align = align)

