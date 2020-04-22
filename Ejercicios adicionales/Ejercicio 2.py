#FUNCIONES        
def main():
    esPar = lambda num: True if num %2 == 0 else False
    listaPar = []
    listaImpar = []
    num = int(input("Ingrese un numero (0 para finalizar): "))
    while (num <1 or num >50) and num != 0:
            num = int(input("Reingrese un numero (0 para finalizar): "))
    while num != 0:
        if esPar(num):
            listaPar.append(num)
        else:
            listaImpar.append(num)
        num = int(input("Ingrese otro numero: "))
        while (num <1 or num >50) and num != 0:
            num = int(input("Reingrese un numero (0 para finalizar): "))
        
#PROGRAMA PRINCIPAL
main()