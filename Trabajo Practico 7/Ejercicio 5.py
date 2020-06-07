# 5.Realizar una función que devuelva el resto de dos números enteros, utilizando restas sucesivas.

def resto(a,b):
    if a < b:
        return a
    else:
        return resto(a-b, b)

print(resto(10,4))