# 6.Ídem anterior, pero determinando si los vectores son paralelos. Cuando dos vectores son paralelos los cocientes de sus
# coordenadas correspondientes son iguales entre sí. Ejemplo: U = (3,-1) y V = (-9,3)

from random import randint
# FUNCIONES
def vectoresParalelos(tupla1,tupla2):
    veri = False
    if tupla1[0] == tupla2[1]:
        veri = True
    return veri

def main():
    vector1 = (randint(1,20),randint(1,20))
    vector2 = (randint(1,20), randint(1,20))
    print(f"Vector 1: {vector1}")
    print(f"Vector 2: {vector2}")
    if vectoresParalelos(vector1,vector2):
        print("Son paralelos")
    else:
        print("No son paralelos")
    return None

main()