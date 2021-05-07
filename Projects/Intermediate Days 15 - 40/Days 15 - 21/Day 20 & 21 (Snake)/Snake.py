from turtle import Turtle

# Storage for Variables and Lists

starting_pos = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20

up = 90
left = 180
down = 270
right = 0

# Snake Body
# Snake Square is by default 20 x 20


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        
    def create_snake(self):
        for postition in starting_pos:
            new_segment = Turtle(shape = "square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(postition)
            self.snake.append(new_segment)
    
    def move(self):
        for seg in range(len(self.snake)- 1, 0, -1):
            pos_x = self.snake[seg - 1].xcor()
            pos_y = self.snake[seg - 1].ycor()
            self.snake[seg].goto(pos_x, pos_y)
        self.head.forward(move_distance)

    def Up(self):
        if self.head.heading() != down:
            self.head.setheading(up)
    
    def Down(self):
        if self.head.heading() != up:
            self.head.setheading(down)
    
    def Left(self):
        if self.head.heading() != right:
            self.head.setheading(left)
    
    def Right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def add_segment(self):
        new_segment = Turtle(shape = "square")
        new_segment.color("white")
        new_segment.penup()
        self.snake.append(new_segment)