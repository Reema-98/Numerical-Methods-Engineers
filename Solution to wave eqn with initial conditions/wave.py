from sympy import * 
from sympy import diff, Symbol
from sympy.parsing.sympy_parser import *
from math import *
import numpy as np
u_i_j, u_iminus1_j, u_iplus1_j,u_i_jminus1,alphasquare,csquare= symbols('u_i_j u_iminus1_j u_iplus1_j u_i_jminus1 alphasquare csquare') 
u_x_0=input("u(x,0)  = f(x) : ")
Ut_x_0=input("Ut(x,0) = g(x): ")
N=float(eval(input("boundary : ")))
u_0_t_fn=input("u(0,t)")
t=0
u_0_t=eval(u_0_t_fn)
u_n_t_fn=input("u(n,t)")
t=N
u_n_t=eval(u_n_t_fn)
c2=float(eval(input("c^2: ")))

c=int(input("1. h is given k not given\n2. k is given h not given \n3. both h and k given  \nEnter option:"))
if c==1:
	alpha2=float(1/c2)
	h=float(eval(input("h: ")))
	k=float(sqrt(alpha2)/h)
if c==2:
	alpha2=float(1/c2)
	k=float(eval(input("k: ")))
	h=float(sqrt(alpha2)/k)
if c==3:
	h=float(eval(input("h: ")))
	k=float(eval(input("k: ")))
	alpha=k/h
	alpha2=alpha**2
print("alpha^2: ",alpha2)
print("h: ",h)
print("k : ",k)
ansmartrix=[]
xn=int((N/h)+1)
Tn=float(eval(input("Enter upto what value of t, levels are to be found : ")))
tn=int((Tn/k)+1)
print("---------------")
j=0
print("row 1")

u_jminus1=[0 for i in range(xn)] 
#print(u)
x=h
u_jminus1[0]=u_0_t
for i in range(1,xn-1):
	u_jminus1[i]=eval(u_x_0)
	print("x: ",x)
	print("i : ",i)
	print("using u(x,0) u("+str(i)+",0) = "+str(u_jminus1[i]))
	x=x+h
u_jminus1[xn-1]=u_n_t
print(u_jminus1)
ansmartrix.append(u_jminus1)
print("---------------")
j=1
print("row 2")
print("using eqn u(i,j+1)-u(i,j)/k=g(x)")

u_j=[0 for i in range(xn)] 
#print(u)
x=0
u_j[0]=u_0_t
for i in range(1,xn-1):
	blah=eval(Ut_x_0)
	
	print("x: ",x)
	print("Ut(x,0)"+str(blah))
	print("i : ",i)
	u_j[i]=k*blah + u_jminus1[i]
	print("u(i,1) = ("+str(i)+",1) ="+str(u_j[i]))
	x=x+h
u_j[xn-1]=u_n_t
print(u_j)
ansmartrix.append(u_j)
print("---------------")
eqn='(2*(1-alphasquare*csquare)*u_i_j)+(alphasquare*csquare*(u_iminus1_j+u_iplus1_j))-u_i_jminus1'
csquare=c2
print(eval(eqn))
alphasquare=alpha2
print(eval(eqn))

for j in range(2,tn):
	
	temp=[u_0_t]
	print("j + 1 =  ",j)
	for i in range(1,xn-1):
		print("i = ",i)
		term1='2*(1-alphasquare*csquare)*u_i_j'
		term2='alphasquare*csquare*(u_iminus1_j+u_iplus1_j)'
		term3='-u_i_jminus1'
		u_i_j=u_j[i]
		u_iminus1_j=u_j[i-1]
		u_iplus1_j=u_j[i+1]
		u_i_jminus1=u_jminus1[i]
		print("term1 : ",eval(term1))
		print("term2 : ",eval(term2))
		print("term3 : ",eval(term3))
		ans=eval(eqn)
		print("u(i,j+1) = u("+str(i)+","+str(j)+") = ",ans)
		temp.append(ans)
	temp.append(u_n_t)
	print(temp)
	ansmartrix.append(temp)
	u_jminus1=u_j
	u_j=temp
	print("---------")
for i in ansmartrix:
	print(i)










