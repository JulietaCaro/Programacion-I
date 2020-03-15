#FUNCIONES
def validarMonto (total, monto):
    estaBien = True
    if monto < total:
        estaBien = False
        print("El dinero es insuficiente")
    return estaBien

def vueltoADar (total, monto):
    if total == monto:
        print("No se debe entregar cambio")

    elif total < monto:
        resta = monto - total
        billete500 = resta //500
        billete100 = (resta%500)//100
        billete50 = ((resta%500)%100)//50
        billete20 = (((resta%500)%100)%50)//20
        billete10 = ((((resta%500)%100)%50)%20)//10
        billete5 = (((((resta%500)%100)%50)%20)%10)//5
        billete1 = ((((((resta%500)%100)%50)%20)%10)%5)//1
        
    return billete500, billete100, billete50, billete20, billete10, billete5, billete1

def main():
    precioTotal = int(input("Ingrese el precio: "))
    abonado = int(input("Ingrese el monto abonado: "))
    estaOk = validarMonto(precioTotal, abonado)
    if estaOk:
        bill500, bill100, bill50, bill20, bill10, bill5, bill1 = vueltoADar(precioTotal, abonado)
        print("500:",bill500,"100:",bill100,"50:",bill50,"20:",bill20,"10:",bill10,"5:",bill5,"1:",bill1)

#PROGRAMA PRINCIPAL
main()
        