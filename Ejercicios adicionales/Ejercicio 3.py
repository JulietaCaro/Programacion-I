from random import randint as numAzar
# FUNCIONES
def crearMatriz(filas, columnas=100):
    '''Crea y llena una matriz con ceros
    Parametros de entrada: filas y columnas
    Retorna una matriz
    '''
    matriz = [[0]*columnas for i in range(filas)]
    return matriz
        
def llenarMatrizRandom(matriz):
    '''Llena una matriz con numeros random entre 150 y 350
    Parametro de entrada: matriz
    '''
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c] = numAzar(150,350)

def pesoDeCadaCajon(matriz):
    '''Crea una lista con la suma del peso de las naranjas de cada cajon
    Parametro de entrada: matriz
    Retorna la lista
    '''
    listaDePesosXCajon = [sum(matriz[fila]) for fila in range(len(matriz))]
    return listaDePesosXCajon

def imprimirLista(lista):
    'Imprime una lista pasada por parametro con su indice+1'
    for i, valor in enumerate(lista):
        print(f"El cajon {i+1} pesa: {valor} gramos")

def naranjasParaJugo(matriz):
    '''Verifica que los elementos de la matriz no supere o sea menor al rango dado
    Parametros de entrada: matriz
    Retorna la cantidad de naranjas que superan o son menores al rango
    '''
    filas = len(matriz)
    columnas = len(matriz[0])
    listaNaranJugos = []
    for f in range(filas):
        for c in range(columnas):
            if matriz[f][c]< 200 or matriz[f][c]>300:
                listaNaranJugos.append(matriz[f][c])
    return len(listaNaranJugos)

def main():
    'Programa principal'
    cantNaranjas = int(input("Ingrese la cantidad de naranjas: "))
    if cantNaranjas <= 0:
        print("No se ingresaron naranjas")
        
    elif cantNaranjas<100:
        print("Cantidad de cajones llenos: 0")
        pesoNaran = [numAzar(150,350) for i in range(cantNaranjas)]
        print(f"Peso de las naranjas: {sum(pesoNaran)} gramos")
        naranjasPJugo = [num for num in pesoNaran if num < 200 or num >300]
        print(f"Cantidad de naranjas para jugo: {len(naranjasPJugo)}")
        
    else:
        cajonesLlenos = cantNaranjas // 100
        print(f"Cantidad de cajones llenos: {cajonesLlenos}")
        matrizPesos = crearMatriz(cajonesLlenos)
        llenarMatrizRandom(matrizPesos)
        pesoPorCajon = pesoDeCadaCajon(matrizPesos)
        imprimirLista(pesoPorCajon)
    
        if cantNaranjas % 100 == 0:
            print(f"Cantidad de naranjas para jugo: {naranjasParaJugo(matrizPesos)}")
            print("No hay naranjas sobrantes")
        
        else:
            naranRestantes = cantNaranjas - ( cajonesLlenos * 100)
            pesoNaranRestantes = [numAzar(150,350) for i in range(naranRestantes)]
            print(f"Peso de las naranjas sobrantes: {sum(pesoNaranRestantes)} gramos")
            naranjasPJugo = [num for num in pesoNaranRestantes if num < 200 or num > 300]
            print(f"Cantidad de naranjas para jugo: {naranjasParaJugo(matrizPesos)+len(naranjasPJugo)}")    

#PROGRAMA PRINCIPAL
main()