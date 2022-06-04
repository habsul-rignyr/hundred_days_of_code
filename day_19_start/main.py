from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?  Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = -90
all_turtles = []
for i in range(6):

    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230, y_position)
    all_turtles.append(new_turtle)
    y_position += 40

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if is_race_on:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)
            if turtle.xcor()>230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won!  The {winning_color} turtle crossed the finish line first!")
                else:
                    print(f"You've lost!  The {winning_color} turtle crossed the finish line first!")








screen.exitonclick()