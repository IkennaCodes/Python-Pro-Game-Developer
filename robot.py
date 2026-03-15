import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    #head
    pygame.draw.rect(screen, "grey", pygame.Rect(180,180,150,180))
    
    #torso
    pygame.draw.rect(screen, "grey", pygame.Rect(205,80,100,100))
    pygame.draw.rect(screen, "#505154FF", pygame.Rect(195,195,120,150))

    #legs
    pygame.draw.rect(screen, "grey", pygame.Rect(180,350,50,100))
    pygame.draw.rect(screen, "grey", pygame.Rect(280,350,50,100))

    #arms
    pygame.draw.rect(screen, "grey", pygame.Rect(130,130,50,100))
    pygame.draw.rect(screen, "grey", pygame.Rect(330,130,50,100))

    #eyes
    pygame.draw.rect(screen, "#505154FF", pygame.Rect(270,110,20,20))
    pygame.draw.rect(screen, "#505154FF", pygame.Rect(220,110,20,20))

    #mouth#
    pygame.draw.rect(screen, "#505154FF", pygame.Rect(230,150,60,10))

    #ears
    pygame.draw.rect(screen, "grey", pygame.Rect(190,110,15,40))
    pygame.draw.rect(screen, "grey", pygame.Rect(305,110,15,40))

    #antenna
    pygame.draw.rect(screen, "grey", pygame.Rect(270,40,20,40))
    pygame.draw.rect(screen, "grey", pygame.Rect(220,40,20,40))
    


    pygame.display.update()