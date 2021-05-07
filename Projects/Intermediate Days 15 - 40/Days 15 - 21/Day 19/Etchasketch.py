from turtle import Turtle, Screen

john = Turtle()
screen = Screen()


def move_forwards():
    john.forward(8)

def turn_right():
    john.right(5)

def turn_left():
    john.left(5)

def move_back():
    john.backward(8)

def clear():
    john.clear()
    john.penup()
    john.setposition(0, 0)
    john.pendown()

screen.listen()
screen.onkey(key = "w", fun = move_forwards)
screen.onkey(key = "d", fun = turn_right)
screen.onkey(key = "a", fun = turn_left)
screen.onkey(key = "s", fun = move_back)
screen.onkey(key = "c", fun = clear)
screen.exitonclick()