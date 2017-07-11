from os import system
matrices = []#arreglo padre de matrices creadas
suma = []#arreglo padre de matrices sumadas
multiplicacion = []#arreglo padre de matrices multiplicadas

def menu():
    print '''
    1) Crear una matriz
    2) Ver las matrices
    3) Eliminar una matriz
    4) Operaciones de matrices
    '''

def menuMostrar():
    print '''
 ======Cuales Matrices desea ver======
    1) Matrices creadas
    2) Matrices sumadas
    3) Matrices multiplicadas
    '''
    opc = int(raw_input('Elige una opcion: '))
    if opc == 1:
        mostrarMatrices(matrices)
    elif opc == 2:
        mostrarMatrices(suma)
    elif opc == 3:
        mostrarMatrices(multiplicacion)

def menuOperaciones(matrizPadre, matrizSuma, matrizMulti):
    print '''
 ======Que operacion desea realizar======
    1) Sumar matrices
    2) Multiplicar matrices
    '''
    opc = int(raw_input('Elige una opcion: '))
    if opc == 1:
        sumarMatrices(matrizPadre, matrizSuma)
    elif opc == 2:
        multiplicarMatrices(matrizPadre, matrizMulti)

def crearMatriz(matriz):
    numeroMatriz = len(matriz)
    cantidadMatriz = int(raw_input('\n Cuantas matrices desea: '))
    for i in range(cantidadMatriz):
        matriz.append([])#agrega un arreglo al final del arreglo padre
        filas = int(raw_input('\n Introduce el numero de filas para la matriz numero '+str(i+1)+': '))
        columnas = int(raw_input(' Introduce el numero de columnas para la matriz numero '+str(i+1)+': '))
        for k in range(filas):#este for() agrega una fila de la matriz dentro del arreglo hijo en el que nos encontramos(el que acabamos de crear arriba)
            matriz[numeroMatriz].append([])
            for j in range(columnas):#este for() agrega los valores dentro del la fila que acabamos de crear
                valor = '\n Introduce el valor que desea para '+str(k+1)+','+str(j+1)+': '
                x = int(raw_input(valor))#valor
                matriz[numeroMatriz][k].append(x)#agrego el valor al final de la fila que acabamos de crear
        numeroMatriz += 1

def mostrarMatrices(matriz):
    contadorMatrices = 1
    algo = ''
    for i in matriz:#accede a las matrices que contiene el arreglo padre
        for ii in i:# accede a los valores que contienen la  ya accedidos
            algo += str(ii)+'\n\t'
        print'''
        %i)\n\t%s'''%(contadorMatrices,algo)
        contadorMatrices += 1
        algo = ''

def verificarDimensionMatrices(matrizPadre, indiceMatriz1, indiceMatriz2):
    for i in matrizPadre[indiceMatriz1 - 1]:
        filaMatriz1 = len(matrizPadre[indiceMatriz1 - 1])#filas de la matriz 1
        colMatriz1 = len(i)#columnas de la matriz 1
    for i in matrizPadre[indiceMatriz2 - 1]:
        filaMatriz2 = len(matrizPadre[indiceMatriz2 - 1])#filas de la matriz 2
        colMatriz2 = len(i)#columnas de la matriz 2
    return filaMatriz1, colMatriz1, filaMatriz2, colMatriz2

def eliminarMatriz(matriz):
    mostrarMatrices(matriz)
    elegirMatriz = int(raw_input("Elige que matriz desea eliminar: "))
    if matrices[elegirMatriz - 1] in matriz:
        matrices.pop(elegirMatriz - 1)

def sumarMatrices(matriz,matrizSuma):
    iterador = 0
    numeroMatrices = len(matrizSuma)
    # print numeroMatrices
    mostrarMatrices(matriz)
    elegirMatriz1 = int(raw_input("Elige una de las matrices para sumarla: "))
    if matrices[elegirMatriz1 - 1] in matrices:
        mostrarMatrices(matriz)
        elegirMatriz2 = int(raw_input("Elige una de las matrices para sumarla con la elegida anteriormente: "))
        if matrices[elegirMatriz2 - 1] in matrices:
            filaMatriz1, colMatriz1, filaMatriz2, colMatriz2 = verificarDimensionMatrices(matriz, elegirMatriz1, elegirMatriz2)
    if filaMatriz1 == filaMatriz2:
        if colMatriz1 == colMatriz2:
            for i in range(1):
                matrizSuma.append([])
                for j in range(filaMatriz2):
                    iterador2 = 0
                    matrizSuma[numeroMatrices].append([])
                    for k in range(colMatriz1):
                        matrizSuma[numeroMatrices][iterador].append(matriz[elegirMatriz1 - 1][iterador][iterador2] + matriz[elegirMatriz2 - 1][iterador][iterador2])
                        iterador2 += 1
                    iterador += 1
        else:
            print 'Las columnas no coinciden'
    else:
        print 'Las filas no coinciden'

def multiplicarMatrices(matriz, matrisMulti):
    print 'Hola'

def main():
    while True:
        menu()
        opc = int(raw_input('\n elige una opcion: '))
        if opc == 1:
            crearMatriz(matrices)#Si si el usuario eligio la opcion uno del menu se ejecutara este bloque de codigo que es la funcion de crear matrices
        elif opc == 2:
            menuMostrar()
            #Si si el usuario eligio la opcion uno del menu se ejecutara este bloque de codigo que es la funcion de mostrar la o las matrices
        elif opc == 3:
            eliminarMatriz(matrices)
        elif opc == 4:
            menuOperaciones(matrices, suma, multiplicacion)
        else:
            system('cls')
            break#si no se escoge ninguna opcion se cierra el programa

main()
