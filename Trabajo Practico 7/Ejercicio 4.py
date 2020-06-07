# 4.Desarrollar una función que devuelva el producto de dos números enteros por sumas sucesivas.

def producto(a,b):
    if a == 0:
        return 0
    else:
        return b + producto(a-1,b)

print(producto(-8,6))