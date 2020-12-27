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

    def snakeMove(self):
        if self.dir == "UP":
            self.y -= self.vel
            if self.y == 0:
                self.y = screenSize

        elif self.dir == "DOWN":
            self.y += self.vel
            if self.y == screenSize:
                self.y = 0

        elif self.dir == "RIGHT":
            self.x += self.vel
            if self.x == screenSize:
                self.x = 0

        elif self.dir == "LEFT":
            self.x -= self.vel
            if self.x == 0:
                self.x = screenSize


player = snake()

def reDrawGameWindow():
    display.fill((0,0,0))
    player.snakeMove()
    pygame.draw.rect(display, (0, 255,0), [player.x, player.y, player.width, player.height])
    pygame.display.update()
    print(player.x, player.y)

running = True
# Game loop
while running:
    pygame.time.delay(25) # Delay 25 miliseconds

    for event in pygame.event.get():
        # Checks for quit command
        if event.type == pygame.QUIT:
            running = False
    
    # Dictionary of key presses
    keys = pygame.key.get_pressed()

    # This part handles controls for the snake
    if keys[pygame.K_LEFT]:
        if player.dir == ("UP" or "DOWN"):
            player.dir = "LEFT"

    elif keys[pygame.K_RIGHT]:
        if player.dir == ("UP" or "DOWN"):
            player.dir = "RIGHT"
    
    elif keys[pygame.K_UP]:
        if player.dir == ("LEFT" or "RIGHT"):
            player.dir = "UP"

    elif keys[pygame.K_DOWN]:
        if player.dir == ("LEFT" or "RIGHT")

    reDrawGameWindow()

quit()