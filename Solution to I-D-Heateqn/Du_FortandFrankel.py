from sympy import * 
from sympy import diff, Symbol
from sympy.parsing.sympy_parser import *
from math import *
u_iminus1_j, u_iplus1_j,u_i_jminus1= symbols('u_iminus1_j u_iplus1_j u_i_jminus1') 
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
u_jminus1=[0 for i in range(xn)] 
#print(u_jminus1)
x=0
for i in range(xn-1):
	u_jminus1[i]=eval(u_x_0)
	print("x: ",x)
	print("u(x,0)"+str(u_jminus1[i]))
	x=x+h
u_jminus1[xn-1]=u_n_t
print("u(i,0")
print(u_jminus1)
print("**********************")
j=0
print ("using schimdt method we get u(i,1)")
print("u(i,j+1 = "+str(alpha)+"+u(i-1,j) + "+str(1-2*alpha)+"u(i,j) + "+str(alpha)+"+u(i+1,j) ")
print("j : ",j)
u_j=[u_0_t]
for i in range(1,xn-1):
	print("i : ",i)
	term1=float(alpha*u_jminus1[i-1])
	print("u(i-1,j)"+" ("+str(i-1)+","+str(j)+") = "+str(u_jminus1[i-1]))
	term2=float((1-(2*alpha))*u_jminus1[i])
	print("u(i,j)"+" ("+str(i)+","+str(j)+") = "+str(u_jminus1[i]))
	term3=float(alpha*u_jminus1[i+1])
	print("u(i+1,j)"+" ("+str(i+1)+","+str(j)+") = "+str(u_jminus1[i+1]))
	val=float(term3+term2+term1)
	print("u("+str(i)+","+str(j+1)+") = "+str(term1)+" + "+str(term2)+" + "+str(term3))
	print("=",val)
	u_j.append(val)
	
	print("---------------")
u_j.append(u_n_t)

print(u_j)
print("******************")
eqn='(((1-2*alpha)/(1+2*alpha))*u_i_jminus1)+(((2*alpha)/(1+2*alpha))*(u_iminus1_j+u_iplus1_j))'
print(eval(eqn))

for j in range(1,tn-1):
	print("--------------------")
	print("j : ",j)
	print("")
	temp=[u_0_t]
	for i in range(1,xn-1):
		print("i : ",i)
		term1='((1-2*alpha)/(1+2*alpha))*u_i_jminus1'
		u_i_jminus1=u_jminus1[i]
		print("u(i,j-1)"+" ("+str(i)+","+str(j-1)+") = "+str(u_i_jminus1))
		term2='((2*alpha)/(1+2*alpha))*(u_iminus1_j+u_iplus1_j)'
		u_iminus1_j=u_j[i-1]
		u_iplus1_j=u_j[i+1]
		print("u(i-1,j)"+" ("+str(i-1)+","+str(j)+") = "+str(u_iminus1_j))
		print("u(i+1,j)"+" ("+str(i+1)+","+str(j)+") = "+str(u_iplus1_j))
		
		print("u("+str(i)+","+str(j+1)+") = "+str(eval(term1))+" + "+str(eval(term2)))
		val=eval(eqn)
		print("u("+str(i)+","+str(j+1)+",) = ",val)
		temp.append(val)
		
		print("===================")
	temp.append(u_n_t)
	u_jminus1=u_j
	u_j=temp
	print("--------------------")


	





