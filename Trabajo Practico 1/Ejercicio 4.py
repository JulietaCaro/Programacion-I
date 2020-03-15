#FUNCIONES
def totalGastado(tarifa, viajes):
    if viajes > 1 and viajes <= 20:
        total = viajes * tarifa
    if viajes > 20 and viajes <= 30:
        tarifaFinal = tarifa - (20*tarifa)//100
        total = viajes * tarifaFinal
    if viajes > 30 and viajes <= 40:
        tarifaFinal = tarifa - (30*tarifa)//100
        total = viajes * tarifaFinal
    if viajes > 40:
        tarifaFinal = tarifa - (40*tarifa)//100
        total = viajes * tarifaFinal
    return total

def main ():
    viajesHechos = int(input("Ingrese los viajes realizados: "))
    while viajesHechos < 1:
        viajesHechos = int(input("Error, reingrese los viajes realizados: "))
    gastos = int(input("Ingrese el precio de la tarifa: "))
    while gastos < 1:
        gastos = int(input("Error, reingrese el precio de la tarifa: "))
    totalPagado = totalGastado(gastos, viajesHechos)
    print("Usted realizó",viajesHechos,"viajes con un gasto total de $",totalPagado)

#PROGRAMA PRINCIPAL
main()