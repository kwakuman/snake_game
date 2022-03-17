from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

HIGHSCORE_DATA_FILE = 'data.txt'

# set up game screen
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()

food = Food()
scoreboard = Scoreboard(HIGHSCORE_DATA_FILE)
screen.update()


time.sleep(2)
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #Detect collision with wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        scoreboard.reset()
        snake.reset_snake()


    #Detect collision with tail
    for segment in snake.snake[1:]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset_snake()

screen.exitonclick()



















screen.exitonclick()