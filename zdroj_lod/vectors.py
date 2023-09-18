from math import *
u = [1, 0, 0]
v = [0, 1, 0]

uv_dot = u[0] * v[0] + u[1] * v[1] + u[2] * v[2]
print(uv_dot)
uv_cross = [u[1] * v[2] - v[1] * u[2], u[2]*v[0] - v[2] * u[0], u[0]*v[1] - v[0]*u[1]]
print(uv_cross)
u_norm = (u[0] * u[0] + u[1] * u[1] + u[2] * u[2])**0.5
v_norm = (v[0] * v[0] + v[1] * v[1] + v[2] * v[2])**0.5
phi = acos(uv_dot / (u_norm * v_norm))
print(phi)