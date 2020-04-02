#4. Definir una función superposición() que reciba como parámetros dos listas de cualquier tipo
#y devuelva True si tienen al menos un elemento en común, o False encaso contrario.
#Desarrollar un programa para verificar su comportamiento.

#FUNCIONES
def superposicion(listaA,listaB):
    'Devuelve true si tienen al menos un elemento en comun'
    esta = False
    for i in listaA:
        if i in listaB:
            esta = True
    return esta

def main():
    'Programa principal'
    if superposicion([4,9,1,6,7], [8,4,2,9]):
        print("Tienen elementos en comun")
        
#PROGRAMA PRINCIPAL
main()