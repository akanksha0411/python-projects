import turtle as t

tim = t.Turtle()
s = t.Screen()
tim.speed(0)

def move_forwards():
    tim.fd(10)

def move_backwards():
    tim.bk(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.reset()
    tim.home()
s.listen()
s.onkeypress(fun = move_forwards, key = "w")
s.onkeypress(fun= move_backwards, key = "s")
s.onkeypress(fun= turn_left, key = "a")
s.onkeypress(fun= turn_right, key = "d")
s.onkeypress(fun = clear, key = "c")
s.exitonclick()