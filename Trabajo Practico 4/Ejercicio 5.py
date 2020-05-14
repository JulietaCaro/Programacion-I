#5. Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo una frase
#y un entero N, y devuelva otra cadena con las palabras que tengan N o más caracteres de la cadena original.
#Escribir también un programa para verificar el comportamiento de la misma. Hacer tres versiones de la función,
#paracada uno de los siguientes casos:
#a. Utilizando sólo ciclos normales
#b. Utilizando listas por comprensión
#c. Utilizando la función filter

#FUNCIONES
def filtrar_palabras_a(cad, num):
    lista = cad.split(" ")
    frase = []
    for palabra in lista:
        if num <= len(palabra):
            frase.append(palabra)
        
    cadena = " ".join(frase)
    return cadena

def filtrar_palabras_b(cad, num):
    lista = cad.split(" ")
    frase = [palabra for palabra in lista if len(palabra) >= num]
    cadena = " ".join(frase)
    return cadena

def filtrar_palabras_c(cad, num):
    lista = cad.split(" ")
    lista = filter(lambda palabra:len(palabra)>=num, lista)
    return (" ").join(lista)

def main():
     cade = input("Ingrese una frase: ")
     numN = int(input("Ingrese un numero: "))
     cadena = filtrar_palabras_a(cade, numN)
     print("Función A")
     print(f"Cadena con {numN} o más caracteres: {cadena}")
     cadB = filtrar_palabras_b(cade, numN)
     print("Función B")
     print(f"Cadena con {numN} o más caracteres: {cadB}")
     cadC = filtrar_palabras_c(cade, numN)
     print("Función C")
     print(f"Cadena con {numN} o más caracteres: {cadC}")
#PROGRAMA PRINCIPAL
main()