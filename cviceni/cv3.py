# 1. bankomat (seznamy)

castka = 1000 # int(input("Zadejte castku:"))

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

# 2. vektorovy pocet (seznamy)
import math
u = [1, 0, 0]
v = [0, 1, 0]

uv_dot = u[0] * v[0] + u[1] * v[1] + u[2] * v[2]
print("skalarni soucin:", uv_dot)
uv_cross = [u[1] * v[2] - v[1] * u[2], u[2] * v[0] - v[2] * u[0], u[0] * v[1] - v[0]*u[1]]
print("vektorovy soucin:", uv_cross)
u_norm = (u[0] * u[0] + u[1] * u[1] + u[2] * u[2])**0.5 # norma (velikost) vektoru u
v_norm = (v[0] * v[0] + v[1] * v[1] + v[2] * v[2])**0.5
phi = math.acos(uv_dot / (u_norm * v_norm))
print("uhel dvou vektoru:", (phi * 180) / math.pi)

# 3. maticovy pocet (seznamy)
A = [[3, 7], [1, -4]]
det_A = A[0][0] * A[1][1] - A[1][0] * A[0][1]
print("det(A):", det_A)

# 4a. prevod polarnich souradnic na pravouhle (seznam)
r = 2.1
gamma = 30
xy =[r * math.cos(gamma * math.pi / 180),
     r * math.sin(gamma * math.pi / 180)]
print("x, y:", xy[0], ',', xy[1])

# 4b. prevod pravouhlych souradnic na polarni (slovnik)
bod = {'x': 1, 'y': 1}
bod['r'] = math.sqrt(bod['x']*bod['x'] + bod['y']*bod['y'])
bod['gamma'] = (math.atan(bod['y'] / bod['x']) * 180) / math.pi
print(bod)
