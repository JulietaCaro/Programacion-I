#FUNCIONES
def numMayor (numeroA, numeroB, numeroC):
    if numeroA>numeroB:
        if numeroA>numeroC:
            mayor = numeroA
    
    if numeroB>numeroA:
        if numeroB>numeroC:
            mayor = numeroB
    
    if numeroC>numeroA:
        if numeroC>numeroB:
            mayor = numeroC
    
    if numeroA == numeroB:
        if numeroA>numeroC:
            mayor = -1
    
    if numeroA == numeroC:
        if numeroA > numeroB:
            mmayor = -1
    
    if numeroB == numeroC:
        if numeroB > numeroA:
            mayor = -1
    return mayor

#PROGRAMA PRINCIPAL
primerNum = int(input("Primer valor: "))
segundoNum = int(input("Segundo valor: "))
tercerNum = int(input("Tercer valor: "))
valorMayor = numMayor(primerNum, segundoNum, tercerNum)
if valorMayor == -1:
    print("No hay un mayor valor")
else:
    print("Valor mayor: ",valorMayor)