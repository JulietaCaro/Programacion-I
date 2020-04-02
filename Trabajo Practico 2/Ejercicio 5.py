#5. Escribir un programa que calcule la suma acumulada a partir de una lista de números.
#El programa debe generar una nueva lista donde el primer elemento es el mismo de la lista original,
#el segundo elemento es la suma del primero más el segundo, el tercer elemento es la suma del primero
#más el segundo más el tercero y así sucesivamente. Por ejemplo, la suma acumulada de [1,2,3] es [1,3,6].

#FUNCIONES
def sumaAcumulada(lista):
    'Calcula la suma acumulada a partir de una lista de numeros'
    listaSuma = []
    suma = 0
    for i in lista:
        suma = suma + i
        listaSuma.append(suma)
    return listaSuma

def main():
    'Programa principal'
    lista = [25,96,104]
    listaSum = sumaAcumulada(lista)
    print(listaSum)

#PROGRAMA PRINCIPAL
main ()

