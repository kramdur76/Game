import numpy as np
import random as r
def norm(v):
    return (v[0]**2+v[1]**2)**.5

def normalize(v):
        s=0
        for i in v:
            s+=abs(i)
        if s==0:
            return 0
        return v/norm(v)

def random_point(w):
    return np.array([r.random()*w, r.random()*w])
def random_polygon(n, w):
    """list of np.segments, segment being list of two np.array points"""
    res = []
    points = [random_point(w) for i in range(n)]
    for i in range(n):
        res.append([points[i-1], points[i]])
    
    return res

def polygon(points):
    """list of np.segments, segment being list of two np.array points"""
    res = []
    for i in range(len(points)):
        res.append([points[i-1], points[i]])
    
    return res


def col(D):
    """couleur du mur en fonction uniquement de sa distance à la caméra"""
    A = 10 #limite en +inf
    B = 255 #valeur en 0
    A, B = B, A
    K = 1/(1/A-1/B)
    C = 1/(B/A-1)
    a=10**(-3.75)
    return K/(np.exp(-a*D)+C)