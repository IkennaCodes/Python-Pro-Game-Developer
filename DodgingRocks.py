import pygame
import random
import time

pygame.init()

# make score variable
score = 0

# set the sizes of the screen and display
screenWidth = 800
screenHeight = 700
screen = pygame.display.set_mode((screenWidth,screenHeight))

# set title of game
pygame.display.set_caption("Dodging the Rocks")

# set the dimensions of player
playerWidth = 60
playerHeight = 60

# set the location of the playermand speed
playerx = 400
playery = 640
playerSpeed = 10

# set dimensions of rock and speed
rockWidth = 40
rockHeight = 40
rockSpeed = 5

# create a list of rocks to be stored
rocks = []

# create a function on how to create the rocks
def createRock():
    # set a random location to appear on the x and range
    x = random.randrange(20,780)
    # it will fall based on the rock height continuously
    y = -rockHeight
    # creates the shape for the rock
    return pygame.Rect(x, y, rockWidth, rockHeight)

# main function
def main():
    # game should be contiuous
    run = True
    global playerx, playery, score, playerRect
    while run:
        screen.fill("white")
        font = pygame.font.SysFont("Lexend", 40)
        text = font.render("Score = " + str(score), True, "blue")
        screen.blit(text, (200,100))

        # endoreses movement
        for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()
                keyPressed = pygame.key.get_pressed()
                if keyPressed[pygame.K_LEFT]:
                    playerx -= 30
                    keyPressed = pygame.key.get_pressed()
                elif keyPressed[pygame.K_RIGHT]:
                    playerx += 30
            
        for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()
        # set player appearance
        playerRect = pygame.Rect(playerx, playery, playerWidth, playerHeight)

        # when it collides take away score
   #     hitting = pygame.sprite.spritecollide(playerRect,rocks,True)
    #    for i in hitting:
    #        score = score - 1

    # whenever the random value is 1 create a rock and put it in the list
        if random.randint(1,30) == 1:
             rocks.append(createRock())
             # loop to make it fall
        for i in rocks:
            i.y += rockSpeed
            # set appearance
            pygame.draw.rect(screen, "gray", i)

            if playerRect.colliderect(i):
                print("Game over! Rocks collided!")
                screen.fill("white")
                font = pygame.font.SysFont("Lexend", 100)
                text = font.render("GAME OVER!" + str(score), True, "red")
                screen.blit(text, (400,400))
                time.sleep(2)
                #exit()
                 
        pygame.draw.rect(screen, "orange", playerRect)
        pygame.display.update()

main()
                  
             