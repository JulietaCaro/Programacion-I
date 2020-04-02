#11. Intercalar los elementos de una lista entre los elementos de otra. La intercalación
#deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará
#una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3]
#y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7].

#FUNCIONES
def intercalarListas(listaA, listaB):
    'Intercala dos listas mediante la tecnica de rebanadas'
    listaC = []
    listaC = listaA + listaB
    listaC[::2] = listaA
    listaC[1::2] = listaB
    return listaC

def main():
    'Programa principal'
    lista1 = [8,1,3]
    lista2 = [5,9,7]
    print("Lista 1:",lista1)
    print("Lista 2:",lista2)
    lista3 = intercalarListas(lista1,lista2)
    print("Lista intercalada:",lista3)

#PROGRAMA PRINCIPAL
main()