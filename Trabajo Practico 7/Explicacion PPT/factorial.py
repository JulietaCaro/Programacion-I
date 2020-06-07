# Desarrollar una función para calcular el factorial de un número.

def factorialRecursivo(n):
    if n < 0:
        return -1
    elif n==0 or n==1:
        return 1
    else:
        return n * factorialRecursivo(n-1)

print(factorialRecursivo(5))