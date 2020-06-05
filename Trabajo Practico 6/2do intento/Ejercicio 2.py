# 2.Escribir un programa que permita grabar un archivo los datos de lluvia caída durante un año. Cada línea del archivo se
# grabará con el siguiente formato:
# <dia>;<mes>;<lluvia caída en mm>  por ejemplo  25;5;319
# Los datos se generarán mediante números al azar, asegurándose que las fechas sean válidas. La cantidad de registros también
# será un número al azar entre 50 y 200. Por último se solicita leer el archivo generado e imprimir un informe en formato
# matricial donde cada columna represente a un mes y cada fila corresponda a los días del mes. Imprimir además el total de
# lluvia caída en todo el año.
from random import randint
def crearArchivo():
    try:
        archivo = open("LluviaCaida.txt","w")
    except IOError:
        print("No se pudo crear el archivo")
    else:
        cantReg = randint(50,200)
        while cantReg != 0:
            mes = str(randint(1,12))
            if mes in [1,3,5,7,8,10,12]:
                dia = str(randint(1,31))
            elif mes == 2:
                dia = str(randint(1,28))
            else:
                dia = str(randint(1,30))
            lluvia = str(randint(100,800))
            archivo.write(dia+";"+mes+";"+lluvia+"\n")
            
            cantReg = cantReg - 1
    finally:
        archivo.close()
        print("Se cerró el archivo")
        
def crearMatriz():
    filas = 31
    columnas = 12
    matriz = []
    for f in range(filas):
        matriz.append([0]*columnas)
        
    return matriz

def imprimirMatriz(matriz):
    print("    1    2    3    4    5    6    7    8    9   10   11   12 ")
    filas = 31
    columnas = 12
    for f in range(filas):
        for c in range(columnas):
            print("%5d" %matriz[f][c], end="")
        print()

def informeMatricial():
    try:
        archivo = open("LluviaCaida.txt","r")
    except IOError:
        print("Se produjo un error al leer el archivo")
    else:
        matriz = crearMatriz()
        while True:
            registro = archivo.readline()
            if registro == "":
                break
            registro = registro.replace("\n","")
            registro = registro.split(";")
            dia,mes,lluvia = registro
            dia = int(dia)
            mes = int(mes)
            lluvia = int(lluvia)
            
#             for f in range(1,32):
#                 for c in range(1,13):
#                     if c == mes and f == dia:
#                         matriz[f][c] = lluvia

            matriz[dia-1][mes-1] = lluvia
        
        imprimirMatriz(matriz)

def main():
    crearArchivo()
    informeMatricial()
    
main()