## Imports
import pygame
import time
import random

## Set player speed
speed = 33

## Define window area
screen_x = 1024
screen_y = 768

## Set color space (custom)
dark_blue = pygame.Color(0, 0, 25)
white = pygame.Color(255, 255, 255)
teal = pygame.Color(0, 135, 153)
green = pygame.Color(0, 251, 68)
pink = pygame.Color(221, 0, 108)

## Initialize pygame libraries
pygame.init()

## Sound Effect Setup
collect_sound = pygame.mixer.Sound("sounds/yoshi-eat.wav")
collide_sound = pygame.mixer.Sound("sounds/slam.wav")

## Music Setup
bg_music = pygame.mixer.music.load("music/xtremebgm.wav")
pygame.mixer.music.play(-1)

## Set app icon
appicon = pygame.image.load("icons/caterpillar_xtreme.png")
pygame.display.set_icon(appicon)

## Initialize window
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Hungry Caterpillar X-Treme")
framerate = pygame.time.Clock()

## Initialize snake object
snake_position = [100, 50]
body = [  [100, 50],
          [90, 50],
          [80, 50],
          [70, 50]
      ]

## Initialize fruit object
fruit_position = [random.randrange(1, (screen_x//10)) * 10,
                  random.randrange(1, (screen_y//10)) * 10]
fruit_spawn = True

## Initialize starting direction
direction = "RIGHT"
change_to = direction

## Initialize score
score = 0

## Initialize score counter
def show_score(choice, color, font, size):
    '''Takes the value of "score" and displays it during gameplay'''
    score_font = pygame.font.SysFont("papyrus", 20)
    score_surf = score_font.render('Score: ' + str(score), True, white)
    score_rect = score_surf.get_rect()
    screen.blit(score_surf, score_rect)

## Game over function
def game_over():
    '''Stops music, plays impact sound, shows final score, and then exits'''
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(collide_sound)
    death_font = pygame.font.SysFont("papyrus", 50)
    death_surf = death_font.render("Final Score: " + str(score), True, pink)
    death_rect = death_surf.get_rect()
    death_rect.midtop = (screen_x/2, screen_y/4)
    screen.blit(death_surf, death_rect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()

## Gameplay loop
while True:

    ## Keybinds
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    ## Direction check
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    ## Movement values
    if direction == "UP":
        snake_position[1] -= 10
    if direction == "DOWN":
        snake_position[1] += 10
    if direction == "LEFT":
        snake_position[0] -= 10
    if direction == "RIGHT":
        snake_position[0] += 10
    body.insert(0, list(snake_position))

    ## Collect fruit
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 2
        pygame.mixer.Sound.play(collect_sound)
        fruit_spawn = False
    else:
        body.pop()
    
    ## Replace collected fruit
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (screen_x//10)) * 10,
                          random.randrange(1, (screen_y//10)) * 10]   
    fruit_spawn = True

    ## Set background color
    screen.fill(dark_blue)

    ## Draw snake
    for pos in body:
        pygame.draw.rect(screen, teal,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    
    ## Draw fruit
    pygame.draw.rect(screen, green, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
    
    ## Game over
    if snake_position[0] < 0 or snake_position[0] > screen_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > screen_y - 10:
        game_over()
    for block in body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    ## Draw scoreboard
    show_score(1, white, 'papyrus', 20)

    ## Draw screen
    pygame.display.update()
    framerate.tick(speed)