from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

# Create a screen object
screen = Screen()

# Screen setup
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create a snake object
snake = Snake()

# Create food
food = Food()

# Create score
score = Score()

# Listen for keystrokes
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Move the snake
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    # Move snake
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 16:
        food.provide_food()
        score.update_score()
        # Extend tail
        snake.extend()
    # Detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -299 or snake.head.ycor() > 280 or snake.head.ycor() < -299:
        game_is_on = False
        score.game_over()

    # Detect tail collision
    for body_part in snake.snake_body[1:]:
        if snake.head.distance(body_part) < 10:
            game_is_on = False
            score.game_over()
screen.exitonclick()
