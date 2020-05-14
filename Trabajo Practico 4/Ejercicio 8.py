'''8. Escribir una función que reciba como parámetro una cadena de caracteres en la que las palabras se encuentran
separadas por uno o más espacios. Devolver otra cadena con las palabras ordenadas alfabéticamente, dejando un espacio
entre cada una.'''

#FUNCIONES
def ordenarCadena (cadena):
    lista = cadena.split()
    lista.sort()
    cadena = " ".join(lista)
    return cadena

def main():
    cad = input("Ingrese una palabras: ")
    cadOrd = ordenarCadena(cad)
    print(f"Ordenada: {cadOrd}")
    
    
    
    
    
#PROGRAMA PRINCIPAL
main()