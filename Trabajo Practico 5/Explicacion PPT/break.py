# Funcion para sumar los ultimos 5 digitos.

def sumarUltimosDigitos(num):
    suma = 0
    cantD = 0
    while num > 0:
        digito = num%10
        num = num//10
        suma = suma+digito
        cantD = cantD+1
        if cantD == 5:
            break
    return suma

def main():
    num = int(input("Ingrese un numero: "))
    print(f"Suma de los ultimos cinco digitos: {sumarUltimosDigitos(num)}")

main()