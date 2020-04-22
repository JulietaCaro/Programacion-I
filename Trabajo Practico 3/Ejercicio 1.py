# 1. Desarrollar cada una de las siguientes funciones:
# a. Cargar números enteros en una matriz de N x N, ingresando los datos desde teclado.
# b. Ordenar en forma ascendente cada una de las filas de la matriz.
# c. Intercambiar dos filas, cuyos números se reciben como parámetro.
# d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
# e. Intercambiar una fila por una columna, cuyos números se reciben como parámetro.
# f. Transponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji).
#g. Calcular el promedio de los elementos de una fila, cuyo número se recibe como parámetro.
#h. Calcular el porcentaje de elementos con valor impar en una columna,
#cuyo número se recibe como parámetro.
#i. Determinar si la matriz es simétrica con respecto a su diagonal principal.
#j. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
# FUNCIONES
def imprimirMatriz(matriz):
    'Imprime una matriz con formato'
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end="")
        print()
        
# FUNCION a.    
def crearMatrizPorTeclado(n):
    '''Crea una matriz NxN, cuadrada
    Parametro de entrada: n
    Retorna una matriz
    '''
    matriz = []
    filas = n
    columnas = n
    for f in range(filas):
        'Cantidad de filas que quiero'
        matriz.append([]) # Agrego una lista que representa una fila de la matriz
        for c in range(columnas):
            matriz[f].append(int(input("Ingrese un numero: ")))
    return matriz

# FUNCION b.
def ordenarFilas(matriz):
    '''Ordena todas las filas de la matriz
    Parametro de entrada: matriz
    '''
    for f in range(len(matriz)):
        matriz[f].sort()
        
# FUNCION c.
def intercambiarFilas(matriz, filaA, filaB):
    '''Intercambia dos filas
    Parametro de entrada: matriz, filas a intercambiar
    '''
    aux = matriz[filaA]
    matriz[filaA] = matriz[filaB]
    matriz[filaB] = aux

# FUNCION d.
def intercambiarColumnas(matriz,columnaA, columnaB):
    '''Intercambia columnas
    parametros de entrada: matriz, columnas a intercambiar
    '''
    for fila in matriz:
        aux = fila[columnaA]
        fila[columnaA] = fila[columnaB]
        fila[columnaB] = aux

# FUNCION e.
def intercambiarFilaPorColumna(matriz, fila):
    '''Intercambia fila y columna
    Parametros de entrada: matriz y fila por cambiar
    '''
    for i in range(len(matriz)):
        aux = matriz[fila][i]
        matriz[fila][i] = matriz[i][fila]
        matriz[i][fila] = aux

# FUNCION f.
def transponerMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(0,i):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux
            
#FUNCION g.
def promedioDeUnaFila(fila, matriz):
    prom = sum(matriz[fila])//len(matriz)
    return prom

#FUNCION h.
def porcentajeImpares(columna, matriz):
    c = columna
    acum = 0
    for f in range(len(matriz)):
        if matriz[f][c] % 2 != 0:
            acum = acum + 1    
    if acum == 0:
        porcen = 0
    else:
        porcen = (acum*100)//len(matriz)
    return porcen

#FUNCION i.
def matrizSimetrica(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    acum = 0
    esSimetrica = False
    for f in range(filas):
        for c in range(columnas):
            if matriz[f][c]==matriz[c][f]:
                acum = acum + 1
    if acum == (filas*columnas):
        esSimetrica = True
    return esSimetrica
        
#FUNCION j.
def matrizSimetricaSecun(matriz):
    tamano = len(matriz)-1
    acum = 0
    esSime = False
    for f in range(tamano,-1,-1):
        for c in range(tamano):
            if matriz[f][c] == matriz[c][f]:
                acum = acum + 1
    if acum == len(matriz)*2:
        esSime = True
    return esSime

#FUNCION k.
        
def main():
    'Programa principal'
    tamano = int(input("Ingrese el tamaño de la matriz: "))
    matriz = crearMatrizPorTeclado(tamano)
    print("Matriz creada de",tamano,"x",tamano,":")
    imprimirMatriz(matriz)
    print("Filas de la matriz ordenadas: ")
    ordenarFilas(matriz)
    imprimirMatriz(matriz)
    print("Filas intercambiadas: ")
    intercambiarFilas(matriz,0,2)
    imprimirMatriz(matriz)
    print("Columnas intercambiadas: ")
    intercambiarColumnas(matriz,0,1)
    imprimirMatriz(matriz)
    print("Fila intercambiada con columna: ")
    intercambiarFilaPorColumna(matriz,0)
    imprimirMatriz(matriz)
    print("Matriz transpuesta: ")
    transponerMatriz(matriz)
    imprimirMatriz(matriz)
    promedio = promedioDeUnaFila(2, matriz)
    print("Promedio de la fila: ",promedio)
    porcentaje = porcentajeImpares(2,matriz)
    if porcentaje == 0:
        print("No hay numeros impares en esa columna")
    else:
        print("Porcentaje de impares en la columna 3: ",porcentaje,"%")
    matrizSime = matrizSimetrica(matriz)
    if matrizSime:
        print("La matriz es simetrica segun su diagonal principal")
    else:
        print("La matriz no es simetrica segun su diagonal principal")
    matrizSimeSecun = matrizSimetricaSecun(matriz)
    if matrizSimeSecun:
        print("La matriz es simetrica segun su diagonal secundaria")
    else:
        print("La matriz no es simetrica segun su diagonal secundaria")

# PROGRAMA PRINCIPAL
main()