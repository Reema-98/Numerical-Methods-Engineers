h=float(input('enter h:'))
x0=float(input('enter x0:'))
y0=float(input('enter y0:'))
x=x0
y=y0
expr = input("Enter dy/dx: ")
t=float(input("enter target x for which y is required:"))
while(x<t):
	#print("x= ",x)
	#print("y= ",y)
	
	f=eval(expr)
	print("dy/dx: ",f)
	y=y+(h*f)
	#print("new y:",y)
	x=x+h
	print("y("+str(x)+") = "+str(y))


	
