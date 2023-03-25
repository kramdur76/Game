

class Wall: 
    segment = [[0,0], [1, 10]]
    colour = (255,255,0)
    height = 2

    def __init__(self,a,b,c,d):
        self.segment = [(a,b),(c,d)]
