import turtle as t
import time

from scoreboard import Scoreboard
from snake import Snake
from food import Food
from scoreboard import Scoreboard

s = t.Screen()
s.setup(600, 600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

#TODO -1 Create Snake body
snake_obj = Snake()

#TODO -3 Create food
food = Food()
score = Scoreboard()

s.listen()
s.onkey(snake_obj.left, "a")
s.onkey(snake_obj.right, "d")
s.onkey(snake_obj.up, "w")
s.onkey(snake_obj.down, "s")

#TODO -2 Move the snake
game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    snake_obj.move()

    #TODO-4 Detect Collision with food
    if snake_obj.head.distance(food) < 15:
        food.refresh()
        snake_obj.extend()
        score.increase_score()

    #TODO -5 Detect Collision with wall
    if snake_obj.head.xcor() > 300  or snake_obj.head.xcor() < -300 or snake_obj.head.ycor() > 300 or snake_obj.head.ycor() < -300:
        game_is_on = False
        score.game_over()

    for segment in snake_obj.segments[1:]:
        if snake_obj.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

s.exitonclick()
