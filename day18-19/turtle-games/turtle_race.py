import turtle as t
import random

s = t.Screen()
is_race_on = False
s.setup(500, 400)

user_bet = s.textinput(title = "Make your bet!", prompt= "Which turtle will win the race? Enter a color:")

colors = ["red", "orange", "green", "yellow", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. {winning_color} won the race")
            else:
                print(f"You've lost. {winning_color} won the race")
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

s.exitonclick()