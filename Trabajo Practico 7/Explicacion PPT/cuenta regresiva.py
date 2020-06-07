# Desarrollar una función para mostrar una cuenta regresiva desde N por pantalla.

def cuentaRegresiva(n):
    if n == 0:
        print("0")
    else:
        print(n)
        cuentaRegresiva(n-1)
        
cuentaRegresiva(10)