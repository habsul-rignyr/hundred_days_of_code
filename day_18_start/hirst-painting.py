from turtle import Turtle, Screen
import colorgram
import random



tim = Turtle()
tim.speed(0)
scr = Screen()
scr.colormode(255)
scr.screensize(canvwidth=600, canvheight=600)
tim.penup()
tim.goto(-275, -250)
tim.pendown()


# Uncomment and run this code the first time you add a new image.
# You can then save the color tuples as a list (below called 'colors').
# The first colors will likely be background colors so you may want to delete them.

# color_list = []

# pic_colors = colorgram.extract('image.jpg', 25)
# muh_tuple = ()
# for color in pic_colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     muh_tuple = (red, green, blue)
#     color_list.append(muh_tuple)
#
# print(color_list)

colors = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162),
          (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90),
          (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48),
          (184, 103, 113)]


for i in range (10):
    for i in range (10):
        new_color = random.choice(colors)
        tim.fillcolor(new_color)
        tim.pencolor(new_color)
        tim.penup()
        tim.forward(50)
        tim.pendown()
        tim.begin_fill()
        tim.circle(20)
        tim.end_fill()
    tim.penup()
    tim.goto(-275, tim.position()[1] + 50)
    tim.pendown()










scr.exitonclick()











