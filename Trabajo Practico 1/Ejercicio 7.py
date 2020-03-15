#FUNCIONES
def concatenar(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    concat = num1 + num2
    return concat

def main():
    primerNum = int(input("Ingrese un numero: "))
    segundoNum = int(input("Ingrese otro numero: "))
    concatenado = concatenar (primerNum, segundoNum)
    print("Concatenado: ", concatenado)

#PROGRAMA PRINCIPAL
main()