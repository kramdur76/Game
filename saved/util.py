
def norm(v):
    return (v[0]**2+v[1]**2)**.5
def normalize(v):
        s=0
        for i in v:
            s+=abs(i)
        if s==0:
            return 0
        return v/norm(v)