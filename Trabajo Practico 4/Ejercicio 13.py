# 13.Escribir un programa que cuente cuántas veces se encuentra una subcadena dentro de otra cadena, sin diferenciar
# mayúsculas y minúsculas. Tener en cuenta que los caracteres de la subcadena no necesariamente deben estar en forma
# consecutiva dentro de la cadena, pero sí respetando el orden de los mismos.

# FUNCIONES
def buscarSubcadena(cad, subCad):
    cad = cad.lower()
    subCad = subCad.lower()
    i = 0
    cont = 0
    #indice de la cadena 
    ind = -1 
    #Si es -1 el metodo find no encontró el caracter
    while i != -1:
        carac = 0
        #Inicio el indice de la subcad en 0 y las condiciones se ejecutan mientras sea menor a la cant de elementos
        #de la subcad y encuentre el caracter
        while carac < len(subCad) and i != -1:
            #busco un caracter de la subcadena desde la posicion que se indica con ind+1 y me quedo con el
            #indice del caracter encontrado en la cadena
            ind = cad.find(subCad[carac], ind+1)
            #cambio el indice de la subcadena por el siguiente
            carac = carac + 1
            #ind = indice de la palabra encontrada
            i = ind
        
        if carac == len(subCad):
            cont = cont + 1
    return cont

def main():
    cadena = input("Ingrese una cadena: ")
    subCad = input("Ingrese la subcadena: ")
    contador = buscarSubcadena(cadena, subCad)
    print(f"Cantidad de veces que {subCad} aparece en {cadena}: {contador}")
    
# PROGRAMA PRINCIPAL
main()
    