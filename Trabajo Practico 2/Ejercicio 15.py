#15. Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con
#los elementos de la primera que sean impares. El proceso deberá realizarse utilizando
#listas por comprensión. Imprimir las dos listas por pantalla.

from random import randint
#FUNCIONES
def listaAzar():
    lista = []
    for i in range(50):
        lista.append(randint(1,100))
    return lista
def main():
    lista = listaAzar()
    listaImpares = [num for num in lista if num%2!=0]
    print("Lista:",lista)
    print("Lista impares:",listaImpares)
    
#PROGRAMA PRINCIPAL
main()