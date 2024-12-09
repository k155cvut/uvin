#print(a)
a = 10  
print(a)
b = 20
print(a)
print(b)

def test():
    c = 30
    print(c)
    
test()
#print(c)

x = -10

if x > 0:
    x = x + 30

print(x)

a = 4
b = 5
c = 10

D = b*b - 4*a*c

#Two real roots x1 != x2
if D > 0:
    x1 = (-b + D**0.5) / (2 * a)
    x2 = (-b - D**0.5) / (2 * a)
    print('2 real roots:',x1, x2)
    
#One real root
elif D == 0:
    x1 = -b / (2*a)
    print('1 real root:',x1)
    
else:
    print('No real root:')

print('end...')  