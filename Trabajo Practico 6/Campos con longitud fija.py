# Campos de longitud fija

def pedirNombre():
    nombre = input("Ingrese su nombre: ")
    nombre = nombre.replace(" ","")
    while not nombre.isalpha() and nombre != "":
        nombre = input("Error, reingrese su nombre: ")
    return nombre

def pedirApellido():
    apellido = input("Ingrese su apellido: ")
    apell = apellido.replace(" ", "")
    while not apellido.isalpha():
        apellido = input("Error, reingrese su apellido: ")
    return apellido

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
        archivo = open("CamposLongitudFija.txt","w")
    except IOError:
        print("Error al crear el archivo")
    else:
        while True:
            nombre = pedirNombre()
            if nombre == "":
                break
            apellido = pedirApellido()
            apeynom = formatoNombreYApellido(nombre,apellido)
            dni = pedirDNI()
            domicilio = pedirDomicilio()
            cade = f"{apeynom:<20s}{dni:<20d}{domicilio:<30s}"
            archivo.write(cade+"\n")
            
    finally:
        archivo.close()

def leerArchivo():
    try:
        archivo = open("CamposLongitudFija.txt","r")
    except IOError:
        print("Error al abrir el archivo")
    else:
        while True:
            registro = archivo.readline()
            if registro == "":
                break
            apynom = registro[:20]
            apynom = apynom.rstrip()
            dni = registro[20:39]
            dni = dni.rstrip()
            domicilio = registro[40:]
            domicilio = domicilio.rstrip()
            cad = apynom+" "+dni+" "+domicilio
            print(cad)
            
    finally:
        archivo.close()

escribirArchivo()
leerArchivo()