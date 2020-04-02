#14.Repetir el ejercicio anterior, pero utilizando la técnica de listas por comprensión.

#FUNCIONES
def main():
    'Programa principal'
    #Creo lista entre 2000 y 3500
    lista = list(range(2000,3501))
    #Creo una lista nueva donde los elementos entre la lista de arriba entran si son multiplos de 7
    #pero no de 5
    listaMulti = [num for num in lista if num%7==0 and num%5!=0]
    print(listaMulti)

#PROGRAMA PRINCIPAL
main ()