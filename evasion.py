## Imports
from gameassets.player import Player, turtle, PLAYER_STEP_V, PLAYER_STEP_H
from gameassets.enemy import Enemy, random 
from gameassets import collectables
from gameassets import inner_workings
from gameassets.collectables import Item, random
import time

## Game window
window = turtle.Screen()
window.tracer(0)
window.setup(width = 640, height = 480)
window.bgcolor("black")
window.title("Evasion")
LEFT = -window.window_width() / 2
RIGHT = window.window_width() / 2
TOP = window.window_height() / 2
BOTTOM = -window.window_height() / 2
H_GUTTER = 0.025 * window.window_width()
V_GUTTER = 0.025 * window.window_height()

## You
PLAYER_ATTEMPTS = 3
player = Player()
Baddie = []
enemy = Enemy()
Coins = []
score = 0

## Adds coin (worth 10 points)
def addcoin():
    if len(Coins) == 0:
        newcoin = collectables.Item()
        Coins.append(newcoin)

## Collect coin
def collect():
    global score
    for Checking in Coins:
        if inner_workings.hit_check(player, Checking, 20):
            Checking.hideturtle()
            Coins.remove(Checking)
            score += 10

## Ouch
def ouch():
    global score
    global PLAYER_ATTEMPTS
    if inner_workings.hit_check(player, enemy, 20):
        PLAYER_ATTEMPTS -= 1
        score -= 100
        if score <= 100:
            score = 0
            window.update()
        current_heading_h = enemy.heading()
        enemy.setheading(current_heading_h + random.randint(35, 70))
        player.setposition(0, 0)
        window.update()    

## Text (lives counter)
lives = turtle.Turtle()
lives.penup()
lives.hideturtle()
lives.setposition(LEFT * 0.1, TOP * 0.9)
lives.color("orange")

## Text (score)
scoreboard = turtle.Turtle()
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.setposition(RIGHT * 0.6, TOP * 0.9)
scoreboard.color("red")

## Text (timer)
text = turtle.Turtle()
text.penup()
text.hideturtle()
text.setposition(LEFT * 0.9, TOP * 0.9)
text.color("red")

## Keybinds for controlling the player
window.onkeypress(player.move_player_left, 'Left')
window.onkeypress(player.move_player_right, 'Right')
window.onkeypress(player.move_player_down, 'Down')
window.onkeypress(player.move_player_up, 'Up')
window.onkeypress(turtle.bye, 'Escape')
window.onkeyrelease(player.stop_moving, 'Left')
window.onkeyrelease(player.stop_moving, 'Right')
window.onkeyrelease(player.stop_moving, 'Up')
window.onkeyrelease(player.stop_moving, 'Down')

## Timer initialize
game_end = False
game_timer = time.time()

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
    if LEFT + H_GUTTER <= new_x <= RIGHT - H_GUTTER:
        player.setx(new_x)
    new_y = player.ycor() + PLAYER_STEP_V * player.v_player_movement
    if BOTTOM + V_GUTTER <= new_y <= TOP - V_GUTTER:
        player.sety(new_y)
    window.listen()    
    window.update()

    ## Game loop (enemy movement)
    enemy.start_moving()
    if enemy.ycor() >= TOP - V_GUTTER or enemy.ycor() <= BOTTOM + V_GUTTER:
        current_heading_v = enemy.heading()
        enemy.setheading(current_heading_v + random.randint(35, 70))
    if enemy.xcor() <= LEFT - H_GUTTER or enemy.xcor() >= RIGHT + H_GUTTER:
        current_heading_h = enemy.heading()
        enemy.setheading(current_heading_h + random.randint(35, 70))
    window.update()
        
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
        window.update()
        time.sleep(5)
        game_end = True
    ouch()    
    collect()
    addcoin()
else:
    exit()       

## Kills script on exiting
turtle.done()