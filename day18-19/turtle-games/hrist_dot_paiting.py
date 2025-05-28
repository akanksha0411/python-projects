import colorgram
import turtle as t
import random

# Use the commented code once to extract color values from any image file of your choice.

# colors = colorgram.extract("images.jpg", 48)
# rgb_values = []
# for color in colors:
#     rgb_values.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(rgb_values)

color_list = [(235, 231, 224), (165, 164, 160), (150, 98, 60), (227, 210, 89), (157, 9, 30), (199, 156, 22), (137, 164, 151), (54, 91, 156), (19, 40, 70), (123, 163, 205), (129, 68, 98), (39, 27, 18), (85, 11, 55), (200, 137, 157), (163, 13, 4), (29, 50, 43), (197, 93, 144), (228, 166, 188), (13, 55, 128), (156, 218, 199), (63, 95, 78), (37, 82, 60), (185, 186, 208), (220, 178, 172), (187, 101, 85), (41, 74, 77), (96, 113, 171), (78, 172, 135), (225, 204, 22), (102, 136, 152), (71, 65, 53), (174, 203, 209)]

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.penup()
tim.fd(300)
tim.setheading(0)

for i in range(10):
    for j in range(10):
        tim.dot(15, random.choice(color_list))
        tim.fd(50)
    tim.setheading(90)
    tim.fd(50)
    tim.setheading(180)
    tim.fd(500)
    tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
