# Escribir un programa que lea un archivo de texto conteniendo un conjunto de apellidos y nombres en formato "Apellido, Nombre"
# y guarde en el archivo ARMENIA.TXT los nombres de aquellas personas cuyo apellido terminan con la cadena "IAN", en el archivo
# ITALIA.TXT los terminados en "INI" y en el archivo ESPAÑA.TXT los terminados en "EZ". Descartar el resto.

def leerArchivo():
    try:
        apell = open("ApellidoyNombre.txt","r")
        armenia = open("ARMENIA.TXT", "w")
        italia = open("ITALIA.TXT","w")
        espana = open("ESPAÑA.TXT","w")
    except IOError:
        print("Se produjo un error al abrir/crear el archivo")
    else:
        while True:
            registro = apell.readline()
            if registro == "":
                break
            registro = registro.rstrip()
            lista = registro.split(",")
            apellido = lista[0]
            if apellido[len(apellido)-3:] == "ian":
                armenia.write(registro+"\n")
            elif apellido[len(apellido)-3:] == "ini":
                italia.write(registro+"\n")
            elif apellido[len(apellido)-2:] == "ez":
                espana.write(registro+"\n")
    finally:
        apell.close()
        armenia.close()
        espana.close()
        print("Se modificaron los archivos")

leerArchivo()