#FUNCIONES
def diadelasemana(dia,mes,año):
    if mes < 3:
        mes = mes + 10
        año = año - 1
    else:
        mes = mes - 2
    siglo = año // 100
    año2 = año % 100
    diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

def main ():
    dia = int(input("Ingrese un dia: "))
    mes = int(input("Ingrese un mes: "))
    año = int(input("Ingrese un año: "))
    '''dSem = diadelasemana(dia, mes, año)
    if dSem == 0:
        print("Domingo")
    elif dSem == 1:
        print("Lunes")
    elif dSem == 2:
        print("Martes")
    elif dSem == 3:
        print("Miercoles")
    elif dSem == 4:
        print("Jueves")
    elif dSem == 5:
        print("Viernes")
    else:
        print("Sabado")'''
    
    for i in range(31):
        dSem = diadelasemana(dia, mes, año)
        if dSem == 0:
            print("Domingo: ", dia)
        if dSem == 1:
            print("Lunes: ", dia)
        if dSem == 2:
            print("Martes: ", dia)
        if dSem == 3:
            print("Miercoles: ", dia)
        if dSem == 4:
            print("Jueves: ", dia)
        if dSem == 5:
            print("Viernes: ", dia)
        if dSem == 6:
            print("Sabado: ",dia)
        dia = dia + 1

#PROGRAMA PRINCIPAL
main ()