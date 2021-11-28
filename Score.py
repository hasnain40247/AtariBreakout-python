from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 340)
        self.speed("fastest")
        self.score = 000
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.write(f"Score {self.score}", align='center', font=('Silkscreen', 45))
