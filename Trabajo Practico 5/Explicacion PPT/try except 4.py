try:
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    div = num1 // num2

except ValueError:
    print("Error, se esperaba el ingreso de un numero")

except ZeroDivisionError:
    print("Error, division por cero")

else:
    print(f"La division entre {num1} y {num2} es {div}")