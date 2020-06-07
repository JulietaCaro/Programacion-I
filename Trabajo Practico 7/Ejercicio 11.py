# 11.Desarrollar una función que devuelva el elemento de valor mínimo de una matriz de M x N

def valorMinimo(matriz,f=0,minimo=1000000000000000000):
    if len(matriz) != f:
        if minimo > min(matriz[f]):
            minimo = min(matriz[f])
        return valorMinimo(matriz,f+1,minimo)
    else:
        return 0

matriz = [[6,9,1],[2,8,7]]
print(valorMinimo(matriz))
        