from turtle import Turtle



class Paddle(Turtle):
    def __init__(self,position,dimx,dimy,color):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.shapesize(dimx,dimy)
        self.color(color)
        self.penup()
        initial_speed = self.speed()
        self.speed("fastest")
        self.goto(position)
        self.speed(initial_speed)
        self.showturtle()

    def move_right(self):
        new_x = self.xcor() + 38
        if new_x <= 760:
            self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 38
        if new_x >= -760:
            self.goto(new_x, self.ycor())
