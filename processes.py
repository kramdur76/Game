"""
les fonctions processus, jsp comme expliquer mais ça permet de mieux ranger
"""
import pygame
import numpy as np
from util import *

def refresh_cursor(width = 500):
    w= width
    pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
    print(f'pygame.mouse.get_cursor() = {pygame.mouse.get_cursor().__dict__}')
    M = pygame.mouse.get_cursor()[1] #Mouse
    M=np.array(M)
    C = np.array([w/2, w/2]) #Center
    print(f'norm(M-C) = {norm(M-C)}')
    if norm(M-C)>=400:
        M = C+(C-M)*380/norm(M-C)
        pygame.mouse.set_cursor(tuple(M))
        