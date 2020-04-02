#12. Utilizar la técnica de listas por comprensión para construir una lista con todos los
#números impares comprendidos entre 100 y 200.

#FUNCIONES
def numerosImpares ():
    'Crea una lista donde guarda los numeros impares entre 100 y 200'
    lista = list(range(100,201))
    listaImpares = [num for num in lista if num %2 !=0]
    return listaImpares

def main():
    'Programa principal'
    listaImpar = numerosImpares()
    print(listaImpar)
    
#PROGRAMA PRINCIPAL
main()