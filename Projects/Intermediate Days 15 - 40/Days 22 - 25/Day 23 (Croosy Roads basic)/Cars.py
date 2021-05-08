from turtle import Turtle
from random import randint

colours = ["red", "blue", "pink", "orange", "brown", "green", "yellow"]

headings = [0, 180]

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.cars = []
        self.speed = 6
        self.create_cars()
        self.move_cars()
        
        
    def create_cars(self):
        for i in range(20):
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(0.5, 1)
            new_car.color(colours[randint(0, 6)])
            new_car.penup()
            new_car.setheading(headings[randint(0, 1)])
            new_car.goto(randint(-250, 250), randint(-200, 260))
            self.cars.append(new_car)
    
    def move_cars(self):
        for i in self.cars:
            i.forward(self.speed)
            if i.xcor() > 280 or i.xcor() < -280:
                old_head = i.heading()
                i.setheading(old_head + 180)
                i.forward(self.speed)
    
