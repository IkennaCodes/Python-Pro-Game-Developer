import pygame
import time
from pygame.locals import *
pygame.init()
#Defining width and length of screen
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Controlling Rocket in SPACE!")
rocket = pygame.image.load("Rocket Screen Project/rocket.png")
spacebg = pygame.image.load("Rocket Screen Project/space.png")
#To make the output stay on the screen until cross button is pressed
objectx = 300
objecty = 300
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if objecty > 550:
            exit()
        if i.type == pygame.KEYDOWN:
            if i.key == K_UP:
                objecty -= 10
            if i.key == K_DOWN:
                objecty += 10
            if i.key == K_LEFT:
                objectx -= 10
            if i.key == K_RIGHT:
                objectx += 10
            

    objecty += 1
    time.sleep(0.01)

    screen.blit(spacebg,(0,0))
    screen.blit(rocket,(objectx,objecty))
    pygame.display.update()