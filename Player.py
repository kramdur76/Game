import numpy as np
import pygame
from util import *

class Player:
    loc = np.array([250.,250.])
    dir = np.array([1,0])

    length = 20
    butt=5
    speed = 50
    height = 1.

    #optique
    s = 1 #distance player-écran, distance focale
    l = 2 #longueur de l'écran
    pix = 250 #nombre de pixels en longueur 
    def __init__(self):
        # self.l = self.s/.6185 #pour avoir l'angle de vue de l'oeil humain 150°
        1
    
    def orth(self):
        d = self.dir
        return np.array([d[1], -d[0]])
    
    def display(self,screen, mode2D=True):
        """
        Affiche le player en 2D sur l'écran screen, sous forme de petit triangle (mignon)
        """
        if not mode2D:
            return

        self.dir = normalize(self.dir)
        orth = self.orth()

        # print(f"dir {self.dir}")
        a = self.loc + self.dir*self.length

        b = self.loc + orth*self.butt
        c = self.loc - orth*self.butt
        # print(a)
        pygame.draw.polygon(screen, (255,0,0), [tuple(a),tuple(b),tuple(c)])
    
    def move(self, e):        
        """
        à appeler à chaque fois qu'on presse le clavier
        """
        if e.key == pygame.K_z:
            self.loc+=self.speed*self.dir
            moving_mode = 1

        
        if e.key == pygame.K_s:
            self.loc-=self.speed*self.dir
            moving_mode = 2

        orth = self.orth()
        if e.key == pygame.K_q:
            self.loc += orth*self.speed
            moving_mode = 3

        if e.key == pygame.K_d:
            self.loc -= orth*self.speed
            moving_mode = 4
    
    def move2(self, e):
        self.loc += self.dir*self.speed

    def turn(self, rel):
        x=rel[0]
        theta = x/80
        s, c = np.sin(theta), np.cos(theta)
        R= np.array(((c, -s), (s, c)))
        self.dir =  np.matmul(R, self.dir)
        self.dir = normalize(self.dir)

    def turn2(self, rel):
        G = pygame.mouse.get_pos()
        P = self.loc
        self.dir = G-P
        self.dir = normalize(self.dir)
    