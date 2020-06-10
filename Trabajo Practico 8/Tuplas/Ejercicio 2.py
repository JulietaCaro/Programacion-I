# 2.Escribir una función que reciba como parámetro una tupla conteniendo una fecha (día,mes,año) y devuelva una cadena de
# caracteres con la misma fecha expresada en formato extendido. Por ejemplo, para (12,10,17) devuelve "12 de Octubre de 2017".
# Escribir también un programa para verificar su comportamiento.

# FUNCIONES
def fechaFormatoExt(fecha):
    meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    cad = f"{fecha[0]} de {meses[fecha[1]-1]} de {fecha[2]}"
    return cad
    
def main():
    dia = int(input("Dia: "))
    mes = int(input("Mes: "))
    año = int(input("Año: "))
    fecha = dia,mes,año
    print(fechaFormatoExt(fecha))

main()
