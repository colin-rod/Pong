from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle = Paddle()
screen.update()



START_POSITION = {'paddle_left':[(-380,0),(-380,20),(-380,-20)],'paddle_right':[(380,0),(380,20),(380,-20)]}
print(START_POSITION.items())

screen.exitonclick()