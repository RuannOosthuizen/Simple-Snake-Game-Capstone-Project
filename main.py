# Imported Libraries:
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


# Setup of screen object for use:
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


# Creating the object to start:
snake = Snake()
food = Food()
scoreboard = Scoreboard()


# User controls for snake:
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Snake controls and behaviours:
# moving the snake forward.
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detecting collision with food:
    if snake.head.distance(food) < 15:
        food.refresh() # Resets the location of the food.
        scoreboard.increase_score() # Keeps score.
        snake.extend() # extends the snake when it eats the food.

    # Detecting collision with wall:
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False # Ends the game.
        scoreboard.game_over()

    # Detecting collisiong with tail:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


# Closes the window on a click.
screen.exitonclick()