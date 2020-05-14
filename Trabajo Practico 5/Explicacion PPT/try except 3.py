try:
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    div = num1 // num2
    print(f"La division es {div}")

except(ValueError,ZeroDivisionError):
    print("Error, se ingresó un valor que no permite realizar la división")