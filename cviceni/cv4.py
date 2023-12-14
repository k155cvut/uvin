# 0. uvod (vyucujici)
a = 0
a == 0

import random
a = random.randint(-10, 10)
print(a)
b = None
# resi studenti
if a == 0:
    b = 0
print(b)
if a > 0:
    b = 1
else:
    b = -1
print(b)
if a > 0:
    b = 1
elif a == 0:
    b = 0
else:
    b = -1
print(b)

# 1. bankomat (kontrola vstupu)

# castka = int(input("Zadejte castku: "))
castka = 120

if castka > 0:
    b = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    n = []
    n.append(castka // b[0])
    z = castka - (n[0] * b[0])
    n.append(z // b[1])
    z = z - (n[1] * b[1])
    n.append(z // b[2])
    z = z - (n[2] * b[2])
    n.append(z // b[3])
    z = z - (n[3] * b[3])
    n.append(z // b[4])
    z = z - (n[4] * b[4])
    n.append(z // b[5])
    z = z - (n[5] * b[5])
    n.append(z // b[6])
    z = z - (n[6] * b[6])
    n.append(z // b[7])
    z = z - (n[7] * b[7])
    n.append(z // b[8])
    z = z - (n[8] * b[8])
    n.append(z // b[9])
    z = z - (n[9] * b[9])
    n.append(z // b[10])
    z = z - (n[10] * b[10])
    n.append(z // b[11])
    z = z - (n[11] * b[11])

    print("5000:", n[0], "2000:", n[1], "1000: ", n[2],"500:", n[3], '200:', n[4], '100:', n[5],
          '50:', n[6], '20:', n[7], '10:', n[8], '5:', n[9], '2:', n[10], '1:', n[11] )
else:
    print("Castka musi byt nenulove kladne cislo")

# 2. polarni souradnice (kontrola vstupu)
import math

r = 1
gamma = 45
if r > 0 and (gamma >= 0 and gamma < 360):
    xy =[r * math.cos(gamma * math.pi / 180),
         r * math.sin(gamma * math.pi / 180)]
    print("x, y:", xy[0], ',', xy[1])
else:
    print("Nevalidni vstup")

# 3. min
a = 3
b = -6
c = -3

## verze 1
if a < b and a < c:
    m = a
if b < a and b < c:
    m = b
if c < a and c < b:
    m = c
print(m)

## verze 2
if a < b and a < c:
    m = a
elif b < c:
    m = b
else:
    m = c
print(m)

## verze 3
if a < b:
    m = a
else:
    m = b
if c < m:
    m = c
print(m)

# vysvetlit
a = 1 # 0
bool(a)
a = "aaa" # ""
bool(a)
a = [0, 1] # []
bool(a)
