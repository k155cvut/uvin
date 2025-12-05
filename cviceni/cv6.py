import math

### 1. prvocislo (cv5)

# V1
def isPrime(x):
    is_prime = True
    for d in range(2, x // 2):
        if x % d == 0:
            is_prime = False
            break

    return is_prime

x = 71
res = isPrime(x)
print(res)

for x in range(1, 10):
    res = isPrime(x)
    if res is True:
        print(x, 'je prvocislo')
    else:
        print(x, 'neni prvocislo')

# V2
def isPrimeD(x):
    is_prime = True
    d1 = 1

    for d in range(2, x // 2):
        if x % d == 0:
            is_prime = False
            d1 = d

    return is_prime, d1

for x in range(1, 10):
    res, d = isPrimeD(x)
    if res is True:
        print(x, 'je prvocislo')
    else:
        print(x, 'neni prvocislo, prvni delitel:', d)

### 2. min/max (cv5)

def findMinMax(x):
    xmin = xmax = x[0]
    for v in x[1:]:
        if v < xmin:
            xmin = v
        if v > xmax:
            xmax = v

    return xmin, xmax

cisla = [10, 12, 2024, 5, 21, 3, 11 ]
print(findMinMax(cisla))

### 3. bankomat (cv5)

def money(m):
    b = (5000, 2000, 1000, 500, 200,100)
    n = []

    nb = len(b)
    for i in range(nb):
        n.append( m // b[i])
        m = m % b[i]
    
    return b, n

m = 28300
b, n = money(m)

for i in range(len(b)):
    print(n[i],'x', b[i], 'CZK')

### 4. turtle (cv5)

import turtle as t

def square(d):
    for i in range(4):
        t.forward(d)
        t.left(90)

square(200)

def shape(d, n):
    for i in range(n):
        t.forward(d)
        t.left(360/n)

t.reset()
shape(200, 6)

def grid(n, s):
    t.speed(0)
    t.left(0)
    # horizontalni linky
    d=n*s
    for i in range(n+1):
        t.setpos(0, i*s)
        t.down()
        t.forward(d)
        t.up()
        t.setpos(d, i*s)

    # vertikalni linky
    t.left(90)
    for i in range(n+1):
        t.setpos(i*s, 0)
        t.down()
        t.forward(d)
        t.up()
        t.setpos(i*s, d)

t.reset()
grid(10, 30)

### 5. Eratosthenovo síto

def eratosthenes (b):
    # Find all prime numbers in interval <0, b>
    PN = [True] * (b+1)
    
    # Not prime numbers
    PN [0] = False
    PN [1] = False
    
    # Browse all number
    for i in range (2, b // 2 + 1):
        # Is i prime number
        if PN[i]:
            for j in range (2 * i, b + 1, i):
                PN[j] = False

    # Store all prime numbers
    PNS = []
    for i in range(b + 1):
        if PN[i]:
            PNS.append(i)
    return PNS

pns = eratosthenes(50)
print(pns)
