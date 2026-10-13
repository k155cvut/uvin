#3 types of imports
import math
from math import sqrt 
from math import * 

#1. Distance between two points#
#Input data
xa=10
ya=10
xb, yb = 20, 20 

#Coordinates differences
dx = xb - xa
dy = yb - ya

#Distance
dist = (dx*dx + dy*dy)**0.5
dist = (dx**2 + dy**2)**0.5
dist = sqrt(dx**2 + dy**2)

print('Distance=', dist, 'm')

#2. Deg, min, sec - > angle, V1
deg, min, sec = -45, 34, 26.36
alpha = deg + (min/60) + (sec/3600)
print (alpha)

#2. Deg, min, sec - > angle, V2
deg, min, sec = -45, 34, 26.36
sign = abs(deg)/deg
alpha = abs(deg) + (min/60) + (sec/3600)
alpha_sign = alpha * sign 
print (alpha_sign)

#3. Circle
r = 12.5
O = 2 * pi * r
S = pi * r * r
print(O, S) 
















































67 