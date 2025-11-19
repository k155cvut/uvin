import math

# 0. Ukazat vs code v debug rezimu
x = 1
if x > 0:
    print("x > 0")
else:
    print("x <= 0")
          
#
# 1. vratit se k minulemu cviceni - bankomat
#
castka = int(input("Zadej castku: "))
if castka > 0:
    pass # zde je vypocet z minuleho cviceni
else:
    print("Chyba: zadej castku jako kladnou hodnotu")

#
# 2. Test, zda je cislo sude/ liche
#
x  = 5

if x % 2 == 0:
    # Sudost
    print('Cislo', x, 'je sude')
else:
    # Lichost
    print('Cislo', x, 'je liche')

# vs.

if x % 2 == 1:
    # Lichost
    print('Cislo', x, 'je liche')
else:
    # Sudost
    print('Cislo', x,'je sude')
    
# Aplikace pouze na cela cisla
if x == int(x): # isinstance(x, int)
    if x % 2 == 0:
        # Sudost
        print('Cislo', x, 'je sude')
    else:
        # Lichost
        print('Cislo', x, 'je liche')
else:
    print("cislo", x, "neni cele")

#
# 3. Kladne / zaporne cislo
#
if x > 0:
    print('Cislo', x, 'je kladne')
elif x < 0:
    print('Cislo', x, 'je zaporne')
else:
    print ('Cislo', x, 'je 0')

#
# 4. Vypocet smerniku
#
x1, y1 = 0, 0
x2, y2= 10, 10

# Sour. rozdily
dx = x2 - x1
dy = y2 - y1

# Pomocny uhel
fi = abs(math.atan(dy/dx)) * (180 / math.pi)

if dx > 0 and dy > 0:
    # Prvni kvadrant
    sigma = fi
elif dx < 0 and dy > 0:
    # Druhy kvadrant
    sigma = 180 - fi
elif dx < 0 and dy < 0:
    # Treti kvadrant
    sigma = 180 + fi
else:
    # Ctvrty kvadrant
    sigma = 360 - fi

print(sigma)

#
# 5. Minimum ze 3 cisel, v1
#
a, b, c = 3, 4, 5

# a minimum
if a < b and a < c:
    m = a
#b minimum  
elif b < a and b < c:
    m = b
# c minimum   
elif c < b and c < a:
    m = c
    
print(m)

# Minimum ze 3 cisel, v2

# a minimum
if a < b and a < c:
    m = a
# b minimum  
elif b < c:
    m = b
# c minimum   
else:
    m = c
    
# Minimum ze 3 cisel, v3

# a minimum
m = a

# b minimum
if b < m:
    m = b
    
# c minimum
if c < m:
    m = c
    
print(m)

# Aplikace podminek pro stanoveni definicniho oboru funkce
# Odmocnina / Logaritmus nedefinovaný
# y = log((5 - x) / sqrt(x^2 - 5x + 14)))
