#Boolean operators
>>> x = (0,1)
>>> not(x[0])
True
>>> not(x[1])
False
>>> int(True)
1
>>> int(False)
0
>>> bool(0)
False
>>> bool(1)
True

>>> x1=(0,0,1,1)
>>> x2 = (0,1,0,1)
>>> y = x1[0] and x2[0]
>>> y = x1[0] & x2[0]
>>> y = x1[3] and x2[3]
>>> y
1
>>> y = x1[0] or x2[0]
>>> y
0
>>> y = x1[1] or x2[1]
>>> y
1
>>> y = x1[3] or x2[3]
>>> y
1
>>>

#Condition, partial
t = 37
if t > 35:
    print('Swim')
    print('Water is hot')

water = True
if t > 35:
    if water:
        print('swim')

if t > 35 and water:
    print('swim')   

#Condition full
t = 30

#Yes
if t > 35:
    print('swim')     

#No   
else:
    print('paddle')  

print('text')     

from math import *

#Quadratic equation
a = 1
b = 4
c = 40

#Discriminant
D = b*b - 4 * a * c

#D>0, 2 roots
if D > 0:
    x1 = (-b + sqrt(D))/(2*a)  
    x2 = (-b - sqrt(D))/(2*a)  
    print(x1, x2)

#D == 0, double root
elif D == 0:
    x1 = -b/(2*a) 
    x2 = x1
    print(x1, x2)
    
#D < 0, no solution in R
else:
    print('No solution in R')
    
