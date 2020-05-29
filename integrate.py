from scipy.integrate import quad
def integrand(x):
	return x**2 + 1
#I = quad(integrand, 0, 1, args=(a,b))
I = quad(integrand, 0, 1)
print(I)
