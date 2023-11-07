#True / false representation
True
False
print(int(True))
print(int(False))

#Variable scope, global
a = 6
print(a)

b = 0
if a == 5:
    b = 10
    print(b)

print(b) #May cause errors

#Variable scope, local
def test():
    c = 10
    print(c)
    
test()
#print(c)  #Cuase errors

#Incomplete condition
a = 5
b = 7
if b > 0:
    a = a + 10
    
#Two incomplete conditions
a = 5
b = 7
c = 10
if b > 0:
    if c > 0:
        a = a + 10
        print(a)

#Merge conditions
if (b > 0) and (c > 0):
    a = a + 10
    print(a)
    
#Complete condition
a = 5
b = -7
if b > 0:
    a = a + 10
else:
    a = a - 10
    
#Combined condition
from math import *

a = 1
b = 4
c = 40

D = b*b - 4 * a * c

#Positive discriminant
if D > 0:
    x1 = (-b + sqrt(D)) / (2*a)
    x2 = (-b - sqrt(D)) / (2*a)

#Discriminat is zero
elif D == 0:
    x1 = -b  / (2*a)
    x2 = x1
    
#Negative discriminant
else:
    print('No solution in R')