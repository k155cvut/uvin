m=28300

b=(5000, 2000, 1000, 500, 200,100)
n=[]

#V1: For + index
nb = len(b)
for i in range(nb):
    n.append ( m//b[i])
    m = m%b[i]
    
for i in range(nb):
    print(n[i], 'x', b[i], 'CZK')

#V2: for-each
for bi in b:
    n.append ( m//bi)
    m = m%bi
    
for i in range(nb):
    print(n[i],'x', b[i], 'CZK')

#V1: Is x a prime number
x = 17

#Test all dividers
for d in range(2, x//2):
    
    #x is divided by d
    if x%d == 0:
        print ('Number',x , 'is prime number')
        break
 
#V2: Is x a prime number, improved version
x = 17
is_prime = True
#Test all dividers
for d in range(2, x//2):
    
    #x is divided by d
    if x%d == 0:
        is_prime = False
        break

#Additional test
if is_prime :
    print ('Number',x , 'is prime number')
else : 
    print ('Number',x , 'is not prime number')   

#V3: Is x a prime number + find the first divider d1
x = 17
is_prime = True
d1 = 1

#Test all dividers
for d in range(2, x//2):
    
    #x is divided by d
    if x%d == 0:
        is_prime = False
        d1 = d
        break
        
#Additional test   
if is_prime :
    print ('Number',x , 'is prime number')
else : 
    print ('Number',x , 'is not prime number, is divided by',d1)
    
    
#V4: Is x a prime number + find all dividers
x = 18
is_prime = True
D = []
#Test all dividers
for d in range(2, x//2):
    
    #x is divided by d
    if x%d == 0:
        is_prime = False
        D.append(d)

#Additional test    
if is_prime :
    print ('Number', x , 'is prime number')
else : 
    print ('Number', x , 'is not prime number, is divided by',D)
    
#Turtle graphics
from turtle import *
from time import *
from math import *
from numpy import *

#Square
d=200
for i in range(4):
    forward(d)
    left(90)
    
#Triangle
for i in range(3):
    forward(d)
    left(120)
    
#Hexagon
for i in range(6):
    forward(d)
    left(60)
    
#Regular shape with n-vertices
n = 8
for i in range(n):
    forward(d)
    left(360/n)
    
reset()

#Grid
d = 10
n = 8

#Horizontal lines
for i in range (n+1):
    setpos (0,d*i)
    down()
    forward (d*n)
    up()
    
#Vertical lines
left(90)
for j in range (n+1):
    setpos (j*d,0)
    down()
    forward (d*n)
    up()

#Sin(x)
reset()
X = arange(0,2*pi,0.1)
Y = [100*sin(x) for x in X]

down()
for i in range(len(X)):
    setpos(100*X[i], Y[i])
    
sleep(10)
    