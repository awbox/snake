import random
from turtle import Turtle


class Food(Turtle):
    """
    class Food to create Food objects.
    Food is a circle-shaped object on screen that snake aims to eat.
    Food object is initialized given (x, y) coordinates on the screen.
    """

    def __init__(self, x: int, y: int):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('blue')
        self.speed('fastest')
        self.x = x
        self.y = y
        self.goto(x, y)

    def refresh(self, screen_height: int, screen_width: int):
        """
        Method to refresh randomly Food instance.
        :param screen_height: screen height, constant for game, int
        :param screen_width: screen width, constant for game, int
        :return: None
        """
        # select random values for x, y coordinates
        # within the range of screen size
        x = random.randrange(-screen_width, screen_width)
        y = random.randrange(-screen_height, screen_height)
        # update Food instance with given coordinates
        self.x = x
        self.y = y
        self.goto(x, y)
