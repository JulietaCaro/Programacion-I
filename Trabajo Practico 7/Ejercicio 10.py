# 10.Escribir una función que sume todos los elementos de una matriz de M x N y devuelva el resultado.

def sumarMatriz(matriz,f=0):
    if len(matriz) != f:
        return sum(matriz[f]) + sumarMatriz(matriz,f+1)
    else:
        return 0
    
matriz = [[2,6,1],[7,3,1],[2,7,1]]
print(sumarMatriz(matriz))
    