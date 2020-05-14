try:
     num1 = int(input("Ingrese un numero: "))
     num2 = int(input("Ingrese otro numero: "))
     divi = num1//num2
     print(f"La división entre {num1} y {num2} es {divi}")

except ValueError:
    print("Error, se espera que ingrese un numero")

except ZeroDivisionError:
    print("Error, división por cero")
    