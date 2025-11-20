## Imports
import turtle

## Player movement values
PLAYER_STEP_V = 3
PLAYER_STEP_H = 3

## Player character initialize
class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.name = 'player'    
        self.color("white")   
        self.shape("turtle")    
        self.penup()   
        self.move_player_up()      
        self.move_player_down()       
        self.move_player_left()
        self.move_player_right()
        self.setposition(0, 0)
        self.h_player_movement = 0
        self.v_player_movement = 0

    ## Player movement
    def move_player_up(self):
        self.v_player_movement = 1
    def move_player_right(self):
        self.h_player_movement = 1
    def move_player_left(self):
        self.h_player_movement = -1
    def move_player_down(self):
        self.v_player_movement = -1
    def stop_moving(self):
        self.h_player_movement = 0
        self.v_player_movement = 0   

## Troubleshooting player character issues        

if __name__ == "__main__":
    window = turtle.Screen()
    window.tracer(0)
    window.setup(width = 640, height = 480)
    window.bgcolor("orange")
    window.title("Test Mode")
    player = Player()
    window.update()
    turtle.done()

