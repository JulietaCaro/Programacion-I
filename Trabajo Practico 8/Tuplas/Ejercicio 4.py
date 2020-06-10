# 4.Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son recibidas en dos tuplas,
# por ejemplo: (3, 4) y (5, 4). La función devuelve True o False. Escribir también un programa para verificar su comportamiento.
from random import randint
# FUNCIONES
def domino(tupla1,tupla2):
    encajan = False
    if tupla1[0] == tupla2[0] or tupla1[0] == tupla2[1]:
        encajan = True
    elif tupla1[1] == tupla2[0] or tupla1[1] == tupla2[1]:
        encajan = True
    return encajan

def main():
    ficha1 =(randint(1,6),randint(1,6))
    ficha2 = (randint(1,6),randint(1,6))
    print(f"Dado 1: {ficha1}")
    print(f"Dado 2: {ficha2}")
    if domino(ficha1,ficha2):
        print("Encajan")
    else:
        print("No encajan")
        
main()