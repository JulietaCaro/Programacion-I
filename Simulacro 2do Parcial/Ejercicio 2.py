# Desarrolle un programa que ingrese contraseñas hasta ingresar una contraseña vacía. A medida que se ingresan verifique e
# informe si cumple con las reglas:
# a. No puede comenzar con número.
# b. Debe contener al menos dos números. Contar la cantidad de numeros de una cadena mediante una función recursiva.
# Resolver utilizando exclusivamente manejo de excepciones y estructura While-True, creando una nueva excepción o generando una
# existente (ValueError) cuando no cumpla alguno de las dos reglas, mostrar mensaje aclaratorio correspondiente en cada caso.

# FUNCIONES
def contarNumeros(contr):
    'Cuenta los numeros de una cadena con recursividad'
    if contr == "":
        return 0
    if contr[0].isdigit():
        return 1 + contarNumeros(contr[1:])
    else:
        return 0 + contarNumeros(contr[1:])
    
def main():
    '''Pide una contraseña hasta no ingresar nada, verifica que no empiece con un numero.
    Verifica que contenga al menos dos numeros. Si ocurre un error se muestra por pantalla.
    
    '''
    while True:
        try:
            contr = input("Ingrese la contraseña: ")
            if contr == "":
                break
            if contr[0].isdigit():
                raise ValueError ("No debe comenzar con un numero")
            if contarNumeros(contr)<2:
                raise ValueError ("Debe contener al menos dos numeros")
            
        except ValueError as mensaje:
            print(mensaje)
            
main()