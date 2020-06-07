# 9.Realizar una función recursiva para imprimir una matriz de M x N.

def imprimirMatriz(matriz,f=0):
    if len(matriz)!= f:
        for c in range(len(matriz[f])):
            print("%4d" %matriz[f][c], end="")
        print()
        imprimirMatriz(matriz,f+1)

matriz= [[6,7,9],[9,3,4],[4,6,2]]
imprimirMatriz(matriz)
        
        