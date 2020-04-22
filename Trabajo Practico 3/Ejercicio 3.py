#3. Desarrollar un programa para rellenar una matriz de N x N con números enteros al
#azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repita.
#Imprimir la matriz por pantalla.

from random import randint
#FUNCIONES
def crearMatriz(N = 4):
    'Crea matriz de NxN'
    matriz = []
    for f in range(N):
        matriz.append([0]*N)
    return matriz

def llenarMatriz1(matriz):
    numAzar = randint(1, len(matriz)**2)
    filas = len(matriz)
    columnas = len(matriz[0])
    while numAzar not in matriz:
        for f in range(filas):
            for c in range(columna):
                matriz[f][c] = numAzar
        numAzar = randint(1,len(matriz)**2)

def llenarMatriz2(matriz):
    lista = []
    numAzar = randint(1,len(matriz)**2)
    cont = 0
    while len(lista) < len(matriz)**2:
        while numAzar not in lista:
            lista.append(numAzar)
            cont = cont + 1
        numAzar = randint(1, len(matriz)**2)
        
    
               
        
def imprimirMatriz(matriz):
    'Imprime la matriz con formato'
    for f in range(len(matriz)):
        for c in range(len(matriz)):
            print("%3d" %matriz[f][c],end="")
        print()
        
def main():
    matriz = crearMatriz()
    llenarMatriz(matriz)
    imprimirMatriz(matriz)

#PROGRAMA PRINCIPAL
main()
    

