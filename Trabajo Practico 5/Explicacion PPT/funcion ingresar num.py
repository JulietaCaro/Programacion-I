def ingresarNumero (texto="Ingrese un numero: "):
    while True:
        try:
            num = int(input(texto))
            break
        except ValueError:
            print("Error, se esperaba el ingreso de un numero")
            print("Vuelva a intentar")
    return num

def main():
    while True:
        try:
            dividendo = ingresarNumero("Ingrese un numero: ")
            divisor = ingresarNumero("Ingrese otro numero: ") 
            division = dividendo // divisor
            print(f"La division entre {dividendo} y {divisor} es {division}")
            break
        
        except ZeroDivisionError:
            print("Error, división por cero")
            print("Intente de nuevo")
        
        except:
            print("Error no esperado")
            print("Intente de nuevo")
        
main()