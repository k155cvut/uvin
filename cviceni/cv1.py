#Jupyter notebook, markdown mode
Hello
# Hello world
## I love Python
- Moday
- Tuesday
- Wednesday

#Link to Jupyter markdown syntax
#https://www.ibm.com/docs/en/watson-studio-local/1.2.3?topic=notebooks-markdown-jupyter-cheatsheet

#Jupyter notebook, source code mode
#Literals
3
3 + 3
3 + 3 * 3
2/3
2//3
63//8
3**2
3**(-2)
-3**1/2        #Error, priority
(-3)**(1/2)    #Complex number support
(-3)**(0.5)
3/0
2**64
2**128         #Large numbe support

%Types
a = 1
type(a)
b = 2
type(b)
z = a / b
b = float(b)
type(b)
z = a / b
type(z)
c = 3.0
z = a / c
type(z)
zi = int(z)
type(zi)


#Simple equations
x = 2
y = X**2   #Error, case sensitive
y = x**2
print(y)
print('y = ', y)
print("y = ", y)
y = sin(x) #Error, import library

from math import *
y = sin(x)
y = Sin(x) #Error, case sensitive

#Square
a = 10
S = a * a
O = 4 * a
print(S + O) #Error
print(S, O)
print('Square area: ', S, 'm2, square length: ', O, 'm')

#Circle
r = 10
S = pi * r * r
O = 2 * pi * r
print('Circle area: ', S, 'm2, circle length: ', O, 'm')

#Simple operation with the input
name = input('name:')
surname = input('surname:')
print('You are:' + name + surname)

#Using inputs
r = input('Radius: ', r)
# and continue with circle example

#Convert to real number
D = 5
M = 26
S = 43
R =  D + M/60 + S/3600
print(R)
