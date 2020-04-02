#6. Eliminar de una lista de palabras las palabras que se encuentren en una segunda
#lista. Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.

from funciones import imprimirLista
#FUNCIONES
def palabrasRepetidas(listaA,listaB):
    'Compara las palabras y guarda las repetidas en una nueva lista'
    palabrasAEliminar = []
    for palabras in listaA:
        if palabras in listaB:
            palabrasAEliminar.append(palabras)
    return palabrasAEliminar

def eliminarRepetidas(listaB, listaEliminar):
    'Elimina los elementos repetidos en listaB'
    for i in listaEliminar:
        listaB.remove(i)
    return listaB

def main():
    'Programa principal'
    lista1 = ["sol","juli","mar","campo"]
    lista2 = ["casa", "sol", "juli","dia","mono"]
    imprimirLista(lista1)
    imprimirLista(lista2)
    listaElim = palabrasRepetidas(lista1, lista2)
    print("Elementos repetidos: ")
    imprimirLista(listaElim)
    listaFin = eliminarRepetidas(lista2, listaElim)
    print("Lista resultante:")
    imprimirLista(listaFin)

#PROGRAMA PRINCIPAL
main()
    

