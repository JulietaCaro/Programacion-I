# 1.Desarrollar las siguientes funciones utilizando tuplas para representar fechas y horarios, y luego escribir un programa para
# verificar su comportamiento:
# a.Ingresar una fecha desde el teclado, verificando que corresponda a una fecha válida.
# b.Sumar N días a una fecha.
# c.Ingresar un horario desde teclado, verificando que sea correcto.
# d.Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al segundo se considerará que el primero
# corresponde al día anterior. En ningún caso la diferencia en horas puede superar las 24 horas.

#FUNCIONES
esBisiesto = lambda año:(año%4==0 and año%100!=0) or año%400

def verificarFecha(dia,mes,año):
    fecha = dia,mes,año
    validacion = False
    if fecha[1] in [1,3,5,7,8,10,12] and fecha[0]>0 and fecha[0]<=31:
        validacion = True
    elif fecha[1] in [4,6,9,11] and fecha[0]>0 and fecha[0]<=30:
         validacion = True
    elif mes == 2:
        if esBisiesto(fecha[2]) and fecha[0]>0 and fecha[0]<=29:
            validacion = True
        elif fecha[0]>0 and fecha[0]<=28:
            validacion = True
    return validacion

def sumar1Dia(fecha):
    if verificarFecha(fecha[0]+1,fecha[1],fecha[2]):
        fechaSum =(fecha[0]+1,fecha[1],fecha[2])
    elif verificarFecha(1,mes+1,año):
        fechaSum =(fecha[0],fecha[1]+1,fecha[2])
    else:
        fechaSum = (1,1,fecha[2]+1)
        
    return fechaSum

def verificarHorario(hora):
    validacion = False
    if hora[0]>=0 and hora[0]<=23:
        if hora[1]>=0 and hora[1]<=59:
            validacion = True
    return validacion

def diferenciaHorarios(hora1,hora2):
    if hora1[1]>hora2[1]:
        diferencia = (hora1[1]-hora2[1],)
    return diferencia

def main():
    # FECHA
    '''dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))
    fecha = dia,mes,año
    if verificarFecha(dia,mes,año):
        n = int(input("Ingrese el numero de dias a sumar: "))
        fechaSumada = fecha
        for i in range(n):
            fechaSumada = sumar1Dia(fechaSumada)    
        print(fechaSumada)'''
    
    #HORA
    hora = int(input("Ingrese la hora: "))
    minutos = int(input("Ingrese los minutos: "))
    horario = hora,minutos
    if verificarHorario(horario):
        ho = int(input("Hora: "))
        minu = int(input("Minutos: "))
        horar = ho,minu
        verificarHorario(horar)
        print(diferenciaHorarios(horario,horar))
        
    
    

main()
    
