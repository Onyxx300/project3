## Imports
import turtle
import random

## Item initialize
class Item(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.name = 'bonus'
        self.ycor = random.randrange(-200, 200)
        self.xcor = random.randrange(-200, 200)
        self.addbonus()

    ## Iten spawn
    def addbonus(self):
        self.penup()
        self.color("yellow")
        self.setposition(self.xcor, self.ycor)
        self.shape("circle")
        self.penup()


