import pygame
pygame.init()
#Defining width and length of screen
screen = pygame.display.set_mode((600,600))
screen.fill("white")

pygame.display.update()
class Rect():
    def __init__(self, color, dimensions):
        self.dimensions = dimensions
        self.color = color
        self.surface = screen

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.dimensions)

    def growRect(self, amount):
        x, y, w, h = self.dimensions
        w += amount
        h += amount
        self.dimensions = (x, y, w, h)
        pygame.draw.rect(self.surface, self.color, self.dimensions)
     
redRect = Rect("red", (100, 100, 100, 200))

#To make the output stay on the screen until cross button is pressed
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("white")
            redRect.draw()
            pygame.display.update()
        elif i.type == pygame.MOUSEBUTTONUP:
            screen.fill("white")
            redRect.growRect(15)
            pygame.display.update()