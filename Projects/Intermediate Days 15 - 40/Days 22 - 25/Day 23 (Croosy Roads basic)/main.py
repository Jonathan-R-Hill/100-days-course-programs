from turtle import Screen
import time
from Player import player
from Scoreboard import Level
from Lives import Lives
from Cars import Car

# Variable and list Storage
got = []

# Screen setup
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Crossy Roads")
screen.tracer(0)    # 0 = off

# Classes being defined
player = player()
level = Level()
lives = Lives()
car = Car()

# Controls
screen.listen()

screen.onkey(key = "w", fun = player.up)
screen.onkey(key = "s", fun = player.down)

while lives.Lives > 0:
    car.move_cars()
    screen.update()
    time.sleep(0.1)
    
    # Level Up
    if player.ycor() > 280:
        player.reset()
        level.update()
        car.move_cars()
        car.speed += 2
        
    
    # Lose a life if hit by car
    for i in car.cars:
        if i.distance(player) < 15:
            player.reset()
            time.sleep(0.1)
            lives.die()
  
    # End game if all lives are lost
    if lives.Lives == 0:
        print(f"You got to Level: {level.level}. Well done!")
        level.game_over()
    
    # Gain a life every 5 levels
    if level.level % 5 == 0 and level.level not in got:
        lives.gain()
        got.append(level.level)
        
    
    
screen.exitonclick()