#Newton divided difference Interpolation
#Input: Set of known points(x,y) and value at which f(x) is to be found
#Output:
#1. Newtons Divided Difference Table
#2. Interpolation polynomial
#3. f(x) at value given as input by user


#function to print interpolation polynomial
def interpolation_polynomial(known_points, get_string=False):
    """Create an string of interpolation polynomial of upto n degree passing through all 
    of the supplied n+1 points.
    Inputs: known_points - a table of known points on your function supplied 
            as a list of (x,y) tuples, where each x value is unique.
             p_string - a string representation of polynomial.
    """

    x_knots = sorted(point[0] for point in known_points)
    n = len(x_knots) - 1
    f_cache = {(xi,):yi for xi,yi in sorted(known_points)}
    def f(xs):
        xi_tuple = tuple(sorted(xs))
        if xi_tuple not in f_cache:
            f_cache[xi_tuple] = (f(xi_tuple[1:]) - f(xi_tuple[:-1])) /  \
                             float(xi_tuple[-1]  -   xi_tuple[0])
        return f_cache[xi_tuple]
	
    div_diffs = f
    
    # coefficients - f(x0), f(x0,x1), ..., f(x0,x1,...,xn):
    coeffs = [div_diffs(x_knots[:i+1]) for i in range(len(x_knots))]
    
    # polynomial:
    def p(x):
        total = coeffs[0]  # coeffs[0] = div_diff(x0) = y0
        basis = 1
        for i in range(n): 
            basis = basis * (x - x_knots[i])
            total = total + coeffs[i+1] * basis
        return total

    basis, poly_string = '', str(coeffs[0])
    for ci,xi in zip(coeffs[1:], x_knots[:-1]):
        # basis (x - x0)(x - x1)...(x - xi)
        if xi < 0:
            basis += '(x + ' + str(-xi) + ')'
        elif xi == 0:
            basis += 'x'
        else:
            basis += '(x - ' + str(xi) + ')'
        
        # append the ith's term, e.g. ci(x-x0)(x-x1)...(x-xi)
        add = ' + ' if ci >= 0 else ' - '
        if ci == 0:
            next
        elif abs(ci) == 1: 
            poly_string += add + basis
        else:
            poly_string += add + str(abs(ci)) + basis
    return 'p(x) = ' + poly_string


##################################################################################    
# Function to find the product term 
def proterm(i, value, x): 
	pro = 1; 
	for j in range(i): 
		pro = pro * (value - x[j]); 
	return pro; 

###################################################################################
#create divided difference table 
def dividedDiffTable(x, y, n): 

	for i in range(1, n): 
		for j in range(n - i): 
			y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
									(x[j] - x[i + j])); 
	return y; 

#####################################################################################

# Function for applying Newton's 
# divided difference formula 
def applyFormula(value, x, y, n): 

	sum = y[0][0]; 

	for i in range(1, n): 
		sum = sum + (proterm(i, value, x) * y[0][i]); 
	
	return sum; 
######################################################################################
# Function for printing divided 
# difference table 
def printDiffTable(y, n): 

	for i in range(n): 
		for j in range(n - i): 
			print(round(y[i][j], 4), "\t", 
							end = " "); 

		print(""); 



if __name__ == '__main__':
	

	print("Newton’s Divided Difference Interpolation\n")

	n=int(input("Enter the number of known_points: "))
	
	known_points=[]
	y = [[0 for i in range(10)] 
		for j in range(n)];
	x=[0 for i in range(n)]
	print("Enter known points in the form x,y :  ")
	for i in range(n):
		coordinates=input("x"+str(i)+",y"+str(i)+" :").split(',')
		xi=float(coordinates[0])
		yi=float(coordinates[1])
		known_points.append((xi,yi))
		x[i]=xi
		y[i][0]=yi


	# calculating divided difference table 
	y=dividedDiffTable(x, y, n); 
	print("\nAnswer:")
	print("The Divided difference Table (Note: spacing not correct when displayed):\n")
	# displaying divided difference table 
	printDiffTable(y, n);

	#print interpolating polynomial
	p_string = interpolation_polynomial(known_points, get_string=True)
	print("\nThe interpolated polynomial is "+p_string)
	k=int(input('Enter number values at which f(x) is to be calculated: '))
	print("")
	for i in range(k):
		value=float(input("\nEnter value"+str(i+1)+" for which f(x) needs to be evaluated using interpolation: "))

		# printing the value 
		print("f(x) at ", value, " = ", 
				round(applyFormula(value, x, y, n), 5)) 


