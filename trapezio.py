#Bibliotecas
import math
from math import *
import time
from decimal import *
def funcao(x):
	return e**(-x**2)
ini = time.time()
a=0.0
b=1.0
n=4
total=0
tamanho=(b-a)/n #h
total=total+funcao(a)
total=total+funcao(b) 
aux=a
for i in range(n-1):
	aux=aux+tamanho
	total=total+2*funcao(aux)
total=(tamanho/2.0)*total #total
print '%.14f' %total #resultado final
fim = time.time()
print "Tempo que levou para a variavel de Pareto com o metodo Simpson real: ", fim-ini
