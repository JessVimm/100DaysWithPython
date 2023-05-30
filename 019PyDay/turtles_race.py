import turtle
from turtle import Turtle, Screen
import random

# Screen settings
screen = Screen()
screen.setup(width=500, height=400)

# Game flag
is_race_on = False

# Get user bet
user_bet = screen.textinput(title="Turtles race", prompt="Which is your turtle? Choose a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y_cord = -100

# Initialise turtles
for participant in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[participant])
    new_turtle.goto(x=-230, y=y_cord)
    all_turtles.append(new_turtle)
    y_cord += 50

if user_bet:
    is_race_on = True

winner_color = "blank"

# Begin race
while is_race_on:
    user_bet = user_bet.lower()

    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()

# Print winner
if winner_color == user_bet:
    print("You win!")
else:
    print(f"Sorry. You lost against {winner_color} turtle.")

screen.exitonclick()

