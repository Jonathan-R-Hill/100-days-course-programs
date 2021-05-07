from turtle import Screen
import random
import time
from Snake import Snake
from Food import Food
from Scoreboard import Score

# Storage for Variables and Lists
game_over = False
local_score = 0

# Screen setup
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)    # 0 = off


# Creating the snake and food using the Class imported above 
snake = Snake()
food = Food()
Score = Score()

# Key's for movement
screen.listen()
screen.onkey(key = "w", fun = snake.Up)
screen.onkey(key = "s", fun = snake.Down)
screen.onkey(key = "a", fun = snake.Left)
screen.onkey(key = "d", fun = snake.Right)



while game_over == False:

    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Collision with Food   
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_segment()
        Score.update_score()
        local_score += 1

    # Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_over = True
        Score.game_over()
        print(f"Game Over. \nYour score was: {local_score}\n")
    
    # Collision with itself
    for segment in snake.snake[1:]:
        
        if snake.head.distance(segment) < 15:
            game_over = True
            Score.game_over()
            print(f"Game Over. \nYour score was: {local_score}\n")
            
    
screen.exitonclick()