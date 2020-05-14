# 2.Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo números reales, sume ambos valores
# y devuelva el resultado como un número real. Devolver -1 si alguna de las cadenas no contiene un número válido,
# utilizando manejo de excepciones para detectar el error.

# FUNCIONES
def sumaNumReales (cad1,cad2):
    try:
        num1 = float(cad1)
        num2 = float(cad2)
        suma = num1 + num2
    except ValueError:
        suma = -1
    return suma

def main():
    while True:
        cad1 = input("Ingrese una cadena de numeros: ")
        cad2 = input("Ingrese otra cadena de numeros: ")
        suma = sumaNumReales(cad1, cad2)
        if suma == -1:
            print("Alguna de las cadenas no contiene un numero valido")
            continue
        print(f"La suma es {suma}")
        break


# PROGRAMA PRINCIPAL
main()