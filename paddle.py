from turtle import Turtle

START_LEFT = [(-380,0),(-380,20),(-380,-20)]
START_RIGHT = [(380,0),(380,20),(380,-20)]

START_POSITION = {'paddle_left':[(-380,0),(-380,20),(-380,-20)],'paddle_right':[(380,0),(380,20),(380,-20)]}

class Paddle:
    def __init__(self):
        self.create_paddle(START_LEFT)
        self.create_paddle(START_RIGHT)

    def create_paddle(self,paddle_locations):
        for location in paddle_locations:
            new_paddle = Turtle(shape = "square")
            new_paddle.pencolor("black")
            new_paddle.color("white")
            new_paddle.penup()
            new_paddle.goto(location)
            self.paddles.append(new_paddle)

