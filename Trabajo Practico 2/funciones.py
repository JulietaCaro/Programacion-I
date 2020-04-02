#FUNCIONES
def maximo(lista):
    'Maximo de una lista'
    maximo = max(lista)
    return maximo

def minimo(lista):
    'Minimo de una lista'
    minimo = min(lista)
    return minimo

def suma(lista):
    'Suma de la lista'
    suma = sum(lista)
    return suma

def imprimirLista(lista):
    'Imprimir lista sin indice'
    for numero in lista:
        print(numero, end=" ")
    print()

def imprimirListaConIndice(lista):
    'Imprimir lista con valores y sus posiciones'
    for i, valor in enumerate(lista):
        print("Pos:",i,"Valor:",valor)

def listaRandom(cantElementos, min, max):
    'Crea una lista random'
    from random import randint
    listaRandom = []
    for i in range(cantElementos):
        listaRandom.append(randint(min,max))
    return listaRandom

def pedirYValidarNum():
    'Pide y valida un numero entero positivo'
    numero = int(input("Ingrese un numero: "))
    while numero < 1:
        numero = int(input("Reingrese un numero positivo: "))
    return numero

def eliminarValor(lista, valor):
    'Eliminar valor pasado por parametro todas las veces que aparezca'
    while valor in lista:
        lista.remove(valor)

def estaEnLaLista(lista, valor):
    'Devuelve true si el valor esta en la lista'
    esta = True
    if valor in lista:
        esta = True
    else:
        esta = False
    return esta

def invertirLista(lista):
    'Invierte la lista'
    return reverse(lista)

def ordenarMenorAMayor(lista):
    'Ordena la lista de menor a mayor'
    return(lista.sort())

def ordenarMayorAMenor(lista):
    'Ordena la lista de mayor a menor'
    return (lista.sort(reverse=True)) 

def superposicion(listaA,listaB):
    'Devuelve true si tienen al menos un elemento en comun'
    esta = False
    for i in listaA:
        if i in listaB:
            esta = True
    return esta

def estaOrdenada(lista):
    'Se fija si la lista es igual a la lista ordenada, devuelve true si es asi'
    estaOrd = False
    listaCopia = lista.copy()
    listaCopia.sort()
    if lista == listaCopia:
        estaOrd = True
    return estaOrd

def interseccionListas (listaM, listaN):
    'Crea una nueva lista cuyos elementos son la interseccion de las dos listas'
    listaNueva = [num for num in listaM if num in listaN]
    return listaNueva

def normalizar (lista):
    suma = sum(lista)
    listaNueva = [i/suma for i in lista]
    return listaNueva

def partirLista(lista):
    'Parte la lista generando dos nuevas a traves de la tecnica de rebanadas'
    listaPrimeraParte = lista[:len(lista)//2]
    listaSegundaParte = lista[len(lista)//2:]
    return listaPrimeraParte, listaSegundaParte

def intercalarListas(listaA, listaB):
    'Intercala dos listas mediante la tecnica de rebanadas'
    listaC = []
    listaC = listaA + listaB
    listaC[::2] = listaA
    listaC[1::2] = listaB
    return listaC