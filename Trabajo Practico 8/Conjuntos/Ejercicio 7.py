# Ingresar una frase desde el teclado y eliminar las palabras repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar
# las palabras ordenadas según su longitud. La eliminación de las palabras duplicadas debe realizarse a través de un conjunto.

def eliminarRepetidas(frase):
    frase = frase.lower()
    lista = frase.split()
    conjunto = set(lista)
    
    return list(conjunto)

def main():    
    frase = input("Ingrese una frase: ")
    sinRep = eliminarRepetidas(frase)
    sinRep.sort(key=lambda x:len(x))
    sinRep = " ".join(sinRep)
    print(sinRep)


main()