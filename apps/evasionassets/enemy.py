## Imports
import turtle
import random
import time

## Enemy character initialize
class Enemy(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.name = 'enemy'
        self.color("green")
        self.shape("classic")
        self.penup()
        self.speed(10)
        self.turtlesize(2, 4)
        self.setposition(random.randrange(-200, 200), random.randrange (-200, 200))
        self.enemy_movement = 0
        self.ismoving = False
        self.start_moving()

    ## Enemy movement
    def start_moving(self):
        if not self.ismoving:
            self.ismoving = True
            self.forward(5)
            self.ismoving = False
