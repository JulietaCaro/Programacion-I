#10. Generar una lista con números al azar entre 0 y 100, donde su cantidad de elementos
#será un número par también obtenido al azar entre 10 y 50. Luego se solicita partir la lista
#por la mitad a través de la técnica de las rebanadas, creando dos nuevas listas.
#Imprimir las tres listas por pantalla.

from random import randint
#FUNCIONES
def cantElemPar():
    'Genera un numero random entre 10 y 50 par'
    cantidad = randint(10,50)
    while cantidad%2!=0:
        cantidad = randint(10,50)
    return cantidad

def generarLista(cant):
    'Crea lista random'
    lista = []
    for i in range(cant):
        lista.append(randint(0,100))
    return lista

def partirLista(lista):
    'Parte la lista generando dos nuevas a traves de la tecnica de rebanadas'
    listaPrimeraParte = lista[:len(lista)//2]
    listaSegundaParte = lista[len(lista)//2:]
    return listaPrimeraParte, listaSegundaParte

def main():
    'Programa principal'
    elementos = cantElemPar()
    lista = generarLista(elementos)
    print(lista)
    primera, segunda = partirLista(lista)
    print("Primera parte: ",primera)
    print("Segunda parte: ",segunda)
    
#PROGRAMA PRINCIPAL
main()
    