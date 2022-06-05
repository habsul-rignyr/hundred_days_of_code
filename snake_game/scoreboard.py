from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(0, 280)
        self.score = 0

    def text(self, str1):
        self.write(str1, align='center', font=('Arial', 12, 'normal'))

    def score_up(self):
        self.score += 1

    def refresh(self):
        self.clear()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align='center', font=('Arial', 12, 'normal'))
