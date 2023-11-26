n=5
fn=1
#Fact, v1
while n > 1:
    fn *= n
    n -= 1
    
print(fn)

#Fact, v2
n = 5
i = 2
fn2 = 1

while i <= n:
    fn2 *=  i
    i += 1
    
print(fn2)

M = [2.5, 1.7, 4.0, 3.5, 8.1, 1.5]

m_max = M[0]

for m in M:
    #Update maxima
    if m > m_max:
        m_max = m
        
print(m_max)       

m_max = M[0]
m_min = M[0]

for m in M:
    #Update maximum
    if m > m_max:
        m_max = m
        
     #Update manimum
    if m < m_min:
        m_min = m
        
print(m_min, m_max) 

X = range(12)   
for x in X:
    print(x)

n = len(M)
I = range(n)

for i in I:
    print(i)
    
I = range(len(M))
for i in I:
    print(i)

i_max = 0  
m_max = M[i_max]

for i in range(len(M)):
    #Update maximum
    if M[i] > m_max:
        m_max = M[i]    
        i_max = i
    
print(i_max, m_max)

m_my = 4.0

for m in M:
    if m == m_my:
        print('found')
        break 
