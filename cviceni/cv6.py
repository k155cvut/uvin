# 1. bankomat (funkce)

# castka = int(input("Zadejte castku: "))
castka = 230

def bankomat(castka):
    print("Castka:", castka)
    b = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    for bi in b:
        n = castka // bi
        castka = castka - (n * bi)
        if n > 0:
            print("-", bi, ":", n)

bankomat(castka)
bankomat(10200)

# 2. min (funkce)
x = [3, -6, -3]

def findMinMax(x):
    xmin = xmax = x[0]
    for v in x[1:]:
        if v < xmin:
            xmin = v
        if v > xmax:
            xmax = v
    return xmin, xmax

xmin, xmax = findMinMax(x)
print("min: " + str(xmin) + "; max: " + str(xmax))

# 3. prevod souradnic (polarni <-> pravouhle) (funkce)
import math

def polarToOrtho(r, gamma):
    return [r * math.cos(gamma * math.pi / 180),
            r * math.sin(gamma * math.pi / 180)]

x, y = polarToOrtho(1, 45)

def orthoToPolar(x, y):
    return [math.sqrt(x*x + y*y),
            (math.atan(y / x) * 180) / math.pi]

print(orthoToPolar(x, y))

# 4. prvocisla (funkce)
def isPrime(x):
    for c in range(2, int(x**0.5)+1):
        if x % c == 0:
            return False
    
    return True

c = 4
print("Je", c, "prvocislo?", isPrime(c))

# 5. Eratosthenovo sito
def eratosthenes(xmax):
    #Auxilliary list
    P = [True] * (xmax+1)
    
    #Not prime numbers
    P[0] = False
    P[1] = False
    
    #Check all numbes inside the interval
    for i in range(2, xmax + 1):  #int(xmax**0.5)+1
        if P[i]:
            for j in range(2 * i, xmax+1, i):
                P[j] = False
                
    PT = []
    for i in range(2, xmax + 1):
        if P[i]:
            PT.append(i)
            
    return PT

print(eratosthenes(35))

# 6. vypocet plochy (L'Huillierovy vzorce)
def getArea(x, y):
    n = len(x)
    area = 0

    # Process all vertices one by one
    for i in range(n):
        area += x[i]* (y[(i + 1) % n] - y[(i - 1 + n) % n])

    return (0.5 * abs(area))

print(getArea([0, 1, 1, 0, 0], [0, 0, 1, 1, 0]))
# print(getArea([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]))
