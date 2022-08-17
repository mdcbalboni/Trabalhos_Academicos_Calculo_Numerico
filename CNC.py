#!/usr/bin/python
# -*- coding: UTF-8 -*-

__license__ = 'GPL, GNU Public License'
__credits__ = 'http://doc.async.com.br/python/Tkinter/index.htm'
#As bibliotecas usadas foram, intpy, scipy, math e TKinter
#Para instalar a biblioteca intpy, primeiro instala https://pypi.python.org/pypi/fpconst, com o comando sudo python setup.py install 
#depois instala https://pypi.python.org/pypi?:action=display&name=IntPy&version=0.1.3 com o comando  sudo python setup.py install 
#Para instalar a scipy, usa o comando sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
#E pra instalar a TKinter usa sudo apt-get install python-tk

from Tkinter import *
from math import *
import sys
import math
from scipy import integrate
from scipy import inf
from math import exp, expm1
from intpy import *
from intpy.support.stdfunc import sqrt
from math import sqrt
from decimal import *
import time
from math import cos
from math import e

def secante(x0,x1,erro):
	while abs(funcao(x1)-funcao(x0)) >= erro:
		if funcao(x1)-funcao(x0) == 0:
			return x1
		aux= ((x0*funcao(x1))-(funcao(x0)*x1))/(funcao(x1)-funcao(x0))
		x0 = x1
		x1 = aux
		#print x1
	return x1
	
def funcao(x):
	return x*e**x-1



def ErroAbsoluto(xk, xi):
    print("Erro Absoluto: " + str(abs(xk - (xi.middle()))) + " < " + str((xi.diameter()/2)))
    print ""
    
def Diametro(x):
	d=(x.sup-x.inf)
	print "O diametro do intervalor é: " + str(d)
	print ""
	
def ErroRelativo(xk, xi):
    print("Erro Relativo: " + str(abs((xk - xi.middle())/xk)) + " <= " + str((xi.diameter()/(2*xi.inf))))
    print ""

def Pareto(alp, beta, a, b):
	f=lambda x,a: (alp*beta**alp)/(x**(alp+1)) #coloca a expressao numa variavel
	y, err = integrate.quad(f, a, b, args=(1,)) #realiza a integral
	return y

def Exponencial(alp, a, b):
	e=2.7182818284590452353602874713526624977572470936999595
	return ((e**(-alp*a))-e**(-alp*b)) #printa a expressao

def Normal(alpha, mi, a, b):
	pi=3.14159265358979323846264338327950288419716939937510
	eu=2.7182818284590452353602874713526624977572470936999595
	f=lambda x,a: (1/(alpha*sqrt(2*pi)))*eu**(-(x-mi)**2/(2*alpha**2)) #coloca a expressao numa variavel
	y, err = integrate.quad(f, a, b, args=(1,)) #realiza a integral
	return y # Resultado final

def Gama(lamb, v, a, b):
	f=lambda x,a: exp(-lamb*x)*x**(v-1)#salva o valor da expressao numa variavel.
	y, err = integrate.quad(f, 0, inf, args=(1,))#Faz a integral do valor com 0 e inf, segunda parte do slide. salva o resultado na variavel y.
	y=y**-1 #Inverte a variavel pra usar na primeira parte do slide. 
	z, err = integrate.quad(f, a, b, args=(1,)) #Faz a integral do valor com a, e b. E salva na variavel z.
	return z*y #Printa o resultado final.

def Uniforme(a, b, c, d):
	z=lambda x,a: 1 #Coloca a expressao numa variavel
	z, err = integrate.quad(z, c, d, args=(1,)) #Faz a integral
	return (z*1.0/(b-a))

