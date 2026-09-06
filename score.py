from turtle import Turtle


FONT = ("Arial ", 18, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-360, y=460)
        self.score_text = "Score"
        self.score_count = 0
        self.score_board()

    # Method to increse the score
    def score_board(self):
        self.clear()
        self.write(arg=f"{self.score_text}: {self.score_count}", move=False, align='left', font=FONT)

    def increase(self):
        self.score_count += 1
        self.score_board()
