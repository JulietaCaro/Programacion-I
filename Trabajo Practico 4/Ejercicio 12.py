# 12.Desarrollar una función para reemplazar todas las apariciones de una palabra por otra en una cadena de caracteres
# y devolver la cadena obtenida y un entero con la cantidad de reemplazos realizados.
# Escribir también un programa para verificar el comportamiento de la función.

# FUNCIONES
def reemplazarApariciones(cad, aCambiar,cambio):    
#     lista = cad.split(" ")
#     cont = 0
#     for palabra in lista:
#         if palabra == aCambiar:
#             cont = cont + 1
    cont = cad.count(aCambiar)
    cad = cad.replace(aCambiar,cambio)
    return cont, cad

 


def main():
    cadena = input("Ingrese una frase: ")
    reemplazos, cadena = reemplazarApariciones(cadena, "hola", "chau")
    print(f"Cantidad de reemplazos: {reemplazos}")
    print(f"Cadena final: {cadena}")


# PROGRAMA PRINCIPAL
main()