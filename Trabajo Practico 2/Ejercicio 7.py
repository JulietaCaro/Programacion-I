#7. Escribir una función que reciba una lista como parámetro y devuelva True si la lista
#está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
#ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
#además un programa para verificar el comportamiento de la función.

#FUNCIONES
def estaOrdenada(lista):
    'Se fija si la lista es igual a la lista ordenada, devuelve true si es asi'
    estaOrd = False
    listaCopia = lista.copy()
    listaCopia.sort()
    if lista == listaCopia:
        estaOrd = True
    return estaOrd

def main():
    'Programa principal'
    lista = [1,2,4]
    if estaOrdenada(lista):
        print("La lista esta ordenada")
    else:
        print("La lista no esta ordenada")

#PROGRAMA PRINCIPAL
main()   