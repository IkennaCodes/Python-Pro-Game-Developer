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
score = 0

bulletx = zukox
bullety = zukoy

fireball = False

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

    font = pygame.font.SysFont("Lexend", 40)
    text = font.render("score = " + str(score), True, "yellow")
    screen.blit(text, (100,100))
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_LEFT]:
            zukox -= 30
            keyPressed = pygame.key.get_pressed()
        elif keyPressed[pygame.K_RIGHT]:
            zukox += 30
        elif keyPressed[pygame.K_SPACE]:
            if not fireball:
                bulletx = zukox
                bullety = zukoy
                fireball = True

    for i in parachutes:

        screen.blit(parachute,(i[0], i[1]))
        i[1] += 1 - 0.5
        parachute_rect = pygame.Rect(i[0], i[1], 60, 60)
        bullet_rect = pygame.Rect(bulletx, bullety, 20, 40)
        if fireball and parachute_rect.colliderect(bullet_rect):
            parachutes.remove(i)
            score = score + 1
            fireball = False
            
    if fireball:
        bullety -= 7
        screen.blit(bullet, (bulletx, bullety))
    pygame.display.update()