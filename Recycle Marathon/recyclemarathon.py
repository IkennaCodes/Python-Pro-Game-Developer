import pygame
import random
pygame.init()
#Defining width and length of screen
screen = pygame.display.set_mode((800,800))
EcoBg = pygame.image.load("Recycle Marathon/ecobg.png")
score = 0

pygame.display.set_caption("Recycle Marathon")
#To make the output stay on the screen until cross button is pressed
# sprites have 4 parts, x,y,w,h
class Bin(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("Recycle Marathon/recyclebin.png")
        self.image = pygame.transform.scale(self.image,(30,40))
        # rectangle base of the image
        self.rect = self.image.get_rect()

class Recyclable(pygame.sprite.Sprite):
    def __init__ (self, img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image,(30,30))
        # rectangle base of the image

        self.rect = self.image.get_rect()

class NonRecyclable(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("Recycle Marathon/plasticbag.png")
        self.image = pygame.transform.scale(self.image,(30,40))
        # rectangle base of the image
        self.rect = self.image.get_rect()

recyclableItems = pygame.sprite.Group()
nonRecyclableItems = pygame.sprite.Group()
allSpriteItems = pygame.sprite.Group()

images = ["Recycle Marathon/paperbag.png", "Recycle Marathon/pencil.png", "Recycle Marathon/woodenbox.png"]


bin = Bin()
bin.rect.x = 100
bin.rect.y = 100

allSpriteItems.add(bin)
for i in range(30):
    item = Recyclable(random.choice(images))
    item.rect.x = random.randint(50,750)
    item.rect.y = random.randint(50,750)
    recyclableItems.add(item)
    allSpriteItems.add(item)

for i in range(20):
    item1 = NonRecyclable()
    item1.rect.x = random.randint(50,750)
    item1.rect.y = random.randint(50,750)
    nonRecyclableItems.add(item1)
    allSpriteItems.add(item1)



while True:
    screen.blit(EcoBg, (0,0))
    font = pygame.font.SysFont("Lexend", 40)
    text = font.render("Score = " + str(score), True, "blue")
    screen.blit(text, (200,100))
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_LEFT]:
            bin.rect.x -= 15
            keyPressed = pygame.key.get_pressed()
        elif keyPressed[pygame.K_RIGHT]:
            bin.rect.x += 15
            keyPressed = pygame.key.get_pressed()
        elif keyPressed[pygame.K_UP]:
            bin.rect.y -= 15
            keyPressed = pygame.key.get_pressed()
        elif keyPressed[pygame.K_DOWN]:
            bin.rect.y += 15
        itemsHitList = pygame.sprite.spritecollide(bin,recyclableItems, True)
        plasticItemsHitList = pygame.sprite.spritecollide(bin,nonRecyclableItems, True)
        for i in itemsHitList:
            score = score + 1
        for i in plasticItemsHitList:
            score = score - 1
    allSpriteItems.draw(screen)
    pygame.display.update()