#Desarrollar una funcion para sumar los digitos pares.
def sumarDigitos(num):
    '''Suma los digitos pares de un numero.
    Utiliza continue cuando el digito es impar.'''
    suma = 0
    while num > 0:
        digito = num%10
        num = num//10
        if digito %2!=0:
            continue
        suma = suma+digito
    return suma

def main():
    num = int(input("Ingrese un num: "))
    suma = sumarDigitos(num)
    print(f"Suma de los digitos pares: {suma}")

main()