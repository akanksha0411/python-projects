import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

directions = [0, 90, 180, 270]

for _ in range(200):
    tim.pencolor((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
    tim.pensize(8)
    tim.speed("fastest")
    tim.fd(30)
    tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()