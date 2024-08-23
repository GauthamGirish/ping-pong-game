from turtle import Turtle

class Paddle(Turtle):
    orientation={"left":(-350,0), "right":(350,0)}
    def __init__(self, side : str) -> None:
        """Select side as 'left' or 'right'"""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(1,5)
        self.setheading(90)
        self.penup()
        self.teleport(*self.orientation[side])

    #move paddle up
    def move_up(self):
        if self.pos()[1] < 240:
            self.forward(15)

    #move paddle down
    def move_down(self):
        if self.pos()[1] > -240:
            self.back(15)
