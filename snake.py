import random
from turtle import Turtle, delay, screensize, goto


class Snake:
    STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_DISTANCE = 20
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in Snake.STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.color('green')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        pass

    def move(self):
        for segment in self.segments:
            x = segment.xcor()
            y = segment.ycor()
            segment.goto(x, y)
            segment.forward(Snake.MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != Snake.DOWN:
            self.head.setheading(Snake.UP)

    def move_down(self):
        if self.head.heading() != Snake.UP:
            self.head.setheading(Snake.DOWN)

    def move_left(self):
        if self.head.heading() != Snake.RIGHT:
            self.head.setheading(Snake.LEFT)

    def move_right(self):
        if self.head.heading() != Snake.LEFT:
            self.head.setheading(Snake.RIGHT)

    # def reset_snake(self):

