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
    
blackCircle = Circle(50, "black", (300,250), 10)
blueCircle = Circle(50, "blue", (190,250), 10)
redCircle = Circle(50, "red", (410,250), 10)
yellowCircle = Circle(50, "yellow", (245,300), 10)
greenCircle = Circle(50, "green", (355,300), 10)


#To make the output stay on the screen until cross button is pressed
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    screen.fill("white")
    blackCircle.draw()
    blueCircle.draw()
    redCircle.draw()
    yellowCircle.draw()
    greenCircle.draw()

    pygame.display.update()