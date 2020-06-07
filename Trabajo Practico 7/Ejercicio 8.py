# 8.Realizar la implementación recursiva del método de selección para ordenar una lista de números enteros.
# Sugerencia: Colocar el elemento más pequeño en la primera posición, y luego ordenar el resto de la lista con una llamada
# recursiva.

def metodoSeleccionRecursivo(lista,i=0):
    if len(lista)!=i:
        posMin = lista.index(min(lista[i:]))
        aux = lista[i]
        lista[i] = lista[posMin]
        lista[posMin] = aux
        metodoSeleccionRecursivo(lista,i+1)
    
lista = [6,2,96,103,698,32,76]
print(lista)
metodoSeleccionRecursivo(lista)
print(lista)
    