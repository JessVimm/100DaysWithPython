from turtle import Turtle, Screen

MOVE_DISTANCE = 20
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

class Snake:
    def __init__(self):
        self.snake = []
        self.x_pos = 20
        self.y_pos = 0
        self.body_parts = 3
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        # Creating snake body
        for _ in range(self.body_parts):
            new_body_part = Turtle("square")
            new_body_part.color("white")
            new_body_part.penup()
            self.x_pos -= MOVE_DISTANCE
            new_body_part.setposition(self.x_pos, self.y_pos)
            self.snake.append(new_body_part)

    def move(self):
        for body_part in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[body_part - 1].xcor()
            new_y = self.snake[body_part - 1].ycor()
            self.snake[body_part].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def down(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)

    def left(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)

    def right(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)
