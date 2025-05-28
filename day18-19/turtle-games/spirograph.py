import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

for _ in range(72):
    tim.pencolor((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
    tim.speed("fastest")
    tim.circle(75)
    tim.tilt(5)
    tim.right(5)


screen = t.Screen()
screen.exitonclick()