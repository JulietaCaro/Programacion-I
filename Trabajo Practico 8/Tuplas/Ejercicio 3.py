# 3.Desarrollar un programa que utilice una función que reciba como parámetro una cadena de caracteres conteniendo una dirección
# de correo electrónico y devuelva una tupla con las distintas partes que componen dicha dirección.
# Ejemplo: alguien@uade.edu.ar -> (alguien, uade, edu, ar).

# FUNCIONES
def deCadenaATupla(cad):
    alguien = cad.split("@")
    tupla = alguien[0],
    alguien ="".join(alguien[0])
    cad = cad.replace(alguien,"")
    cad = cad.replace("@","")
    lista = cad.split(".")
    for i in range(len(lista)):
        tupla += lista[i],
    return tupla
        
        
print(deCadenaATupla("alguien@uade.edu"))