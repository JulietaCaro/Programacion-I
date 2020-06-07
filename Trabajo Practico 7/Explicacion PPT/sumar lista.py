# Desarrollar una función para sumar los elementos de una lista

def sumarElementos(lista,i=0):
    if len(lista) == i:
        return 0
    else:
        return lista[i] + sumarElementos(lista,i+1)

lista = [5,9,10,2]
print(sumarElementos(lista))
