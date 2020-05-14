# 3.Desarrollar una función que devuelva una cadena de caracteres con el nombre del mes cuyo número se recibe como parámetro.
# Los nombres de los meses deberán obtenerse de una lista de cadenas de caracteres inicializada dentro de la función.
# Devolver una cadena vacía si el número de mes es inválido. La detección de meses inválidos deberá realizarse a través
# de excepciones.

# FUNCIONES
def mesSegunNum(num):
    meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    try:
        mes = meses[num-1]
            
    except (IndexError,ValueError):
        mes = []
    return mes

def main():
    num = int(input("Ingrese un numero: "))
    mes = mesSegunNum(num)
    print(mes)
    



# PROGRAMA PRINCIPAL
main()