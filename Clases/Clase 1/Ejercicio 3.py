numero = int(input("Ingrese un numero: "))
binario = 0
potencia = 0
contUnos = 0
while numero >0:
    binario = binario + (10**potencia)*(numero%2)
    if (10**potencia)*(numero%2) >0:
        contUnos = contUnos + 1
    numero = numero //2
    potencia = potencia + 1
        
print("Binario: ", binario)
print("Cant 1: ", contUnos)
