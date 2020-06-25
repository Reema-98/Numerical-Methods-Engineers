from sympy import * 
from sympy import diff, Symbol
from sympy.parsing.sympy_parser import *
from math import *
import numpy as np
x,y_iminus1, y_iplus1,y_i,x_iminus1,x_i,m_i,m_iminus1= symbols('x y_iminus1 y_iplus1 y_i x_iminus1 x_i m_i m_iminus1') 
n=int(input('number of points: '))
h=float(eval(input('h : ')))

xstring=input('x separated by commas :')
ystring=input('y separated by commas :')
xlist=xstring.split(',')
y=ystring.split(',')
for i in range(len(xlist)):
	xlist[i]=float(eval(xlist[i]))
for i in range(len(y)):
	y[i]=float(eval(y[i]))
A=np.zeros((n-2,n-2))
B=np.zeros(n-2)
s='(((((x_i-x)**3)*m_iminus1)+(((x-x_iminus1)**3)*m_i))/(6*h))+(((x_i-x)*(y_iminus1-(((h**2)/6)*m_iminus1)))/h)+(((x-x_iminus1)*(y_i-(((h**2)/6)*m_i)))/h)'
d='(6*(y_iminus1-2*y_i+y_iplus1))/(h**2)'
#first eqn
i=1
print("i : ",i)
#A[0][n-1]=u_n_t
A[0][0]=4
A[0][1]=1
y_iminus1=y[i-1]
y_i=y[i]
y_iplus1=y[i+1]
B[0]=eval(d)
for i in range(2,n-2):
	A[i-1][i-1]=1
	A[i-1][i]=4
	A[i-1][i+1]=1
	y_iminus1=y[i-1]
	y_i=y[i]
	y_iplus1=y[i+1]
	B[i-1]=eval(d)

#lasteqn
i=n-2
A[n-3][n-3]=4
A[n-3][n-4]=1
y_iminus1=y[i-1]
y_i=y[i]
y_iplus1=y[i+1]
B[i-1]=eval(d)

print("A =",A)
print("")
print("B = ",B)
print("")
M=np.linalg.solve(A,B)
print("M (m1 ,...mn-1) = ",M)
m=[0]
for i in M:
	m.append(i)
m.append(0)

for i in range(1,n):
	print("interval ("+str(i-1)+","+str(i)+")")
	x_i=xlist[i]
	#print("x_i ; ",x_i)
	x_iminus1=xlist[i-1]
	#print("x_iminus1 : ",x_iminus1)

	m_i=m[i]
	#print("m_i : ",m_i)

	m_iminus1=m[i-1]
	#print("m_iminus1 : ",m_iminus1)
	y_iminus1=y[i-1]
	y_i=y[i]
	print(eval('(((((x_i-x)**3)*m_iminus1)+(((x-x_iminus1)**3)*m_i))/(6*h))'))
	print(eval('(((x_i-x)*(y_iminus1-(((h**2)/6)*m_iminus1)))/h)'))
	print(eval('(((x-x_iminus1)*(y_i-(((h**2)/6)*m_i)))/h)'))
	print("= ")
	a=eval(s)
	print(str(a))








	