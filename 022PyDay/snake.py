from turtle import Turtle, Screen

MOVE_DISTANCE = 20
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180


class Snake:
    def __init__(self):
        self.snake_body = []
        self.x_pos = 20
        self.y_pos = 0
        self.body_parts = 3
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        # Creating snake body
        for _ in range(self.body_parts):
            self.x_pos -= MOVE_DISTANCE
            new_position = (self.x_pos, self.y_pos)
            self.add_body(new_position)

    def add_body(self, position):
        new_body_part = Turtle("square")
        new_body_part.color("white")
        new_body_part.penup()
        new_body_part.goto(position)
        self.snake_body.append(new_body_part)

    def extend(self):
        self.add_body(self.snake_body[-1].position())

    def move(self):
        for body_part in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body_part - 1].xcor()
            new_y = self.snake_body[body_part - 1].ycor()
            self.snake_body[body_part].goto(new_x, new_y)
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
