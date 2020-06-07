# 3.Escribir una función que devuelva la suma de los N primeros números naturales.

def suma(n):
    if n == 0:
        return 0
    else:
        return n + suma(n-1)
    
print(suma(14))