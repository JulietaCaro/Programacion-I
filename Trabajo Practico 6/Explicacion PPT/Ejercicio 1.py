# Crear un archivo con el legajo y nombre de cada alumno, cada uno se guarda en un registro y cada dato se separa con ;.
# Finalizar la carga con legajo -1

def validarNumero(texto= "Ingrese un legajo: "):
    while True:
        try:
            legajo = int(input(texto))
            break
        except ValueError:
            print("Error, se esperaba que ingrese un numero")
            print("Vuelva a intentarlo")
    return legajo

try:
    arch = open("Alumnos.txt","w")
    print("Se creó el archivo")
except IOError:
    print("Error al crear el archivo")

else:
    legajo = validarNumero()
    while legajo != -1:
        nombre = input(f"Ingrese el nombre del legajo {legajo}: ")
        arch.write(str(legajo)+";"+" "+nombre+"\n")
        
        print("Se agregó al archivo")
        legajo = validarNumero("Ingrese otro legajo: ")

finally:
    arch.close()
    print("Se cerró el archivo")
        