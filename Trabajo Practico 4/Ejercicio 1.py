# 1. Desarrollar una función que determine si una cadena de caracteres es capicúa, sin
#utilizar cadenas auxiliares. Escribir además un programa que permita verificar su
#funcionamiento.

#FUNCIONES
def esCapicua(cadena):
    esCapi = False
    cadena = cadena.lower()
    if cadena[::-1] == cadena:
        esCapi = True
    return esCapi

def esCapicua1(cadena):
    esCapi = False
    for i in range (len(cadena)//2):
        esCapi = False
        if cadena[i] == cadena[len(cadena)-1-i]:
            esCapi = True
    return esCapi

def main():
    cad = input("Ingrese una palabra: ")
    if esCapicua(cad):
        print(f"{cad} es capicúa")
    else:
        print(f"{cad} no es capicúa")
        
    if esCapicua1(cad):
        print(f"{cad} es capicúa")
    else:
        print(f"{cad} no es capicúa")
    
#PROGRAMA PRINCIPAL
main()