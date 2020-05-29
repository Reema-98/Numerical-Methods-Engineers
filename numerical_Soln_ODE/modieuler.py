from math import *
h=float(input('enter h:'))
x0=float(input('enter x0:'))
y0=float(input('enter y0:'))
x=x0
y=y0
expr = input("Enter dy/dx: ")
t=float(input("enter target x for which y is required:"))
while(x<t):
	print("x= ",x)
	#print("y= ",y)
	f=eval(expr)
	print("dy/dx: ",f)
	y1=y
	y=y+(h*f)
	print("new y:",y)
	x=x+h
	#x=round(x,1) #otherwise error?
	for i in range(3):
		print("x:",x)
		f1=eval(expr)
		print("dy/dx: ",f1)
		meanslope=(f+f1)/2
		print("meanslope: ",meanslope)
		y=y1+(h*meanslope)
		print("new y*: ",y)
	print("------------------------------------------------------")




	
