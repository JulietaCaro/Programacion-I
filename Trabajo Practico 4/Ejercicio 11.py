# 11.Escribir un programa que permita ingresar una cadena de caracteres y coloque en mayúscula
# la primera letra posterior a un espacio, eliminando todos los espacios que contenga.
# Imprimir por pantalla la cadena obtenida.

#FUNCIONES
def eliminarEspacios(cadena):
    cad = ""
    for caracter in cadena:
        if caracter !=" ":
            cad = cad+caracter
    return cad

def main ():
    cadena = input("Ingrese una frase: ")
    cadena = cadena.title()
    cadena = eliminarEspacios(cadena)
    print(cadena)
   






#PROGRAMA PRINCIPAL
main()