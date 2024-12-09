#Function
def factorial(n):
    fn = 1

    while n > 1:
        fn = fn * n
        n = n - 1
    
    return fn

#Function
def factorial2(n:int)->int:
    fn = 1

    while n > 1:
        fn = fn * n
        n = n - 1
    
    return fn


def asm(a, b):
    #Return 3 values, v1
    an = a + b
    sn = a - b
    mn = a * b
    
    return an, sn, mn

def asm2(a, b):
    #Return 3 values, v2  
    return a+b, a-b, a*b

def im(x):
    #Immutable
    print(id(x))
    x = x + 1
    print(id(x))

def mu(L):
    #Mutable
    print(id(L))
    L[0] = 12
    print(id(L))
    
def dist(x1 = 0, y1 = 0, x2 = 1, y2 = 1):
    #Default parameters
    dx = x2 - x1
    dy = y2 - y1
    
    return (dx * dx + dy * dy) **0.5

def comb(n, k):
    #Call function inside function, v1
    fn = factorial(n)
    fnk = factorial(n-k)
    fk = factorial(k)
    
    return fn / (fnk * fk)

def comb2(n, k):
    #Call function inside function, v2
    return factorial(n)/ (factorial(n-k) * factorial(k))

def comb3(n, k, f):
    #Pass function
    return f(n)/ (f(n-k) * f(k))

def sum(*X):
    #Positional arguments
    s = 0
    for x in X:
        s = s + x
    return s
    


#Factorial, v1
n = 10
fn = factorial2(n)     
print(fn)

#Add, subtract, multiply
x, y = 5, 6
an, sn, mn = asm(x, y)

#Immutable objects
a = 10
print(id(a))
a = im(a)
print(id(a))

#Mutable objects
L = [1, 2, 3, 4, 5]
print(id(L))
mu(L)
print(id(L))

#Default values
x1, y1 = 5, 5
x2, y2 = 10, 10

#User-defined values
d = dist(x1, y1, x2, y2)
print(d)

#Default values
d2 = dist(10,10)
d2 = dist(10, 10, 7)
d2 = dist(10, 10, 7, -5)
print(d2)

#Combination 
n = 10
k = 5
c = comb(n, k)
print(c)

#Combination, pass a function
n = 10
k = 5
c = comb3(n, k, factorial)
print(c)

#Positional arguments
s = sum(1)
print(s)