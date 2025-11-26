## Imports
import pygame
import time
import random

## Set player speed
speed = 15

## Define window area
screen_x = 640
screen_y = 480

## Set color space (CMYK)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
cyan = pygame.Color(0, 255, 255)
magenta = pygame.Color(255, 0, 255)
yellow = pygame.Color(255, 255, 0)

## Initialize pygame libraries
pygame.init()

## Initialize window
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Hungry Caterpillar")
framerate = pygame.time.Clock()

snake_position = [100, 50]

body = [  [100, 50],
          [90, 50],
          [80, 50],
          [70, 50]
      ]

fruit_position = [random.randrange(1, (screen_x//10)) * 10,
                  random.randrange(1, (screen_y//10)) * 10]
fruit_spawn = True

direction = "RIGHT"
change_to = direction

score = 0

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont("papyrus", 15)
    score_surf = score_font.render('Score: ' + str(score), True, yellow)
    score_rect = score_surf.get_rect()
    screen.blit(score_surf, score_rect)

def game_over():
    death_font = pygame.font.SysFont("papyrus", 50)
    death_surf = death_font.render("Final Score: " + str(score), True, yellow)
    death_rect = death_surf.get_rect()
    death_rect.midtop = (screen_x/2, screen_y/4)
    screen.blit(death_surf, death_rect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    quit()

while True:
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

    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    if direction == "UP":
        snake_position[1] -= 10
    if direction == "DOWN":
        snake_position[1] += 10
    if direction == "LEFT":
        snake_position[0] -= 10
    if direction == "RIGHT":
        snake_position[0] += 10

    body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 5
        fruit_spawn = False
    else:
        body.pop()
    
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (screen_x//10)) * 10,
                          random.randrange(1, (screen_y//10)) * 10]
        
    fruit_spawn = True

    screen.fill(black)

    for pos in body:
        pygame.draw.rect(screen, cyan,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, magenta, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
    
    if snake_position[0] < 0 or snake_position[0] > screen_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > screen_y - 10:
        game_over()

    for block in body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(1, yellow, 'papyrus', 15)

    pygame.display.update()

    framerate.tick(speed)