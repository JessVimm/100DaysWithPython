from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.points = 0
        self.goto(0, 260)
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.points}", align="center", font=('Arial', 14, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Arial', 14, 'normal'))

    def update_score(self):
        self.points += 1
        self.clear()
        self.show_score()
