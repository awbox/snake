import random
from turtle import Turtle, addshape


class Snake(Turtle):
    STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_DISTANCE = 20
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0
    HEADING_OPTIONS = [UP, DOWN, LEFT, RIGHT]

    def __init__(self, head_x=0, head_y=0, segments=4):
        self.segments = segments
        self.head_x = head_x
        self.head_y = head_y
        poly = ((self.head_x+5, self.head_y),
                (self.head_x+5, self.head_y+self.segments*10),
                (self.head_x-5, self.head_y+self.segments*10),
                (self.head_x-5, self.head_y))
        addshape('snake', poly)
        super().__init__(shape='snake')
        self.color('green')
        self.penup()


    @staticmethod
    def create_snake():
        """
        Creates snake instance at one of the defined starting positions,
        heading towards random choice of heading options
        :return newly create snake instance
        """
        # get new coordinates into x, y variables
        new_position = random.choice(Snake.STARTING_POSITIONS)
        x = new_position[0]
        y = new_position[1]
        # create Snake instance with given position
        new_snake = Snake(head_x=x, head_y=y)
        # set heading of the new instance to one of the heading options
        new_snake.setheading(random.choice(Snake.HEADING_OPTIONS))
        # return new snake
        return new_snake

    def add_segment(self):
        self.segments += 1

    def extend(self):
        pass

    def move(self):
        pass

    def up(self):
        pass

    def down(self):
        pass

    def left(self):
        pass

    def right(self):
        pass

    def reset(self):
        pass