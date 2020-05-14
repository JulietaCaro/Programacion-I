#Ingresar numeros hasta -1

suma = 0
while True:
    num = int(input("Ingrese un numero: "))
    if num == -1:
        break
    suma = suma+num

print("Suma: ",suma)