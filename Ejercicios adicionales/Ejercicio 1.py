from random import randint

# FUNCIONES
def imprimirLista(lista):
    'Imprime la lista pasada por parametro'
    for i in lista:
        print(i, end=" ")

def crearLista(n=20, desde=1, hasta=100):
    '''Crea una lista
    Parametros de entrada: cantidad de elementos, rango de los elementos
    Retorna una lista
    '''
    lista = []
    for i in range(n):
        lista.append(randint(desde, hasta))
    return lista

def main():
    lista = crearLista()
    prom = sum(lista) // len(lista)
    print("El promedio de la lista es ",prom)
    listaMayores = [num for num in lista if num > prom]
    listaMayores.sort()
    imprimirLista(listaMayores)

# PROGRAMA PRINCIPAL
main()