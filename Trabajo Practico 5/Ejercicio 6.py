# 6.El método index permite buscar un elemento dentro de una lista, devolviendo la posición que éste ocupa.
# Sin embargo, si el elemento no pertenece a la lista se produce una excepción de tipo ValueError.
# Desarrollar un programa que cargue una lista con números enteros ingresados a través del teclado (terminando con -1)
# y permita que el usuario ingrese el valor de algunos elementos para visualizar la posición que ocupan,
# utilizando el método index. Si el número no pertenece a la lista se imprimirá un mensaje de error y se solicitará
# otro para buscar. Abortar el proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.

# FUNCIONES
def main():
    lista = []
    cont = 0
    while True:
        num = int(input("Ingrese un numero: "))
        if num == -1:
            break
        lista.append(num)
    
    while True:
        try:
            nro = int(input("Ingrese un numero a buscar: "))
            pos = lista.index(nro)
            print(f"El numero {nro} se encuentra en la posicion {pos}")
        except ValueError:
            print(f"El numero {nro} no se encuentra en la lista")
            cont = cont + 1
            if cont == 3:
                break
        





# PROGRAMA PRINCIPAL
main()