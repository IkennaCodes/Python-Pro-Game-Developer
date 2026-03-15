import pygame
pygame.init()
#Defining width and length of screen
screen = pygame.display.set_mode((600,600))

class Rect():
    def __init__(self, color, dimensions):
        self.dimensions = dimensions
        self.color = color
        self.surface = screen

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.dimensions)

#To make the output stay on the screen until cross button is pressed
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    screen.fill("orange")
    yellowRect = Rect("yellow", (100, 100, 100, 200))
    yellowRect.draw()
    pygame.display.update()