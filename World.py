import pygame
from Walls import *
from util import *
import random as r
import numpy as np
from numpy.linalg import inv

class World:

    walls = []

    background_color = (100, 0, 100)
    def __init__(self):
        with open("walls_data.txt", "r") as f:
            segments = []
            for line in f.readlines():
                points = []
                for i in line.split(";"):
                    print(f"i = {i}")
                    x, y = i.split(",")
                    x = float(x)
                    y = float(y)
                    points.append(np.array([x, y])*10)
                segments += polygon(points)
            
            for seg in segments:
                a, b, c, d = tuple(seg[0])+tuple(seg[1])
                self.walls.append(Wall(a, b, c, d))
        
        
        

    def display(self, screen, player, width=500, height = 500, mode2D = True):
        w=width #TODO : changer
        player.dir = player.dir/norm(player.dir)
        if False:# Affichage en 2D
            for i in self.walls :
                pygame.draw.line(screen, (i.colour), i.segment[0], i.segment[1])
        if True: #Affichage 3D

            #Déclaration des variables --------------------
            n = player.pix
            orth = player.orth()
            P = player.loc
            d = player.dir
            s = player.s
            l = player.l
            color = (0, 0, 0)


            check_mate = []#nom un peu incongru mais c'est la liste de toutes les intersections (la plus proche à chaque fois) du player, pour chaque rayon
            for i in range(n): #8===============================D
                V = P+d*s+orth*l*(1/2-i/n)#position du pixel dans l'espace du player
                PV = V-P #rayon
                inter = None #intersection la plus proche
                
                #Check tous les murs pour une intersection avec le rayon PV
                for j in range(len(self.walls)):
                    wall = self.walls[j]
                    A, B = tuple(wall.segment)
                    A = np.array(A)*np.array([2, 1])
                    B = np.array(B)*np.array([2, 1])
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

                    G = A + alpha*AB #intersection

                    
                    if np.dot(player.dir, G-P)<0:
                        continue

                    dot = np.dot(G-A, AB)
                    if dot<0 or norm(A-G)>norm(AB):
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
                    K=800
                    color = col(D)
                    if color<0:
                        color=0
                        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                    color = int(color)
                    color = tuple([color]*3)

                    H = 10# hauteur du mur
                    h = height*H/(D/s-1) #taille du mur à l'écran en longueur réelle
                    cx = w/n #longueur en pixels d'un pixel virtuel de caméra virtuelle
                    cy = height/n
                    x = i*w/n #absisse du rectangle à dessiner
                    T = player.height

                    AB = np.array([0, l])
                    SF = np.array([s-D, T])
                    SA = np.array([-D, T-l/2])
                    AB = np.array([0, -l/2])
                    X = np.matmul(inv(np.array([AB, SF])), SA)
                    BY = (1 - norm(X[0]*AB)/l)*height
                    y = height/2-T/(D/s-1)
                    y=BY
                    r = pygame.Rect(x, y, cx, h*cy)
                    # r = pygame.Rect(x, y, cx, h*height/player.l, color=(0, 0, 0))
                    pygame.draw.rect(screen, color, r)
                
