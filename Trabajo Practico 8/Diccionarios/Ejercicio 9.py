# 9.Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y 20 (ambos incluidos) y los valores
# asociados sean el cuadrado de las claves.

def main():
    dic = {}
    for i in range(1,21):
        dic[i] = i**2
        
    for clave,valor in dic.items():
        print(clave,valor)

main()

dic={x:x**2 for x in range (1,21)}
print (dic)