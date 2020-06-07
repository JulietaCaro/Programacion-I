# Desarrollar una función para contar cuantas veces aparece un numero en una matriz.

# REBANADAS
def contarValorRebanadas(matriz,valor):
    if len(matriz)==0:
        return 0
    else:
        return matriz[0].count(valor) + contarValorRebanadas(matriz[1:],valor)
    
# SIN REBANADAS Y SIN METODO COUNT
def contarValor(matriz,valor,f=0):
    if len(matriz) == f:
        return 0
    else:
        suma = 0
        for c in range(len(matriz[f])):
            if matriz[f][c] == valor:
                suma += 1
        return suma + contarValor(matriz,valor,f+1)

matriz=[[1,3,4],[5,7,3],[6,3,3]]
print(contarValorRebanadas(matriz,3))
print(contarValor(matriz,3))