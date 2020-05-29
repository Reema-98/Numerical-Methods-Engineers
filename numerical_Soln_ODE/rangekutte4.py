h=float(input('enter h:'))
x0=float(input('enter x0:'))
y0=float(input('enter y0:'))

expr = input("Enter f(x,y):")
t=float(input("enter target x for which y is required:"))
curx=x0
cury=y0
while(curx<t):
	print(curx)
	print(cury)
	x=curx
	y=cury
	k1=h*eval(expr)
	print("k1: ",k1)
	x=curx+(h/2)
	y=cury+(k1/2)
	k2=h*eval(expr)
	print("k2: ",k2)
	x=curx+(h/2)
	y=cury+(k2/2)
	k3=h*eval(expr)
	print("k3: ",k3)
	x=curx+h
	y=cury+k3
	k4=h*eval(expr)
	print("k4: ",k4)
	k=(k1+(2*k2)+(2*k3)+k4)/6
	print("k: ",k)
	cury=cury+k
	curx=curx+h
print("y=",cury)
