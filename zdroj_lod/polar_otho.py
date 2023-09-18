from math import *
def polaToOrtho(rho, eps):
    x = rho * cos(eps)
    y = rho * sin(eps)

    return x,y

def orthoToPolar(x, y):
    rho = (x**2 + y**2)**0.5
    eps = atan2(y, x)

    return rho, eps

x = 1
y = 1

rho, eps = polaToOrtho(x, y)
print(rho, eps)

x2, y2 = orthoToPolar(rho, eps)
print(x2, y2)