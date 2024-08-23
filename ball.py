from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_change=10
        self.y_change=10
        self.move_speed=0.1

    def move(self):
        x,y=self.pos()
        self.setpos(x+self.x_change,y+self.y_change)

    def bounce(self, wall_or_paddle: str):
        if wall_or_paddle == "wall":
            self.y_change*=-1
        elif wall_or_paddle == "paddle":
            self.x_change*=-1

    def check_hit_paddle(self, paddle, score):
        """
        If it hits the paddle, bouces back the ball and increases speed
        If it misses the paddle, increases opponent score
        """
        bally=self.ycor()
        paddley=paddle.ycor()
        if abs(paddley-bally) <= 50:
            self.bounce("paddle")
            self.move_speed*=0.9
        else:
            score.increase_score()
            self.move_speed=0.1
        