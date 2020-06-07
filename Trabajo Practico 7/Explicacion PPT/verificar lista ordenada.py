# Desarrollar una función para determinar si esta ordenada en forma ascendente

# REBANADAS
def listaOrdenadaRebanadas(lista):
    if len(lista)<2:
        return True
    else:
        if lista[0] < lista[1]:
            return listaOrdenadaRebanadas(lista[1:])
        else:
            return False
        
lista = [1,6,9]
if listaOrdenadaRebanadas(lista):
    print("Esta ordenada")
else:
    print("No esta ordenada")