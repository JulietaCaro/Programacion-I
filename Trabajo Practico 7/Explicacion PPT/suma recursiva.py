# Calcular la suma de los N primeros números naturales.

def sumaRecursiva(n):
    if n == 0:
        return 0
    else:
        return n + sumaRecursiva(n-1)

print(sumaRecursiva(3))