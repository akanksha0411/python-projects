import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

# colors_list = ["dark orange", "chartreuse", "magenta", "medium purple", "brown", "deep sky blue", "slate blue", "red","orange","yellow","green","blue","indigo","purple"]
n = 3
for _ in range(7):
    tim.pencolor((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
    tim.pensize(6)
    for i in range(n):
        tim.fd(100)
        tim.right(360/n)
    n += 1

screen = t.Screen()
screen.exitonclick()
