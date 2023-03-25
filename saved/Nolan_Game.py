import pygame
from pygame.locals import *
from World import *
from Player import *
from Walls import *

pygame.init()

w, h = 500, 500
screen = pygame.display.set_mode([w, h])

running = True

world = World()
player = Player()
mode2D = True

while running:
    screen.fill((0,0,0))
    world.display(screen, player, mode2D=mode2D)
    player.display(screen, mode2D=mode2D)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            player.move(event)
        
    player.turn(pygame.mouse.get_rel())
    pygame.display.flip()

pygame.quit()