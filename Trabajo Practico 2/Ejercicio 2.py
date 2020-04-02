#2. Escribir funciones para:
#a. Generar una lista de 50 números aleatorios del 1 al 100.
#b. Recibir una lista como parámetro y devolver True si la misma contiene algún
#elemento repetido. La función no debe modificar la lista.
#c. Recibir una lista como parámetro y devolver una nueva lista con los elementos
#únicos de la lista original, sin importar el orden.
#Combinar estas tres funciones en un mismo programa.

from random import randint
import funciones
#funciones
def crearLista():
    'Crea lista de 50 elementos random'
    cont = 0
    lista = []
    while cont < 10:
        lista.append(randint(1,10))
        cont = cont + 1
    return lista

def elementoRepetido(lista):
    repe = False
    listaRepetidos = []
    for i in lista:
        repetido = lista.count(i)
        listaRepetidos.append(repetido)
    if max(listaRepetidos)>1:
        repe = True
    else:
        repe = False
    return repe

def listaSinRepetidos(lista):
    listaNueva = []
    for i in lista:
        if i not in listaNueva:
            listaNueva.append(i)
    return listaNueva

def main():
    'Programa principal'
    lista = crearLista()
    funciones.imprimirLista(lista)
    if elementoRepetido(lista):
        print("Hay elementos repetidos")
    else:
        print("No hay elementos repetidos")
    listaSinRep = listaSinRepetidos(lista)
    print("Lista sin repetidos: ")
    funciones.imprimirLista(listaSinRep)
    
#PROGRAMA PRINCIPAL
main()