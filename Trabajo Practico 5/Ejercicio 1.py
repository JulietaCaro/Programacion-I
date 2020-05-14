# 1.Desarrollar una función para ingresar a través del teclado un número natural. La función rechazará cualquier ingreso
# inválido de datos utilizando excepciones y mostrará la razón exacta del error. Controlar que se ingrese un número,
# que ese número sea entero y que sea mayor que 0. Devolver el valor ingresado cuando éste sea correcto.
# Escribir también un programa que permita probar el correcto funcionamiento de la misma.

# FUNCIONES
def ingresarNumero(texto):
    while True:
        try:
            num = int(input(texto))
            if num > 0:
                break
            print("Se debe ingresar un numero natural")
        except ValueError:
            print("Error, se esperaba el ingreso de un numero")
            print("Vuelva a intentar")
    return num

def main():
    num = ingresarNumero("Ingrese un numero ")
    print("Numero ingresado: ",num)



# PROGRAMA PRINCIPAL
main()