# 1. Bankomat
#############

m = 8300

b = (5000, 2000, 1000, 500, 200, 100) # n-tice vs. seznam 
n = []

# Use 5000 CZK
n.append( m // b[0])
m = m % b[0]

# Use 2000 CZK
n.append(m // b[1])
m = m % b[1]

# Use 1000 CZK
n.append(m // b[2])
m = m % b[2]

# Use 500 CZK
n.append(m // b[3])
m = m % b[3]

# Use 200 CZK
n.append(m // b[4])
m = m % b[4]

# Use 100 CZK
n.append(m // b[5])
m = m % b[5]

# Print results
print(n[0], 'x', b[0], 'CZK')
print(n[1], 'x', b[1], 'CZK')
print(n[2], 'x', b[2], 'CZK')
print(n[3], 'x', b[3], 'CZK')
print(n[4], 'x', b[4], 'CZK')
print(n[5], 'x', b[5], 'CZK')

### 2. Vektorový počet
######################

# Skalární součin
u = (1,0,0)
v = (0,1,0)
dot = u[0] * v[0] + u[1] * v[1] + u[2] * v[2]
print(dot)

# Vektorový součin
nx = u[1] * v[2] - u[2] * v[1]
ny = - (u[0] * v[2] - u[2] * v[0])
nz = u[0] * v[1] - u[1] * v[0]
n = (nx, ny, nz)
print(n)

# Norma vektoru
import math
nu = math.sqrt(u[0]**2 + u[1]**2 + u[2]**2)
print(nu)
nv = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
print(nv)

# Úhel mezi vektory
phi = math.acos(dot / (nu * nv)) * 180 / math.pi
print(phi)
