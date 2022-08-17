def PFalsaPP(f,x0,x1,erro): #Step-by-Step
	cont=0
	x2=x0 - f(x0)*(x1-x0)/(f(x1)-f(x0))
	print " K       a         b           x        f(a)       f(b)       Erro    "
	while abs(f(x2))> erro:
		print "%2d"%cont," |","%1f" % x0,"|","%1f" % x1,"|","%1f" % x2,"|","%1f" % f(x0),"|","%1f" %f(x1), "|","%1f" %f(x2)
		if (f(x0)*f(x2)>0):
			 x0=x2
		else:
			 x1=x2
		x2=x0 - f(x0)*(x1-x0)/(f(x1)-f(x0))
		cont+=1
	return x2
def PFalsa(f,x0,x1,erro):
	x2=x0 - f(x0)*(x1-x0)/(f(x1)-f(x0))
	while abs(f(x2))> erro:
		if (f(x0)*f(x2)>0):
			 x0=x2
		else:
			 x1=x2
		x2=x0 - f(x0)*(x1-x0)/(f(x1)-f(x0))
	return x2
#print PFalsaPP(lambda x: x**3-9*x+3, 0.0,1.0,0.0001)
#print PFalsa(lambda x: x**3-9*x+3, 0.0,1.0,0.0001)
