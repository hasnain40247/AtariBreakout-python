from turtle import Turtle


class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.shape("circle")

        self.color("#FF7878")
        self.penup()
        initial_speed = self.speed()
        self.speed("fastest")
        self.goto(position)
        self.speed(initial_speed)
        self.showturtle()
        self.y_move = 5
        self.x_move = -5

    def move(self, paddleList):

        hitObject = -1

        if self.xcor() <= -750 or self.xcor() >= 750:
            print("Here@")
            self.bouncex()

        for i in range(len(paddleList)):

            dist_x = paddleList[i].xcor() - self.xcor()
            dist_y = paddleList[i].ycor() - self.ycor()

            if paddleList[i].distance(self) < 58:
                print("Hit")
                hitObject = i
                print(hitObject)
                self.bouncey()
                break

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        if hitObject != -1:
            return hitObject
        else:
            return False

    def bouncey(self):
        self.y_move *= -1

    def bouncex(self):
        self.x_move *= -1
