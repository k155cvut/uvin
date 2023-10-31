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
b2000 = 2000
b1000 = 1000
b500 = 500
b200 = 200
b100 = 100
b50 = 50
b20 = 20
b10 = 10
b5 = 5
b2 = 2
b1 = 1

m = int(input("Get money: "))
n5000 = m//b5000
m = m - n5000*b5000  # m = m % b5000
n2000 = m//b2000
m = m - n2000*b2000  # m = m % b2000
n1000 = m//b1000
m = m - n1000*b1000  # m = m % b1000
n500 = m//b500
m = m - n500*b500    # m = m % b500
n200 = m/b200
m = m - n200*b200    # m = m % b200
n100 = m//b100
m = m - n100*b100    # m = m % b100
n50 = m//b50
m = m - n50*b50      # m = m % b50
n20 = m//b20
m = m - n20*b20      # m = m % b20 
n10 = m//b10
m = m - n10*b10      # m = m % b10
n5 = m//b5
m = m - n5*b5        # m = m % b5
n2 = m//b2
m = m - n2*b2        # m = m % b2
n1 = m//b1
m = m - n1*b1        # m = m % b1

print("5000: " + str(n5000) + " 2000: " + str(n2000) + " 1000: " + str(n1000) + \
      "500: "  + str(n500)  + " 200: "  + str(n200)  + " 100: " + str(n100) + \
      "50: " + str(n50) + " 20: " + str(n20) + " 10: " + str(n10) + \
      "5: " + str(n5) + " 2: " + str(n2) + " 1: " + str(n1))

#Round
a = -16.689
k = 2
m = 10**k
az = int(a * m +0.5)/m
print(az)