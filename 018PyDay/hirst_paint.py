import turtle

import colorgram
import random
from turtle import Turtle, Screen


# Create a Turtle object
turtle.colormode(255)
johnny = Turtle()


def turtle_config():
    johnny.shape("turtle")
    johnny.color("medium aquamarine")


def change_pen_color(color):
    # Change pen color
    red = color[0]
    green = color[1]
    blue = color[2]

    johnny.pencolor(red, green, blue)


def get_colors():
    num_colors = 15
    colors_list = []
    colors_data = colorgram.extract('image.jpg', num_colors)

    for color in colors_data:
        color_tuple = color.rgb
        r = color_tuple[0]
        g = color_tuple[1]
        b = color_tuple[2]

        color_tuple = (r, g, b)

        colors_list.append(color_tuple)

    return colors_list


# Set initial turtle configuration
turtle_config()

# Ger colors from image
colors = get_colors()
DOT_SIZE = 20

# Set turtle position
johnny.penup()
johnny.setposition(-180, -150)
johnny.pendown()

x = johnny.xcor()
y = johnny.ycor()

# Draw the dots
for row in range(10):
    johnny.pendown()
    for col in range(10):
        new_color = random.choice(colors)
        johnny.dot(DOT_SIZE, new_color)
        x = x + 50
        johnny.penup()
        johnny.setposition(x, y)
        johnny.pendown()

    x = -180
    y = y + 50
    johnny.penup()
    johnny.setposition(x, y)


# Set screen
screen = Screen()
screen.exitonclick()

