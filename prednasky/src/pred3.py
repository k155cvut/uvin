#List, basic operations
>>> a=3
>>> L= []
>>> L
[]
>>> L=[1,2,4,3,20,10,2026]
>>> L
[1, 2, 4, 3, 20, 10, 2026]
>>> L[0]
1
>>> L[2]
4
>>> L[6]
2026
>>> len(L)
7
>>> n = len(L)
>>> n
7
>>> L[n]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> L[-1]
2026
>>> L[-2]
10
>>> L[-n]
1
>>> L
[1, 2, 4, 3, 20, 10, 2026]
>>> a = L[0]+L[1]
>>> a
3
>>> from math import *
>>> m=sum(L)
>>> m
2066
>>> l = sum(L)/n
>>> l
295.14285714285717
>>> type(l)
<class 'float'>
>>> L[0]=37
>>> L
[37, 2, 4, 3, 20, 10, 2026]
>>> L.append(111)
>>> L
[37, 2, 4, 3, 20, 10, 2026, 111]
>>> L.append(222)
>>> L
[37, 2, 4, 3, 20, 10, 2026, 111, 222]
>>> L.append(333)
>>> len(L)
10
>>> L.pop()
333
>>> L
[37, 2, 4, 3, 20, 10, 2026, 111, 222]
>>> L.pop()
222
>>> L
[37, 2, 4, 3, 20, 10, 2026, 111]
>>> L.pop()
111
>>> L
[37, 2, 4, 3, 20, 10, 2026]
>>> L.insert(2,4)
>>> L
[37, 2, 4, 4, 3, 20, 10, 2026]
>>> L.insert(2,555)
>>> L
[37, 2, 555, 4, 4, 3, 20, 10, 2026]
>>> L.pop(0)
37

#List, slices
>>> L
[2, 555, 4, 4, 3, 20, 10, 2026]
>>> L2 = L[0:2]
>>> L2
[2, 555]
>>> L[0:3]
[2, 555, 4]
>>> L[0:4]
[2, 555, 4, 4]
>>> L[2:4]
[4, 4]
>>> L[0:n-1]
[2, 555, 4, 4, 3, 20]
>>> n = len(L)
>>> L[0:n-1]
[2, 555, 4, 4, 3, 20, 10]
>>> L[0:n-1:2]
[2, 4, 3, 10]
>>> L[0:n-1:3]
[2, 4, 10]
>>> L[2:n-1]
[4, 4, 3, 20, 10]
>>> L[2:]
[4, 4, 3, 20, 10, 2026]
>>> L[2:n]
[4, 4, 3, 20, 10, 2026]
>>> L[0:4]
[2, 555, 4, 4]
>>> L[:4]
[2, 555, 4, 4]
>>> L[::1]
[2, 555, 4, 4, 3, 20, 10, 2026]
>>> L[::-1]
[2026, 10, 20, 3, 4, 4, 555, 2]
>>> L[::-2]
[2026, 20, 4, 555]


#Strings
>>> S = 'Hello world'
>>> S
'Hello world'
>>> n = len(S)
>>> n
11
>>> S[0]
'H'
>>> S[n]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> S[n-1]
'd'
>>> S[-1]
'd'
>>> S[-n]
'H'
>>> S[2:n]
'llo world'
>>> S[2:]
'llo world'
>>> S[::-1]
'dlrow olleH'
>>> S[0:n:-1]
''
>>> S[-1:-n:-1]
'dlrow olle'
>>> S[0:-n:-1]
''
>>> S[-1:-n:-1]
'dlrow olle'
>>> S
'Hello world'
>>> S[0]='h'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> S.append('.')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'append'
>>> S.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'pop'
>>> S1 = 'Tuesday'
>>> S2 = S1 + S2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'S2' is not defined. Did you mean: 'L2'?
>>> S2 = S1 + S
>>> S
'Hello world'
>>> S
'Hello world'
>>> S1
'Tuesday'
>>> S2
'TuesdayHello world'
>>> ord(T)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'T' is not defined
>>> ord('T')
84
>>> ord(S[0])
72
>>> chr(72)
'H'
>>> 'H' in S
True
>>> 'h' in S
False

