# Crea el archivo con el que se trabaja en el ejercicio 4, con el formato indicado en los apellidos.

def formatoNombreYApellido(nombre, apell):
    nombre = nombre.lower()
    apell = apell.lower()
    nombre = nombre.rstrip()
    nombre = nombre.lstrip()
    apell = apell.rstrip()
    apell = apell.lstrip()
    cad = apell+", "+nombre
    cad = cad.title()
    return cad

def escribirArchivo():
    try:
        archivo = open("ApellidoyNombre.txt","w")
    except IOError:
        print("Error al crear el archivo")
    else:
        while True:
            apellido = input("Ingrese su apellido: ")
            if apellido == "":
                break
            nombre = input("Ingrese su nombre: ")
            cade = formatoNombreYApellido(nombre,apellido)
            archivo.write(cade+"\n")
    finally:
        archivo.close()

escribirArchivo()
            