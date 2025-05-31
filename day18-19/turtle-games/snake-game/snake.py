import turtle as t

INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DEFAULT_MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(object):

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in INITIAL_POSITIONS:
            self.add_segment(position=i)

    def add_segment(self, position):
        segment = t.Turtle(shape='square')
        segment.shapesize(stretch_wid=0.8, stretch_len=0.8)
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            coordinates = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(coordinates[0], coordinates[1])
        self.head.fd(DEFAULT_MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
