from math import *
from sympy import diff, Symbol
u_x_0=input("u(x,0): ")
N=float(eval(input("boundary : ")))
u_0_t_fn=input("u(0,t)")
t=0
u_0_t=eval(u_0_t_fn)
u_n_t_fn=input("u(n,t)")
t=N
u_n_t=eval(u_n_t_fn)
h=float(eval(input("h: ")))
k=float(eval(input("k: ")))
c2=float(eval(input("c^2: ")))
alpha=float(k*c2/(h**2))
print("alpha: ",alpha)
xn=int((N/h)+1)
tn=int(input("no. of levels including base line.. (no. of steps +1),give 3 as default: "))
u=[0 for i in range(xn)] 
print(u)
x=0
for i in range(xn-1):
	u[i]=eval(u_x_0)
	print("x: ",x)
	print("u(x,0)"+str(u[i]))
	x=x+h
u[xn-1]=u_n_t
print("u(i,j+1 = "+str(alpha)+"+u(i-1,j) + "+str(1-2*alpha)+"u(i,j) + "+str(alpha)+"+u(i+1,j) ")
print("***************")
j=0
for j in range(tn-1):
	print("j : ",j)
	print("")
	temp=[u_0_t]
	for i in range(1,xn-1):
		print("i : ",i)
		term1=float(alpha*u[i-1])
		print("u(i-1,j)"+" ("+str(i-1)+","+str(j)+") = "+str(u[i-1]))
		term2=float((1-(2*alpha))*u[i])
		print("u(i,j)"+" ("+str(i)+","+str(j)+") = "+str(u[i]))
		term3=float(alpha*u[i+1])
		print("u(i+1,j)"+" ("+str(i+1)+","+str(j)+") = "+str(u[i+1]))
		val=float(term3+term2+term1)
		print("u("+str(i)+","+str(j+1)+") = "+str(term1)+" + "+str(term2)+" + "+str(term3))
		print("=",val)
		temp.append(val)
		
		print("---------------")
	temp.append(u_n_t)
	u=temp
	print(u)
	print("******************")
	





