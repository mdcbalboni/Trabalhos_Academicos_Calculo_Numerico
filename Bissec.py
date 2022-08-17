from math import *
def Bissec(func,a,b,erro):
	while (b - a) >= erro:
		x = (a + b)/2.0
		if func(x) > 0:
			a = x
		else:
			b = x
	return a
def BissecPP(func,a,b,erro): #Bissec step-by-step
	cont=0
	print " K       a         b           x        f(a)       f(b)       Erro    "
	while (b - a) >= erro:
		print "%2d"%cont," |","%1f" % a,"|","%1f" % b,"|","%1f" % ((b+a)/2.0),"|","%1f" % func(a),"|","%1f" %func(b), "|","%1f" %(b-a)
		x = (a + b)/2.0
		if func(x) > 0:
			a = x
		else:
			b = x
		cont+=1
	return a
print Bissec(lambda x: x**3-9*x+3, 0,1,0.0001)
print BissecPP(lambda x: x**3-9*x+3, 0,1,0.0001)
