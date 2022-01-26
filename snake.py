from turtle import Turtle


class Snake:
    """
    Snake moves around the TurtleScreen given the direction of user.
    Snake's segments are subclasses of Turtle, however Snake itself is not.
    Class variables:
        STARTING_POSITIONS - starting position of Snake object on screen
        MOVE_DISTANCE - move length
        UP - numeric value of direction "up"
        DOWN - numeric value of direction "down"
        LEFT - numeric value of direction "left"
        RIGHT -  numeric value of direction "right"
    Instance variables:
        segments = Snake's body, list of segment objects
        head = first segment of the list
    Methods:
        __init__() - define Snake's head and body (segments), then construct snake of segments
        create_snake() - construct snake of segments
        add_segment() - add new segment at a given position
        extend() - find last segment, add new segment at a given position
        move() - move Snake forward
        move_up() - change direction to Snake.UP
        move_down() - change direction to Snake.DOWN
        move_left() - change direction to Snake.LEFT
        move_right() - change direction to Snake.RIGHT
    """
    STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_DISTANCE = 20
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0

    def __init__(self):
        """Define Snake's head and body (segments), then construct snake of segments."""
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Construct snake of segments."""
        for position in Snake.STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add new segment at a given position."""
        new_segment = Turtle(shape='square')
        new_segment.color('green')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Find last segment, add new segment at a given position"""
        current_tail_position = self.segments[-1].position()
        self.add_segment(current_tail_position)

    def move(self):
        """Move Snake forward."""
        copy_segments = self.segments.copy()
        for i in range(len(copy_segments)-1, 0, -1):
            self.segments[i].goto(copy_segments[i-1].position())
        self.head.forward(Snake.MOVE_DISTANCE)

    def move_up(self):
        """Change direction to Snake.UP. Do nothing if Snake is moving in opposite direction."""
        if self.head.heading() != Snake.DOWN:
            self.head.setheading(Snake.UP)

    def move_down(self):
        """Change direction to Snake.DOWN. Do nothing if Snake is moving in opposite direction."""
        if self.head.heading() != Snake.UP:
            self.head.setheading(Snake.DOWN)

    def move_left(self):
        """Change direction to Snake.LEFT. Do nothing if Snake is moving in opposite direction."""
        if self.head.heading() != Snake.RIGHT:
            self.head.setheading(Snake.LEFT)

    def move_right(self):
        """Change direction to Snake.RIGHT. Do nothing if Snake is moving in opposite direction."""
        if self.head.heading() != Snake.LEFT:
            self.head.setheading(Snake.RIGHT)
