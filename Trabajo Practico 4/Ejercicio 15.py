# 15. Muchas aplicaciones financieras requieren que los números sean expresados también en letras.
# Por ejemplo, el número 2153 puede escribirse como "dos mil cientocincuenta y tres".
# Escribir un programa que utilice una función para convertir un número entero entre 0 y 1 billón (1.000.000.000.000) a letras.
# ¿En qué cambiaría la función si también aceptara números negativos? ¿Y números con decimales?

#FUNCIONES
def convertirNumALetras(num):
    unDig = ["cero","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve", "diez","once","doce","trece","catorce","quince","dieciseis","diecisiete","dieciocho","diecinueve"]
    dosDig = ["veinte","treinta","cuarenta","cincuenta","sesenta","setenta","ochenta","noventa"]
    
    letras = ""
    
    if num < 20:
        letras = unDig[num]
    elif num >=20 and num <100:
        letras = dosDig
        
        
    return letras
    
    
    
    
def main():
    num = int(input("Ingrese un numero: "))
    letras = convertirNumALetras(num)
    print(letras)



#PROGRAMA PRINCIPAL
main()