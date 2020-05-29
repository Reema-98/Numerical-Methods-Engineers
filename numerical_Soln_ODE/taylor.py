import math
from math import *
def differentiate(x,y):
	ylist=[]
	ylist.append(y)
	expr1= input("Enter y':")
	y1=eval(expr1)
	print("y'=",y1)
	ylist.append(y1)
	expr2= input("Enter y''(use y1 for y'): ")
	y2=eval(expr2)
	print("y''=",y2)
	ylist.append(y2)
	expr3= input("Enter y'''(use y2,y1 for y' y''): ")
	y3=eval(expr3)
	print("y'''=",y3)
	ylist.append(y3)
	expr4= input("Enter y'''':")
	y4=eval(expr4)
	print("y''''=",y4)
	ylist.append(y4)
	return ylist	

x0=float(input("enter x0:"))
y0=float(input("enter y0:"))


#expr4= input("Enter y'''':")
#y4=eval(expr4)
#print("y''''=",y4)
#ylist.append(y4)

n=int(input("ennter upto how many derivatives: "))
ylist=[]
targetx=float(input("enter x for which f(x) is to be found"))
c=int(input("enter use x-x0(press 2) fomula or h formula(press 1): "))
exprlist=[]
if c==1:
	x=x0
	y=y0
	y11= input("Enter y':")
	y22= input("Enter y'':")
	y33= input("Enter y''':")
	h=float(input('enter h:'))
	while(x<targetx):
		ylist=[]
		ylist.append(y)
		
		y1=eval(y11)
		print("y'=",y1)
		ylist.append(y1)
		
		y2=eval(y22)
		print("y''=",y2)
		ylist.append(y2)
		
		y3=eval(y33)
		print("y'''=",y3)
		ylist.append(y3)
		f=0
		for i in range(n):
			f=f+(((h**i)/math.factorial(i))*ylist[i])
		x=x+h
		y=f
		print("x=",x)
		print("y=",y)
		
		





else:
	
	x=x0
	y=y0

	ylist.append(y)
	expr1= input("Enter y':")
	y1=eval(expr1)
	print("y'=",y1)
	ylist.append(y1)
	expr2= input("Enter y'':")
	y2=eval(expr2)
	print("y''=",y2)
	ylist.append(y2)
	expr3= input("Enter y''':")
	y3=eval(expr3)
	print("y'''=",y3)
	ylist.append(y3)
	expr4= input("Enter y'''':")
	y4=eval(expr4)
	print("y''''=",y4)
	ylist.append(y4)
	

		
	f=0
	for i in range(n):
		f=f+((((targetx-x0)**i)/math.factorial(i))*ylist[i])
	print("f("+str(targetx)+")=",f)


	
	
	

