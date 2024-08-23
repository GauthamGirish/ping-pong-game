from turtle import Turtle, Screen
import time

from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

def draw_divider():
    line=Turtle()
    line.hideturtle()
    line.left(90)
    line.pencolor("white")
    for i in range(-290, 300, 40):
        line.teleport(0,i)
        line.forward(20)

s=Screen()
s.setup(800,600)
s.bgcolor("black")
s.tracer(0)

p1=Paddle("left")
score1=Scoreboard(-50,250)
p2=Paddle("right")
score2=Scoreboard(50,250)
ball=Ball()
draw_divider()
s.update()

s.listen()
s.onkeypress(p1.move_up,"w")
s.onkeypress(p1.move_down,"s")
s.onkeypress(p2.move_up,"Up")
s.onkeypress(p2.move_down,"Down")

while True:
    ballx,bally=ball.pos()
    if bally>280 or bally<-280:
        ball.bounce("wall")

    if ballx<-370 or ballx>370:
        ball.setpos(0,0)
        ball.bounce("paddle")
        s.update()

    if ballx==330:
        ball.check_hit_paddle(p2,score1)

    if ballx==-330:
        ball.check_hit_paddle(p1,score2)

    ball.move()
    s.update()
    time.sleep(ball.move_speed)

s.exitonclick()
