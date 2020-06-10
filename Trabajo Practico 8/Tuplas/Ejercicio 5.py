# Escribir una función que reciba dos vectores en forma de tuplas y devuelva un valor de verdad indicando si son ortogonales o 
# no. Desarrollar también un programa que permita verificar el comportamiento de la función.
# A = (2,3) y B = (-3,2) => 2 * (-3) + 3 * 2 = -6 + 6 = 0 => Son ortogonales

def verificarOrtogonales(tupla1,tupla2):
    veri = False
    cuenta = tupla1[0]*tupla2[0] + tupla1[1]*tupla2[1]
    if cuenta == 0:
        veri = True
    return veri

def main():
    com1 = int(input("Ingrese el primer componente: "))
    com1_2 = int(input("Ingrese el primer componente: "))
    com2 = int(input("Ingrese el segundo componente: "))
    com2_2 = int(input("Ingrese el segundo componente: "))
    tupla1 = (com1,com1_2)
    tupla2 = (com2,com2_2)
    if verificarOrtogonales(tupla1,tupla2):
        print(f" Los componentes {tupla1} y {tupla2} son ortogonales")
    else:
        print(f" Los componentes {tupla1} y {tupla2} no son ortogonales")
    
main()