import pygame
from pygame.locals import *
pygame.init()
#Defining width and length of screen
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("spaceinvadersgame")
bg = pygame.image.load("Space Invaders/space.png")
ship1 = pygame.image.load("Space Invaders/yellowship.png")
ship2 = pygame.image.load("Space Invaders/redship.png")

RED_HIT = pygame.USEREVENT
YELLOW_HIT = pygame.USEREVENT

fps = 60
yellowhealth = 5
redhealth = 5

yellowship = pygame.transform.rotate(pygame.transform.scale(ship1,(60,40)),90)
redship = pygame.transform.rotate(pygame.transform.scale(ship2,(60,40)), 270)

#display the ships and bg on screen
def drawwindow(yellow, red, yellowbullet, redbullet):
    screen.blit(bg, (0,0))
    screen.blit(yellowship, (yellow.x,yellow.y))
    screen.blit(redship, (red.x,red.y))
    for i in yellowbullet:
        pygame.draw.rect(screen, "yellow", i)
    for i in redbullet:
        pygame.draw.rect(screen, "red", i)

    font = pygame.font.SysFont("Lexend", 40)
    text = font.render("Yellow Health = " + str(yellowhealth), True, "yellow")
    screen.blit(text, (100,100))

    font = pygame.font.SysFont("Lexend", 40)
    text1 = font.render("Red Health = " + str(redhealth), True, "red")
    screen.blit(text1, (750,100))

    pygame.display.update()

def yellowshipmovement(keypress, yellow):
    if keypress[pygame.K_a]:
        yellow.x -= 2
    if keypress[pygame.K_d]:
        yellow.x += 2
    if keypress[pygame.K_s]:
        yellow.y += 2
    if keypress[pygame.K_w]:
        yellow.y -= 2


def redshipmovement(keypress, red):
    if keypress[pygame.K_LEFT]:
        red.x -= 2
    if keypress[pygame.K_RIGHT]:
        red.x += 2
    if keypress[pygame.K_DOWN]:
        red.y += 2
    if keypress[pygame.K_UP]:
        red.y -= 2

def handlebullet(yellowbullet, redbullet, yellow, red):
    global yellowhealth, redhealth
    for i in yellowbullet:
        i.x += 5
        if red.colliderect(i):
            redhealth = redhealth - 1
            print(redhealth)
            #generating user event 'RED_HIT'
            yellowbullet.remove(i)
            pygame.event.post(pygame.event.Event(RED_HIT))
            break
    for i in redbullet:
        i.x -= 5
        if yellow.colliderect(i):
            yellowhealth = yellowhealth - 1
            print(yellowhealth)
            #generating user event 'YELLOW_HIT'
            redbullet.remove(i)
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            break

#To make the output stay on the screen until cross button is pressed
def main():
    yellow = pygame.Rect(100,300,60,40)
    red = pygame.Rect(900,300,60,40)
    redbullet = []
    yellowbullet = []
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_LSHIFT:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height, 15, 5)
                    yellowbullet.append(bullet)
                if i.key == pygame.K_RSHIFT:
                    bullet = pygame.Rect(red.x + red.width, red.y + red.height, 15, 5)
                    redbullet.append(bullet)

        #gets you the key thats pressed
        keypress = pygame.key.get_pressed()
        yellowshipmovement(keypress, yellow)
        handlebullet(yellowbullet, redbullet, yellow, red)
        redshipmovement(keypress, red)
        drawwindow(yellow, red, yellowbullet, redbullet)
        pygame.display.update()
main()