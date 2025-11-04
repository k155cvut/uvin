#List, construction
L=[]
print(L)
L = [1, 2, 3]
print(L)
len(L)
3
n = len(L)
L = [1, 2, 'Hello world']
L = [1, 2, 3]
L.append(323)
print(L)
L.append(45)
print(L)
[1, 2, 3, 323, 45]

#List, access
L[0]
L[1]
L[4]
L[-1]
L[-1] == L[4]
L[-2]
L[-5]
L[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
L[-6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
L[1]=2025
print(L)
p=L[1]

#Nested list
L[4] = [ 10, 11, 12, 20]
print(L)
L[4]
L[4][1]
L.pop()
[10, 11, 12, 20]
L.pop()
323
print(L)
[1, 2025, 3]
L.pop(0)
1
L
[2025, 3]
L.append(4)
L.append(5)
L.append(8)
L.append(10)
print(L)
[2025, 3, 4, 5, 8, 10]

#Slices
L[0:2]
[2025, 3]
L[0:3]
[2025, 3, 4]
L[3:5]
[5, 8]
L[:5]
[2025, 3, 4, 5, 8]
L[2:]
[4, 5, 8, 10]
L[:]
[2025, 3, 4, 5, 8, 10]
L(0:5:2)
  File "<stdin>", line 1
    L(0:5:2)
       ^
SyntaxError: invalid syntax
L[0:5:2]
[2025, 4, 8]
L[-1:-5]
[]
L[-1:-5:-1]
[10, 8, 5, 4]
L[::-1]
[10, 8, 5, 4, 3, 2025]
L.insert(2, 2110)
L
[2025, 3, 2110, 4, 5, 8, 10]

#String
T = 'Hello world'
len(T)
11
T[0]
'H'
T[-1]
'd'
t = T[0]
t
'H'
T[0] = 'h'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
T[::-1]
'dlrow olleH'
'H' in T
True
'h' in T
False
ord('H')
72
chr(72)
'H'

#Stack
S = []
S.append(0)
S.append(1)
S.append(2)
S.append(3)
S
[0, 1, 2, 3]
L.pop()
10
S.pop()
3
S.pop()
2
S.pop()
1
S.pop()
0
S.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop from empty list

#Priority queue
from queue import *
PQ = PriorityQueue()
PQ.put((0.1, 'Monday'))
PQ.put((-10.1, 'Tuesday'))
PQ.put((10, 'Wednesday'))
PQ.put((21, 'Thursday'))
PQ.get()
PQ.get()
PQ.get()
PQ.get()
PQ.get()

#Tuple
N = (0, 1, 2, 3, 4)
print(N[2:4])

#Set
S = {'Jan', 'Marie', 'Petr', 'Lucie', 'Sasa'}
print(S)
print('Jana' in S)
S2 = {'Misa', 'Marie', 'Cyril', 'Pavel'}

#Boolean operations
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
