# Una librería almacena su lista de precios en un diccionario. Diseñar un programa para crearlo, incrementar los precios de los
# cuadernos en un 15%, imprimir un listado con todos los elementos de la lista de precios e indicar cuál es el ítem más costoso
# que venden en el comercio.

# FUNCIONES
def incrementar(dic):
    for clave,valor in dic.items():
        if "cuaderno" in clave:
            dic[clave] = valor + (15*valor)//100

def imprimirClave(dic):
    for clave,valor in dic.items():
        print(clave,valor)

def main():
    dic = {}
    while True:
        clave = input("Ingrese un item: ")
        if clave == "":
            break
        precio = float(input(f"Ingrese el precio del item {clave}: "))
        dic[clave] =precio
    
    incrementar(dic)
    print("CUADERNO: ",dic["cuaderno"])
    
    precios = dic.values()
    items = dic.keys()
    for i in items:
        print(i)
    
    masCaro = max(precios)
    
    for clave,valor in dic.items():
        if valor == masCaro:
            print(f"El item {clave} es el mas caro")
        

main()
    