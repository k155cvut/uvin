from numpy import *
from turtle import *
from time import *

#Function definitions
# ----------------------------------------------------------------------------

def money(m):
    #Minimum amount of bills
    b = (5000, 2000, 1000, 500, 200, 100)
    n = []

    #V1: For + index
    nb = len(b)
    for i in range(nb):
        n.append ( m//b[i])
        m = m%b[i]
        
    return b, n
        
def isPrime (x):
    #Is x the prime number?
    is_prime = True
    
    #Test all dividers
    for d in range(2, x//2):
        
        #x is divided by d
        if x%d == 0:
            is_prime = False
            break
        
    return is_prime 


def isPrime2(x):
    #V4: Is x a prime number + find all dividers
    is_prime = True
    D = []
    
    #Test all dividers
    for d in range(1, x + 1):
        
        #x is divided by d
        if x%d == 0:
            if d != 1 and d != x:
                is_prime = False
            D.append(d)
            
    return is_prime, D

def shape(d, n):    
    #Plot regular shape with n-vertices
    for i in range(n):
        forward(d)
        left(360/n)
        
def grid (d, n):
#Plot horizontal lines
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

def drawSin (a,b,t):
    #Plot graph of the sine, interval <a, b>
    scale = 50

    X = arange(a, b, t)
    Y = [scale * sin(x) for x in X]

    down()
    for i in range(len(X)):
        setpos(scale * X[i], Y[i]) 
       
def findMinMax(X):
    #Find min and max and their indexes
    imin, imax = 0, 0
    xmin, xmax = X[imin], X[imax]

    #Browse all elements
    for i in range(len(X)):
        
        #Update minimum
        if X[i] < xmin:
            xmin = X[i]
            imin = i
        
        #Update maximum
        if X[i] > xmax:
            xmax = X[i]
            imax = i  
            
    return imin, imax, xmin, xmax  

def eratosthenes (b):
    #Find all prime numbers in interval <0, b>
    PN = [True]*(b+1)
    
    #Not prime numbers
    PN [0] = False
    PN [1] = False
    
    #Browse all number
    for i in range (2,b//2+1):
        #Is i prime number
        if PN[i]:
            for j in range (2*i, b+1, i):
                PN[j] = False

    #Store all prime numbers
    PNS = []
    for i in range(b+1):
        if PN[i]:
            PNS.append(i)
    return PNS

#----------------------------------------------------------------------------
#Function calls

#Money example
m = 28300
b, n = money(m)

for i in range(len(b)):
    print(n[i],'x', b[i], 'CZK')

#Test, whether x is prime number, V1
x = 71
res = isPrime(x)
print (res)

#Test, whether x is prime number, V2 + list of dividers
x = 17
is_prime, D = isPrime2(x)
print (is_prime, D)


'''
#Draw shape  
d = 25
n = 10
shape(d, n)
    
#Draw grid
d = 10
n = 8
grid (d ,n)


#Draw sin(x) on interval <a, b> with the step t
a = 0
b = 2*pi
t = 0.1
drawSin (a,b,t)
sleep(10)
'''

#Find min, max
X = [10, 12, 2024, 5, 21, 3, 11 ]
imin, imax, xmin, xmax  = findMinMax(X)
print(imin, imax, xmin, xmax)

#Eratosthenes sieve
PNS = eratosthenes(50)
print(PNS)