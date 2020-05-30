from math import *
x0=float(input("xo: "))
y0=float(input("yo: "))
x1=float(input("x1: "))
y1=float(input("y1: "))
x2=float(input("x2: "))
y2=float(input("y2: "))
x3=float(input("x3: "))
y3=float(input("y3: "))
expr=input("y' = ")
x=x0
y=y0
f0=eval(expr)
x=x1
y=y1
f1=eval(expr)
x=x2
y=y2
f2=eval(expr)
x=x3
y=y3
f3=eval(expr)
x4=float(input("x4: "))
h=float(input("h : "))
y4=y3+((h/24)*((55*f3)-(59*f2)+(37*f1)-(9*f0)))
n=int(input("no. of iterations: "))
for i in range(n):
	y=y4
	x=x4
	f4=eval(expr)
	y4=y3+((h/24)*((9*f4)+(19*f3)-(5*f2)+f1))
	print("iteration"+str(i+1))
	print(y4)





