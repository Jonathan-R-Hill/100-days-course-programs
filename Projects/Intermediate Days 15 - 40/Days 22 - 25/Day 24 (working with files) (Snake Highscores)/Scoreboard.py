from turtle import Turtle

alignment = "center"
FONT = ("Courier", 15, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.h_score = int(data.read())
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.setposition(0, 280)
        self.write(arg = f"Score: {self.score} | High score: {self.h_score}", move = False, align = alignment, font = FONT)
    
    def update_score(self):
        self.setposition(0, 280)
        self.clear()
        self.write(arg = f"Score: {self.score} | High score: {self.h_score}", move = False, align = alignment, font = FONT)
        
        
    def game_over(self):
        self.setposition(0, 0)
        self.write(arg = f"Game Over. You scored {self.score} points.", move = False, align = alignment, font = FONT)
        
        if self.score > self.h_score:
            self.h_score = self.score
            with open("data.txt", mode = "w" ) as data:               
                data.write(f"{self.h_score}")
                
        self.score = 0
        

        
            
    
    