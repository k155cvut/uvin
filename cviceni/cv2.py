# 1. prevod DMS -> DD
d = 10
m = 31
s = 24.5

d + m / 60 + s / (60*60)
type(d)

d = input("Zadejte stupne:")
m = input("Zadejte minuty:")
s = input("Zadejte vteriny:")

# d + m / 60
mi = float(m)
type(mi), m, mi

print("Vysledek DD:", int(d) + int(m) / 60 + float(s) / (60 * 60))

# 2. prevod DD -> DMS

dd = float(input("Vstup:"))
d = int(dd)
m = int((dd - d) * 60)
v = (((dd - d) * 60) - m) * 60
print("Vysledek DMS:", d, ":", m, ":", v)

# 3. bankomat

castka = 11800

b5000 = 5000
b2000 = 2000
b1000 = 1000
b500 = 500
b200 = 200
b100 = 100

n5000 = castka // b5000
z = castka - (n5000 * b5000)
n2000 = z // b2000
z = z - (n2000 * b2000)
n1000 = z // b1000
z = z - (n1000* b1000)
n500 = z // b500
z = z - (n500 * b500)
n200 = z // b200
z = z - (n200 * b200)
n100 = z // b100
z = z - (n100 * b100)
### alternativni reseni
# castka=castka%b5000
# n2000=castka//b2000
# castka=castka%b2000
# n1000=castka//b1000
# castka=castka%b1000
# n500=castka//b500
# castka=castka%b500
# n200=castka//b200
# castka=castka%b200
# n100=castka//b100

print("5000:", n5000, "2000:", n2000, "1000: ", n1000,"500:", n500, '200:', n200, '100:', n100)

# 4. zaokrouhleni

a = 13.56985124
int(a * 10) / 10
