#Buscar un numero

lista = [3,23,45,18,32,8]
nro = int(input("Ingrese un numero a buscar: "))
i = 0
while i<len(lista):
    if nro == lista[i]:
        print("El nro se encontró en la ubicación",i)
        break
    i = i + 1
else:
    print("El nro no se encontró")