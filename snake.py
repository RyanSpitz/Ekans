import pygame
from pygame.constants import K_UP, QUIT

pygame.init()

screenSize = 800

display = pygame.display.set_mode((screenSize, screenSize))

class snake:
    name = "name"
    width = 20
    height = 20
    x = screenSize/2
    y = screenSize/2
    dir = "UP"
    size = 1
    vel = 5

# Handles movement
    def moveRight(self):
        self.x += self.vel
        if self.x == screenSize:
            self.x = 0

    def moveLeft(self):
        self.x -= self.vel
        if self.x == 0:
            self.x = screenSize

    def moveUp(self):
        self.y -= self.vel
        if self.y == 0:
            self.y = screenSize

    def moveDown(self):
        self.y += self.vel
        if self.y == screenSize:
            self.y = 0


def reDrawGameWindow():
    # Draws black background
    display.fill((0,0,0))
    pygame.draw.rect(display, (0, 255,0), [player.x, player.y, player.width, player.height])
    pygame.display.update()

player = snake()

running = True
# Game loop
while running:
    pygame.time.delay(50)

    pygame.event.pump()
    keys = pygame.key.get_pressed()

    # Check for keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if (keys[pygame.K_RIGHT]):
        player.moveRight()

    if (keys[pygame.K_LEFT]):
        player.moveLeft()

    if (keys[pygame.K_UP]):
        player.moveUp()

    if (keys[pygame.K_DOWN]):
        player.moveDown()


    reDrawGameWindow()

quit()