# 1. vratit se k bankomatu
##########################
# navazat na kod z cviceni c.3: https://github.com/k155cvut/uvin/blob/main/cviceni/cv3.py

m = 8300

b = (5000, 2000, 1000, 500, 200,100)
n = []

# V1: For + index
nb = len(b)
for i in range(nb):
    n.append( m // b[i])
    m = m % b[i]
    
for i in range(nb):
    print(n[i], 'x', b[i], 'CZK')

# V2: for-each
for bi in b:
    n.append(m // bi)
    m = m % bi

# 2. min (cykly)
################
# navazat na kod z cviceni c.4: https://github.com/k155cvut/uvin/pull/3/files#diff-f9b92b69f2550f7f0ecbda45bc68df056c1c7bb16dd59a6ff17434c8b6d795fbR90
x = [3, -6, -3]
xmin = xmax = x[0]
for v in x[1:]:
    if v < xmin:
        xmin = v
    if v > xmax:
        xmax = v
print(xmin, xmax)
    
# 3. prvocislo
##############

x = 17

# V1: Test all dividers
for d in range(2, x // 2):
    # x is divided by d
    if x % d == 0:
        print('Number', x , 'is prime number')
        break
 
# V2: Is x a prime number, improved version

is_prime = True
for d in range(2, x // 2):
    if x % d == 0:
        is_prime = False
        break

# Additional test
if is_prime:
    print('Number', x , 'is prime number')
else: 
    print('Number', x , 'is not prime number')   

# V3: Is x a prime number + find the first divider d1

is_prime = True
d1 = 1

for d in range(2, x // 2):
    if x % d == 0:
        is_prime = False
        d1 = d
        break
        
if is_prime:
    print('Number',x , 'is prime number')
else: 
    print('Number',x , 'is not prime number, is divided by', d1)
    
    
# V4: Is x a prime number + find all dividers

x = 18
is_prime = True
D = []

for d in range(2, x // 2):
    if x % d == 0:
        is_prime = False
        D.append(d)

if is_prime:
    print('Number', x , 'is prime number')
else: 
    print('Number', x , 'is not prime number, is divided by', D)

# 4. urtle graphics
###################

import turtle as t

# Square
d = 200
for i in range(4):
    t.forward(d)
    t.left(90)
    
# Triangle
for i in range(3):
    t.forward(d)
    t.left(120)
    
# Hexagon
for i in range(6):
    t.forward(d)
    t.left(60)
    
# Regular shape with n-vertices
n = 8
for i in range(n):
    t.forward(d)
    t.left(360/n)
    
# Grid
t.reset()
n = 10
s = 30

## tady zacinaji studenti
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

t.mainloop()
