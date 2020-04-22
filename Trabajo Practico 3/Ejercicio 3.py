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

def existe(matriz, num):
    """Verifica si un numero esta en la matriz.
    Retorna True si el numero se encuentra, False si no.
    
    Parametros de entrada: matriz y numero a buscar.
    
    """
    encontrado = False
    for fila in matriz:
        if num in fila:
            encontrado = True
    return encontrado
    

def llenarMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            numAzar = randint(1,len(matriz)**2)
            while existe(matriz, numAzar):
                numAzar = randint(1,len(matriz)**2)
            matriz[f][c] = numAzar
                     
        
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
    

