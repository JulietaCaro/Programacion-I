#FUNCIONES
def patron1(filas):
    for i in range(filas):
        for j in range(10):
            print("*",end="")
        print()

def patron2(filas):
    aster = 2
    for i in range(filas):
        for j in range(aster):
            print("*",end="")
        aster = aster + 2
        print()
    
def main():
    filas = int(input("Ingrese el numero de filas: "))
    patron1(filas)
    print()
    patron2(filas)

#PROGRAMA PRINCIPAL
main()