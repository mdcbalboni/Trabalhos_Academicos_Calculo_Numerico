from math import e
def secante(b,x0,x1,erro):
	while abs(b(x1)-b(x0)) >= erro:
		if b(x1)-b(x0) == 0:
			return x1
		aux= ((x0*b(x1))-(b(x0)*x1))/(b(x1)-b(x0))
		x0 = x1
		x1 = aux
	return x1	
print secante(lambda x: x*e**x-1,0.6,0.7,0.0001)
