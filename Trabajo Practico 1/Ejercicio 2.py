#FUNCIONES
def positivo (valor):
    while valor < 0:
        valor = int(input("Ingrese un numero positivo: "))
    return valor

def fechaValida(dia, mes, año):
    fecha = True
    bisiesto = False
    
    if ((año%4 == 0 and año%100 != 0) or año%400 == 0):
        bisiesto = True
        
    if mes <=12 and dia <=31:
        if (dia == 30 and mes %2==1) or (dia == 31 and mes%2==0):
            fecha = False
        if mes == 2 and (bisiesto == True and dia>29):
            fecha = False
        if mes == 2 and (bisiesto == False and dia > 28):
            fecha = False
    else:
        fecha = False
    return fecha

#PROGRAMA PRINCIPAL
dia = int(input("Ingrese un numero: "))
dia = positivo(dia)
mes = int(input("Ingrese otro numero: "))
mes = positivo(mes)
año = int(input("Ingrese otro numero: "))
año = positivo(año)
fecha = fechaValida(dia, mes, año)
if fecha == False:
    print("Los numeros ingresados no corresponden a una fecha valida")
else:
    print("Corresponde a una fecha")
