try:
    n1 = int(input("Ingrese un numero: "))
    n2 = int(input("Ingrese otro numero: "))
    div = n1 // n2
    
except ValueError:
    print("Error, se esperaba el ingreso de un numero")

except:
    print("Error no esperado")

else:
    print(f"La division entre {n1} y {n2} es {div}")

finally:
    print("accion a ejecutar independientemente del error")