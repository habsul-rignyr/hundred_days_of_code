from turtle import Turtle, Screen
import random

tim = Turtle()
scr = Screen()
scr.colormode(255)
tim.speed(10)


def random_color():
    num1 = random.randint(0, 255)
    num2 = random.randint(0, 255)
    num3 = random.randint(0, 255)
    muh_tuple = (num1, num2, num3)
    return muh_tuple

# making a spirograph
for i in range (36):
    tim.pencolor(random_color())
    tim.circle(100)
    tim.right(10)










# # random walk with random colors
# right_list = [0, 90, 180, 270]
#
# tim.pensize(10)
#
# for i in range(100):
#     num1 = random.randint(0, 255)
#     num2 = random.randint(0, 255)
#     num3 = random.randint(0, 255)
#     tim.pencolor(num1, num2, num3)
#     tim.right(random.choice(right_list))
#     tim.fd(20)

## drawing several different randomly covered polygons on top of one another
# sides = 3
#
# for i in range(7):
#     num1 = random.randint(0, 255)
#     num2 = random.randint(0, 255)
#     num3 = random.randint(0, 255)
#     tim.pencolor(num1, num2, num3)
#     for i in range(sides):
#         tim.fd(100)
#         tim.right(360 / sides)
#     sides += 1

scr.exitonclick()
