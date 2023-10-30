#List, create
L = []
print(L)
L.append(1)
print(L)
L.append(2)
L.append(3)
L.append(4)
L.append(5)
print(L)
n = len(L)
print(n)

L2 = [1, 2, 3, 4, 5]
L2.append(6)
print(L2)

#List, indices + slices
print(L[0])
print(L[1])
print(L[4])
print(L[5])
print(L[-1])
print(L[-5])

print(L2[-6]==L2[0])
L3 = [L, L2]
print(L3)
print(L3[0][3])

print(L2[0:5:2])
print(L2[5:0:-1])
L4 = L2[5:0:-1]

#Removal
L2.pop()
print(L2)
L2.pop()
print(L2)
L2 = [1, 2, 3, 4, 5]
L2.append(6)
print(L2)

#Element inside list
print(0 in L2)

#String
S = 'It is Tuesday'
n = len(S)
print(len(S))
print(S[n-1:0:-2])
LS = ['Monday', 'Tuesday']
print(LS[0][5])
print(ord(LS[0][5]))

#Stack
S = []
S.append('Monday')
S.append('Tuesday')
S.append('Wednesday')
S.append('Thursday')
print(S)
S.pop()
print(S)
S.pop()
print(S)
S.pop()
print(S)
d = S.pop()
print(S)
print(d)

#Queue
Q = []
Q.append('Monday')
Q.append('Tuesday')
Q.append('Wednesday')
Q.append('Thursday')
print(Q)
Q.pop(0)
print(Q)
Q.pop(0)
print(Q)

#Priority queue
import queue
from queue import *
PQ=PriorityQueue()
PQ.put((4, 'Monday'))
PQ.put((2, 'Tuesday'))
PQ.put((6, 'Wednesday'))
PQ.put((5, 'Thursday'))
PQ.put((4, 'Friday'))
print(PQ)
it = PQ.get()
print(it)
it = PQ.get()
print(it)
it = PQ.get()
print(it)
it = PQ.get()
print(it)

#Tuple
N = (0, 1, 2, 3, 4)
print(N[2:4])

#Set
S = {'Jan', 'Marie', 'Petr', 'Lucie', 'Sasa'}
print(S)
print('Jana' in S)
S2 = {'Misa', 'Marie', 'Cyril', 'Pavel'}

U = S.union(S2)
print(U)
I = S.intersection(S2)
print(I)
I2 = S2.intersection(S)
print(I2)
D1 = S.difference(S2)
print(D1)
D2 = S2.difference(S)
print(D2)

#Dictionary
D = { 1 : ['Jana', 'Novak'], 2 : ['Petr', 'Kolar'] }
print(1 in D)
print(D.get(1))
