import pygame
from pygame.locals import *
from World import *
from Player import *
from Walls import *
from util import *
from processes import *
pygame.init()

w, h = 1000, 700
screen = pygame.display.set_mode([w, h])

running = True

world = World()
player = Player()
mode2D = True
moving_mode = 3 #1, 2, 3, 4
while running:
    screen.fill((20,0,20))
    player.dir = player.dir/norm(player.dir)

    if moving_mode== 1:
        vec = player.dir
        
    if moving_mode== 2:
        vec = player.orth()
        
    if moving_mode== 3:
        vec = - player.dir
        
    if moving_mode== 4:
        vec = -player.orth()
        
        


    player.loc +=vec*player.speed
    world.display(screen, player, width =w, height = h, mode2D=mode2D)
    # player.display(screen, mode2D=mode2D)

    # refresh_cursor(width = w)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            player.move(event)

            if event.key == pygame.K_z:
                moving_mode = 1
            if event.key == pygame.K_q:
                moving_mode = 2
            if event.key == pygame.K_s:
                moving_mode = 3
            if event.key == pygame.K_d:
                moving_mode = 4

    player.turn(pygame.mouse.get_rel())
    pygame.display.flip()
    player.s+=.000
    player.l = player.s/.5444
    print(f'player.height = {player.height}')
    print(f'player.s = {player.s }')

pygame.quit()