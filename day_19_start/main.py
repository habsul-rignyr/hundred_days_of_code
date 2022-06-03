from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.fd(10)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

screen.listen()
screen.onkeypress(key="space", fun=move_forward)
screen.onkeypress(key="Right", fun=turn_right)
screen.onkeypress(key="Left", fun=turn_left)









screen.exitonclick()