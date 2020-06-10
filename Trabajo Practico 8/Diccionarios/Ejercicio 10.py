# 10.Escribir una función que reciba un número entero N y devuelva un diccionario con la tabla de multiplicar de N del 1 al 12.
# Escribir también un programa para probar la función

def tablaMultiplicar(n):
    dic = {}
    for i in range(1,13):
        dic[i] = n*i
    return dic

def imprimirDiccionario(dic):
    for clave,valor in dic.items():
        print(clave,valor)
    
def main():
    num = int(input("Ingrese un numero entero: "))
    dic = tablaMultiplicar(num)
    imprimirDiccionario(dic)

main()