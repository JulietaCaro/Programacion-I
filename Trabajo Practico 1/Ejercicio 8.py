#FUNCIONES
def validez(num):
    while num < 1 or num > 9:
        num = int(input("Ingrese otro numero: "))

def suma (num):
    primero = num
    segun = str(num)+str(num)
    segundo = int(segun)
    terc = segun + str(num)
    tercero = int(terc)
    cuar = terc + str(num)
    cuarto = int(cuar)
    suma = primero + segundo + tercero + cuarto
    return suma

def main():
    numero = int(input("Ingrese un numero: "))
    validez(numero)
    sumaNum = suma(numero)
    print("La suma es: ",sumaNum)
    
#PROGRAMA PRINCIPAL
main()