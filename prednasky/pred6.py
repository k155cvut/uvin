import sys

#Version 1
def add2Numbers(a, b):
    c = a + b
    return c 

#Version, refined
def add2Numbers(a, b):
    return a + b

#Return 2 values
def addSubtract2Numbers(a, b):
    return a + b, a - b

#Version with type hints
def add2Numbers2(a:float, b:float)->float:
    c = a + b
    return c 

def f(a):
    a = 7
    
#Function main
def main(args):
    #Return one value
    c = add2Numbers(3, 4)
    print(c)

    #Retur two values
    c, d  = addSubtract2Numbers(3, 4)
    print(c, d)

if __name__ == '__main__':
    main(sys.argv)

    #Pass by value, test
    a = 10
    f(a)
    print(a)

#Immutable object
x=10
id(x)
type(x)

#New variable
x = 5
id(x)
x=x+5
id(x)

#Mutable object
L=[1, 2, 3, 4]
id(L)
L[0]=10
id(L)

#Immutable object
def f2(x):
    x = 10
    print(id(x))
    print(x)
    
#Mutable object    
def f3(L):
    L[0] = 10
    print(id(L))
    print(L)
    

#Immutable object
x = 27
print(id(x))
f2(x)
print(x)

#Mutable object
L = [1, 2, 3]
print(id(L))
f3(L)
print(L)

#Default parameters
def dist(x1 = 0, y1 = 0, x2 = 0, y2 =0 ):
    dx = x2 - x1
    dy = y2 - y1
    return (dx*dx + dy*dy)**0.5 

#Default paramaters
x1 = 0
y1 = 0
x2 = 10
y2 = 10

d = dist(x1, y1, x2, y2)
d2 = dist()
print(d)
print(d2)

#Find min and max (function)
def minMax(M):
    mmin = M[0]
    mmax = M[0]
    
    for m in M:
        if m < mmin:
            mmin = m
        elif m > mmax:
            mmax = m
    
    return mmin, mmax    

#Min, max
M = [2.2, 6.7, 4, 3.5, 5.4]
mmin, mmax = minMax(M)
print(mmin, mmax)

#Compute factorial
def fact (n):
    fn = 1
    
    while n > 1:
        fn *= n
        n -= 1
        
    return fn

#Combinations
def comb(n, k):
    num = fact(n)
    denom = fact(n-k) * fact(k)
    return num / denom

#Combinations, pass function as a parameter
def comb2(n, k, f):
    num = f(n)
    denom = f(n-k) * f(k)
    return num / denom

#Current method
n = 5
k = 3
res = comb(n, k)
print(res)

#Pass function as a parameter
n = 5
k = 3
res = comb2(n, k, fact)
print(res)

def sum(*X):
    s = 0
    for x in X:
        s += x
    return s

def printPersons(**X):
    for x in X:
        print(x, X[x])

s = sum(5, 3, 4, 2)
print(s)
s = printPersons(name = 'Jana', surname = 'Vonaskova', job ='student')