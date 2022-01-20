import random
from turtle import Turtle, screensize


class Food(Turtle):
    """
    class Food to create Food objects.
    Food is a circle-shaped object on screen that snake aims to eat.
    Food object is initialized given (x, y) coordinates on the screen.
    """

    def __init__(self):
        # initialize the Turtle object class
        super().__init__()
        # draw the Food object
        self.shape('circle')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('blue')
        self.speed('fastest')
        self.penup()
        # get the screen size to correctly position the Food object on the screen
        self.screen_width, self.screen_height = screensize()
        # position the Food object on the screen
        self.x = random.randrange(-self.screen_width, self.screen_width)
        self.y = random.randrange(-self.screen_height, self.screen_height)
        self.goto(self.x, self.y)

    def refresh(self):
        """
        Method to refresh Food instance at a random position on the screen.
        :return: None
        """
        # select random values for x, y coordinates
        # within the range of screen size
        x = random.randrange(-self.screen_width, self.screen_width)
        y = random.randrange(-self.screen_height, self.screen_height)
        # update Food instance with given coordinates
        self.x = x
        self.y = y
        # position the new Food object on the screen
        self.goto(x, y)
