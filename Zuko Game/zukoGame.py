import pygame
pygame.init()
#Defining width and length of screen
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Zuko Game")

bg = pygame.image.load("Zuko Game/ZukoBg.png")
bullet = pygame.image.load("Zuko Game/Bullet.png")
zuko = pygame.image.load("Zuko Game/Zuko.png")
parachute = pygame.image.load("Zuko Game/Parachute.png")

parachutes = []

zukox = 500
zukoy = 500

#To make the output stay on the screen until cross button is pressed
def displayParachute():
    for i in range(7):
        x = 130 * i + 33
        y = 20
        parachutes.append([x,y])

displayParachute()

while True:
    screen.blit(bg, (0,0))
    screen.blit(zuko, (zukox,zukoy))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    for i in parachutes:
        screen.blit(parachute,(i[0], i[1]))
    pygame.display.update()