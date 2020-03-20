#FUNCIONES
def diaSiguiente(dia, mes, año):
    diaSig = 0
    mesSig = 0
    añoSig = 0
    if mes >= 1 and mes <= 12:
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia >=1 and dia < 31:
                diaSig = dia + 1
                mesSig = mes
                añoSig = año
            else:
                diaSig = 1
                mesSig = 1
                añoSig = año+1
        
        elif mes == 2:
            if (año%4==0 and año%100==0) or año%4==0:
                if dia>=1 and dia <29:
                    diaSig = dia + 1
                    mesSig = mes
                    añoSig = año
                elif dia == 29:
                    diaSig = 1
                    mesSig = 3
                    añoSig = año
            
            else:
                if dia >= 1 and dia < 28:
                    diaSig = dia + 1
                
                else:
                    if dia == 28:
                        diaSig = 1
                        mesSig = 3
                        añoSig = año
        
        else:
            if dia >=1 and dia < 30:
                diaSig = dia + 1
                mesSig = mes
                añoSig = año
            elif dia == 30:
                diaSig = 1
                mesSig = mes+1
                añoSig = año
    else:
        print("No existe")
    return diaSig, mesSig, añoSig

def main():
    dias = int(input("Ingrese un dia: "))
    meses = int(input("Ingrese un mes: "))
    años = int(input("Ingrese un año: "))
    nDias = int(input("Ingrese el numero de dias a sumar: "))
    
    for i in range (nDias):
        diasi, mesesi, añosi = diaSiguiente(dias, meses, años)
        dias, meses, años = diasi, mesesi, añosi
    
    print(dias,"/",meses,"/",años)
    
    dia1 = int(input("Ingrese un dia: "))
    mes1 = int(input("Ingrese un mes: "))
    año1 = int(input("Ingrese un año: "))
    
    dia2 = int(input("Ingrese otro dia: "))
    mes2 = int(input("Ingrese otro mes: "))
    año2 = int(input("Ingrese otro año: "))
    
    contDias = 0
    while dia2 != dia1 or mes2 != mes1 or año2 != año1:
        dia1, mes1, año1 = diaSiguiente(dia1, mes1, año1)
        contDias=contDias+1
    
    print("Cantidad de dias: ",contDias)
    
#PROGRAMA PRINCIPAL
main()
            