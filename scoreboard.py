from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score(self.l_score,self.r_score)

    def add_right_scores(self):
        self.clear()
        self.r_score += 1
        self.update_score(self.l_score,self.r_score)

    def add_left_scores(self):
        self.clear()
        self.l_score += 1
        self.update_score(self.l_score,self.r_score)

    def update_score(self,l_score,r_score):
        self.goto(-100, 200)
        self.write(l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(r_score, align="center", font=("Courier", 80, "normal"))
