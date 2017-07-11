#-*- coding: utf-8 -*-
def poli(x):
    y=pow(x,2)-3.0*x-4
    return y

print "Método de la secante"

x1=float(raw_input('Introduce el valor de inicio x1: '))
x0=float(raw_input('Introduce el valor de inicio x0: '))
erroru=float(raw_input('Introduce el error '))
raiz=[]
raiz.insert(0,0)
i=0
error=1
while abs(error) > erroru:
    x2 = x1 - (poli(x1)*(x1-x0))/(poli(x1)-poli(x0))
    raiz.append(x2)
    x0 = x1
    x1 = x2
    i += 1
    error=(raiz[i]-raiz[i-1])/raiz[i]
    print x2
