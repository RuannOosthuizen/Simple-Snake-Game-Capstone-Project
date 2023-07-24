# Imported Libraries:
from turtle import Turtle
import random


# Defined Food class to inherit from Turtle class:
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # Making a 10x10 circle.
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    # Setting the positiong for the food:
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