#Stack
>>> S = []
>>> S.append('M')
>>> S.append('T')
>>> S.append('W')
>>> S
['M', 'T', 'W']
>>> S.append('T')
>>> S.append('F')
>>> S.append('S')
>>> S.append('S')
>>> S
['M', 'T', 'W', 'T', 'F', 'S', 'S']
>>> S.pop()
'S'
>>> S
['M', 'T', 'W', 'T', 'F', 'S']
>>> S.pop()
'S'
>>> S
['M', 'T', 'W', 'T', 'F']
>>> S.pop()
'F'
>>> S
['M', 'T', 'W', 'T']

#Query
>>> Q = []
KeyboardInterrupt
>>> Q = ['M', 'T', 'W', 'T', 'F', 'S', 'S']
>>> Q
['M', 'T', 'W', 'T', 'F', 'S', 'S']
>>> Q.pop(0)
'M'
>>> Q
['T', 'W', 'T', 'F', 'S', 'S']
>>> Q.pop(0)
'T'
>>> Q
['W', 'T', 'F', 'S', 'S']
>>> Q.pop(0)
'W'
>>> Q
['T', 'F', 'S', 'S']

#Priority queue
>>> from queue import *
>>> PQ = PriorityQueue()
>>> PQ
<queue.PriorityQueue object at 0x0000024D09D2D360>
>>> PQ.put((0.37,'M'))
>>> PQ.put((0.89,'T'))
>>> PQ.put((0.10,'W'))
>>> PQ.put((0.91,'W'))
>>> PQ.put((0.91,'T'))
>>> PQ.put((0.25,'F'))
>>> PQ.put((0.98,'S'))
>>> PQ.put((0.64,'S'))
>>> PQ.get()
(0.1, 'W')
>>> PQ.get()
(0.25, 'F')
>>> PQ.get()
(0.37, 'M')
>>> PQ.get()
(0.64, 'S')
>>> PQ.get()
(0.89, 'T')
>>> PQ.get()
(0.91, 'T')
>>>
>>> PQ.get()
(0.91, 'W')
>>> PQ.get()
(0.98, 'S')
>>> PQ.get()

#Tuple
Type "help", "copyright", "credits" or "license" for more information.
>>> N = ()
>>> N.append(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
>>> N=[13, 37, 20, 10, 2026]
>>> N[0]
13
>>> N[4]
2026
>>> N[-1]
2026
>>> N[::2]
[13, 20, 2026]
>>> N[::-1]
[2026, 10, 20, 37, 13]
>>> N.append(555)
>>> N
[13, 37, 20, 10, 2026, 555]
>>> N = (13, 39, 20, 10, 20226)
>>> N[::-1]
(20226, 10, 20, 39, 13)
>>> N.append(555)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
>>> N[0]=456
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

#Set
>>> S = {1, 2, 4, 5, 6, 7, 8}
>>> len(S)
7
>>> S.add(555)
>>> S
{1, 2, 4, 5, 6, 7, 8, 555}
>>> S
{1, 2, 4, 5, 6, 7, 8, 555}
>>> S[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
>>> 8 in S
True
>>> 9 in S
False
>>> S.remove(555)
>>> S
{1, 2, 4, 5, 6, 7, 8}
>>> T = {6, 7, 8, 9, 10}
>>> U = S.union(T)
>>> U
{1, 2, 4, 5, 6, 7, 8, 9, 10}
>>> I = S.intersection(T)
>>> I
{8, 6, 7}

#Dictionary
>>> D1 = S.difference(T)
>>> D1
{1, 2, 4, 5}
>>> D2 = T.difference(S)
>>> D2
{9, 10}
>>> D = {123:['Jan','Novak', 23], 456:['Jana','Nova', 21]}
>>> len(D)
2
>>> 123 in D
True
>>> D.get(123)
['Jan', 'Novak', 23]
>>>
