# importing the things
import pygame
import time

pygame.init()

#Defining width and length of screen
screen = pygame.display.set_mode((600,600))

#creating first image
pygame.display.set_caption("Mothers Day")
image1 = pygame.image.load("Mothers Day/images/motherday.png")
finalImage1 = pygame.transform.scale(image1,(600,600))

#To make the output stay on the screen until cross button is pressed
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    #displaying first image with text
    font = pygame.font.SysFont("Lexend", 40)
    text = font.render("Happy Mothers Day!", True, "orange")
    screen.blit(finalImage1, (0,0))
    screen.blit(text, (200,200))
    pygame.display.update()
    time.sleep(2)

    #creating second image
    image2 = pygame.image.load("Birthday Animation/images/cake.jpg")
    finalImage2 = pygame.transform.scale(image2,(600,600))

    #displaying second image with text
    font = pygame.font.SysFont("Lexend", 40)
    text = font.render("Have a great day!", True, "blue")
    screen.blit(finalImage2, (0,0))
    screen.blit(text, (200,100))
    pygame.display.update()
    time.sleep(2)

    #creating third image
    image3 = pygame.image.load("Birthday Animation/images/gift.jpg")
    finalImage3 = pygame.transform.scale(image3,(600,600))

    #displaying the third image with text
    font = pygame.font.SysFont("Lexend", 40)
    text = font.render("You deserve to be loved!", True, "red")
    screen.blit(finalImage3, (0,0))
    screen.blit(text, (200,200))
    pygame.display.update()
    time.sleep(2)