import pygame
pygame.init()
#Defining width and length of screen
screen = pygame.display.set_mode((800,800))
EcoBg = pygame.image.load("Recycle Marathon/ecobg.png")

pygame.display.set_caption("Recycle Marathon")
#To make the output stay on the screen until cross button is pressed
# sprites have 4 parts, x,y,w,h
class Bin(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("Recycle Marathon/recyclebin.png")
        # rectangle base of the image
        self.rect = self.image.get_rect()

bin = Bin()
bin.rect.x = 100
bin.rect.y = 100

while True:
    screen.blit(EcoBg, (0,0))
    bin.draw()
    pygame.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()