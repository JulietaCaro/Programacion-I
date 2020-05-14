# 5.La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del módulo math. Escribir un programa
# que utilice esta función para calcular la raíz cuadrada de un número cualquiera ingresado a través del teclado.
# El programa debe utilizar manejo de excepciones para evitar errores si se ingresa un número negativo.

from math import sqrt
def main():
    while True:
        try:
            num = int(input("Ingrese un numero: "))
            print("Raiz cuadrada: %.2f"%sqrt(num))
            break
        except ValueError:
            print("Error, se ingresó un numero negativo")
            resp = input("Desea intentar de nuevo? s/n: ")
            if resp.lower() == "n":
                break

# PROGRAMA PRINCIPAL
main()
