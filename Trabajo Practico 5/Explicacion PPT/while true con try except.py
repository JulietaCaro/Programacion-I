#Si hay un error, ejecuta todo de nuevo, pide los numeros desde el principio, no desde el error
while True:
    try:
        n1 = int(input("Ingrese un numero: "))
        n2 = int(input("Ingrese otro numero: "))
        print(f"La division de los numeros {n1} y {n2} es {n1//n2}")
        break
    except ValueError:
        print("Error, se esperaba el ingreso de un numero")
    except ZeroDivisionError:
        print("Error, division por cero")
    except:
        print("Error no esperado")
    