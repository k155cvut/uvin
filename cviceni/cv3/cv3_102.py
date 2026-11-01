from math import *

#Pr. 1: Bankomat
#*****************************************************
c = 8300
B = [5000, 2000, 1000, 500, 200, 100]
N = []

#5000 CZK
n=c//B[0]
N.append(n)
c=uxv=c%B[0]

#2000 CZK
n=c//B[1]
N.append(n)
c=c%B[1]

#1000 CZK
n=c//B[2]
N.append(n)
c=c%B[2]

#500 czk
n=c//B[3]
N.append(n)
c=c%B[2]

#200 CZK
n=c//B[4]
N.append(n)
c=c%B[4]

#100 CZKc
n=c//B[5]
N.append(n)
c=c%B[5]

print(N)
c=c//B[4]
N.append(n)
c=c%B[4]

#100 CZK
n=c//B[5]
N.append(n)
c=c%B[5]

print(N)

c = 8300
n = c/B[0]
n = int(n)

c=c-n*B[0]

#Pr. 2: souciny vektoru u, v
#******************************************************
u = (1,0,0)
v = (0,0,1)
uv_sk = u[0]*v[0] + u[1]*v[1] + u[2]*v[2]
print(uv_sk)
uv_vekt = (u[1]*v[2]-u[2]*v[1], -(u[2]*v[0]-u[0]*v[2]), u[0] * v[1] - u[1] * v[0])
print(uv_vekt)

#Pr. 3: norma a uhel vektoru
#******************************************************
nu=(u[0]**2 +u[1]**2 +u[2]**2)**0.5
nv=(v[0]**2 +v[1]**2 +v[2]**2)**0.5

alpha = acos(uv_sk/(nu*nv))
print(alpha)
alpha_deg= alpha*180/pi
alpha_grad=alpha*200/pi
print(alpha_deg,alpha_grad)

#Pr. 4: rastr
R = [[120,105,89],[105,0,95],[98,90,87]]
m = len(R)
n = len(R[:])
sum = R[0][0] + R[0][1] + R[0][2] + R[1][0] + R[1][1] + R[1][2] + R[2][0] + R[2][1] + R[2][2] 
prumer= sum/(m*n-1)
print(prumer)

#Pr. 5: Studenti
studenti = [
    {"jmeno": "Anna", "body": 82},
    {"jmeno": "Jan", "body": 65},
    {"jmeno": "Eva", "body": 91}
]

prumer = (studenti[0]["body"] + studenti[1]["body"] + studenti[2]["body"]) / 3
nejlepsi = min(studenti[0]["body"], studenti[1]["body"], studenti[2]["body"])
nejhorsi = max(studenti[0]["body"], studenti[1]["body"], studenti[2]["body"]) 