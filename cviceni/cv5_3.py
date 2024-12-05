# 1. bankomat (cykly)

# castka = int(input("Zadejte castku: "))
castka = 230

b = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
for bi in b:
    n = castka // bi
    castka = castka - (n * bi)
    if n > 0:
        print(bi, ":", n)

# 2. min (cykly)
x = [3, -6, -3]
xmin = xmax = x[0]
for v in x[1:]:
    if v < xmin:
        xmin = v
    if v > xmax:
        xmax = v
print(xmin, xmax)

# 3. zelvi grafika

## ctvercovy grid
## zacatek pise vyucujici
import turtle as t

n = 10
s = 30

# horizontalni linka
t.forward(n*s)
t.up()
t.setpos(n*s, 0)
t.setpos(0, 0)

# vertikalni linka
t.left(90)
t.down()

t.forward(n*s)
t.up()
t.setpos(0, n*s)
t.setpos(0, 0)


t.reset()

## tady zacinaji studenti
t.speed(0)
t.left(0)
# horizontalni linky
d=n*s
for i in range(n+1):
    t.setpos(0, i*s)
    t.down()
    t.forward(d)
    t.up()
    t.setpos(d, i*s)

# vertikalni linky
t.left(90)
for i in range(n+1):
    t.setpos(i*s, 0)
    t.down()
    t.forward(d)
    t.up()
    t.setpos(i*s, d)

t.mainloop()
