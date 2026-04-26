import pygame
from pygame.locals import *
pygame.init()
#Defining width and length of screen
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("spaceinvadersgame")
bg = pygame.image.load("Space Invaders/space.png")
ship1 = pygame.image.load("Space Invaders/yellowship.png")
ship2 = pygame.image.load("Space Invaders/redship.png")

yellowship = pygame.transform.rotate(pygame.transform.scale(ship1,(60,40)),90)
redship = pygame.transform.rotate(pygame.transform.scale(ship2,(60,40)), 270)

def drawwindow():
    screen.blit(bg, (0,0))
    screen.blit(yellowship, (50,300))
    screen.blit(redship, (950,300))
    pygame.display.update()

#To make the output stay on the screen until cross button is pressed
def main():
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
        drawwindow()
        pygame.display.update()
main()