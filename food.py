import random
from turtle import Turtle


class Food(Turtle):
    """
    class Food to create Food objects.
    Food is a circle-shaped object on screen that snake aims to eat.
    Food object is initialized given (x, y) coordinates on the screen.
    """

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('blue')
        self.speed('fastest')
        self.penup()
        self.refresh()

    def refresh(self):
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        self.goto(x, y)
