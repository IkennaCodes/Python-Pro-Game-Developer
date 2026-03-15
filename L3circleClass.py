import pygame
pygame.init()
#Defining width and length of screen
screen = pygame.display.set_mode((600,600))

class Circle():
    def __init__(self, radius, color, pos, width):
        self.radius = radius
        self.color = color
        self.pos = pos
        self.width = width
        self.surface = screen

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.pos, self.radius, self.width)
    
yellowCircle = Circle(50, "yellow", (100,100), 8)
bigCircle = Circle(100, "white", (300,300), 0)

#To make the output stay on the screen until cross button is pressed
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    screen.fill("orange")
    yellowCircle.draw()
    bigCircle.draw()
    pygame.display.update()