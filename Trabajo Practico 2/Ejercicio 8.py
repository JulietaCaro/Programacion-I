#8. Generar dos listas con M y N números al azar entre 1 y 50 y construir una tercera
#lista cuyos elementos sean el resultado de la intersección de las dos listas dadas.
#Los valores de M y N se obtienen al azar. Imprimir las tres listas por pantalla.

import funciones
from random import randint

#FUNCIONES
def interseccionListas (listaM, listaN):
    'Crea una nueva lista cuyos elementos son la interseccion de las dos listas'
    listaNueva = [num for num in listaM if num in listaN]
    return listaNueva

def main():
    'Programa principal'
    listaM = funciones.listaRandom(randint(1,20),1,50)
    listaN = funciones.listaRandom(randint(1,20),1,50)
    funciones.imprimirLista(listaM)
    funciones.imprimirLista(listaN)
    print(interseccionListas(listaM, listaN))

#PROGRAMA PRINCIPAL
main()

