#Positive numbers
a = 16.0544
d = int (a)
m = int(60*(a-d))
s=60*(60*(a-d)-m)
print(d)
print(m)
print(s)
a2=d+m/60+s/3600
print (a2)

#Positive and negative numbers
d = 16
m = 20
s = 30
sign = (-1)**(d<0)
print(sign)
a3 = d + sign * m / 60 + sign * s / 3600
print(a3))

#Money
c = 16373
b5000 = 5000
n5000 = c//b5000 
c = c%b5000 
print(c) 
print (n5000, 'x 5000')
b2000 = 2000
n2000 = c//2000
c = c%b2000
print(c)
print(n2000, 'x 2000')
b1000 = 1000
n1000 = c//b1000
c = c%b1000
print(c)
print(n1000, 'x 1000')
b500 = 500
n500 = c//b500
c = c%b500
print (c)
print (n500, 'x 500')

#Round
a = -16.689
k = 2
m = 10**k
az = int(a * m +0.5)/m
print(az)