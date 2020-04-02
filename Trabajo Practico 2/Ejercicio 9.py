#9. Escribir una función que reciba una lista de números enteros como parámetro y la
#normalice, es decir que todos sus elementos deben sumar 1.0, respetando las proporciones
#relativas que cada elemento tiene en la lista original. Desarrollar también un programa
#que permita verificar el comportamiento de la función.
#Por ejemplo, normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].

#FUNCIONES
def normalizar(lista):
    'Normaliza la lista, suma los elementos y divide los elementos con la suma'
    suma = sum(lista)
    listaNueva = []
    for i in lista:
        listaNueva.append(i/suma)
    return listaNueva

def normalizar2 (lista):
    suma = sum(lista)
    listaNueva = [i/suma for i in lista]
    return listaNueva

def main():
    'Programa principal'
    lista = [1,1,2]
    print(lista)
    listaNor = normalizar2(lista)
    print(listaNor)
    
#PROGRAMA PRINCIPAL
main()