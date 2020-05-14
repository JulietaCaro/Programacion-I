#4. Escribir una función que reciba como parámetro un número entero entre 0 y 3999
#y lo convierta en un número romano, devolviéndolo en una cadena de caracteres.
#¿En qué cambiaría la función si el rango de valores fuese diferente?

#FUNCIONES
def numRomano(num):
    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 1]
    simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "X", "XL", "IX", "V", "I"]
    numRom = ""
    i = 0
    while num > 0:
        for x in range(num//numeros[i]):
            numRom = numRom + simbolos[i]
            num = num - numeros[i]
        i = i + 1
    return numRom    
    
def main():
    num = int(input("Ingrese un numero: "))
    while num < 0 or num >3999:
        num = int(input("Ingrese otro numero: "))
    romano = numRomano(num)
    print(f"El numero {num} en romano es {romano}")
    
#PROGRAMA PRINCIPAL
main()