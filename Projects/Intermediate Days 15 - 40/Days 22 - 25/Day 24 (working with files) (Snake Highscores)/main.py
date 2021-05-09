from turtle import Screen
import random
import time
from Snake import Snake
from Food import Food
from Scoreboard import Score

# Storage for Variables and Lists
game_over = False

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



while 1:

    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Collision with Food   
    if snake.head.distance(food) < 15:
        Score.score += 1
        food.refresh()
        snake.add_segment()
        Score.update_score()
        

    # Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
            Score.game_over()
            snake.reset()
            Score.update_score()
    
    # Collision with itself
    for segment in snake.snake[1:]:
        
        if snake.head.distance(segment) < 15:
            Score.game_over()
            snake.reset()
            Score.update_score()
            
    
    
screen.exitonclick()