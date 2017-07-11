#-*- coding: utf-8 -*-
import numpy
filas=int(raw_input('Valor de filas:'))
columnas=int(raw_input('Valor de columnas:'))
matrix = numpy.zeros((filas,columnas))
vector= numpy.zeros((columnas))
x=numpy.zeros((filas))
print 'Introduce la matriz de coeficientes y el vector solución columnas'
for r in range(filas):
    for c in range(columnas):
        matrix[(r),(c)]=(raw_input("Elemento a["+str(r+1)+","+str(c+1)+"] "))
    vector[(r)]=(raw_input('b['+str(r+1)+']: '))
print(matrix)
for k in range(filas):
    for r in range(k+1,filas):
        factor=(matrix[r,k]/matrix[k,k])
        vector[r]=vector[r]-(factor*vector[k])
        for c in range(0,columnas):
            matrix[r,c]=matrix[r,c]-(factor*matrix[k,c])
        print matrix
#sustituciócolumnas hacia atrás
x[filas-1]=vector[filas-1]/matrix[filas-1,filas-1]
print x[filas-1]
for r in range(filas-2,-1,-1):
    suma = 0
    for c in range(0,columnas):
        suma=suma+matrix[r,c]*x[c]
    x[r]=(vector[r]-suma)/matrix[r,r]
print 'Resultado matriz'
print(matrix)
print 'Resultado del vector'
print(vector)
print 'Resultados: '
print(x)
