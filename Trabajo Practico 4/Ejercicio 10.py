# 10.Escribir un programa que permita ingresar una cadena de caracteres e imprima un mensaje indicando cuántas letras
# y cuántos números contiene.
# Por ejemplo, si se ingresa "Hola Mundo 123" debe indicar que se ingresaron 9 letras y 3 números.

# FUNCIONES
def contarLetrasYNum(cadena):
    contNum = 0
    contLet = 0
    for caracter in cadena:
        if caracter.isdigit():
            contNum = contNum + 1
        elif caracter.isalpha():
            contLet = contLet + 1
    return contNum, contLet

def main():
    cadena = input("Ingrese una palabra/frase: ")
    contN, contL = contarLetrasYNum(cadena)
    print(f"Cantidad de letras: {contL}")
    print(f"Cantidad de numeros: {contN}")




# PROGRAMA PRINCIPAL
main()