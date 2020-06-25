from sympy import * 
from sympy import diff, Symbol
from sympy.parsing.sympy_parser import *
from math import *
from sympy import diff, Symbol
x, y ,yiminus1,yiplus1,yi,yiplus2,yiminus2= symbols('x y yiminus1 yiplus1 yi yiplus2 yiminus2') 
f=input('f: ')
a=float(eval(input("a: ")))
fa=float(eval(input("f(a): ")))

b=float(eval(input("b: ")))
fb=float(eval(input("f(b): ")))
c=int(input('enter 1 for h and 0 for n: '))
if c==1:
	h=float(eval(input('h: ')))
	n=int((b-a)/h)
else:
	n=int(input('n: '))
	h=float((b-a)/n)
print("h :",h)
print("n :",n)
y3str='(yiplus2-2*yiplus1+2*yiminus1-yiminus2)/2*(h**3)'
y2str='(1/h**2)*(yiminus1-(2*yi)+yiplus1)'
y1str='(yiplus1-yiminus1)/(2*h)'
x=a
#first eqn
x=x+h

y2str1='(1/h**2)*(y0-(2*yi)+yiplus1)'
y1str1='(yiplus1-y0)/(2*h)'
y=eval('yi')
y0=fa
y2=eval(y2str1)
print("y''(x) : ",y2)
y1=eval(y1str1)
print("y'(x) : ",y1)
y3=eval(y3str)
print("y'''(x) : ",y3)
print("")
print("i : 1")
print(eval(f))
print("")
for i in range(2,n):
	print("i : ",i)
	
	if i==n-1:
		yiplus1=fb
	x=x+h
	y=eval('yi')
	y2=eval(y2str)
	y1=eval(y1str)
	print(eval(f))
	yiminus1=eval('yiminus1')





