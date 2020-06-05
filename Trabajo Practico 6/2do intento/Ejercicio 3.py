# Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los próximos Juegos Panamericanos. Para eso
# encargó la realización de un programa que incluya las siguientes funciones:
# GrabarRangoAlturas() Graba en un archivo las alturas de los atletas de distintas disciplinas, los que se ingresan desde el
# teclado. Cada dato se debe grabar en una línea distinta.
# GrabarPromedio() Graba en un archivo los promedios de las alturas de los atletas presentes en el archivo generado en el paso
# anterior. La disciplina y el promedio deben grabarse en líneas diferentes.
# MostrarMasAltos() Muestra por pantalla las disciplinas deportivas cuyos atletas superan la estatura promedio general.
# Obtener los datos del segundo archivo.

# FUNCIONES
def grabarRangoAlturas():
    try:
        archivo = open("RangoAlturas.txt","w")
    except IOError:
        print("No se pudo crear el archivo RangoAlturas.txt")
    else:
        while True:
            deporte = input("Ingrese el deporte(enter para terminar): ")
            if deporte == "":
                break
            archivo.write(deporte+"\n")
            while True:
                altura = float(input("Ingrese la altura (-1 para terminar): "))
                if altura == -1:
                    break
                archivo.write(str(altura)+"\n")
    finally:
        archivo.close()
        
def grabarPromedio():
    try:
        alturas = open("RangoAlturas.txt","r")
        promedio = open("PromedioAlturas.txt","w")
    except IOError:
        print("Error al crear/leer el archivo")
    else:
        suma = 0
        cant = 0
        registro = alturas.readline()
        while registro != "":
            registro = registro.rstrip()
            if registro.isalpha():
                promedio.write(registro)
            while registro.isdigit():
                if registro.isdigit():
                    suma = suma + float(registro)
                    cant += 1
            registro = alturas.readline()
            
def GrabarPromedio():
    try:
        alturas = open("RangoAlturas.txt","r")
        promedio = open("PromedioAlturas.txt","w")
    except IOError:
        print("No se pudo abrir/crear los archivos")
    else:
        cont = 0
        suma = 0
        for registro in alturas:
            registro = registro.rstrip()
            if registro.isalpha():
                if cont != 0:
                    prom = suma /cont
                    suma = 0
                    cont = 0
                    promedio.write(str(prom)+"\n")
                promedio.write(registro+"\n")
            else:
                cont += 1
                suma = suma + float(registro)
        prom = suma / cont
        promedio.write(str(prom)+"\n")
    finally:
        alturas.close()
        promedio.close()

def mostrarMasAltos():
    try:
        alturas = open("RangoAlturas.txt","r")
        promedio = open("PromedioAlturas.txt","r")
        masAltos = open("MasAltos.txt","w")
    except IOError:
        print("Se produjo un error al abrir/crear el archivo")
    else:
        while True:
            regis = promedio.readline()
            if regis == "":
                break
            for prom in promedio:
                regis = regis.rstrip()
                if regis.isalpha():
                    masAltos.write(regis+"\n")
                else:
                    for alt in alturas:
                        if prom < alt:
                            masAltos.write(alt+"\n")
    finally:
        alturas.close()
        promedio.close()
        masAltos.close()
    
grabarRangoAlturas()
GrabarPromedio()
mostrarMasAltos()                