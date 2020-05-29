expr = input("Enter f(x):")


def y(x):
    
    return eval(expr)


def trapezoidal (a, b, n): 
      
    # Grid spacing 
    h = (b - a) / n 
      
    # Computing sum of first and last terms 
    # in above formula 
    s = (y(a) + y(b)) 
  
    # Adding middle terms in above formula 
    i = 1
    while i < n: 
        s += 2 * y(a + i * h) 
        i += 1
          
    # h/2 indicates (b-a)/2n.  
    # Multiplying h/2 with s. 
    return ((h / 2) * s) 

def simpsons_onebythree( ll, ul, n ): 
  
    # Calculating the value of h 
    h = ( ul - ll )/n 
  
    # List for storing value of x and f(x) 
    x = list() 
    fx = list() 
      
    # Calcuting values of x and f(x) 
    i = 0
    while i<= n: 
        x.append(ll + i * h) 
        fx.append(y(x[i])) 
        i += 1
  
    # Calculating result 
    res = 0
    i = 0
    while i<= n: 
        if i == 0 or i == n: 
            res+= fx[i] 
        elif i % 2 != 0: 
            res+= 4 * fx[i] 
        else: 
            res+= 2 * fx[i] 
        i+= 1
    res = res * (h / 3) 
    return res 


def simpsons_threebyeight(lower_limit, upper_limit, interval_limit ): 
      
    interval_size = (float(upper_limit - lower_limit) / interval_limit) 
    sum = y(lower_limit) + y(upper_limit); 
   
    # Calculates value till integral limit 
    for i in range(1, interval_limit ): 
        if (i % 3 == 0): 
            sum = sum + 2 * y(lower_limit + i * interval_size) 
        else: 
            sum = sum + 3 * y(lower_limit + i * interval_size) 
      
    return ((float( 3 * interval_size) / 8 ) * sum ) 




a=int(input("a: "))
b=int(input("b: "))
n=int(input("n: "))
print("trapezoidal: ",trapezoidal (a, b, n))
print("simpsons_onebythree",simpsons_onebythree(a,b,n))
print("simpsons_threebyeight",simpsons_threebyeight(a,b,n))





