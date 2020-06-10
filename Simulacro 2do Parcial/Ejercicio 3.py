# Desarrollar una función que reciba una cadena e informe para cada palabra sus repeticiones, teniendo en cuenta: 
# 1. Todas las claves deben estar en minúsuculas (es decir, ‘Hola’ y ‘hola’ deberían sumar al mismo contador). 
# 2. Se deben ignorar los signos de puntuación y los números (es decir, “ ‘(),.;:?¡¿[]{}-’ ”). 
# Desarrollar un programa principal para ingresar una frase y luego mostrar por pantalla el listado de palabras y sus
# repeticiones ordenado alfabeticamente.

#FUNCIONES
def limpiarCadena(cad):
    "Elimina de una cadena los signos (),.;:?¡¿[]{}-’!'"
    signos = "‘(),.;:?¡¿[]{}-’!'"
    for signo in signos:
        cad = cad.replace(signo,"")
    return cad

def repeticiones(cad):
    '''Crea un diccionario donde se cuentan las repeticiones de palabras en una cadena.
    Las claves son las palabras, los valores son la cantidad de veces que aparece esa palabra.
    Retorna el diccionario.
    
    '''
    cad = cad.lower()
    cad = limpiarCadena(cad)
    palabras = cad.split()
    dic = {}
    for palabra in palabras:
        if palabra not in dic:
            dic[palabra] = 1
        else:
            dic[palabra] += 1
    return dic

def main():
    frase = input("Ingrese una frase: ")
    dic = repeticiones(frase)
    claves = list(dic)
    claves.sort()
    for clave in claves:
        if dic[clave] == 1:
            print(clave,"aparece 1 vez")
        else:
            print(clave,"aparece",dic[clave],"veces")
    
main()      