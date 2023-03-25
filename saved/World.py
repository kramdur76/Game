import pygame
from Walls import *
from util import *
import random as r
import numpy as np

class World:

    walls = []

    background_color = (100, 0, 100)
    def __init__(self):
        w=500
        for i in range(2):
            x=r.randint(0, 1)
            a = r.randint(0, 10)*w/10
            b = r.randint(0, 10)*w/10 
            c = r.randint(0, 10)*w/10
            d = r.randint(0, 10)*w/10
            if x==0:
                a=c
            else:
                b=d
            self.walls.append(Wall(a, b, c, d))
        
        

    def display(self, screen, player, mode2D = True):
        w=500 #TODO : changer
        if True:# Affichage en 2D
            for i in self.walls :
                pygame.draw.line(screen, (i.colour), i.segment[0], i.segment[1])
        if True: #Affichage 3D
            n = player.pix
            orth = player.orth()
            P = player.loc
            d = player.dir
            s = player.s
            l = player.l
            color = (0, 0, 0)

            check_mate = []#nom un peu incongru mais c'est la liste de toutes les intersections les plus proches du player
            for i in range(n): #8===============================D
                V = P+d*s+orth*l*(1/2-i/n)#chibre
                PV = V-P #bite
                inter = None #intersection la plus proche
                
                #Check tous les murs pour une intersection avec le rayon (P, P->V)
                for i in range(len(self.walls)):
                    wall = self.walls[i]
                    A, B = tuple(wall.segment)
                    A = np.array(A)
                    B = np.array(B)
                    AB = B-A
                    det = AB[1]*PV[0]-AB[0]*PV[1]

                    if det==0:
                        continue


                    M1 = np.array(
                    [[-PV[1], PV[0]],
                    [-AB[1], AB[0]]]
                    )/det
                    R = P-A
                    X = np.matmul(M1, R)
                    alpha = X[0]

                    G = A + alpha*AB

                    
                    if np.dot(player.dir, G-P)<0:
                        continue

                    dot = np.dot(G-A, AB)
                    if dot<0 or dot/norm(A-G)<norm(AB):
                        continue
                    #TODO : IL FAUT VÉRIFIER SI L'INTERSECTION G EST DANS LE SEGMENT? LA ON SAIT JUSTE QU'IL EST SUR LA DROITE AB
                    # print(f'inter={inter}')
                    # print(f'P={P}')
                    # print(f'G={G}')
                    

                        
                    try:
                        if norm(inter-P) > norm(G-P):
                            inter = G
                    except: 
                        inter = G
                    finally:
                        1
                check_mate.append(inter)

            assert len(check_mate) == n

            dist = 1.7e308
            # print(f"check_mate={check_mate}")
            for i in range(len(check_mate)):
                b=False
                color = self.background_color 
                point = check_mate[i] #le point d'intersection sur le mur, il faut afficher la bande de pixels verticale par rapport à lui
                
                if type(check_mate[i]) != type(None):
                    D = norm(P-check_mate[i])-s
                    K=400
                    color = (1-D/K)*255
                    if color<0:
                        color=0
                    color = int(color)
                    color = tuple([color]*3)

                    h = n*s/(s+D)
                    for j in range(int(h)):

                        c = w/n
                        x = i*w/n
                        print(f'color = {color}')
                        r = pygame.Rect(x, -j*c+w/2+h*c/2, c, c)
                        pygame.draw.rect(screen, color, r)
                
