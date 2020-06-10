# 12.Crear una función contarvocales(), que reciba una palabra y cuente cuántas letras "a" contiene, cuántas "e", cuántas "i",
# etc. Devolver un diccionario con los resultados. Desarrollar un programa para leer una frase e invocar a la función por cada
# palabra que contenga la misma. Imprimir cada palabra y la cantidad de vocales hallada.

# FUNCIONES
def contarVocales(palabra):
    dic = {"a":0,"e":0,"i":0,"o":0,"u":0}
    palabra = palabra.lower()
    for letra in palabra:
        if letra in dic:
            dic[letra] += 1
    
    return dic

def imprimirDiccionario(dic):
    for clave,valor in dic.items():
        print(clave,valor)

def main():
    palabra = input("Ingrese una palabra: ")
    dic = contarVocales(palabra)
    imprimirDiccionario(dic)

main()