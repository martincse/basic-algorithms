__author__ = 'martin'

def FindSet(x):
    while x != x.Parent:
        x = x.Parent
    return x

def Union(a, b):
    if a.Height <= b.Height:
        if a.Height == b.Height:
            b.Height+=1
        a.Parent = b
    else:
        b.Parent = a
