from turtle import Turtle, Screen
import colorgram
import random

pic_colors = colorgram.extract('image.jpg', 25)

tim = Turtle()
tim.speed(10)
scr = Screen()
scr.colormode(255)

muh_tuple = ()
for i in range(len(pic_colors)):
    choice = random.choice(pic_colors)
    red = choice.rgb.r
    green = choice.rgb.g
    blue = choice.rgb.b
    muh_tuple = (red, green, blue)


    tim.fillcolor(muh_tuple)
    tim.pencolor(muh_tuple)
    tim.penup()
    tim.forward(30)
    tim.pendown()
    tim.begin_fill()
    tim.circle(10)
    tim.end_fill()











scr.exitonclick()











