import random
from turtle import Turtle


class Food(Turtle):
    """
    Food is a circle-shaped object on screen that snake aims to eat.
    Food is a subclass of Turtle, adding one method: refresh().
    """

    def __init__(self):
        """
        Initialization of the Food object consists of:
        1) setting the shape of the object using inherited Turtle class attributes,
        2) using self.refresh() method to move to random position on the screen.
        """
        super().__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self) -> None:
        """
        Generates random (x,y) coordinates of the Food object, moves it to the new spot.
        :return: None
        """
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        self.goto(x, y)
