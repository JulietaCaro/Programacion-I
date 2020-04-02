#13. Escribir un programa para generar una lista con los múltiplos de 7 que no sean
#múltiplos de 5, entre 2000 y 3500. Imprimir la lista obtenida.

#FUNCIONES
def generarLista():
    'Genera una lista entre los elementos 2000 y 3500'
    lista = list(range(2000,3500))
    return lista

def listaConMultiplos(lista):
    '''Crea una lista con los elementos multiplos de 7 pero no de 5 entre los elementos de la lista
       pasada como parametro
    '''
    listaMulti = []
    for i in lista:
        if i%7 == 0 and i%5!= 0:
            listaMulti.append(i)
    return listaMulti

def main ():
    'Programa principal'
    lista = generarLista()
    listaMul = listaConMultiplos(lista)
    print(listaMul)
    
#PROGRAMA PRINCIPAL
main()