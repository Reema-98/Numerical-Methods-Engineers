# Driver Code 
  
# Number of values given 
n=int(input("Number of values given:"))
#n = 4; 
#x = [ 45, 50, 55, 60 ]; 
# y[][] is used for difference table 
# with y[][0] used for input 
y = [[0 for i in range(n)] 
        for j in range(n)]; 
x=[]
for i in range(n):
	c=float(input("x "+str(i)+":"))
	x.append(c)
	c=float(input("y "+str(i)+":"))
	y[i][0]=c


      
'''
y[0][0] = 0.7071; 
y[1][0] = 0.7660; 
y[2][0] = 0.8192; 
y[3][0] = 0.8660; 
'''
  
# Calculating the forward difference 
# table 
for i in range(1, n): 
    for j in range(n - i): 
        y[j][i] = round(y[j + 1][i - 1] - y[j][i - 1],7); 
  
# Displaying the forward difference table 
for i in range(n): 
    print(x[i], end = "\t"); 
    for j in range(n - i): 
        print(y[i][j], end = "\t"); 
    print(""); 
h=float(input("h= "))
targetx=float(input("enter targetx for which dy/dx and d2y/dx is to be found: "))
#dy/dx
for i in range(n): 
    if x[i]==targetx:
        m=1
        first_derivative=0
        print("finding first_derivative")
        for j in range(1,n - i):
            print("term "+str(j)+" : "+str(m)+"*1/"+str(j)+"*"+str(y[i][j]))
            first_derivative=first_derivative+(m*(1/j)*y[i][j])
            m=m*-1
        coeff=[1,-1,11/12,-5/6,137/180]
        print("finding second_derivative")
        second_derivative=0
        for j in range(2,n - i):
            print("term "+str(j-1)+" : "+str(coeff[j-2])+"*"+str(y[i][j]))
            second_derivative=second_derivative+(coeff[j-2]*y[i][j])
        print("first_derivative:",first_derivative*(1/h))
        print("second_derivative:",second_derivative*(1/h**2))
        break







