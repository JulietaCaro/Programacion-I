#FUNCIONES
def crearMatriz(N = 4):
    'Crea matriz de NxN'
    matriz = []
    for f in range(N):
        matriz.append([0]*N)
    return matriz

def imprimirMatriz(matriz):
    'Imprime la matriz con formato'
    for f in range(len(matriz)):
        for c in range(len(matriz)):
            print("%3d" %matriz[f][c],end="")
        print()
        
def matrizA(matriz):
    'Carga con numeros impares consecutivos la diagonal principal'
    cont = 1
    for f in range(len(matriz)):
        for c in range(len(matriz)):
            if f == c:
                matriz[f][c] = cont
                cont = cont + 2

def matrizB(matriz):
    cont = 1
    f = len(matriz)-1
    c = 0
    while c < len(matriz):
        matriz[f][c] = cont
        cont = cont * 3
        f = f - 1
        c = c + 1
        
def matrizC(matriz):
    cont = len(matriz)
    for f in range(len(matriz)):
        for c in range(len(matriz)):
            while c <= f:
                matriz[f][c] = cont
                break
        cont = cont - 1

def matrizD(matriz):
    cont = 1
    for f in range(len(matriz)-1,-1,-1):
        for c in range(len(matriz)):
            matriz[f][c] = cont
        cont = cont * 2

def matrizE(matriz):
    cont = 0
    num = 1
    for f in range(len(matriz)):
        for c in range(len(matriz)):
            if cont %2 != 0:
                matriz[f][c] = num
                num = num + 1
            cont = cont + 1
        cont = cont + 1

def matrizF(matriz):
    cont = 1
    for f in range(len(matriz)):
        for c in range(len(matriz)-1,-1,-1):
            if c >= (len(matriz)-1)-f:
                matriz[f][c] = cont
                cont = cont + 1
        
def main():
    'Programa principal'
    print("MATRIZ")
    matriz_A = crearMatriz()
    imprimirMatriz(matriz_A)
    print("MATRIZ A")
    matrizA(matriz_A)
    imprimirMatriz(matriz_A)
    print("MATRIZ B")
    matriz_B = crearMatriz()
    matrizB(matriz_B)
    imprimirMatriz(matriz_B)
    print("MATRIZ C")
    matriz_C = crearMatriz()
    matrizC(matriz_C)
    imprimirMatriz(matriz_C)
    print("MATRIZ D")
    matriz_D = crearMatriz()
    matrizD(matriz_D)
    imprimirMatriz(matriz_D)
    print("MATRIZ E")
    matriz_E = crearMatriz()
    matrizE(matriz_E)
    imprimirMatriz(matriz_E)
    print("MATRIZ F")
    matriz_F = crearMatriz()
    matrizF(matriz_F)
    imprimirMatriz(matriz_F)

#PROGRAMA PRINCIPAL
main()    