from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x_cor,y_cor)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
