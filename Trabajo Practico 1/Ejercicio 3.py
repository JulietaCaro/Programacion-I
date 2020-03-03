#FUNCIONES
def menorA100(num):
    while num>100:
        num = int(input("Ingrese un numero menor a 100: "))
    return num

def sumaCuadrados(numero):
    cont = 1
    suma = 0
    while cont < numero:
        suma = cont**2+suma
        cont = cont+4
    return suma

#PROGRAMA PRINCIPAL
num = int(input("Ingrese un numero: "))
num = menorA100(num)
suma = sumaCuadrados(num)
print("Suma: ", suma)