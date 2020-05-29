from math import *
l=int(input("l:"))
h=int(input("h:"))
a=(h-l)/2
b=(l+h)/2
print("a:",a)
print("b:",b)

expr = input("x=at+b; Enter the function(in terms of x):")
dx=a
t=0
x=a*t + b
s=eval(expr)

print("1 point:")
print("f(0)=",s*dx)

print("2*f(0)",2*eval(expr)*dx)

t=-1/sqrt(3)
x=a*t + b
q=eval(expr)*dx
print("-1/sqrt(3) f:",q)
t=1/sqrt(3)
x=a*t + b
r=eval(expr)*dx
print("1/sqrt(3) f:",r)
print("2 point:",q+r)
t=-sqrt(3/5)
x=a*t + b
q=eval(expr)*dx
t=sqrt(3/5)
x=a*t + b
r=eval(expr)*dx
print("f(-sqrt(3/5)):",q)
print("f(sqrt(3/5)):",r)
print("3 point:",(5*q+8*s+5*r)/9)




