# 1.Escribir una función que devuelva la cantidad de dígitos de un número entero, sin utilizar cadenas de caracteres.

def contarDigitos(numero):
    if numero < 0:
        numero = -numero
    if numero < 10:
        return 1
    else:
        return 1 + contarDigitos(numero//10)

print(contarDigitos(-10))