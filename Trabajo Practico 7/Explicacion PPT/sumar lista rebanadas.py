# Desarrollar una función para sumar los elementos de una lista
# REBANADAS

def sumarListaRebanadas(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0]+sumarListaRebanadas(lista[1:])

lista = [5,9,10,2]
print(sumarListaRebanadas(lista))