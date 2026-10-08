Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 5
5
>>> type(5)
<class 'int'>
>>> 5.0
5.0
>>> type(5.0)
<class 'float'>
>>> 0.0001
0.0001
>>> 1e-4
0.0001
>>> type(1.0e-4)
<class 'float'>
>>> True
True
>>> False
False
>>> false
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'false' is not defined. Did you mean: 'False'?
>>>
>>>
>>>
>>>
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> 'a'
'a'
>>> type('a')
<class 'str'>
>>> type("hello world")
<class 'str'>
>>> sqrt(9)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sqrt' is not defined
>>> from math import *
>>> sqrt(9)
3.0
>>> sqrt(-9)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: math domain error
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> asin(1.01)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: math domain error
>>> sin(0)
0.0
>>> pi
3.141592653589793
>>> sin(45)
0.8509035245341184
>>> sin(45*pi/180)
0.7071067811865476
>>> NaN
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'NaN' is not defined. Did you mean: 'nan'?
>>> inf
inf
>>> nan
nan
>>> NaN
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'NaN' is not defined. Did you mean: 'nan'?
>>> nan
nan
>>> 0*inf
nan
>>> 10*2
20
>>> 10**2
100
>>> 2*127
254
>>> 2**127
170141183460469231731687303715884105728
>>> 2**128
340282366920938463463374607431768211456
>>> 2*200
400
>>> 2**200
1606938044258990275541962092341162602522202993782792835301376
>>> 2**1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
>>> 2.1**50
1.2911144350507218e+16
>>> 2.1**150
2.1522574018942246e+48
>>> 2.1**1000
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OverflowError: (34, 'Result too large')
>>> 2**-1
0.5
>>> 2**-200
6.223015277861142e-61
>>> 2**-1000
9.332636185032189e-302
>>> 2.1**-1000
6e-323
>>> 2.1**-5000
0.0
>>> 2**-5000
0.0
>>> sin
<built-in function sin>
>>> sin(0)
0.0
>>> asin(0)
0.0
>>> asin(sin(0))
0.0
>>> acos(cos(0))
0.0
>>> acos(cos(1))
1.0
>>> acos(cos(1))==1
True
>>> x=1
>>> y=10
>>> x*y
10
>>> x=1.0
>>> y=1.0e-20
>>> x-y
1.0
>>> z=1e20
>>> x+z
1e+20
>>> x-y==1
True
>>> x+z==1.0e20
True
>>> x
1.0
>>> y
1e-20
>>> z
1e+20
>>> x + y + z
1e+20
>>> x + (y +z)
1e+20
>>> (x+y)+z
1e+20
>>> (x+z)+y
1e+20
>>> x + (y+z)
1e+20
>>> 'a'
'a'
>>> int('a']
  File "<stdin>", line 1
    int('a']
           ^
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> int('a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'a'
>>> 'a'
'a'
>>> "a"
'a'
>>> print('Hello')
Hello
>>> print('Hello\n world')
Hello
 world
>>> print('Hello\r world')
 world
>>> print('Hello\t world')
Hello    world
>>> print('Hello ' world')
  File "<stdin>", line 1
    print('Hello ' world')
                        ^
SyntaxError: unterminated string literal (detected at line 1)
>>> print('Hello \' world')
Hello ' world
>>> print('Hello \) world')
Hello \) world
>>> print('Hello ) world')
Hello ) world
>>> print('Hello \" world')
Hello " world
>>> print('Hello " world')
Hello " world
>>> print("Hello " world")
  File "<stdin>", line 1
    print("Hello " world")
                        ^
SyntaxError: unterminated string literal (detected at line 1)
>>> print("Hello \" world")
Hello " world
>>> a=2
>>> type(a)
<class 'int'>
>>> a=2+3/7*96
>>> type(a)
<class 'float'>
>>> b = sin(pi/4)
>>> a,b =2+3/7*96, sin(pi/4)
>>> a,b,c,d,e = 1,2,3,5.7,'Hello world'
>>> a==b
False
>>> int(False)
0
>>> int(Tue)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Tue' is not defined. Did you mean: 'True'?
>>> int(True)
1
>>> bool(0)
False
>>> bool(1)
True
>>> bool(1619)
True
>>> bool('gfgdfg')
True
>>> xa = 0
>>> ya = 0
>>> xb = 10
>>> yb = 10
>>> dx = xb - xa
>>> dy = yb - ya
>>> d = sqrt(dx*dx + dy**2)
>>> print(d)
14.142135623730951
>>> a:int = 7
>>> a
7
>>> a:int = 7.0
>>> a
7.0
>>> a=1
>>> b = True
>>> c = a+b
>>> print(c)
2
>>> d=3.14
>>> c = a + b + d
>>> print(c)
5.140000000000001
>>> c==5.514
False
>>> int(d)
3
>>> e=3.9
>>> int(e)
3
>>> bool(e)
True
>>> type(bool(e))
<class 'bool'>
>>> type(c)
<class 'float'>
>>> type(d)
<class 'float'>
>>> 5**2
25
>>> 5//2
2
>>> 5%2
1
>>> c=c*5
>>> print(c)
25.700000000000003
>>> c*=5
>>> print(c)
128.5
>>> print(c)
128.5
>>> a=a+10
>>> a+=10
>>>