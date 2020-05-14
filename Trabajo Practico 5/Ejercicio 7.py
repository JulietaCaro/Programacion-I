# 7.Escribir un programa que juegue con el usuario a adivinar un número. El programa debe generar un número al azar
# entre 1 y 500 y el usuario debe adivinarlo. Para eso, cada vez que se introduce un valor se muestra un mensaje
# indicando si el número que tiene  que adivinar es mayor o menor que el ingresado. Cuando consiga adivinarlo,
# se debe imprimir en pantalla la cantidad de intentos que le tomó hallar el número. Si el usuario introduce algo que no
# sea un número se mostrará un mensaje en pantalla y se lo contará como un intento más.

from random import randint
# FUNCIONES
def main():
    intentos = 0
    random = randint(1,100)
    print("Se generó un numero, intente adivinarlo")
    while True:
        try:
            num = int(input("Ingrese un numero: "))
            if num == random:
                print("Muy bien! Adivinó el número ☺☻♥")
                break
                if intentos != 0:
                    print(f"Cantidad de intentos: {intentos}")
            elif num > random:
                intentos += 1
                print("El numero debe ser mas chico")
            else:
                intentos += 1
                print("El numero debe ser mas grande")
        except ValueError:
            print("Se espera el ingreso de un numero!")
            intentos += 1
            
# PROGRAMA PRINCIPAL
main()