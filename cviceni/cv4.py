from math import *
#Test,  zda je cislo sude/ liche
x  = 5
#x = 5.1

#Sudost
if x%2 == 0:
    print('Cislo', x, 'je sude')
    
#Lichost
else:
    print('Cislo', x, 'je liche')

#Lichost
if x%2 ==1:
    
    print('Cislo', x, 'je liche')
#Sudost
else:
    print('Cislo', x,'je sude')
    
#Aplikace pouze na cela cisla
if x==int(x):
    #Sudost
    if x%2 == 0:
        print('Cislo', x, 'je sude')
        
    #Lichost
    else:
        print('Cislo', x, 'je liche')
else:
    print("cislo", x, "neni cele")
    
#Kladne / zaporne cislo
if x > 0:
    print('Cislo', x, 'je kladne')
elif x < 0:
    print('Cislo', x, 'je zaporne')
else:
    print ('Cislo', x, 'je 0')
    
#Vypocet smerniku
x1, y1 = 0, 0
x2, y2= 10, 10

#Sour. rozdily
dx = x2 - x1
dy = y2 - y1

#Pomocny uhel
fi = abs(atan(dy/dx))*(180/pi)

#Prvni kvadrant
if dx > 0 and dy > 0:
    sigma=fi

#Druhy kvadrant
elif dx < 0 and dy > 0:
    sigma = 180 - fi
    
#Treti kvadrant
elif dx < 0 and dy < 0:
   sigma = 180 + fi
   
#Ctvrty kvadrant
else:
    sigma = 360 - fi

print(sigma)

#Minimum ze 3 cisel, v1
a, b, c = 3, 4, 5

#a minimum
if a < b and a < c:
    m = a
    
#b minimum  
elif b < a and b < c:
    m = b
    
#c minimum   
elif c < b and c < a:
    m = c
    
print(m)

#Minimum ze 3 cisel, v2

#a minimum
if a < b and a < c:
    m = a
    
#b minimum  
elif b < c:
    m = b
    
#c minimum   
else:
    m = c
    
#Minimum ze 3 cisel, v3
#a minimum
m = a

#b minimum
if b < m:
    m = b
    
#c minimum
if c < m:
    m = c
    
print(m)

#Aplikace podminek pro stanoveni definicniho oboru funkce 
#y = log((5 - x) / sqrt(x^2 - 5x + 14)))