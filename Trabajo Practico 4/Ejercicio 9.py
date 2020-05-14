# 9.Desarrollar una función que devuelva una subcadena con los últimos N caracteres de una cadena dada.
# La cadena y el valor de N se pasan como parámetros.

def ultimosNCaracteres(cadena, num):
    return cadena[len(cadena)-num:]

def main():
    cad = input("Ingrese una cadena: ")
    num = int(input("Ingrese los caracteres a mostrar: "))
    print(f"Últimos {num} caracteres de la cadena dada: {ultimosNCaracteres(cad, num)}")

main()