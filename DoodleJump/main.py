import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

GRAVITY_TIME = 0.4
jump_strength = -10

#Test_player: a rectangle
player = pygame.Rect(180, 500, 30, 30)
velocity_y = 0

platforms = [
    pygame.Rect(150, 550, 100, 10),
    pygame.Rect(200, 420, 100, 10),
    pygame.Rect(100, 290, 100, 10),
]
#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:    
            running = False
    # Inputs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    #Here's the physics of the game
    velocity_y += GRAVITY_TIME
    player.y += velocity_y

    # The player can bounce only when they are descending
    if velocity_y > 0:
        for plat in platforms:
            if player.colliderect(plat) and player.bottom <= plat.bottom + velocity_y:
                velocity_y = jump_strength
                player.bottom = plat.top

    # This is the drawing part
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 150, 0), player)
    for plat in platforms:
        pygame.draw.rect(screen, (100, 100, 100), plat)

#Finish the job and turn off the window
pygame.quit()
sys.exit()
