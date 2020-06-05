# Todos los campos de este archivo están precedidos por un número de dos dígitos que indica la longitud del campo
# a leer.
# 10Pérez Juan082008021114Corrientes 348
def formatoNombreYApellido(nombre, apell):
    nombre = nombre.lower()
    apell = apell.lower()
    nombre = nombre.rstrip()
    nombre = nombre.lstrip()
    apell = apell.rstrip()
    apell = apell.lstrip()
    cad = apell+" "+nombre
    cad = cad.title()
    return cad

def pedirDNI():
    while True:
        try:
            dni = int(input("Ingrese su DNI: "))
            while len(str(dni))>8 or len(str(dni))<7:
                dni = int(input("Error, reingrese su DNI: "))
            break
        except ValueError:
            print("Se esperaba el ingreso de un numero")
    return dni

def pedirDomicilio():
    domic = input("Ingrese su domicilio: ")
    dom = domic.replace(" ","")
    while not dom.isalnum():
        domic = input("Error, reingrese su domicilio: ")
    return domic.title()

def escribirArchivo():
    try:
        archivo = open("CampoConSuLongitud.txt","w")
    except IOError:
        print("Error al crear el archivo")
    else:
        while True:
            apellido = input("Ingrese su apellido: ")
            if apellido == "":
                break
            nombre = input("Ingrese su nombre: ")
            apynom = formatoNombreYApellido(nombre,apellido)
            dni = str(pedirDNI())
            dom = pedirDomicilio()
            cad = f"{len(apynom):02d}{apynom}{len(dni):02d}{dni}{len(dom):2d}{dom}"
            archivo.write(cad+"\n")
    finally:
        archivo.close()

def leerArchivo():
    try:
        archivo = open("CampoConSuLongitud.txt","r")
    except IOError:
        print("Error al abrir el archivo")
    else:
        while True:
            registro = archivo.readline()
            if registro == "":
                break
            #SACO EL \n
            registro = registro.rstrip()
            #NOMBRE
            longitud = int(registro[0:2])
            nombre = registro[2:longitud+2]
            registro = registro[2+longitud:]#CORTO LO QUE YA USE CON REBANADAS
            #DNI
            longitud = int(registro[0:2])
            dni = registro[2:longitud+2]
            registro = registro[2+longitud:]
            #DOMICILIO
            longitud = int(registro[0:2])
            dom = registro[2:longitud+2]
            registro = registro[2+longitud:]
            
            print(nombre,dni,dom)
    
    finally:
        archivo.close()
        
#escribirArchivo()
leerArchivo()