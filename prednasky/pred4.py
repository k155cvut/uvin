#True and false
True
True
False
False
int(True)
1
int(False)
0

#Not
not(True)
False
not(False)
True

#And
0 and 0
0
0 and 1
0
1 and 0
0
1 and 1
1

#Or
0 or 0
0
0 or 1
1
1 or 0
1
1 or 1
1

#Equivalence
0 == 0
True
0 == 1
False
1 == 0
False
1 == 1
True

#Partial condition
week = 37

if week%2==0:
    print('Lecture')

#Full condition
if week%2==0:
    print('Lecture')
else:
    print('Seminar')
    
#Nested condition
holiday = False
if not(holiday):
    if week%2==0:
        print('Lecture')
    else:
        print('Seminar')

#Solve quadratic equation
a = 1
b = 4
c = 5

#Compute discriminant
D = b * b - 4 * a *c

#Two different roots
if D > 0:
    x1 = (-b + D**(0.5)) / (2*a)
    x2 = (-b - D**(0.5)) / (2*a)
    print (x1, x2)

#Double root
elif D==0:
    x1 = (-b) / (2*a)
    x2 = x1
    print (x1, x2)

#No solution in R
else:
    print('No solution in R')