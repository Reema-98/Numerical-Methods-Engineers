#User inputs 
#1. f= function f(x) 
#2. n=number of decimal places correct to be found
#3. x0=an initial approximation for root

#Output
#real root of f(x) correct upto n decimal places


# import sympy for findingderivative 
from sympy import * 
from sympy import diff, Symbol
from sympy.parsing.sympy_parser import *
from math import *

print("Newton Raphson Method\n")
x, y = symbols('x y') 
#my_symbols = {'x': Symbol('x', real=True)}
f=input('Enter the function whose real roots are to be found: ')
n=int(input('Enter how many decimal places correct to be found: '))
x0=float(input('Enter initial approximation x0 : '))
my_func = parse_expr(f)
expr_diff= Derivative(my_func,x)
df=expr_diff.doit()
df=str(df)
print("Answer:")
print("Derivative of f(x)= f'(x)= "+df)

temp=modf(x0)
decimal1=str(temp[0])
decimal_upto_n_places1=decimal1[2:2+n]
print("Using formula x(n+1)=x(n)-(f(x)/f'(x))")
i=0
x=x0
while(i<100):
	print("x"+str(i)+" = "+str(x))
	#using formula x(n+1)=x(n)-(f(x)/f'(x))
	newx=x-(eval(f)/eval(df))
	temp=modf(newx)
	decimal2=str(temp[0])
	decimal_upto_n_places2=decimal2[2:2+n]
	if(decimal_upto_n_places1==decimal_upto_n_places2):
		print("x"+str(i+1)+" = "+str(newx))
		break
	x=newx
	decimal_upto_n_places1=decimal_upto_n_places2

	i=i+1

if(i!=100):
	print("The root of f(x) is "+str(newx)+" correct upto "+str(n)+" decimal places.")
else:
	print("Exceeded 100 iterations!")






