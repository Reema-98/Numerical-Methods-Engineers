from math import *
from sympy import diff, Symbol
import numpy as np
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
#print(u)
x=0
for i in range(xn-1):
	u[i]=eval(u_x_0)
	print("x: ",x)
	print("u(x,0)"+str(u[i]))
	x=x+h
u[xn-1]=u_n_t
print("===========")
print(str(-alpha)+"u(i-1,j+1) + "+str(2+(2*alpha))+"u(i,j+1) + "+str(-alpha)+"u(i+1,j+1) = "+str(alpha)+"u(i-1,j) + "+str(2-(2*alpha))+"u(i,j) + "+str(alpha)+"u(i+1,j")
print("-----------------")
i=1
j=0
n=xn-2
for j in range(tn-1):
	print("j : ",j)
	A=np.zeros((n,n))
	B=np.zeros(n)
	#first eqn
	#A[0][0]=u_0_t
	#A[0][n-1]=u_n_t
	A[0][i-1]=2+(2*alpha)
	A[0][i]=-alpha
	print("i : ",i)
	print("LHS\n"+str(-alpha)+"u"+"("+str(i-1)+","+str(j+1)+") +"+str(2+(2*alpha))+"u" +"("+str(i)+","+str(j+1)+") +"+str(-alpha)+"u("+str(i+1)+","+str(j+1)+") ")
	print("RHS\n="+str(alpha)+"u"+"("+str(i-1)+","+str(j)+") +"+str(2-(2*alpha))+"u" +"("+str(i)+","+str(j)+") +"+str(alpha)+"u("+str(i+1)+","+str(j)+") ")
	term1=float(alpha*u[i-1])
	print("u(i-1,j)"+" ("+str(i-1)+","+str(j)+") = "+str(u[i-1]))
	term2=float((2-(2*alpha))*u[i])
	print("u(i,j)"+" ("+str(i)+","+str(j)+") = "+str(u[i]))
	term3=float(alpha*u[i+1])
	print("u(i+1,j)"+" ("+str(i+1)+","+str(j)+") = "+str(u[i+1]))
	val=float(term3+term2+term1)
	print("val = "+str(term1)+" + "+str(term2)+" + "+str(term3))
	print("=",val)
	#temp.append(val)
	B[i-1]=val
	temp=[u_0_t]
	for i in range(2,xn-2):
		A[i-1][i-2]=-alpha
		A[i-1][i-1]=2+(2*alpha)
		A[i-1][i]=-alpha

		print("i : ",i)
		term1=float(alpha*u[i-1])
		print("LHS\n"+str(-alpha)+"u"+"("+str(i-1)+","+str(j+1)+") +"+str(2+(2*alpha))+"u" +"("+str(i)+","+str(j+1)+") +"+str(-alpha)+"u("+str(i+1)+","+str(j+1)+") ")
		print("RHS\n="+str(alpha)+"u"+"("+str(i-1)+","+str(j)+") +"+str(2-(2*alpha))+"u" +"("+str(i)+","+str(j)+") +"+str(alpha)+"u("+str(i+1)+","+str(j)+") ")
		print("u(i-1,j)"+" ("+str(i-1)+","+str(j)+") = "+str(u[i-1]))
		term2=float((2-(2*alpha))*u[i])
		print("u(i,j)"+" ("+str(i)+","+str(j)+") = "+str(u[i]))
		term3=float(alpha*u[i+1])
		print("u(i+1,j)"+" ("+str(i+1)+","+str(j)+") = "+str(u[i+1]))
		val=float(term3+term2+term1)
		print("sum = "+str(term1)+" + "+str(term2)+" + "+str(term3))
		print("=",val)
		#temp.append(val)
		B[i-1]=val
		
		print("---------------")
	#temp.append(u_n_t)
	#last eqn
	A[n-1][n-1]=2+(2*alpha)
	A[n-1][n-2]=-alpha
	i=n-1
	print("i : ",i)
	print("LHS\n"+str(-alpha)+"u"+"("+str(i-1)+","+str(j+1)+") +"+str(2+(2*alpha))+"u" +"("+str(i)+","+str(j+1)+") +"+str(-alpha)+"u("+str(i+1)+","+str(j+1)+") ")
	print("RHS\n="+str(alpha)+"u"+"("+str(i-1)+","+str(j)+") +"+str(2-(2*alpha))+"u" +"("+str(i)+","+str(j)+") +"+str(alpha)+"u("+str(i+1)+","+str(j)+") ")
	term1=float(alpha*u[i-1])
	print("u(i-1,j)"+" ("+str(i-1)+","+str(j)+") = "+str(u[i-1]))
	term2=float((2-(2*alpha))*u[i])
	print("u(i,j)"+" ("+str(i)+","+str(j)+") = "+str(u[i]))
	term3=float(alpha*u[i+1])
	print("u(i+1,j)"+" ("+str(i+1)+","+str(j)+") = "+str(u[i+1]))
	val=float(term3+term2+term1)
	print("val = "+str(term1)+" + "+str(term2)+" + "+str(term3))
	print("=",val)
	B[n-1]=val
	#print(A)

	#print(B)
	X=np.linalg.solve(A,B)
	

	for r in range(1,xn-1):
		print("u("+str(r)+","+str(j+1)+") = "+str(X[r-1]))
	print("U=",X)
	for q in X:

		temp.append(q)

	temp.append(u_n_t)
	u=temp
	


	
	print("******************")
	





