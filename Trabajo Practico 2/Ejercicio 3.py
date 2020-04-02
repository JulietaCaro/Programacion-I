#3. Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
#donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista.
from funciones import pedirYValidarNum
#FUNCIONES
def main():
    'Programa principal'
    numN = pedirYValidarNum()
    listaCuadrados = [num**2 for num in range (1,numN+1)]
    print(listaCuadrados[-10:])

#PROGRAMA PRINCIPAL
main()
    
    