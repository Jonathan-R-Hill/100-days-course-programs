from turtle import Screen
from Scoreboard import Score
from Ball import Ball
from Paddles import Paddle
import time

# Storage for Varibles 

max_score = 5
game_over = False

# Screen setup
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)    # 0 = off

# Creating parts from classes
score = Score()
ball = Ball()
p1 = Paddle(-340, 0)    # left
p2 = Paddle(340, 0)     # right

# Keys for Movement
screen.listen()

# Player 1 
screen.onkey(key = "w", fun = p1.Up)
screen.onkey(key = "s", fun = p1.Down)

# Player 2
screen.onkey(key = "Up", fun = p2.Up)
screen.onkey(key = "Down", fun = p2.Down)


while game_over == False:
    screen.update()
    time.sleep(0.01)
    ball.move()
    
    # Score update and reset ball
    if ball.xcor() > 400:
        score.update_one()
        ball.reset_ball()
        
    elif ball.xcor() < -400:
        score.update_two()
        ball.reset_ball()
    
    # Wall bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.hit_wall()
    
    # Paddle Collision
    if ball.distance(p1) < 40 and ball.xcor() < -339:
        ball.paddle_bounce()
    
    elif ball.distance(p2) < 40 and ball.xcor() > 339:
        ball.paddle_bounce()
    
    # End the game if score makes it to 5
    if score.p1_score >= 5 or score.p2_score >= 5:
        game_over = True
        print(f"Game over the score was:\n Player 1: {score.p1_score}  |||  Player 2: {score.p2_score}")

screen.exitonclick()