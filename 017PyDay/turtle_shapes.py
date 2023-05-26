from turtle import Turtle, Screen
import random

# Create a Turtle object
johnny = Turtle()


def turtle_config():
    johnny.shape("turtle")
    johnny.color("medium aquamarine")


def draw_figure(no_sides, angle_value):
    # Change pen color
    red = random.uniform(0,1)
    green = random.uniform(0,1)
    blue = random.uniform(0,1)

    johnny.pencolor(red, green, blue)
    # Draw each side
    for step in range(no_sides):
        johnny.forward(50)
        johnny.right(angle_value)


# Set initial turtle configuration
turtle_config()

# Draw figures
for sides in range(3, 11):
    # Calculate angle
    angle = int(360 / sides)
    # Draw
    draw_figure(sides, angle)

# Set screen
screen = Screen()
screen.exitonclick()


