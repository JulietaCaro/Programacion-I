'''6. Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena
como valor de retorno. Escribir también un programa para verificar el comportamiento de la misma.
Ejemplo, dada la cadena "El número de teléfono es 4356-7890" extraer la subcadena que comienza en la posición 25
y tiene 9 caracteres, resultando la subcadena "4356-7890". Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas'''

#FUNCIONES
def rebanadas (cadena, pos, cant):
    cad = cadena[pos:pos+cant]
    return cad
    
def sinRebanadas (cadena, pos, cant):
    '''lista = cadena.split()'''
    subCad = ''
    for i in range(pos, cant+pos):
        subCad = subCad + cadena[i]
    return subCad

def main():
    cad = input("Ingrese una cadena: ")
    posic = int(input("Ingrese la posicion: "))
    cantidad = int(input("Ingrese la cantidad: "))
    cadReb = rebanadas(cad, posic, cantidad)
    print("Utilizando rebanadas")
    print(cadReb)
    cadSin = sinRebanadas(cad, posic, cantidad)
    print("Sin utilizar rebanadas")
    print(cadSin)
    





#PROGRAMA PRINCIPAL
main()