import pygame
pygame.init()
#Defining width and length of screen
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Connect The Logos")
screen.fill("orange")
pygame.display.update()
Drums = pygame.image.load("Connect the Apps/drums.jpg")
screen.blit(Drums, (120,150))
pygame.display.update()
guitar = pygame.image.load("Connect the Apps/guitar.jpg")
screen.blit(guitar, (120,250))
pygame.display.update()
harp = pygame.image.load("Connect the Apps/harp.jpg")
screen.blit(harp, (120, 350))
pygame.display.update()
piano = pygame.image.load("Connect the Apps/piano.jpg")
screen.blit(piano, (120, 450))
pygame.display.update()
font1 = pygame.font.SysFont("Lexend", 60)
font = pygame.font.SysFont("Lexend", 40)
title = font1.render("Connecting the Instuments!", True, "yellow")
screen.blit(title, (80, 75))
pygame.display.update()
subwaySurfersText = font.render("Piano", True, "white")
screen.blit(subwaySurfersText, (300, 180))
pygame.display.update()
templeRunText = font.render("Harp", True, "white")
screen.blit(templeRunText, (300, 280))
pygame.display.update()
candyCrushText = font.render("Drums", True, "white")
screen.blit(candyCrushText, (300, 380))
pygame.display.update()
ludoText = font.render("Guitar", True, "white")
screen.blit(ludoText, (300, 480))
pygame.display.update()

#To make the output stay on the screen until cross button is pressed
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

        if i.type == pygame.MOUSEBUTTONDOWN:
            # wherever you click it gets the position of the mouse
            pos = pygame.mouse.get_pos()
            # black is colour, pos is coordinates, 10 is size, 0 is fill circle
            pygame.draw.circle(screen, "black", (pos), 10, 0)
            pygame.display.update()
        elif i.type == pygame.MOUSEBUTTONUP:
            pos2 = pygame.mouse.get_pos()
            pygame.draw.line(screen, "black", (pos), (pos2), 10)
            pygame.draw.circle(screen, "black", (pos2), 10, 0)
            pygame.display.update()