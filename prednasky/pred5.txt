#Factorial, v1
n = 5
fn = 1

while n > 1:
    fn = fn * n
    n = n - 1
    
print(fn)

#Factorial, v2
n = 5
fn = 1
i = 2

while i <= n:
    fn = fn * i
    i =  i + 1

print(fn)

#For-each loop
L = {1, 3, 9, -14, 19}
for l in L:
    print(l)
    
#Find maximum
M = [1.9, 3.7, 4.1, 2.6, 2.8]
m_max = M[0]

for m in M:
    if m > m_max:
        m_max = m
        
print(m_max)

#Find maximum a and minimum
M = [1.9, 3.7, 4.1, 2.6, 2.8]
m_max = M[0]
m_min = M[0]

for m in M:
    if m > m_max:
        m_max = m
        
    if m < m_min:
        m_min = m
        
print(m_min, m_max)

M3 = [3 * m for m in M]
print(M3)

#Intervals
I = range(1, 5, 1)
I = range(0, 15, 3)
I = range(0, 15)
I = range(15)
for i in I:
    print(i)

I = range(0, len(M))
I = range(len(M))
for i in I:
    print(i)
    
#Use index for loops
for i in I:
    print(M[i])

#Use index, improved syntax
for i in range(len(M)):
    print(M[i])

#Find maximum and its index
M = [1.9, 3.7, 4.1, 2.6, 2.8]
i_max = 0
m_max = M[i_max]

for i in range(len(M)):
    if M[i] > m_max:
        m_max = M[i]
        i_max = i
        
print(m_max, i_max)

#Find minimum, maximum and their indices
i_min, i_max = 0, 0
m_min, m_max = M[i_min], M[i_max]

for i in range(len(M)):
    if M[i] < m_min:
        m_min = M[i]
        i_min = i
    
    if M[i] > m_max:
        m_max = M[i]
        i_max = i
        
print(m_min, i_min, m_max, i_max)

#Find first occurance of an item
X = (1, 2.1, 3.1, 4, 19, 3.1, 15, -5, 3.14)
i_a, a = -1, 3.1

for i in range(len(X)):
    if a == X[i]:
        i_a = i
        break
#Result
if i_a != -1:
    print('Found, first index = ', i_a)
else:
    print('Item a not found')

#Find last occurance of an item
for i in range(len(X)):
    
    if a == X[i]:
        i_a = i
        
#Results
if i_a != -1:
    print('Found, last index = ', i_a)
else:
    print('Item a not found')