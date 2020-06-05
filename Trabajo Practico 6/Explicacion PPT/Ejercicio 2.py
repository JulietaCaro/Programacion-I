# Leer el archivo de alumnos y mostrar por pantalla aquellos que tengan legajo mayor a 5

try:
    arc = open("Alumnos.txt","r")
    print("Se abrio el archivo")
except IOError:
    print("No se pudo abrir el archivo")
else:
    for registro in arc:
        legajo, nombre = registro.split(";")
        if int(legajo)>5:
            print(f"Legajo {legajo}, nombre{nombre}")

finally:
    arc.close()
    print("Se cerró el archivo")

