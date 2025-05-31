import turtle as t

FONT = ('Courier', 24, 'normal')

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.write(f"Score: {self.score}",align="center", font=FONT)

    def increase_score(self):
        self.clear()
        self.score +=1
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over", align="center", font=FONT)
