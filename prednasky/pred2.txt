#Basic types
>>> 5+5
10
>>> 5
5
>>> type(6)
<class 'int'>
>>> 6.0
6.0
>>> type(6.0)
<class 'float'>
>>> type(6.)
<class 'float'>
>>> type(0.000000000001)
<class 'float'>
>>> type(1.0e-12)
<class 'float'>
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> type('Hello world')
<class 'str'>
>>> """Hello
... 5+5
... 5*6
...
  File "<stdin>", line 1
    """Hello
    ^
SyntaxError: unterminated triple-quoted string literal (detected at line 3)
>>> """Hello
... world"""
'Hello \nworld'
>>> sqrt(9)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sqrt' is not defined
>>> sin(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sin' is not defined. Did you mean: 'bin'?

#Functions and exceptions
>>> import math
>>> math.sin(0)
0.0
>>> from math import *
>>> sin(0)
0.0
>>> sin(90)
0.8939966636005579
>>> pi
3.141592653589793
>>> sin(pi/2)
1.0
>>> asin(1)
1.5707963267948966
>>> asin(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: math domain error
>>> sqrt(-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: math domain error
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 0/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> Inf
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Inf' is not defined. Did you mean: 'inf'?
>>> inf
inf
>>> 0*inf
nan
>>> 2**126
85070591730234615865843651857942052864
>>> 2**200
1606938044258990275541962092341162602522202993782792835301376
>>> 2**1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
>>> 2.1**1000
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OverflowError: (34, 'Result too large')
>>> 2.1**200
2.778810599530396e+64
>>> 2.1**200
2.778810599530396e+64
>>> 2.1**500
1.2872039593705846e+161
>>> 2.1**-500
7.768776600788105e-162
>>> 2.1**-500
7.768776600788105e-162
>>> cos(0)
1.0

#Problems: small and large values combined
>>> acos(cos(0))
0.0
>>> acos(cos(1))
0.9999999999999999
>>> 1.0+1.0e-20-1.0
0.0
>>> 1.0+1.0e-16-1.0
0.0
>>> 1.0+1.0e-20-1.0==1.0e-20
False
>>> a=1.0e20
>>> a==a+1
True
>>> 1.0+0.1-1.0
0.10000000000000009
>>> a=117
>>> a==a+1
False
>>> a=1
>>> b=2
>>> c=3
>>> a+(b+c)
6
>>> (a+b)+c
6
>>> b=2.0e25
>>> c=3.0e-21
>>> (a+b)+c
2e+25
>>> a+(b+c)
2e+25
>>> c=-2.0e25
>>> a+(b+c)
1.0
>>> (a+b)+c
0.0
>>> 'Hello world'
'Hello world'
>>> 'Hello \n world'
'Hello \n world'
>>> print('Hello \n world')
Hello
 world
>>> print('Hello \t world')
Hello    world
>>> print('Hello \\ world')
Hello \ world
>>> print('Hello \' world')
Hello ' world
>>> print('Hello ' world')
  File "<stdin>", line 1
    print('Hello ' world')
                        ^
SyntaxError: unterminated string literal (detected at line 1)
>>> a=10
>>> type(a)
<class 'int'>
>>> a='123'
>>> b=6
>>> a+b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> a:int =7
>>> a='k'
>>> x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
>>> a
'k'
>>> b
6
>>> c
-2e+25
>>> x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined

#Initialization
>>> a=5
>>> b=6
>>> a,b = 5,6
>>> a=b
>>> b=6
>>> c=a+b
>>> type(c)
<class 'int'>
>>> a=5.0
>>> b=6.0
>>> c=a+b
>>> type(c)
<class 'float'>
>>> a =5
>>> b
6.0
>>> c=a+b
>>> type(c)
<class 'float'>
>>> b=6.3
>>> c=a+b
>>> type(c)
<class 'float'>
>>> print(c)
11.3
>>> c=int(a+b)
>>> print(c)
11

#Arithmetic operators
>>> 3+3*3
12
>>> 2/3
0.6666666666666666
>>> 11/2
5.5
>>> 11//*2
  File "<stdin>", line 1
    11//*2
        ^
SyntaxError: invalid syntax
>>> 11//2
5
>>> 11%2
1
>>> a=5
>>> print(a)
5
>>> a==5
True
>>> a=a+10
>>> print(a)
15
>>> a=a-1
>>> print(a)
3
>>> a+=10
>>> print(a)
13
>>> a*=100

#Boolean operators
>>> print (a>b)
True
>>> print (a>=b)
True
>>> print (a==b)
False
>>> print (a>10)
True
>>> print (b>10)
False
>>> print (a>10 and b>10)
False
>>> print (a>10 & b>10)
False
>>> print (a>10 or b>10)
True
>>> not(True)
False
>>>