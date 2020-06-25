from sympy import * 
from sympy import diff, Symbol
from sympy.parsing.sympy_parser import *
from math import *
import numpy as np
x, y = symbols('x y') 
f=input('Enter f(x): ')
g=input('Enter g(x): ')
n=int(input('Enter how many decimal places correct to be found: '))
x0=float(input('Enter initial approximation x0 : '))
y0=float(input('Enter initial approximation y0 : '))

F=parse_expr(f)
G=parse_expr(g)

f_x=Derivative(F,x)
f_y=Derivative(F,y)
g_x=Derivative(G,x)
g_y=Derivative(G,y)

df_x=f_x.doit()
df_y=f_y.doit()
dg_x=g_x.doit()
dg_y=g_y.doit()

df_x=str(df_x)
df_y=str(df_y)
dg_x=str(dg_x)
dg_y=str(dg_y)

print("Answer:")
print("f'(x)= "+df_x)
print("f'(y)= "+df_y)
print("g'(x)= "+dg_x)
print("g'(y)= "+dg_y)

temp=modf(x0)
decimalx1=str(temp[0])
decimal_upto_n_placesx1=decimalx1[2:2+n]
temp=modf(y0)
decimaly1=str(temp[0])
decimal_upto_n_placesy1=decimaly1[2:2+n]

global h,k
i=0
x=x0
y=y0
while(i<100):
	print("----------------------------------------------------")
	print ("i : ",i)
	print("x"+str(i)+" = "+str(x))
	print("y"+str(i)+" = "+str(y))
	
	fi=eval(f)
	print("fi : ",fi)
	gi=eval(g)
	print("gi : ",gi)
	df_xi=eval(df_x)
	df_yi=eval(df_y)
	dg_xi=eval(dg_x)
	dg_yi=eval(dg_y)

	print("f'(xi)= "+str(df_xi))
	print("f'(yi)= "+str(df_yi))
	print("g'(xi)= "+str(dg_xi))
	print("g'(yi)= "+str(dg_yi))

	A = np.array([[df_xi, df_yi], [dg_xi, dg_yi]])
	B = np.array([-fi, -gi])
	h_k_sol = np.linalg.solve(A, B)
	h=h_k_sol[0]
	k=h_k_sol[1]
	print("h :",str(h))
	print("k : ",str(k))

	newx=x+h
	newy=y+k

	temp=modf(newx)
	decimalx2=str(temp[0])
	decimal_upto_n_placesx2=decimalx2[2:2+n]
	temp=modf(newy)
	decimaly2=str(temp[0])
	decimal_upto_n_placesy2=decimaly2[2:2+n]

	if((decimal_upto_n_placesx1==decimal_upto_n_placesx2) and (decimal_upto_n_placesy1==decimal_upto_n_placesy2)):
		print("x"+str(i+1)+" = "+str(newx))
		print("y"+str(i+1)+" = "+str(newy))
		break
	x=newx
	y=newy
	decimal_upto_n_placesx1=decimal_upto_n_placesx2
	decimal_upto_n_placesy1=decimal_upto_n_placesy2
	i=i+1
	print("--------------------------------------------------")

if(i!=100):
	print("The root  x is "+str(newx)+" correct upto "+str(n)+" decimal places.")
	print("The root  y is "+str(newy)+" correct upto "+str(n)+" decimal places.")
else:
	print("Exceeded 100 iterations!")

