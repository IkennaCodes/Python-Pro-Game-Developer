import pygame
import time
from pygame.locals import *
pygame.init()
#Defining width and length of screen
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Controlling DODGEBALL in COURT!")
ball = pygame.image.load("Dodgeball Screen Project/images/bomb.png")
basketbg = pygame.image.load("Dodgeball Screen Project/images/basketballbg.jpg")
#To make the output stay on the screen until cross button is pressed
objectx = 300
objecty = 300
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if objecty > 500:
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
            

    objecty += 3
    time.sleep(0.1)

    screen.blit(basketbg,(0,0))
    screen.blit(ball,(objectx,objecty))
    pygame.display.update()