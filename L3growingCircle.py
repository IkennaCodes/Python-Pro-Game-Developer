import pygame
pygame.init()
#Defining width and length of screen
screen = pygame.display.set_mode((600,600))
screen.fill("white")

pygame.display.update()
class Circle():
    def __init__(self, radius, color, pos, width):
        self.radius = radius
        self.color = color
        self.pos = pos
        self.width = width
        self.surface = screen

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.pos, self.radius, self.width)

    def growCircle(self, r):
        self.radius += r
        pygame.draw.circle(self.surface, self.color, self.pos, self.radius, self.width)

     
blueCircle = Circle(50, "blue", (300,300), 0)

#To make the output stay on the screen until cross button is pressed
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("white")
            blueCircle.draw()
            pygame.display.update()
        elif i.type == pygame.MOUSEBUTTONUP:
            screen.fill("white")
            blueCircle.growCircle(5)
            pygame.display.update()