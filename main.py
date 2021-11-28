import time
import tkinter
import turtle

from Ball import Ball
from Score import Score
from paddle import Paddle
from playsound import playsound

timey = Paddle((0, -340), 2, 4, "#79018C")
score = Score()
screen = turtle.Screen()
img = tkinter.Image("photo", file="full-moon.png")
turtle._Screen._root.iconphoto(True, img)
screen.title("Atari")
screen.bgcolor("#160040")
screen.screensize(0, 0)
screen.setup(width=1.0, height=1.0, startx=None, starty=None)
screen.tracer(0)

colorList = ["#9A0680", "#6E3CBC", "#6ECB63", "#B91646", "#FF5DA2", "#5C7AEA"]
newy = 300
paddleList = []
for i in range(6):
    newx = -666
    for j in range(9):
        target = Paddle((newx, newy), 2, 8, colorList[i])
        paddleList.append(target)
        newx = newx + 165

    newy = newy - 45

ball = Ball((0, -250))

screen.listen()
screen.onkey(timey.move_right, "Right")
screen.onkey(timey.move_left, "Left")

is_game_on = True
while is_game_on:
    time.sleep(0.018)
    screen.update()

    index = ball.move(paddleList)
    if index:
        playsound('./hit.mp3',block=False)
        score.score += 10
        score.updateScore()
        paddleList[index].ht()
        del paddleList[index]


    if timey.distance(ball) <= 49:
        ball.bouncey()

screen.exitonclick()
