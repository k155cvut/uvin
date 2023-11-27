from math import *

#Sude vs liche
a = 5
if a%2 == 0:
    print('Sude')
else:
    print('Liche')
    
res = 'Sude' if a%2 == 0 else 'Liche'

#Kladne vs zaporne
a = -0
if a < 0:
    print('Zaporne')
elif a > 0:
    print('Kladne')
else:
    print('Ani kladne, ani zaporne')
    
res = 'Zaporne' if a < 0 else 'Kladne' if a > 0 else 'Ani'
print(res)
    
#Smernik
x1 = 0
y1 = 0
x2 = 1
y2 = 1

#Souradnicove rozdily
dx = x2 - x1
dy = y2 - y1

#Vypocet phi
phi = abs(atan(dy/dx)) * 180 / pi

#1 kvadrant
if (dx > 0) and (dy > 0):
    sigma = phi

#2 kvadrant
elif (dx < 0) and (dy > 0):
    sigma = 180 - phi

#3 kvadrant
elif (dx < 0) and (dy < 0):
    sigma = 180 + phi

#4 kvadrant
else:
    sigma = 360 - phi

print(sigma)
    
#Minima ze 3 cisel
a=3
b=-7
c=-1

#Var1
#A is smallest
if (a<b) and (a<c):
    m = a
if (b<a) and (b<c):
    m = b
if (c<a) and (c<b):
    m = c
print(m)

#Var2
#A is smallest
if (a<b) and (a<c):
    m = a
elif (b<a) and (b<c):
    m = b
else:
    m = c
print(m)

#Var3
#A is smallest
if (a<b) and (a<c):
    m = a
elif b < c:
    m = b
else:
    m = c

#Ternary operator
min = a if (a < b) and (a < c) else b if (b < c) else c

#Var4
if (a<b):
    m = a
else:
    m = b
if c < m:
    m = c

#y = log((5 - x) / sqrt(x^2 - 5x + 14)))
#y = log((5 - x) / (x^2 - 5x + 14)))