class Variaveis:
    def __init__(self, toplevel):

        # Janela
        toplevel.title('Variaveis')
        toplevel.geometry("1500x700")

        # Espaçamento
        self.frame1 = Frame(toplevel)
        self.frame1.pack()
    
        # Box 1
        self.frame2 = Frame(toplevel)
        self.frame2.pack()
        # Box 2
        self.frame3 = Frame(toplevel)
        self.frame3.pack()
        # Box 3
        self.frame4 = Frame(toplevel)
        self.frame4.pack()
        # Box 4
        self.frame5 = Frame(toplevel)
        self.frame5.pack()

        # Operações
        self.frame7 = Frame(toplevel, pady=12)
        self.frame7.pack()
       
        # Botões Pareto
        self.frame8 = Frame(toplevel, pady=12)
        self.frame8.pack()
        
        # Botões Exponencial
        self.frame9 = Frame(toplevel, pady=12)
        self.frame9.pack()
        
        # Botões Normal
        self.frame10 = Frame(toplevel, pady=12)
        self.frame10.pack()
        
        # Botões Gama
        self.frame11 = Frame(toplevel, pady=12)
        self.frame11.pack()
        
        # Botões Uniforme
        self.frame12 = Frame(toplevel, pady=12)
        self.frame12.pack()
        
        #Botão Resultado
        self.frame13 = Frame(toplevel, pady=12)
        self.frame13.pack()
        
        # Cor e tamanho das letras 
        Label(self.frame1,text='', fg='black',
        font=('Sawasdee','10'), height=1).pack()
        fontExp=('Sawasdee','12')
        fonte1=('Sawasdee','15')
        fontNor=('Sawasdee','14')
        fontSecante=('Sawasdee','15')
        fontUni=('Sawasdee','15')

        # Botão ParetoReal
        ParetoR=Button(self.frame7,font=fonte1, text='Bissecção',command=self.ParetoR, bg="red")
        ParetoR.pack(side=LEFT)
        ParetoR.pack(side=LEFT)
        
        # Botão Exponencial Real
        ExponencialR=Button(self.frame8,font=fontExp, text='Posição Falsa',command=self.ExponencialR,bg="red")
        ExponencialR.pack(side=LEFT)
      
         # Botão Normal Real
        NormalR=Button(self.frame9,font=fontNor, text='Newton-Raphson',command=self.NormalR,bg="red")
        NormalR.pack(side=LEFT)
                
         # Botão Secante
        Secante=Button(self.frame10,font=fontSecante, text='Secante',command=self.Secante,bg="red")
        Secante.pack(side=LEFT)
        
        # Botão Limpar
        limpar=Button(self.frame12, font=fonte1, text= 'Limpar', command=self.limpar, bg="red")
        limpar.pack(side=LEFT)

        # Botão Sair
        sair=Button(self.frame12, font=fonte1, text= 'Sair', command=self.sair, bg="red")
        sair.pack(side=LEFT)
        
        # Box 1 para entrada de número
        Label(self.frame2,text='Parametro 1 :', font=fonte1,width=20).pack(side=LEFT)
        self.valor1=Entry(self.frame2,width=10,font=fonte1)
        self.valor1.focus_force()
        self.valor1.pack(side=LEFT)
        
         # Box 1 para entrada de número
        Label(self.frame3,text='Parametro 2 :', font=fonte1,width=20).pack(side=LEFT)
        self.valor2=Entry(self.frame3,width=10,font=fonte1)
        self.valor2.pack(side=LEFT)
        
         # Box 1 para entrada de número
        Label(self.frame4,text='Intervalo Inferior :', font=fonte1,width=20).pack(side=LEFT)
        self.valor3=Entry(self.frame4,width=10,font=fonte1)
        self.valor3.focus_force()
        self.valor3.pack(side=LEFT)

        # Box 2 para entrada de número
        Label(self.frame5,text='Intervalo Superior :',font=fonte1,width=20).pack(side=LEFT)
        self.valor4=Entry(self.frame5,width=10,font=fonte1)
        self.valor4.pack(side=LEFT)

        # Resultado
        Label(self.frame11,text='Resultado ',font=fonte1,width=10).pack(side=LEFT)
        self.msg=Label(self.frame11,width=30,font=fonte1)
        self.msg.pack(side=LEFT)
            
    def ParetoR(self):
		ini = time.time()
		valor1 = float(self.valor1.get())
		#valor2 = float(self.valor2.get())
		valor3 = float(self.valor3.get())
		valor4 = float(self.valor4.get())
		resultado=secante(valor3,valor4,valor1)
		self.msg['text']= '%f' %resultado
		

    def ExponencialR(self):
		ini = time.time()
		valor1 = float(self.valor1.get())
		valor2 = float(self.valor2.get())
		resultado=valor1-valor2
		self.msg['text']= '%f' %resultado
		
    def NormalR(self):
		ini = time.time()
		valor1 = float(self.valor1.get())
		valor2 = float(self.valor2.get())
		print valor1*valor2
		
    def Secante(self):
		ini = time.time()
		valor1 = float(self.valor1.get())
		#valor2 = float(self.valor2.get())
		valor3 = float(self.valor3.get())
		valor4 = float(self.valor4.get())
		resultado=secante(valor3,valor4,valor1)
		self.msg['text']= '%f' %resultado
		
    def UniformeR(self):
		return 0
		
		   
    def limpar(self):
        pass
    
    def sair(self):
        app.destroy()

app=Tk()
Variaveis(app)
app.mainloop()
