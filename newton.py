from math import *
def Derivada(f, x, h):
      return (f(x+h) - f(x-h)) / (2.0*h) #Formula da derivada

def funcao(x):
	return x*e**x-1

def newton(f, x0, h):
    xn1 = x0 + 10* h  
    while (abs(x0 - xn1) > h):  
        novo = f(xn1)                     
        x0 = xn1
        xn1 = x0 - novo / Derivada(f, x0, h)  
        print xn1
    return xn1
#Main
erro=0.00000000001
xn=1.0
print newton(funcao, xn, erro)   
#print Derivada(funcao, 2, 3)

