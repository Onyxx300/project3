## Imports
# from evasionassets.player import Player, turtle, PLAYER_STEP_V, PLAYER_STEP_H
# from evasionassets.enemy import Enemy, random 
# from evasionassets import collectables
# from evasionassets import inner_workings
# from evasionassets.collectables import Item, random
import time, random, turtle, tkinter as tk, tkinter.messagebox

## Initialize screen
class GameWindow(tk.Tk):
    def __init__(self, window: tk.Tk) -> None:
        self.window = tk.Tk()
        window.destroy()
        self.start()

    ## Game window
    def start(self):
        self.window.title("Evasion")
        canvas = tk.Canvas(self.window, width=640, height=480, bg='black')
        canvas.pack(padx=10, pady=10)
        self.screen = turtle.TurtleScreen(canvas)
        self.screen.tracer(0)
        self.screen.bgcolor("black")
        self.LEFT = -self.screen.window_width() / 2
        self.RIGHT = self.screen.window_width() / 2
        self.TOP = self.screen.window_height() / 2
        self.BOTTOM = -self.screen.window_height() / 2
        self.H_GUTTER = 0.025 * self.screen.window_width()
        self.V_GUTTER = 0.025 * self.screen.window_height()

        ## Player movement values
        PLAYER_STEP_V = 3
        PLAYER_STEP_H = 3
     

        ## Player character initialize
        ## You
        PLAYER_ATTEMPTS = 3
        player = turtle.RawTurtle(self.screen)
        enemy = turtle.RawTurtle(self.screen)
        Coins = []
        score = 0
        player.h_player_movement = 0
        player.v_player_movement = 0
        # class Player(turtle.RawTurtle(self.screen)):
        def makeplayer():
            player.name = 'player'    
            player.color("white")   
            player.shape("turtle")    
            player.penup()   
            player.move_player_up()      
            player.move_player_down()       
            player.move_player_left()
            player.move_player_right()
            player.setposition(0, 0)

        ## Player movement
        def move_player_up():
            player.v_player_movement = 1
        def move_player_right():
            player.h_player_movement = 1
        def move_player_left():
            player.h_player_movement = -1
        def move_player_down():
            player.v_player_movement = -1
        def stop_moving():
            player.h_player_movement = 0
            player.v_player_movement = 0 

        ## Enemy

        ## Enemy character initialize
        # class Enemy(turtle.RawTurtle(self.screen)):
        def makeenemy():
            enemy.name = 'enemy'
            enemy.color("green")
            enemy.shape("classic")
            enemy.penup()
            enemy.speed(10)
            enemy.turtlesize(2, 4)
            enemy.setposition(random.randrange(-200, 200), random.randrange (-200, 200))
            enemy.ismoving = False

        ## Enemy movement
        def start_moving_enemy():
            if not enemy.ismoving:
                enemy.ismoving = True
                enemy.forward(5)
                enemy.ismoving = False

        ## Coins

        ## Item initialize
    # class Item(turtle.RawTurtle(self.screen)):
        def bonus():
            self.name = 'bonus'
            self.ycor = random.randrange(-200, 200)
            self.xcor = random.randrange(-200, 200)
            self.addbonus()

        ## Iten spawn
        def addbonus():
            self.penup()
            self.color("yellow")
            self.setposition(self.xcor, self.ycor)
            self.shape("circle")
            self.penup()

        ## Collision detection
        def hit_check(actor1: turtle.RawTurtle, actor2: turtle.RawTurtle, threshold):
            distance = actor1.distance(actor2)
            return distance < threshold

        ## Adds coin (worth 10 points)
        def addcoin():
            if len(Coins) == 0:
                newcoin = addbonus()
                Coins.append(newcoin)

        ## Collect coin
        def collect():
            global score
            for Checking in Coins:
                if hit_check(player, Checking, 20):
                    Checking.hideturtle()
                    Coins.remove(Checking)
                    score += 10

        ## Ouch
        def ouch():
            global score
            global PLAYER_ATTEMPTS
            if hit_check(player, enemy, 20):
                PLAYER_ATTEMPTS -= 1
                score -= 100
                if score < 100:
                    score = 0
                    self.screen.update()
                current_heading_h = enemy.heading()
                enemy.setheading(current_heading_h + random.randint(35, 70))
                player.setposition(0, 0)
                self.screen.update() 

        # ## You
        # PLAYER_ATTEMPTS = 3
        # player = Player()
        # enemy = Enemy()
        # Coins = []
        # score = 0   

        ## Text (lives counter)
        lives = turtle.RawTurtle(self.screen)
        lives.penup()
        lives.hideturtle()
        lives.setposition(self.LEFT * 0.1, self.TOP * 0.9)
        lives.color("orange")

        ## Text (score)
        scoreboard = turtle.RawTurtle(self.screen)
        scoreboard.penup()
        scoreboard.hideturtle()
        scoreboard.setposition(self.RIGHT * 0.6, self.TOP * 0.9)
        scoreboard.color("red")

        ## Text (timer)
        text = turtle.RawTurtle(self.screen)
        text.penup()
        text.hideturtle()
        text.setposition(self.LEFT * 0.9, self.TOP * 0.9)
        text.color("red")

        ## Keybinds for controlling the player
        self.screen.onkeypress(player.move_player_left, 'Left')
        self.screen.onkeypress(player.move_player_right, 'Right')
        self.screen.onkeypress(player.move_player_down, 'Down')
        self.screen.onkeypress(player.move_player_up, 'Up')
        self.screen.onkeypress(turtle.bye, 'Escape')
        self.screen.onkeyrelease(player.stop_moving, 'Left')
        self.screen.onkeyrelease(player.stop_moving, 'Right')
        self.screen.onkeyrelease(player.stop_moving, 'Up')
        self.screen.onkeyrelease(player.stop_moving, 'Down')

        ## Timer initialize
        game_end = False
        game_timer = time.time()

        ## Set coin
        addcoin()
        makeplayer()
        makeenemy()
        

        ## Game loop (timer) and intialize scoring
        while game_end == False:
            time_elapsed = time.time() - game_timer
            
            ## Draw score counter
            scoreboard.clear()
            scoreboard.write(
                f'Score: {score}',
                font = ("Courier", 15, "bold")
            )
        
            ## Draw timer
            text.clear()
            text.write(
                f'Time: {time_elapsed:5.1f} seconds',
                font = ("Courier", 15, "bold")
            )
            ## Draw lives counter
            lives.clear()
            lives.write(
                f'Lives: {PLAYER_ATTEMPTS}',
                font = ("Courier", 15, "bold")
            )

            ## Game loop (player movement)
            new_x = player.xcor() + PLAYER_STEP_H * player.h_player_movement
            if self.LEFT + self.H_GUTTER <= new_x <= self.RIGHT - self.H_GUTTER:
                player.setx(new_x)
            new_y = player.ycor() + PLAYER_STEP_V * player.v_player_movement
            if self.BOTTOM + self.V_GUTTER <= new_y <= self.TOP - self.V_GUTTER:
                player.sety(new_y)
            self.screen.listen()    
            self.screen.update()

            ## Game loop (enemy movement)
            enemy.start_moving()
            if enemy.ycor() >= self.TOP - self.V_GUTTER or enemy.ycor() <= self.BOTTOM + self.V_GUTTER:
                current_heading_v = enemy.heading()
                enemy.setheading(current_heading_v + random.randint(35, 70))
            if enemy.xcor() <= self.LEFT - self.H_GUTTER or enemy.xcor() >= self.RIGHT + self.H_GUTTER:
                current_heading_h = enemy.heading()
                enemy.setheading(current_heading_h + random.randint(35, 70))
            self.screen.update()
                
            ## Game Over
            if PLAYER_ATTEMPTS == 0: 
                text.clear()
                scoreboard.clear()
                text.write(
                    f'Game Over',
                    font = ("Courier", 15, "bold")
                )
                scoreboard.write(
                    f'Total: {score}',
                    font = ("Courier", 15, "bold")
                )
                self.window.update()
                time.sleep(5)
                game_end = True
            ouch()    
            collect()
            addcoin()
        else:
            exit()       

        ## Kills script on exiting
        turtle.done()
        self.window.mainloop()
